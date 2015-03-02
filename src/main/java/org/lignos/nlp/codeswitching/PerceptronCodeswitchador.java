package org.lignos.nlp.codeswitching;

import org.lignos.nlp.codeswitching.features.CodeswitchFeatureSet;
import org.lignos.nlp.ml.Perceptron;
import org.lignos.nlp.sequence.SequenceCorpusReader;
import org.lignos.nlp.util.StringUtil;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * Train a test a Perceptron model of codeswitching
 */
public class PerceptronCodeswitchador {

    private static final String USAGE =
        "Usage: PerceptronCodeswitchador traininput testinput featurepath iterations testoutput";

    private static final boolean TRAIN_DEBUG = false;
    private static final boolean AVERAGED = true;
    private static final boolean GREEDY_DECODE = false;

    private final SequenceCorpusReader trainReader;
    private final SequenceCorpusReader testReader;
    private final CodeswitchFeatureSet featureSet;

    public PerceptronCodeswitchador(SequenceCorpusReader trainReader,
                                    SequenceCorpusReader testReader,
                                    CodeswitchFeatureSet featureSet) {
        this.trainReader = trainReader;
        this.testReader = testReader;
        this.featureSet = featureSet;
    }

    public static PerceptronCodeswitchador getFromPaths(
            String trainPath, String testPath, String featurePath) {
        // Create feature sets and load data
        List<String> featureNames = StringUtil.fileLinesAsStringList(featurePath);
        CodeswitchFeatureSet featureSet = CodeswitchFeatureSet.createFeatureSet(featureNames);
        SequenceCorpusReader trainReader = null;
        try {
            trainReader = new SequenceCorpusReader(trainPath, false);
        } catch (IOException e) {
            System.err.println("Could not open training file: " + trainPath);
            System.exit(1);
        }
        SequenceCorpusReader testReader = null;
        try {
            testReader = new SequenceCorpusReader(testPath, false);
        } catch (IOException e) {
            System.err.println("Could not open training file: " + testPath);
            System.exit(1);
        }

        return new PerceptronCodeswitchador(trainReader, testReader, featureSet);
    }

    public static void main(String[] args) {
        if (args.length != 5) {
            System.err.println(USAGE);
            System.exit(1);
        }
        String trainPath = args[0];
        String testPath = args[1];
        String featurePath = args[2];
        int iterations = Integer.parseInt(args[3]);
        String outPath = args[4];

        PerceptronCodeswitchador codeswitchador = getFromPaths(
                trainPath, testPath, featurePath);
        codeswitchador.run(iterations, outPath);
    }

    public void run(int trainingIterations, String outPath) {
        long startTime = System.nanoTime();

        // Create and train perceptron
        Perceptron perc = new Perceptron(featureSet, GREEDY_DECODE, AVERAGED);
        float[] accuracies = perc.train(trainingIterations, trainReader, TRAIN_DEBUG);
        System.out.println("Training accuracy:");
        for (int i = 0; i < accuracies.length; i++) {
            System.out.println((i + 1) + "\t" + accuracies[i]);
        }

        // Test
        PrintWriter output = null;
        try {
            File file = new File(outPath);
            // Make any dirs needed
            File parent = file.getParentFile();
            if (parent != null) {
                parent.mkdirs();
            }
            output = new PrintWriter(file);
        } catch (FileNotFoundException e) {
            System.err.println("Could not open output file: " + outPath);
            System.exit(1);
        }
        float accuracy = perc.test(testReader, output);
        output.close();
        System.out.println("Testing accuracy:");
        System.out.println(accuracy);
        System.out.println();

        long elapsed = System.nanoTime() - startTime;
        System.out.println("Elapsed time: " + TimeUnit.NANOSECONDS.toSeconds(elapsed) + " seconds");
    }


}
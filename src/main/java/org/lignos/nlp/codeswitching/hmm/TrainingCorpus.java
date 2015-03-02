package org.lignos.nlp.codeswitching.hmm;

import gnu.trove.map.hash.THashMap;
import org.lignos.nlp.sequence.Sequence;
import org.lignos.nlp.sequence.TokenState;

import java.io.IOException;
import java.util.*;

public class TrainingCorpus extends Corpus {

	public TrainingCorpus(String path, boolean keepPunc) throws IOException {
		super(path, keepPunc);
	}

    /**
     * Compute transition probability based on the training data, optionally also updating emssions.
     * @param states the states
     * @param nonStates labels to be ignored in training
     * @param emissions emission counts in the same order as states. May be null to skip updating.
     * @return the state probabilities
     */
    public StateProbabilities computeStateProbabilities(String[] states, String[] nonStates,
                                                        Map<String, TokenCounts> emissions) {
		// Use hashmaps to count each init/transition
		Map<String, Integer> initCounts = new HashMap<String, Integer>();
		int initTotal = 0;
		Map<String, Integer> transCounts = new HashMap<String, Integer>();
		Map<String, Integer> fromCounts = new HashMap<String, Integer>();
		// Zero out the values
		for (String state1 : states) {
			initCounts.put(state1, 0);
			fromCounts.put(state1, 0);
			for (String state2 : states) {
				String key = transKey(state1, state2);
				transCounts.put(key, 0);
			}
		}

		// Keep a set of non-states for fast checking
		Set<String> nonStateSet = new HashSet<String>();
		for (String nonState : nonStates) {
			nonStateSet.add(nonState);
		}

		// Count it up
		for (Sequence utt : this) {
			// Track our index in the utterance so we can get inits right
			boolean first = true;
			String lastState = null;
			for (TokenState tokenState : utt)  {
				// Skip non-states
                if (nonStateSet.contains(tokenState.state)) {
					continue;
				}
				// Init if first, transition otherwise
				if (first) {
                    initCounts.put(tokenState.state, initCounts.get(tokenState.state) + 1);
					initTotal += 1;
					first = false;
				}
				else {
                    String trans = transKey(lastState, tokenState.state);
					int count = transCounts.get(trans);
					transCounts.put(trans, count + 1);
					fromCounts.put(lastState, fromCounts.get(lastState) + 1);
				}
                lastState = tokenState.state;

                // Increment emissions
                if (emissions != null) {
                    TokenCounts stateEmissions = emissions.get(tokenState.state);
                    stateEmissions.incrementCount(tokenState.token.toLowerCase(), 1);
                }
			}
		}

		// Compute the probs
		double[] pi = new double[states.length];
		double[][] a = new double[states.length][states.length];
		for (int i = 0; i < states.length; i++) {
			pi[i] = initCounts.get(states[i]) / (double) initTotal;
			for (int j = 0; j < states.length; j++) {
				String trans = transKey(states[i], states[j]);
				a[i][j] = transCounts.get(trans) / (double) fromCounts.get(states[i]);
			}
		}

		// Sanity check
		double piSum = 0;
		for (int i = 0; i < states.length; i++) {
			piSum += pi[i];
			double aSum = 0;
			for (int j = 0; j < states.length; j++) {
				aSum += a[i][j];
			}
			if (aSum != 1.0) {
				throw new RuntimeException("Transitions out of state " + i + " do not sum to one.");
			}
		}
		if (piSum != 1.0) {
			throw new RuntimeException("Initial states do not sum to one.");
		}

		return new StateProbabilities(pi, a);
	}
}
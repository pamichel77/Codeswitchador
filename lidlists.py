"""
Wordlists for a simple approach to Language IDentification (LID).

"""

# Copyright (c) 2012, Constantine Lignos
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

RATIOLIST_DEFAULT_CONFIG = os.path.join('params', 'model1_defaults.cfg')

SPANISH_TOP32 = \
    ['de', 'la', 'que', 'el', 'en', 'y', 'no', 'es', 'los', 'un', 'se', 'por', 'me', 'para', 
     'con', 'lo', 'te', 'del', 'las', 'q', 'una', 'mi', 'si', 'al', 'como', 'ya', 'tu', 'pero', 
     'esta', 'su', 'yo', 'le']

SPANISH_32PLUS = \
    ['mas', 'hay', 'hoy', 'cuando', 'o', 'este', 'todo', 'nos', 'muy', 'ser', 'sin', 'son', 'd',
     'todos', 'gracias', 'mejor', 'feliz', 'eso', 'solo', 'jajaja', 'ver', 'tiene', 'ahora',
     'quiero', 'ni', 'porque', 'bien', 'tengo', 'vida', 'estoy', 'sus', 'hace', 'desde', 'hasta', 
     'tan', 'siempre', 'nada', 'quien', 'va', 'mis', 'dia', 'hacer', 'les', 'ha', 'xd', 'fue', 
     'dios', 'buen', 'donde', 'x', 'puede', 'gente', 'eres', 'mucho', 'bueno', 'vamos', 'ese', 
     'voy', 'amor', 'soy', 'nuevo', 'algo', 'tus', 'esa', 'saludos', 'jaja', 'nunca', 'jajajaja', 
     'sobre', 'gran', 'vez', 'alguien', 'buenos', 'cada', 'sea', 'buena', 'creo', 'mundo', 'cosas',
     'uno', 'estas', 'fin', 'estar', 'asi', 'dice', 'pa', 'ti', 'semana', 'tiempo', 'menos', 'ir',
     'dos', 'tener', 'da', 'hola', 'casa', 'tienes', 'personas', 'mal', 'entre', 'pues', 'otra',
     'esto', 'puedo', 'e', 'venezuela', 'estamos', 'tienen', 'era', 'buenas', 'hora', 'muchas',
     'noche', 'contra', 'espero', 'otro', 'nuestro', 'k', 'falta', 'toda', 'mismo', 'verdad', 'van',
     'antes', 'pasa', 'nadie', 'decir', 'poco', 'cuenta', 'persona', 'igual', 'amo', 'todas',
     'excelente', 'paso', 'favor', 'quiere', 'gusta', 'veces', 'gobierno', 'tanto', 'nueva', 'han',
     'dias', 'san', 'presidente', 't', 'sabe', 'grande', 'trabajo', 'nuestra', 'saber', 'parece', 
     'sino', 'tenemos', 'sera', 'estan', 'puedes', 'aqui', 'somos', 'parte', 'viendo', 'mil', 
     'mujer', 'vas', 'sabes', 'momento', 'debe', 'hombre', 'jajajajaja', 'unos', 'dicen', 'sigue', 
     'amigos', 'amigo', 'final', 'aun', 'ke', 'estos', 'partido', 'tal', 'chile', 'muchos',
     'tambien', 'tarde', 'ayer', 'abrazo', 'estado', 'primer', 'poder', 'mejores', 'aunque', 
     'dormir', 'dar', 'programa', 'felicidades', 'viene', 'horas', 'deja', 'pueden', 'casi', 
     'esos', 'quieres', 'navidad', 'viernes', 'seguir', 'foto', 'dijo', 'mientras', 'equipo', 
     've', 'luego', 'mujeres', 'ganas', 'primera', 'mucha', 'hacen', 'veo']

ENGLISH_TOP32 = \
    ['the', 'to', 'i', 'in', 'of', 'and', 'you', 'for', 'is', 'on', 'your', 'it', 'my', 'with',
     'this', 'at', 'are', 'that', 'be', 'just', 'have', 'new', 'from', 'not', 'we', 'will', 'out',
     'what', 'by', 'can', 'all', 'how']

ENGLISH_32PLUS = \
    ['if', 'but', 'so', 'get', 'do', 'like', 'more', 'as', 'about', 'via', 'when', 'one', 'an', 
     'up', 'our', 'was', 'or', 'u', 'check', 'who', 'they', 'good', 'free', 'make', 'people', 
     'has', 'now', 'love', 'know', 'time', 'want', 'day', 'see', 'us', 'best', 'need', 'go', 
     'great', 'video', 'only', 'he', 'some', 'today', 'why', 'there', 'its', 'than', 'think', 
     'life', 'their', 'am', 'never', 'his', 'happy', 'back', 'should', 'home', 'really', 'very',
     'here', 'after', 'got', 'going', 'first', 'made', 'facebook', 'been', 'would', 'way', 'over', 
     'still', 'world', 'take', 'find', 'twitter', 'posted', 'work', 'business', 'please', 'help', 
     'money', 'photo', 'always', 'thanks', 'any', 'much', 'follow', 'them', 'most', 'too', 'come', 
     'because', 'every', 'last', 'online', 'say', 'live', 'look', 'news', 'then', 'off', 'into', 
     'right', 'may', 'where', 'had', 'hope', 'her', 'things', 'someone', 'did', 'better', 'year', 
     'being', 'next', 'top', 'marketing', 'thank', 'even', 'give', 'many', 'could', 'social', 
     'looking', 'use', 'feel', 'were', 'let', 'she', 'blog', 'big', 'watch', 'keep', 'other', 'real',
     'start', 'read', 'something', 'man', 'before', 'getting', 'own', 'must', 'those', 'stop', 
     'join', 'everyone', 'without', 'does', 'which', 'win', 'ur', 'show', 'down', 'long', 'try', 
     'using', 'two', 'ever', 'tell', 'god', 'learn', 'these', 'makes', 'internet', 'says', 'media', 
     'working', 'lol', 'days', 'change', 'another', 'morning', 'thing', 'nice', 'call', 'friends', 
     'week', 'hey', 'buy', 'well', 'making', 'night', 'while', 'same', 'wish', 'support', 'nothing',
     'doing', 'few', 'him', 'also', 'part', 'bad', 'through', 'years', 'little', 'old', 'liked', 
     'site', 'said', 'against', 'end', 'everything', 'having', 'music', 'google', 'person', 'phone',
     'hate', 'iphone', 'around', 'believe', 'im', 'miss', 'sure', 'coming', 'ask']

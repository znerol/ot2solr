# -*- coding: utf-8 -*-
#
# Convert text-dumps from openthesaurus.de into synonym mapping files suitable
# for apache SOLR.
#
# If transliteration is desired the python unidecode module must be available
# in the python library path.
# * http://pypi.python.org/pypi/Unidecode/
#
# This script is released to the public domain. No rights reserved.
#
# See https://github.com/znerol/ot2solr for the latest version.

import codecs
import re
import sys

#### SETTNGS: adapt 'clean', 'filt' variables to your needs and optionally
# enable transliteration by installing and importing unidecode module.

# Substrings of words matched by this pattern are removed. Use this expression
# to clean out the tags for slang, technical language or dialect for words *you
# want to keep*.
#
#clean = re.compile(r'\([^\)]*(schweiz)[^\)]*\)')

# Filter expression. Every word matching this pattern will not be considered.
# By default all slang words (like "gehoben", "derb"), technical language
# ("fachsprachlich") and dialect ("österr.") will be excluded except when
# explicitely allowed using the clean expression above.
#
filt = re.compile(r'\([^\)]*\)')

# Uncomment the following code if you want to transliterate (i.e. convert
# output to ascii < 128). sharp s (ß) will become ss, ö -> oe, etc.
#
#from unidecode import unidecode

#### MAIN SCRIPT: normally no changes are necessary below this line

# Pattern used to strip off comments
com = re.compile(r'#.*$')

char_stream = codecs.getreader("utf-8")(sys.stdin)
for line in char_stream:
    # strip comments
    line = com.sub('', line)

    # split lines into words
    words = line.split(';')
    synonyms = []

    for word in words:
        # Remove parts of words matched by the 'clean' pattern
        try:
            word = clean.sub('', word)
        except NameError:
            pass

        # Skip words matched by the 'filt' pattern
        try:
            if filt.search(word):
                continue
        except NameError:
            pass

        # Remove whitespace
        word = word.strip()
        if word == '':
            continue

        # Escape colon character
        word = word.replace(',','\\,')

        # Transliterate
        try:
            word = unidecode(word)
        except NameError:
            pass

        synonyms.append(word)

    if len(synonyms) > 1:
        print ', '.join(synonyms).encode('utf-8')

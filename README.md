OpenThesaurus Dump to SORL Synonyms
===================================

ot2solr.py is a simple python script capable of turning text-dumps from
[openthesaurus.de] into the synonym file format used in [Apache SOLR]. Terms
can be optionally filtered using regular expressions. When [Unidecode] module
is installed, the result also can be transliterated such that only ASCII chars
< 128 remain in the output.

[openthesaurus.de]:
    http://www.openthesaurus.de/
[Apache SOLR]:
    http://lucene.apache.org/solr/
[Unidecode]:
    http://pypi.python.org/pypi/Unidecode

Usage
-----

    python ot2solr.py < dump.txt > synonyms.txt

Contribute
----------

Source code and issue tracker are available from:
https://github.com/znerol/ot2solr

License
-------

This work is released to the public domain. No rights reserved.

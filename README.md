unicode-classifier
==================

This simple Python script classifies Unicode characters for bidi text processing.
To use it, download http://www.unicode.org/Public/UNIDATA/UnicodeData.txt to same directory and run:

  python classify_unicode_chars.py

The script will generate a file called BidiData.txt with a C-compatible array containing weak, netutral and
strong RTL characters. Feel free to generate your own structures.

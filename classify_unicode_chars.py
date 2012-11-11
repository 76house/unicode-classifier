# Read UnicodeData.txt in same directory, parse BiDi info from character description
# and generate a new file DidiData.txt with a character table containing the following
# categories for every character:
#
#   L (strong LTR)
#   R (strong RTL)
#   W (weak)
#   N (neutral)

import sys
import os
import string

inputFilename = "UnicodeData.txt"
outputFilename = "BidiData.txt"


class UnicodeCharClassifier:

  # ---------------------------------------------------------------------        
  # Constructor
  def __init__(self):
    pass

  # ---------------------------------------------------------------------        
  # Generate the character table
  def Run(self):

    print "Parsing %s ..." % inputFilename

    try:
      # open output file
      outputFile = open(outputFilename, "w")

      # read input file line by line
      for line in open(inputFilename):

      # split line to tokens (separator = ';')
        lineSplit = line.split(';')
        code = int(lineSplit[0], 16)

        # select English, Arabic and Hebrew characters
        if (code >= 0x0020 and code <= 0x00FF) \
        or (code >= 0xFE80 and code <= 0xFEFC) \
        or (code >= 0x05B0 and code <= 0x05C3) \
        or (code >= 0x05D0 and code <= 0x05EA) \
        or (code >= 0x05F0 and code <= 0x05F4):
          bidiClass = lineSplit[4]
          if bidiClass in ['R', 'AL']:
            # right-to-left strong character
            category = 'BidiRight'
          elif bidiClass in ['EN', 'ES', 'ET', 'AN', 'CS', 'NSM', 'BN']:
            # week character
            category = 'BidiWeak'
          elif bidiClass in ['B', 'S', 'WS', 'ON']:
            # neutral character
            category = 'BidiNeutral'
          else:
            # left-to-right strong character
            category = 'BidiLeft'

          # write bidi info to output file (but filter 'BidiLeft' category)
          if category <> 'BidiLeft':
            outputFile.write("  { 0x%s, %s },\n" % (lineSplit[0], category))
    
    finally:
      outputFile.close()

    print "Output %s created, done." % outputFilename
    
ucc = UnicodeCharClassifier()
ucc.Run()


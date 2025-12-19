#!/usr/bin/env python3

import os
import re
from glob import glob
from functions import *

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
class database(object):
  def __init__(self):
    """
    """
    self.count_sentences_fr  = {}
    self.count_sentences_als = {}
    self.count_words_fr      = {}
    self.count_words_als     = {}

    self.db = []

  # --------------------------------------------------------------------------------------------------
  def count_sentences_words_als(self, line):
    """
    Fill up the Alsacien dictionary of counts of sentences and words
    """
    # Make the count of sentences : 
    if line in self.count_sentences_als.keys():
      self.count_sentences_als[line] = self.count_sentences_als[line] + 1
    else:
      self.count_sentences_als[line] = 1

    # Make the count of words :
    for word in line.split():
      if word in self.count_words_als.keys():
        self.count_words_als[word] = self.count_words_als[word] + 1
      else:
        self.count_words_als[word] = 1

  # --------------------------------------------------------------------------------------------------
  def count_sentences_words_fr(self, line):
    """
    Fill up the French dictionary of counts of sentences and words
    """
    # Make the count of sentences : 
    if line in self.count_sentences_fr.keys():
      self.count_sentences_fr[line] = self.count_sentences_fr[line] + 1
    else:
      self.count_sentences_fr[line] = 1

    # Make the count of words :
    for word in line.split():
      if word in self.count_words_fr.keys():
        self.count_words_fr[word] = self.count_words_fr[word] + 1
      else:
        self.count_words_fr[word] = 1

  # --------------------------------------------------------------------------------------------------
  def get_data_alsaimmer(self, display=False):
    """
    Function to read the xml files from www.alsa-immer.eu
    and extract the database
    """
    for filename in glob("/content/drive/MyDrive/www.alsa-immer.eu/*xml") + glob("/content/drive/MyDrive/www.alsa-immer.eu/*/*xml") :
      try:
        fic = open(filename, 'r', encoding="utf-8")
        line_als = fic.readline()
      except UnicodeDecodeError: 
        fic = open(filename, 'r', encoding='ISO-8859-1')
        line_als = fic.readline()
      try:
        while True:
          if not len(line_als):
            raise EOFError

          if "<als>" in line_als:
            if "<fr>" in line_als:
              line_fr = line_als
            else: # most of the time : alsacien followed by french. Sometimes on the same line
              line_fr = fic.readline()
            while "<fr>" not in line_fr:
              line_fr = fic.readline()
              if not len(line_fr):
                raise EOFError
 
            # Remove HTML tags:
            line_als_clean = extract_between_tags(line_als, "als")
            line_fr_clean = extract_between_tags(line_fr, "fr")

            if len(line_als_clean) and len(line_fr_clean): # if data for both languages
              # Make the count of sentences : 
              self.count_sentences_words_als(line_als_clean)
              # Make the count of words :
              self.count_sentences_words_fr(line_fr_clean)

              # Fill the database:
              self.db.append({'fr':line_fr_clean, 'als':line_als_clean})
              #print({'fr':line_fr_clean, 'als':line_als_clean})

          # Read next line:
          line_als = fic.readline()
      except EOFError:
        fic.close()

    if display:
      print("Alsacien : %d sentences, %d words"%(sum(self.count_sentences_als.values()), sum(self.count_words_als.values())))
      print("Francais : %d sentences, %d words"%(sum(self.count_sentences_fr.values()), sum(self.count_words_fr.values())))

  # --------------------------------------------------------------------------------------------------
  def get_data_alsatext(self, display=False):
    """
    Script to read the file www.alsatext.eu/cours_grammaire.php
    and extract the database.
    """

    filename="/content/drive/MyDrive/www.alsatext.eu/cours_grammaire.php"
    fic = open(filename, 'rt', encoding='utf8')
    try:
      while True:
        line = fic.readline()
        if not len(line):
          raise EOFError

        if "<ex_als>" in line and "<ex_fr>" in line:
          line_als = extract_between_tags(line, 'ex_als')
          line_fr  = extract_between_tags(line, 'ex_fr')

          # Clean data by removing HTML tags and other things:
          line_als_clean = clean_line(remove_html_tags(line_als))
          line_fr_clean  = clean_line(remove_html_tags(line_fr))

          # Make the count of sentences:
          self.count_sentences_words_als(line_als_clean)
          # Make the count of words :
          self.count_sentences_words_fr(line_fr_clean)

          # Fill the database:
          self.db.append({'fr':line_fr_clean, 'als':line_als_clean})
    except EOFError:
      fic.close()

    if display:
      print("Alsacien : %d sentences, %d words"%(sum(self.count_sentences_als.values()), sum(self.count_words_als.values())))
      print("Francais : %d sentences, %d words"%(sum(self.count_sentences_fr.values()), sum(self.count_words_fr.values())))

  # --------------------------------------------------------------------------------------------------
  def get_data_motsAlsacienMulhouse(self, display=False):
    """
    Script to extract data from mots_alsacien_Mulhouse.csv
    """
    filename="mots_alsacien_Mulhouse.csv"
    fic=open("/content/drive/MyDrive/%s"%filename, 'rt', encoding="iso-8859-1")
    fic.readline() # read header
    try:
      while True:
        line = fic.readline()
        if not len(line):
          raise EOFError

        # Make the count of sentences:
        self.count_sentences_words_als(line.split(";")[0])
        # Make the count of words :
        self.count_sentences_words_fr(line.split(";")[1])

        # Fill the database:
        self.db.append({'fr':line.split(";")[1], 'als':line.split(";")[0]})
        #print({'fr':line.split(";")[1], 'als':line.split(";")[0]})
    except EOFError:
      fic.close()

    if display:
      print("Alsacien : %d sentences, %d words"%(sum(self.count_sentences_als.values()), sum(self.count_words_als.values())))
      print("Francais : %d sentences, %d words"%(sum(self.count_sentences_fr.values()), sum(self.count_words_fr.values())))


  # --------------------------------------------------------------------------------------------------
  def get_data_alignments(self, display=False):
    """
    Script to extract data from alignments.csv
    """
    filename="alignments.csv"
    fic=open("/content/drive/MyDrive/%s"%filename, 'rt') #, encoding="iso-8859-1")
    fic.readline() # read header
    try:
      while True:
        line = fic.readline()
        if not len(line):
          raise EOFError

        als = line.split('\t')[0].split()[0].split(';')[0]
        fr  = line.split('\t')[2].split()[0].split(';')[0]

        # Make the count of sentences:
        self.count_sentences_words_als(als)
        # Make the count of words :
        self.count_sentences_words_fr(fr)

        # Fill the database:
        self.db.append({'fr':fr, 'als':als})
    except EOFError:
      fic.close()

    if display:
      print("Alsacien : %d sentences, %d words"%(sum(self.count_sentences_als.values()), sum(self.count_words_als.values())))
      print("Francais : %d sentences, %d words"%(sum(self.count_sentences_fr.values()), sum(self.count_words_fr.values())))



  # --------------------------------------------------------------------------------------------------
  def get_data_lexique(self, display=False):
    """
    Read the 'lexique_*.pdf' and extract the data
    Create .html using `pdftohtml .pdf` command
    """

    filename="../lexique_artisans"

    os.system('pdftohtml -q %s.pdf'%filename)
    os.system('rm %s-* %s_* %s.html'%(filename, filename, filename))

    fic=open("%ss.html"%filename, 'rt')
    start = False
    N = 0
    try:
      while True:
        line = fic.readline()
        if not len(line) or N>5:
          raise EOFError

        if '<body>' in line: 
          start = True # start processing the file only after '<body>'
        if start: # we can process the line:

          # FR sentences with "&#160;<br/>" at the end of the sentence :
          if "&#160;<br/>\n" in line and len(clean_html(line.split('&#160;<br/>')[0])): 
            line_fr  = clean_html(line.split('&#160;<br/>')[0])
            line_als = line
            while "&#160;</i><br/>\n" not in line_als:
              line_als = clean_html(extract_between_tags(fic.readline(), 'i'))
#FIXME Does not work well. No way to distinguish the languages !! 
# How to extract in the pdf depending on the color text ?

              # Fill the database:
              self.db.append({'fr':line_fr, 'als':line_als})
              print({'fr':line_fr, 'als':line_als})
              N = N +1

              # Make the count of sentences:
              self.count_sentences_words_als(line_als)
              # Make the count of words :
              self.count_sentences_words_fr(line_fr)
              break

# TODO
# - same for titles, in bold :  &#160;</b><br/> --- </b></i><br/>

    
    except EOFError:
      fic.close()


    if display:
      print("Alsacien : %d sentences, %d words"%(sum(self.count_sentences_als.values()), sum(self.count_words_als.values())))
      print("Francais : %d sentences, %d words"%(sum(self.count_sentences_fr.values()), sum(self.count_words_fr.values())))


  # --------------------------------------------------------------------------------------------------
  def create_db(self):
    """
    Create a dictionary for each sentence:
    {'fr': 'ksjdfdk', 'als':'rtefv'}
    """
    




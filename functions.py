#!/usr/bin/env python3

import re

CLEANR = re.compile('<.*?>')

# --------------------------------------------------------------------------------------------------
def extract_between_tags(line, tag):
  """
  Extract the text that is between the tags : <tag>bla bla bla</tag>
  """
  try:
    return line.split("<%s>"%tag)[1].split("</%s>"%tag)[0]
  except IndexError:
    return line

# --------------------------------------------------------------------------------------------------
def remove_html_tags(line):
  """
  Remove HTML tags:
  """
  return re.sub(CLEANR, '', line).strip()

# --------------------------------------------------------------------------------------------------
def remove_parenthesis(line):
  """
  Remove content in parenthesis
  """
  return re.sub(r'\([^)]*\)', '', line).strip()

# --------------------------------------------------------------------------------------------------
def clean_line(line):
  """
  - remove "..., "
  - si "=" dans texte -> enleve ce qui suit (explication en francais du texte alsacien)
  - enlever les "(1)" et "(2)"
  - two options for alsacien:
   . separated by "→" for contraction -> supprimer apres car c'est parfois pour une seconde option et parfois des explications (comment savoir ? -> remove)
   . second option in () -> supprimer le contenu dans "()" car c'est parfois pour juste un mot ou tout le texte. comment savoir ? (fr et als)
  """
  line_clean = line.replace("..., ", "").split("=")[0].replace("-"," ").split("→")[0]

  if "(" in line_clean:
    line_clean = remove_parenthesis(line_clean)

  return line_clean

# --------------------------------------------------------------------------------------------------
def clean_html(line):
  """
  Remove '&#160;<br/>' from the line of an html file that has been converted using pdftohtml
  Remive the HTML tags too.
  """
  return remove_html_tags(line.replace('&#160;', ' '))

# --------------------------------------------------------------------------------------------------
def postprocess_text(preds, labels):
    preds = [pred.strip() for pred in preds]
    labels = [[label.strip()] for label in labels]

    return preds, labels


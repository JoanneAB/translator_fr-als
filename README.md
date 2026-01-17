## What is it ? 

This repository proposes a model for a translation task from French to Alsatian (dialiect in Alsace, North-East France)
languages. Because Alsatian is a spoken and non-standard language with significant regional variation across Alsace, the
development of a robust and accurate models is not expected. The objective of this project is to explore and
apply the concepts learned during the deep-learning course on a challenging application. 
Words and sentences in French and their translation in Alsatian have been downloaded from the Internet from 
several sources.

A full report is availaible [report.pdf](https://github.com/JoanneAB/translator_fr-als/blob/main/report/report.pdf).

## How to use it ?

This study uses python libraries and can be run using the jupyter-notebook [main_translator_fr-als.ipynb](https://github.com/JoanneAB/translator_fr-als/blob/main/main_translator_fr-als.ipynb). All datafile and local functions are available in this repository. 

## Model evaluation from people

The evaluation of some translations has been proposed to people using this form : [human_evaluation_form](https://docs.google.com/forms/d/1OL7qtntguZ22thrj8ia7hV9qc7mFFyPCJ_OTcBJy2GY).
Summary of the evaluation is presented in the table [output_human_evaluation_table](https://github.com/JoanneAB/translator_fr-als/blob/main/model/evaluation/Evaluation%20de%20la%20traduction%20_Fran%C3%A7ais%20-_%20Alsacien_%20(r%C3%A9ponses).xlsx)

The model is available in [model/t5-base_essai6_evaluation](https://github.com/JoanneAB/translator_fr-als/blob/main/model/t5-base_essai6_evaluation)

## Technology stack

### Data processing
- numpy
- pandas
- datasets

### Modeling
- sklearn

### Deep learning
- transformers (AutoTokenizer, AutoConfig, NllbTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer, pipeline)

### Model evaluation:
- nltk
- evaluate
- bleu
- sacrebleu

## Credits

This model has been developed as part of a project for the "Deep Learning with Python" class for Data Science Master's course in Data ScienceTech Institute (DSTI, France). Source codes and supplementary files are available at https://github.com/JoanneAB/Translator_fr-als.

If you mention this project in a publication, please include the citations below.

 - Adam, J.M.-C. (2025). Translator model from French to Alsatian. Master's project at DSTI, France. https://github.com/JoanneAB/Translator_fr-als

## Licence

This work is under a GNU General Public License.

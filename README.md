

## What is it ?

This study used a dataset of personal and medical data of more than $5 000$ patients in order to 
predict the event of stroke. After data analysis and feature selection, three machine learning models 
have been trained and tested. Results show that a linear approach is sufficient in order to accuratly 
predict a stroke event for a patient. The model do however predicts a high rate of false positives 
wich will lead to further clinical testing to patients that actually are not at risk of stroke. In 
medical studies, such prediction is best. 

A full report is availaible [report.pdf](https://github.com/JoanneAB/StrokePrevisionModel/blob/main/report/report.pdf).

## How to use it ?

This study uses python libraries and can be run using the jupyter-notebook [project_stroke.ipynb](https://github.com/JoanneAB/Translator_fr-als/blob/main/main_translator_fr-als.ipynb). All datafile and local functions are available in this repository. 

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

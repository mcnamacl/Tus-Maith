# Tús Maith
# Automatic Competency Question Generation and Evaluation for VRTI Knowledge Graph

This repository contains the code and data used for generating, evaluating, and analyzing competency questions (CQs) for the Virtual Record Treasury of Ireland (VRTI) Knowledge Graph (KG), as part of the LLM-based competency question generation study.

## Overview

The repository includes:

- **LLM-based CQ Generation**  
  - Generation using GPT-4o (OpenAI)
  - Generation using Gemini (Google)
- **Expert Evaluation Analysis**  
  - Inter-rater reliability (ICC 3,k, standard deviation) across relevance, clarity, answerability
- **Ground Truth Comparison**  
  - Comparison of LLM-generated CQs to expert-authored ground truth CQs using SentenceBERT

 ## Data Availability

The full data associated with this experiment is openly available via OSF:

🔗 [OSF Repository: Competency Questions and Evaluation Data](https://osf.io/2xyn4/files/osfstorage)

This includes:

- The full set of LLM-generated competency questions (GPT-4o and Gemini)
- The curated expert-authored ground truth competency questions
- The expert evaluation ratings across relevance, clarity, and answerability
- Spreadsheets used for analysis and scoring
 
## Reproducibility Checklist

| ✅ | **Item**                                     | **Description**                                                            |
| - | -------------------------------------------- | -------------------------------------------------------------------------- |
| ✅ | **Code Available**                           | Full code for generation, evaluation, and analysis included                |
| ✅ | **Data Available**                           | Generated questions, ground truth set, and expert evaluation data included |
| ✅ | **Prompts Included**                         | Full LLM prompts for GPT-4o and Gemini provided                            |
| ✅ | **Dependencies Listed**                      | `requirements.txt` provided                                                |
| ✅ | **Pretrained Models Identified**             | SentenceBERT model specified (`all-mpnet-base-v2`)                          |
| ✅ | **API Requirements Specified**               | OpenAI API and Gemini API keys required                                    |
| ✅ | **Environment Instructions Provided**        | Setup instructions included in README                                      |
| ✅ | **Randomness Controlled (where applicable)** | Seeds set for generation consistency                                       |
| ✅ | **End-to-End Pipeline Documented**           | Full generation + evaluation pipeline reproducible                         |


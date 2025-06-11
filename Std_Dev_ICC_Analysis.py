import pandas as pd
import pingouin as pg

# RELEVANCE
# Relevance_1 = Reviewer 1 Ratings
# Relevance_2 = Reviewer 2 Ratings
data_r_g = pd.DataFrame({
    'Relevance_1': [2, 1, 5, 1, 1, 5, 5, 1, 0, 2, 3, 3, 4, 4, 3, 1, 3, 1, 5, 1],
    'Relevance_2': [2, 1, 3, 3, 5, 5, 5, 2, 4, 5, 2, 1, 1, 1, 5, 3, 5, 4, 4, 3]
})

# Standard deviation for each reviewer
std1 = data_r_g['Relevance_1'].std()
std2 = data_r_g['Relevance_2'].std()

print("Relevance Gemini Standard Deviation Reviewer 1: ", std1, "Reviewer 2: ", std2)

# Add a column to identify each question (required by pingouin)
data_r_g['Question'] = range(1, len(data_r_g) + 1)

# Reshape to long format for ICC
long_data_g = data_r_g.melt(id_vars=['Question'], 
                            value_vars=['Relevance_1', 'Relevance_2'], 
                            var_name='Rater', 
                            value_name='Score')

# Optionally clean Rater names
long_data_g['Rater'] = long_data_g['Rater'].str.replace('Relevance_', '')

# Compute ICC for Gemini relevance ratings
icc_result_g = pg.intraclass_corr(data=long_data_g, targets='Question', raters='Rater', ratings='Score')
print("Inter-rater reliability (Gemini Relevance):")
print(icc_result_g)

# GPT 4o
data_r_o = pd.DataFrame({
    'Relevance_1': [1, 5, 5, 4, 4, 5, 5, 5, 5, 5, 5, 1, 5, 1, 1, 1, 1, 1, 1, 0],
    'Relevance_2': [2, 2, 2, 1, 3, 3, 5, 5, 5, 5, 2, 4, 4, 3, 2, 3, 4, 4, 4, 5]
})

# Standard deviation for each reviewer
std1 = data_r_o['Relevance_1'].std()
std2 = data_r_o['Relevance_2'].std()

print("Relevance GPT4o Standard Deviation Reviewer 1: ", std1, "Reviewer 2: ", std2)

data_r_o['Question'] = range(1, len(data_r_o) + 1)

long_data_o = data_r_o.melt(id_vars=['Question'],
                            value_vars=['Relevance_1', 'Relevance_2'],
                            var_name='Rater',
                            value_name='Score')

long_data_o['Rater'] = long_data_o['Rater'].str.replace('Relevance_', '')

icc_result_o = pg.intraclass_corr(data=long_data_o, targets='Question', raters='Rater', ratings='Score')
print("Inter-rater reliability (GPT4o Relevance):")
print(icc_result_o)

# CLARITY
# Clarity_1 = Reviewer 1 Ratings
# Clarity_2 = Reviewer 2 Ratings
data_c_g = pd.DataFrame({
    'Clarity_1': [1, 1, 4, 2, 0, 5, 5, 2, 5, 4, 1, 2, 4, 4, 5, 1, 5, 2, 2, 4],
    'Clarity_2': [2, 1, 4, 2, 5, 5, 5, 4, 5, 5, 4, 2, 2, 2, 5, 4, 5, 4, 5, 4]
})

std1 = data_c_g['Clarity_1'].std()
std2 = data_c_g['Clarity_2'].std()

print("Clarity Gemini Standard Deviation Reviewer 1: ", std1, "Reviewer 2: ", std2)

data_c_g['Question'] = range(1, len(data_c_g) + 1)

long_data_g = data_c_g.melt(id_vars=['Question'],
                            value_vars=['Clarity_1', 'Clarity_2'],
                            var_name='Rater',
                            value_name='Score')

long_data_g['Rater'] = long_data_g['Rater'].str.replace('Relevance_', '')

icc_result_g = pg.intraclass_corr(data=long_data_g, targets='Question', raters='Rater', ratings='Score')
print("Inter-rater reliability (Gemini Clarity):")
print(icc_result_g)

data_c_o = pd.DataFrame({
    'Clarity_1': [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 1, 5, 1, 5],
    'Clarity_2': [3, 3, 2, 3, 4, 2, 5, 5, 5, 5, 4, 5, 5, 4, 4, 4, 2, 5, 4, 5]
})

std1 = data_c_o['Clarity_1'].std()
std2 = data_c_o['Clarity_2'].std()

print("Clarity GPT4o Standard Deviation Reviewer 1: ", std1, "Reviewer 2: ", std2)

data_c_o['Question'] = range(1, len(data_c_o) + 1)

long_data_o = data_c_o.melt(id_vars=['Question'],
                            value_vars=['Clarity_1', 'Clarity_2'],
                            var_name='Rater',
                            value_name='Score')

long_data_o['Rater'] = long_data_o['Rater'].str.replace('Relevance_', '')

icc_result_o = pg.intraclass_corr(data=long_data_o, targets='Question', raters='Rater', ratings='Score')
print("Inter-rater reliability (GPT4o Clarity):")
print(icc_result_o)

# ANSWERABILITY
# Answerability_1 = Reviewer 1 Ratings
# Answerability_2 = Reviewer 2 Ratings
data_a_g = pd.DataFrame({
    'Answerability_1': [0, 1, 5, 1, 0, 5, 5, 1, 0, 0, 5, 3, 5, 5, 1, 1, 3, 0, 5, 1],
    'Answerability_2': [2, 3, 5, 3, 5, 5, 5, 3, 3, 4, 5, 1, 5, 5, 4, 2, 5, 4, 5, 3]
})

std1 = data_a_g['Answerability_1'].std()
std2 = data_a_g['Answerability_2'].std()

print("Answerability Gemini Standard Deviation Reviewer 1: ", std1, "Reviewer 2: ", std2)

data_a_g['Question'] = range(1, len(data_a_g) + 1)

long_data_g = data_a_g.melt(id_vars=['Question'],
                            value_vars=['Answerability_1', 'Answerability_2'],
                            var_name='Rater',
                            value_name='Score')

long_data_g['Rater'] = long_data_g['Rater'].str.replace('Relevance_', '')

icc_result_g = pg.intraclass_corr(data=long_data_g, targets='Question', raters='Rater', ratings='Score')
print("Inter-rater reliability (Gemini Answerability):")
print(icc_result_g)


data_a_o = pd.DataFrame({
    'Answerability_1': [0, 0, 0, 0, 5, 5, 5, 5, 5, 2, 5, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    'Answerability_2': [2, 3, 3, 3, 4, 4, 5, 4, 4, 4, 2, 2, 3, 2, 2, 2, 3, 3, 3, 5]
})

std1 = data_a_o['Answerability_1'].std()
std2 = data_a_o['Answerability_2'].std()

print("Answerability GPT4o Standard Deviation Reviewer 1: ", std1, "Reviewer 2: ", std2)

data_a_o['Question'] = range(1, len(data_a_o) + 1)

long_data_g = data_a_o.melt(id_vars=['Question'],
                            value_vars=['Answerability_1', 'Answerability_2'],
                            var_name='Rater',
                            value_name='Score')

long_data_o['Rater'] = long_data_o['Rater'].str.replace('Relevance_', '')

icc_result_o = pg.intraclass_corr(data=long_data_o, targets='Question', raters='Rater', ratings='Score')
print("Inter-rater reliability (GPT4o Answerability):")
print(icc_result_o)
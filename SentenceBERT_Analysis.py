import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

# CONFIG 
DATA_FOLDER = "" # Add the file path to your folder of excel files of generated questions.
EXPERT_FILE = "" # Add the file path to the text file of ground truth expert-authored questions.
THRESHOLD = 0.6
MODEL_NAME = 'all-mpnet-base-v2' # SentenceBERT model.

# Load model 
model = SentenceTransformer(MODEL_NAME)

# Load expert questions 
with open(EXPERT_FILE, 'r', encoding='utf-8') as f:
    expert_questions = [line.strip() for line in f if line.strip()]
expert_embeddings = model.encode(expert_questions, convert_to_tensor=True)

# Find all CSVs 
excel_files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith((".xlsx", ".xls"))])

# Process each CSV 
for file in tqdm(excel_files):
    file_path = os.path.join(DATA_FOLDER, file)
    # Read file with header
    df = pd.read_excel(file_path)
    
    # Access column with header '0' (as string)
    questions = df[0].dropna().tolist()

    if len(questions) != 20:
        print(f"Skipping {file}: expected 20 questions, got {len(questions)}")
        continue

    # Encode generated questions 
    generated_embeddings = model.encode(questions, convert_to_tensor=True)

    # Cosine Similarity Matrix (full 20×10 table) 
    sim_matrix = cosine_similarity(
        generated_embeddings.cpu().numpy(),
        expert_embeddings.cpu().numpy()
    )

    sim_df = pd.DataFrame(
        sim_matrix,
        index=[f"GenQ{i+1}" for i in range(20)],
        columns=[f"ExpertQ{i+1}" for i in range(len(expert_questions))]
    )

    print(f"\n Similarity Table for {file} ")
    print(sim_df.round(3).to_string())

    # Quantitative Metrics 
    max_similarities = sim_matrix.max(axis=1)
    average_max = np.mean(max_similarities)
    count_above = np.sum(max_similarities >= THRESHOLD)
    percent_above = (count_above / len(max_similarities)) * 100

    print(f"\n--- Metrics for {file} ---")
    print(f"Average Max Similarity: {average_max:.3f}")
    print(f"Questions ≥ {THRESHOLD}: {count_above}/20 ({percent_above:.1f}%)")

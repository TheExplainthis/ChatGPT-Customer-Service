import numpy as np
import pandas as pd

def data_preprocessing(csv_file, model):
    df = pd.read_csv(csv_file)
    documents = []
    vectors = []
    for idx, r in df.iterrows():
        documents.append({
            'category': r.category,
            'question': r.question,
            'answer': r.answer
        })
        vectors.append(model.embedding(f'{r.category}: {r.question}\n{r.answer}'))
    
    return documents, np.array(vectors)

import pandas as pd
import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_metadata_summary(file_path):
    df = pd.read_csv(file_path)
    schema_summary = df.dtypes.to_dict()
    columns = df.columns.tolist()

    prompt = f"""I have a dataset with the following columns: {columns} 
and types: {schema_summary}. 
Can you generate a detailed data documentation including:
- Description of each column
- Data types explanation
- Sample statistics
- Suggested metadata tags
"""
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.3)
    response = llm.predict(prompt)
    return response

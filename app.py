#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import google.generativeai as genai
import os
import logging
from flask import Flask, request, jsonify, render_template
from io import BytesIO
from dotenv import load_dotenv


# In[2]:


def excel_to_json(file_path, output_file):
    file_stream = BytesIO(file_path.read())
    xls = pd.ExcelFile(file_stream, engine='openpyxl')
    data = {}
    
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)
        df.fillna(value=999, inplace=True)
        data[sheet] = df.to_dict(orient='records')

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Converted {file_path} to output_file')
    return data


# In[3]:


def prepare_prompt(data):
    summary_request = "Please summarize the following data:\n\n"
    summary_request += json.dumps(data, indent=2)
    summary_request += "\n\nProvide a brief summary."
    return summary_request


# In[4]:

load_dotenv()
os.environ["API_KEY"] = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.environ["API_KEY"])


# In[5]:


def generate_summary(prompt_template):
    prompt = prompt_template
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text


# In[6]:

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    file = request.files['file']
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400
    
    try:
        # Save the uploaded Excel file to a temporary location
        output_file = 'output_temp.json'

        # Convert Excel to JSON and return the data
        data = excel_to_json(BytesIO(file.read()), output_file)

        # Prepare the prompt for the AI summarization
        prompt = prepare_prompt(data)

        # Generate the summary from the model
        summary = generate_summary(prompt)

        return jsonify({'summary': summary})
    
    except Exception as e:
        app.logger.error("An error occurred: %s", str(e))
        return jsonify({"error": "An internal error has occurred!"}), 500




#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import google.generativeai as genai
import os


# In[2]:


def excel_to_json(file_path, output_file):
    xls = pd.ExcelFile(file_path)
    data = {}
    
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)
        df.fillna(value=999, inplace=True)
        data[sheet] = df.to_dict(orient='records')

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Converted {file_path} to output_file')


# In[3]:


def prepare_prompt(data):
    summary_request = "Please summarize the following data:\n\n"
    summary_request += json.dumps(data, indent=2)
    summary_request += "\n\nProvide a brief summary."
    return summary_request


# In[4]:


os.environ["API_KEY"] = "AIzaSyCGXDXXEIsNl66VRhgBVTAplJjAb_UaCU4"
genai.configure(api_key=os.environ["API_KEY"])

prompt_template = """
You are a data conversion assistant. Convert the following Radford base data terminology to match the example data terminology:

Radford Data: 
{input_data}

Converted Data:
"""


# In[5]:


def convert_data_with_gpt(prompt_template):
    prompt = prompt_template
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text


# In[6]:


excel_file = r"C:\Users\prathmesh\OneDrive\Desktop\Codes\Excel_reader\Central Job Leveling Framework - Radford reference.xlsx"
excel_to_json(excel_file, f'temp.json')

sample = json.load(open(r"C:\Users\prathmesh\OneDrive\Desktop\Codes\Excel_reader\Radford Data.json"))

prompt = prepare_prompt(sample)
output = convert_data_with_gpt(prompt)
print(output)


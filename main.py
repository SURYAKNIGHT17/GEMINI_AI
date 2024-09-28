# # import requests
# #
# # # Replace with your actual API key
# # API_KEY = 'AIzaSyCxGmyEE5jokRG6LKRKxwE0blo_N5XaORA'
# #
# # # Define the endpoint URL for the Gemini AI API
# # url = 'https://api.gemini.ai/POST /v1beta/{model=models/*'  # Example of a specific endpoint
# # # Adjust the endpoint as necessary
# #
# # # Set up the headers with the API key
# # headers = {
# #     'Authorization': f'Bearer {API_KEY}',
# #     'Content-Type': 'application/json'
# # }
# #
# # # Example payload, adjust according to the API documentation
# # payload = {
# #     'input': 'India'
# # }
# #
# # try:
# #     # Send the request to the API
# #     response = requests.post(url, headers=headers, json=payload)
# #
# #     # Check if the request was successful
# #     if response.status_code == 200:
# #         data = response.json()
# #         print("Response from Gemini AI:", data)
# #     else:
# #         print(f"Error: {response.status_code}, Message: {response.text}")
# #
# # except Exception as e:
# #     print("An error occurred:", e)
# #
#
#
#
#
#
# """
# Install the Google AI Python SDK
#
# $ pip install google-generativeai
# """
#
# import os
# import google.generativeai as genai
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# genai.configure(api_key="AIzaSyCxGmyEE5jokRG6LKRKxwE0blo_N5XaORA")
#
# # Create the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 64,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }
#
# model = genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   generation_config=generation_config,
#   # safety_settings = Adjust safety settings
#   # See https://ai.google.dev/gemini-api/docs/safety-settings
# )
#
# chat_session = model.start_chat(
#   history=[
#   ]
# )
#
# # response = chat_session.send_message("generate python code to diagnose,preprocess,predict, decision making and all the possible analysis for the following data set with the file name SuperStoreOrders.csv {'order_id': ['AG-2011-2040', 'IN-2011-47883', 'HU-2011-1220', 'IT-2011-3647632', 'IN-2011-47883'], 'order_date': ['1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011'], 'ship_date': ['6/1/2011', '8/1/2011', '5/1/2011', '5/1/2011', '8/1/2011'], 'ship_mode': ['Standard Class', 'Standard Class', 'Second Class', 'Second Class', 'Standard Class'], 'customer_name': ['Toby Braunhardt', 'Joseph Holt', 'Annie Thurman', 'Eugene Moren', 'Joseph Holt'], 'segment': ['Consumer', 'Consumer', 'Consumer', 'Home Office', 'Consumer'], 'state': ['Constantine', 'New South Wales', 'Budapest', 'Stockholm', 'New South Wales'], 'country': ['Algeria', 'Australia', 'Hungary', 'Sweden', 'Australia'], 'market': ['Africa', 'APAC', 'EMEA', 'EU', 'APAC'], 'region': ['Africa', 'Oceania', 'EMEA', 'North', 'Oceania'], 'product_id': ['OFF-TEN-10000025', 'OFF-SU-10000618', 'OFF-TEN-10001585', 'OFF-PA-10001492', 'FUR-FU-10003447'], 'category': ['Office Supplies', 'Office Supplies', 'Office Supplies', 'Office Supplies', 'Furniture'], 'sub_category': ['Storage', 'Supplies', 'Storage', 'Paper', 'Furnishings'], 'product_name': ['Tenex Lockers, Blue', 'Acme Trimmer, High Speed', 'Tenex Box, Single Width', 'Enermax Note Cards, Premium', 'Eldon Light Bulb, Duo Pack'], 'sales': ['408', '120', '66', '45', '114'], 'quantity': [2, 3, 4, 3, 5], 'discount': [0.0, 0.1, 0.0, 0.5, 0.1], 'profit': [106.14, 36.036, 29.64, -26.055, 37.77], 'shipping_cost': [35.46, 9.72, 8.17, 4.82, 4.7], 'order_priority': ['Medium', 'Medium', 'High', 'High', 'Medium'], 'year': [2011, 2011, 2011, 2011, 2011]}")
# # response = chat_session.send_message("generate python code to diagnose,preprocess,predict, decision making and all the possible analysis for the following data set with the file name SuperStoreOrders.csv")
# # response = chat_session.send_message("generation_config = {'temperature': 1,'top_p': 0.95,'top_k': 64,'max_output_tokens': 8192,'response_mime_type': 'text/plain',} explain the code")
# # response = chat_session.send_message("generate python code to diagnose, preprocess and all the possible analysis suitable for the date set SuperStoreOrders.csv ")
# response1 = chat_session.send_message("analyse the given datas set SuperStoreOrders.csv : {'order_id': ['AG-2011-2040', 'IN-2011-47883', 'HU-2011-1220', 'IT-2011-3647632', 'IN-2011-47883'], 'order_date': ['1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011'], 'ship_date': ['6/1/2011', '8/1/2011', '5/1/2011', '5/1/2011', '8/1/2011'], 'ship_mode': ['Standard Class', 'Standard Class', 'Second Class', 'Second Class', 'Standard Class'], 'customer_name': ['Toby Braunhardt', 'Joseph Holt', 'Annie Thurman', 'Eugene Moren', 'Joseph Holt'], 'segment': ['Consumer', 'Consumer', 'Consumer', 'Home Office', 'Consumer'], 'state': ['Constantine', 'New South Wales', 'Budapest', 'Stockholm', 'New South Wales'], 'country': ['Algeria', 'Australia', 'Hungary', 'Sweden', 'Australia'], 'market': ['Africa', 'APAC', 'EMEA', 'EU', 'APAC'], 'region': ['Africa', 'Oceania', 'EMEA', 'North', 'Oceania'], 'product_id': ['OFF-TEN-10000025', 'OFF-SU-10000618', 'OFF-TEN-10001585', 'OFF-PA-10001492', 'FUR-FU-10003447'], 'category': ['Office Supplies', 'Office Supplies', 'Office Supplies', 'Office Supplies', 'Furniture'], 'sub_category': ['Storage', 'Supplies', 'Storage', 'Paper', 'Furnishings'], 'product_name': ['Tenex Lockers, Blue', 'Acme Trimmer, High Speed', 'Tenex Box, Single Width', 'Enermax Note Cards, Premium', 'Eldon Light Bulb, Duo Pack'], 'sales': ['408', '120', '66', '45', '114'], 'quantity': [2, 3, 4, 3, 5], 'discount': [0.0, 0.1, 0.0, 0.5, 0.1], 'profit': [106.14, 36.036, 29.64, -26.055, 37.77], 'shipping_cost': [35.46, 9.72, 8.17, 4.82, 4.7], 'order_priority': ['Medium', 'Medium', 'High', 'High', 'Medium'], 'year': [2011, 2011, 2011, 2011, 2011]}.  provide a pyhton code to diagnose,preprocess, and all the possible analysis suitable for the data set").text
# # print(response.text)
# # print(response1)
# import re
#
# def extract_python_code(response):
#     # Regex pattern to match Python code blocks (assuming they are indented)
#     pattern = r'(```python[\s\S]*?```|(?:\n\s*|\s+)(def|class|import|from)\s.*?(\n\s*|\s+)(?:\n\s*|$))'
#     matches = re.findall(pattern, response)
#     return [match[0] for match in matches]
#
# # print(extract_python_code(response1))
# def trim(response):
#     l = len(response)
#     code = response[9:]
#     code = code[:code.find("```")]
#     return code
# # print(trim(response1))
#
# code = trim(response1)
# print(code)
# exec(code)





























import pandas as pd
df = pd.read_csv('SuperStoreOrders.csv')
column = list(df.columns)
# print(column)
data = {}
for col in column:
    column_name = col
    first_10_values = list(df[column_name].head(5))
    data[col] = first_10_values
# print(data)
data = str(data)
query = "analyse the given datas set SuperStoreOrders.csv : " + data +".  provide a pyhthon code to diagnose,preprocess, and all the possible analysis suitable for the data set"
print(query)
import os
import google.generativeai as genai
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# genai.configure()

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message(query).text
response1 = chat_session.send_message("change the data set source of the code to SuperStoreOrders.csv and remove the existing dataset").text
response2 = chat_session.send_message("add all the possible and suitable analysis and visualisations for the data set to the existing code").text
response3 = chat_session.send_message("add general exeception handing to code and save tha error as string in the variable 'error'")
# print(response.text)
print(response3)
# def trim(response):
#     code = response[9:]
#     code = code[:code.find("```")]
#     return code
# # print(trim(response1))
#
# code = trim(response2)
# # print(code)
# # exec(code)
# def write_string_to_file(code_string, filename):
#     with open(filename, 'w') as file:
#         file.write(code_string)
#
# # Example usage
# code = code
#
# filename = "generated.py"
# write_string_to_file(code, filename)































# response = chat_session.send_message("generate python code to diagnose,preprocess,predict, decision making and all the possible analysis for the following data set with the file name SuperStoreOrders.csv {'order_id': ['AG-2011-2040', 'IN-2011-47883', 'HU-2011-1220', 'IT-2011-3647632', 'IN-2011-47883'], 'order_date': ['1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011'], 'ship_date': ['6/1/2011', '8/1/2011', '5/1/2011', '5/1/2011', '8/1/2011'], 'ship_mode': ['Standard Class', 'Standard Class', 'Second Class', 'Second Class', 'Standard Class'], 'customer_name': ['Toby Braunhardt', 'Joseph Holt', 'Annie Thurman', 'Eugene Moren', 'Joseph Holt'], 'segment': ['Consumer', 'Consumer', 'Consumer', 'Home Office', 'Consumer'], 'state': ['Constantine', 'New South Wales', 'Budapest', 'Stockholm', 'New South Wales'], 'country': ['Algeria', 'Australia', 'Hungary', 'Sweden', 'Australia'], 'market': ['Africa', 'APAC', 'EMEA', 'EU', 'APAC'], 'region': ['Africa', 'Oceania', 'EMEA', 'North', 'Oceania'], 'product_id': ['OFF-TEN-10000025', 'OFF-SU-10000618', 'OFF-TEN-10001585', 'OFF-PA-10001492', 'FUR-FU-10003447'], 'category': ['Office Supplies', 'Office Supplies', 'Office Supplies', 'Office Supplies', 'Furniture'], 'sub_category': ['Storage', 'Supplies', 'Storage', 'Paper', 'Furnishings'], 'product_name': ['Tenex Lockers, Blue', 'Acme Trimmer, High Speed', 'Tenex Box, Single Width', 'Enermax Note Cards, Premium', 'Eldon Light Bulb, Duo Pack'], 'sales': ['408', '120', '66', '45', '114'], 'quantity': [2, 3, 4, 3, 5], 'discount': [0.0, 0.1, 0.0, 0.5, 0.1], 'profit': [106.14, 36.036, 29.64, -26.055, 37.77], 'shipping_cost': [35.46, 9.72, 8.17, 4.82, 4.7], 'order_priority': ['Medium', 'Medium', 'High', 'High', 'Medium'], 'year': [2011, 2011, 2011, 2011, 2011]}")
# response = chat_session.send_message("generate python code to diagnose,preprocess,predict, decision making and all the possible analysis for the following data set with the file name SuperStoreOrders.csv")
# response = chat_session.send_message("generation_config = {'temperature': 1,'top_p': 0.95,'top_k': 64,'max_output_tokens': 8192,'response_mime_type': 'text/plain',} explain the code")
# response = chat_session.send_message("generate python code to diagnose, preprocess and all the possible analysis suitable for the date set SuperStoreOrders.csv ")
# response1 = chat_session.send_message("analyse the given datas set SuperStoreOrders.csv : {'order_id': ['AG-2011-2040', 'IN-2011-47883', 'HU-2011-1220', 'IT-2011-3647632', 'IN-2011-47883'], 'order_date': ['1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011', '1/1/2011'], 'ship_date': ['6/1/2011', '8/1/2011', '5/1/2011', '5/1/2011', '8/1/2011'], 'ship_mode': ['Standard Class', 'Standard Class', 'Second Class', 'Second Class', 'Standard Class'], 'customer_name': ['Toby Braunhardt', 'Joseph Holt', 'Annie Thurman', 'Eugene Moren', 'Joseph Holt'], 'segment': ['Consumer', 'Consumer', 'Consumer', 'Home Office', 'Consumer'], 'state': ['Constantine', 'New South Wales', 'Budapest', 'Stockholm', 'New South Wales'], 'country': ['Algeria', 'Australia', 'Hungary', 'Sweden', 'Australia'], 'market': ['Africa', 'APAC', 'EMEA', 'EU', 'APAC'], 'region': ['Africa', 'Oceania', 'EMEA', 'North', 'Oceania'], 'product_id': ['OFF-TEN-10000025', 'OFF-SU-10000618', 'OFF-TEN-10001585', 'OFF-PA-10001492', 'FUR-FU-10003447'], 'category': ['Office Supplies', 'Office Supplies', 'Office Supplies', 'Office Supplies', 'Furniture'], 'sub_category': ['Storage', 'Supplies', 'Storage', 'Paper', 'Furnishings'], 'product_name': ['Tenex Lockers, Blue', 'Acme Trimmer, High Speed', 'Tenex Box, Single Width', 'Enermax Note Cards, Premium', 'Eldon Light Bulb, Duo Pack'], 'sales': ['408', '120', '66', '45', '114'], 'quantity': [2, 3, 4, 3, 5], 'discount': [0.0, 0.1, 0.0, 0.5, 0.1], 'profit': [106.14, 36.036, 29.64, -26.055, 37.77], 'shipping_cost': [35.46, 9.72, 8.17, 4.82, 4.7], 'order_priority': ['Medium', 'Medium', 'High', 'High', 'Medium'], 'year': [2011, 2011, 2011, 2011, 2011]}.  provide a pyhton code to diagnose,preprocess, and all the possible analysis suitable for the data set").text
response = chat_session.send_message(query).text

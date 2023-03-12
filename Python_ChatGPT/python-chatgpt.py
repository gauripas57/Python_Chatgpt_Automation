#from email import header
import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save python code")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

requests_headers = {
"Content-Type": "application/json",
"Authorization" : "Bearer " + api_key

}

requests_data = {
    "model": "text-davinci-003",
    "prompt": f"Write Python script to {args.prompt}. Provide only code no text",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint,headers=requests_headers,json=requests_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name,"w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code : {str(response.status_code)} ")


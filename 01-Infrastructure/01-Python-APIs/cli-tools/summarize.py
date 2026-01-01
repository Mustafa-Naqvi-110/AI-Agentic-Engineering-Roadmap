import os
import argparse
import openai

openai.api_key = os.getenv("YOUR_OPENAI_API_KEY")

parser = argparse.ArgumentParser(
    description = "Summarize the file using OpenAI API"
)
parser.add_argument(
    "file", type = str, help = "Path to the text file to summarize"
)
args = parser.parse_args()

with open(args.file, "r", encoding = "utf-8") as f:
    text = f.read()

responce = openai.chat.completions.create(
    model = "gpt-5.2",
    messages = 
    [
        {"role" : "system", "content" : "You are an assistent that summarizes the text"},
        {"role" : "user", "content" : f"Summarize this text {text}"}
    ],
    temperature = 0
)

summary = responce.choices[0].message.content

print(f"Summarized text : \n\n"{summary})

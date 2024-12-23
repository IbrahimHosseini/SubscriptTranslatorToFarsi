import os
from deep_translator import (GoogleTranslator, ChatGptTranslator)
import openai

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 

file_path = "../SubscriptTranslatorToFarsi"
src_file_name = "src_sub.srt"
dest_file_name = "dest_sub.srt"
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set!")

print(f"API key : {api_key}")

google_translator = GoogleTranslator(source='auto', target='fa')
gpt_translator = ChatGptTranslator(api_key=api_key, target='fa', model='gpt-3.5-turbo')

# join file and path
src_file = os.path.join(file_path, src_file_name)
dest_file = os.path.join(file_path, dest_file_name)

# read file
with open(src_file) as f:
    sub_lines = f.readlines()

# translate and write
with open(dest_file, "w", encoding="utf-8") as read_file:   
    for sub_line in sub_lines:
        if sub_line[0] in nums:
            read_file.write(sub_line)
        elif sub_line == "\n":
            read_file.write("\n\n")
        else:
            line_en = gpt_translator.translate(sub_line)
            read_file.write(line_en)

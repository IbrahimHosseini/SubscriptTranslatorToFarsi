import os
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='fa')

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 

file_path = "../SubscriptTranslatorToFarsi"
src_file_name = "src_sub.srt"
dest_file_name = "dest_sub.srt"

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
            line_en = translator.translate(sub_line)
            read_file.write(line_en)

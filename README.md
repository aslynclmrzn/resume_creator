
# 𝙿𝙳𝙵 𝚁𝚎𝚜𝚞𝚖𝚎 𝙲𝚛𝚎𝚊𝚝𝚘𝚛
This repository contains the code for PDF Resume Creator. 
# 𝐓𝐚𝐬𝐤

PDF Resume Creator
- Create a python program that will create your personal resume in PDF format
- All personal details are stored in a JSON file
-  Your program should read the JSON file and write the details in the PDF
- The output file should be: LASTNAME_FIRSTNAME.pdf

# 𝐏𝐃𝐅 𝐥𝐢𝐛𝐫𝐚𝐫𝐲 𝐮𝐬𝐞𝐝

FPDF is a PHP class which allows generating PDF files with PHP code. It is free to use and it does not require any API keys. FPDF stands for Free PDF. It means that any kind of modification can be done in PDF files.

# 𝐇𝐨𝐰 𝐭𝐨 𝐫𝐞𝐚𝐝 𝐉𝐒𝐎𝐍 𝐟𝐢𝐥𝐞
- import module

      import json

- Opening JSON file

      f = open('resume.json')
 
- returns JSON object as
a dictionary

        data = json.load(data)
 
- Iterating through the json
list

          
      for i in data['emp_details']:   
          print(i)
 
- Closing file

      f.close()

# 𝐎𝐮𝐭𝐩𝐮𝐭 𝐨𝐟 𝐏𝐃𝐅 𝐢𝐧 𝐈𝐦𝐚𝐠𝐞
<img src="https://github.com/aslynicole/ASSIGNMENT9/blob/2d54a6127a19418a67b7557d8c10459295b567b2/ResumeImage.jpg">

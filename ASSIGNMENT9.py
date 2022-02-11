from fpdf import FPDF
import json
file = open("resume.json")
data = json.load(file)

a = data.get("a")
Name =a["Name"]
Label = a["Text"]


b = data.get("b")
Summary =  b["Summary"]
Information = b["Information"]


c = data.get("c")
Home = c["Home Address"]
Address = c["Location"][0]
Postal = c["Location"][1]
City = c["Location"][2]
Country = c["Location"][3]
Region = c["Location"][4]

d = data.get("d")
Work =  d["Work"]
Experience1 =  d["Experience"][0]
Experience2 =  d["Experience"][1]
Experience3 =  d["Experience"][2]
Experience4 =  d["Experience"][3]
Experience5 =  d["Experience"][4]
Experience6 =  d["Experience"][5]
Experience7 =  d["Experience"][6]

e = data.get("e")
Title1 = e["Title1"]
Education1 = e["Education"][0]
Education2 = e["Education"][1]
Education3 = e["Education"][2]
Education4 = e["Education"][3]
Education5 = e["Education"][4]

f = data.get("f")
Title2 = f["Title2"]
skills1 = f["skills"][0]
skills2 = f["skills"][1]
skills3 = f["skills"][2]
skills4 = f["skills"][3]
Title3 = f["Title3"]
languages1 = f["languages"][0]
languages2 = f["languages"][1] 
Title4 = f["Title4"]
interests1 = f["interests"][0]
interests2 = f["interests"][1]
interests3 = f["interests"][2]
interests4 = f["interests"][3]

g = data.get("g")
Email = g["Email"]
Text = g["Contact"]
ContactNumber = g["Number"]
Website = g["Website"]

# Pdf format (Portrait, mm, and Letter Format)
pdf = FPDF("P", "mm", "Letter")
# Add a page
pdf.add_page()                                                                                                                                                                                
# Fonts (B- bold u - underline)
# Footer
pdf.image ('blue.png', 0, 191, 250)
#A
pdf.image ('image.jpg', 85, 5, 43)
pdf.set_font("helvetica", "B")
pdf.cell(85, 35, ln=True, align = "C")
pdf.set_font_size (17)
pdf.cell(195, 5, f"{Name}", ln=True, align = "C")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.cell(195, 5, f"{Label}", ln=True, align = "C")
#B
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Summary}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Information}", ln=True, align = "L")
#C
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Work}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Address}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Postal}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{City}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Country}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Region}", ln=True, align = "L")
#D
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Home}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience1}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience2}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience3}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience4}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience5}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience6}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Experience7}", ln=True, align = "L")
#E
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Title1}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Education1}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Education2}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Education3}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Education4}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{Education5}", ln=True, align = "L")
#F
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Title2}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{skills1}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{skills2}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{skills3}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{skills4}", ln=True, align = "L")
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Title3}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{languages1}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{languages2}", ln=True, align = "L")
pdf.set_font("Times", "B")
pdf.set_font_size (12)
pdf.set_text_color (r= 112, g= 128, b= 144)
pdf.cell(100, 10, f"{Title4}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{interests1}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{interests2}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{interests3}", ln=True, align = "L")
pdf.set_font("arial")
pdf.set_font_size (8)
pdf.set_text_color (r= 0, g= 0, b= 0)
pdf.cell(10, 3, f"{interests4}", ln=True, align = "L")
pdf.cell(195, 10, "", ln=True, align = "C")

#G
pdf.set_font("arial", "I")
pdf.set_font_size (8)
pdf.cell(195, 5, f"{Text}", ln=True, align = "C")
pdf.set_font_size (7)
pdf.set_font("arial")
pdf.cell(195, 3, f"{Email}", ln=True, align = "C")
pdf.set_font_size (7)
pdf.set_font("arial")
pdf.cell(195, 3, f"{ContactNumber}", ln=True, align = "C")

# Output the code to Pdf Format
pdf.output('Marzan_AsleyNicole_C..pdf')


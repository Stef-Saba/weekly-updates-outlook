import csv
from outlook_sender import create_outlook_draft

INPUT_FILE = "sample_weekly_update.csv"
OUTPUT_FILE = "leadership_update.html"



leadership_awareness = []
highlights = []
deliverable_updates = []


def create_line(row, text):
    return (
        f"{row['Status']} | "
        f"{row['Workstream']} | "
        f"{row['Deliverable']} | "
        f"{row['Owner']} | "
        f"{text}"
    )


with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        update = row["This week"]

        has_major = "[MAJOR]" in update
        has_adoption = "[ADOPTION]" in update
        is_complete = row["Status"] == "✅"


        # Leadership Awareness
        if has_major or is_complete:

            leadership_text = update

            if has_major:
                leadership_text = update.split("[MAJOR]", 1)[1]

            if "[ADOPTION]" in leadership_text:
                leadership_text = leadership_text.split("[ADOPTION]", 1)[0]

            leadership_awareness.append(
                create_line(row, leadership_text.strip())
            )


        # Highlights & Achievements
        if has_adoption:

            adoption_text = update.split("[ADOPTION]", 1)[1]

            highlights.append(
                create_line(row, adoption_text.strip())
            )


        # Key Deliverable Updates
        if not has_major and not is_complete:

            deliverable_updates.append(
                create_line(row, update)
            )



html = f"""
<html>

<head>

<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background-color: #f4f6f8;
    padding: 30px;
    color: #1f2937;
}}

.container {{
    max-width: 900px;
    margin: auto;
}}

.section {{
    background: white;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}}

.section h2 {{
    margin-top: 0;
}}

.update-line {{
    padding: 12px 0;
    margin-bottom: 8px;
    border-bottom: 1px solid #e5e7eb;
}}

.update-line:last-child {{
    border-bottom: none;
}}

</style>

</head>


<body>

<div class="container">


<table width="100%" cellpadding="0" cellspacing="0" style="background:#2563eb;">
<tr>
<td style="
padding:30px;
text-align:center;
color:white;
">

<h1 style="
margin:0;
font-size:32px;
color:white;
">
Stefania's Dashboard
</h1>

<h2 style="
margin:10px 0;
font-weight:normal;
color:white;
">
Your Team Dashboard
</h2>

<p style="
margin:10px 0;
color:white;
">
Automated leadership communication engine
</p>

<p style="
margin:10px 0;
color:white;
">
Generated from structured delivery updates
</p>

</td>
</tr>
</table>



<div class="section">

<h2>Leadership Awareness</h2>

{''.join(f'<div class="update-line">{item}</div>' for item in leadership_awareness)}

</div>



<div class="section">

<h2>Highlights & Achievements</h2>

{''.join(f'<div class="update-line">{item}</div>' for item in highlights)}

</div>



<div class="section">

<h2>Key Deliverable Updates</h2>

{''.join(f'<div class="update-line">{item}</div>' for item in deliverable_updates)}

</div>


</div>


</body>

</html>
""" 
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(html)
create_outlook_draft(html)

print("Leadership update generated successfully!")
# cv_generator.py
import re
# --------------
print("""
Welcome to cv_generator program!
=-=-=-=-=-=-=-=-=-=
      Please enter all the rquired input in order for 
      the program to give you an amazing cv for you
      to start apply now for your dream companies!
      0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0
""")

name=input("Enter your name:\n")
phone_number=input("Enter your phone number:\n")
email=input("Enter your email:\n")
city=input("Enter your city:\n")

university_name=input("""
Education:
Enter your university name:\n
""")
major=input("Enter your major:\n")
graduation_date=input("Enter your graduation date:\n")

company_name=input("""
Experience:
Enter company name:\n
""")
job_title=input("Enter job title:\n")
key_summary=input("Enter a summary of your key responsibilities:\n")

skills=input("""
Skills:
Enter your skills:\n
""")

arabic=input("""
Languages:
Enter your level in Arabic:\n
""")

english=input("Enter your level in English:\n")

all_parts=(name, phone_number, email, city, university_name, major, graduation_date, company_name, job_title, key_summary, skills, arabic, english)
# --------------
# --------------
# --------------
def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please provide a valid file path.")

# ---------------- # ---------------- # ----------------

def parse_template(template):
    pattern_one = r'\{([^}]*)\}'
    language_parts = re.findall(pattern_one, template)
    #
    pattern_two = r'\{([^}]*)\}'
    stripped_template = re.sub(pattern_two, '{}', template)
    #
    return stripped_template, tuple(language_parts)

x,y = parse_template(read_template("./assets/cv_template.txt"))

# ---------------- # ---------------- # ----------------

def merge(template, user_inputs):
    return template.format(*user_inputs)

z = merge(x, all_parts)
print(z)

import os

print("Automated Resume Screener")

folder = "resumes"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Create a resumes folder and add resume files.")
else:
    skills = input("Enter required skills: ").lower().split(",")
    education = input("Enter required education: ").lower()

    count = 0

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:
                resume = f.read().lower()

            score = 0

            for skill in skills:
                if skill.strip() in resume:
                    score += 1

            if education in resume:
                score += 1

            print("\nResume:", file)
            print("Matching score:", score)

            if score >= 2:
                print("Status: Shortlisted")
            else:
                print("Status: Not shortlisted")

            count += 1

    print("\nTotal resumes checked:", count)

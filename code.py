import re

def evaluate_resume(resume_text):
    keywords = ["Python", "Machine Learning", "AI", "Data Science", "Java", "SQL"]
    matched_keywords = [kw for kw in keywords if re.search(rf'\b{kw}\b', resume_text, re.IGNORECASE)]
    
    score = len(matched_keywords) * 10
    
    print("Resume Score: ", score)
    print("Matched Keywords: ", matched_keywords)

if __name__ == "__main__":
    resume = input("Paste your resume text: ")
    evaluate_resume(resume)

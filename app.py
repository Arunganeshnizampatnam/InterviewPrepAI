from flask import Flask, render_template, request
from resume_parser import extract_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/aptitude")
def aptitude():
    return """
    <h1>Aptitude Question</h1>
    <p>What is 25 + 25?</p>

    <button onclick="showAnswer()">Show Answer</button>

    <p id="answer"></p>

    <script>
    function showAnswer() {
        document.getElementById("answer").innerHTML = "Answer: 50";
    }
    </script>
    """


@app.route("/technical")
def technical():
    return """
    <h1>Technical Question</h1>
    <p>What is Python?</p>

    <button onclick="showAnswer()">Show Answer</button>

    <p id="answer"></p>

    <script>
    function showAnswer() {
        document.getElementById("answer").innerHTML =
        "Python is a high-level programming language.";
    }
    </script>
    """


@app.route("/hr")
def hr():
    return "<h1>HR Interview Questions</h1>"


@app.route("/resume")
def resume():
    return """
    <h1>Resume Analyzer</h1>

    <form action="/upload" method="post" enctype="multipart/form-data">

        <input type="file" name="resume">

        <br><br>

        <input type="submit" value="Upload Resume">

    </form>
    """


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    file.save(file.filename)

    from docx import Document

    doc = Document(file.filename)

    text = ""

    for para in doc.paragraphs:
        text += para.text + " "

    # Detect Skills
    skill_list = [
        "Python",
        "Java",
        "C",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Flask",
        "Django",
        "Git",
        "GitHub"
    ]

    skills = []

    for skill in skill_list:
        if skill.lower() in text.lower():
            skills.append(skill)

    # Calculate Score
    score = min(len(skills) * 10, 100)

    # Suggestions
    suggestions = []

    if "project" not in text.lower():
        suggestions.append("Add more projects")

    if "certification" not in text.lower():
        suggestions.append("Include certifications")

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    return render_template(
        "result.html",
        filename=file.filename,
        score=score,
        skills=skills,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)
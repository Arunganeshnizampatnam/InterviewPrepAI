from flask import Flask, render_template,request

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

    <form action="/upload" method="post"
          enctype="multipart/form-data">

        <input type="file" name="resume">

        <br><br>

        <input type="submit" value="Upload Resume">

    </form>
    """
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]

    file.save(file.filename)

    score = 85

    return f"""
    <h1>Resume Analysis</h1>

    <h2>Resume Uploaded Successfully!</h2>

    <p><b>File:</b> {file.filename}</p>

    <h3>Resume Score: {score}/100</h3>

    <h3>Skills Detected</h3>
    <ul>
        <li>Python</li>
        <li>Machine Learning</li>
        <li>HTML</li>
        <li>CSS</li>
    </ul>

    <h3>Suggestions</h3>
    <ul>
        <li>Add more projects</li>
        <li>Include certifications</li>
        <li>Improve technical skills section</li>
    </ul>
    """
if __name__ == "__main__":
    app.run(debug=True)


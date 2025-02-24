from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/blogs")
def blogs():
    with open('static/blogs.json', 'r') as file:
        blogs_data = json.load(file)
    return render_template("blogs.html", blog_posts=blogs_data)

@app.route("/about")
def aboutMe():
    return render_template('aboutme.html')

@app.route("/blogs/<type>/<subtype>")
def get_post(type, subtype):
    with open('static/blogs.json', 'r') as file:
        blogs_data = json.load(file)
    for blog_post in blogs_data:
        if blogs_data[blog_post]["type"] == type and blogs_data[blog_post]["subtype"] == subtype:
            blog = blogs_data[blog_post]
            return render_template("blog_post.html", post=blog)
        else:
            return "404: URL Not Found"

@app.route("/crochet101")
def crochet_101():
    with open('static/lessons.json', 'r') as file:
        lessons = json.load(file)
    return render_template("crochet_101.html", lessons=lessons)

@app.route("/crochet101/lesson/<num>")
def lesson_page(num):
    with open('static/lessons.json', 'r') as file:
        lessons = json.load(file)
    lesson = lessons[f"Lesson {num}"]
    return render_template("lesson.html", lesson=lesson, num=num)

@app.route('/origami')
def origami_page():
    return render_template('origami.html')

if __name__ == "__main__":
    app.run(debug=True)





from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/about')
def about():
    return 'The about page'

@app.route('/blog')
def blog():
    return 'This is the blog'

@app.route('/blog/<int:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + str(blog_id)

if __name__ == "__main__":
    app.run()

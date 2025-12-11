from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample posts data
posts = [
    {"title": "First Post", "content": "This is the content of the first post."},
    {"title": "Second Post", "content": "This is the content of the second post."}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/posts')
def show_posts():
    return render_template('posts.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({"title": title, "content": content})
        return redirect(url_for('show_posts'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)


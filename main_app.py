from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'author': 'nick youkhana',
        'title': 'blog post 1',
        'content':'first post content',
        'date_posted':'feb 14, 2022'
    },
    
    {
        'author': 'jonny cassh',
        'title': 'blog post 2',
        'content':'second post content',
        'date_posted':'feb 14, 2022'
        
    },
    
    {
        'author': 'cheese supreme',
        'title': 'blog post 3',
        'content':'third post content',
        'date_posted':'feb 14, 2022'
        
    }
]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) 
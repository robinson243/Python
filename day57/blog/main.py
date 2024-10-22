from flask import Flask, render_template
import requests

# from post import Post


blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# post_objects = []
# for post in blog_data:
#     post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
#     post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=blog_data)


@app.route("/post/<index>")
def show_post(index):
    index = int(index) - 1
    if index <= 0 or index >= len(blog_data):
        return "Blog Id don't exist"
    return render_template("post.html", index=index, posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)

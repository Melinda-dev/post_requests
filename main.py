from flask import Flask, render_template,request
import smtplib
import requests

app = Flask(__name__)
blog_url = f"https://api.npoint.io/eb6cd8a5d783f501ee7d"
all_posts = requests.get(blog_url).json()
print(all_posts)

my_email = "MY_EMAIL"
password = "MY_PASSWORD"



@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

# contact function is the combine of receive_data and

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


# @app.route("/login", methods=['POST'])
# def receive_data():
#     name = request.form['username']
#     password = request.form['password']
#     return f"Name:{name}, Password:{password}"
#
# @app.route("/form-entry", methods=['GET'])
# def receive_data():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return "<h1>successfully sent your message.</h1>"

@app.route("/post/<int:index>")
def each_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sun.melinda@hotmail.com",
            msg=email_message)
if __name__ == "__main__":
    app.run(debug=True)






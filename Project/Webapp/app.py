from flask import Flask, render_template, request
# from chatbot import response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/switch',methods = ['POST', 'GET']) # Route name - switch
# def switch():
#     if request.method == 'POST':
#         print(request.form)
#         if (request.form['led'] == 'on'):
#             print("Switch on LED")
#         elif (request.form['led'] == 'off'):
#             print("Switch off LED")
#         return {"message": "Ok"}


if __name__ == '__main__':
    app.run(debug=True)
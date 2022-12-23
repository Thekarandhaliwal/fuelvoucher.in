
import os
# from Tools.scripts.make_ctype import method
from flask import *
from flask import Flask, render_template, request
from saidatabaseconnection import Database, SaiHiTech
import tkinter
from tkinter import messagebox
import pyautogui as pag
from werkzeug.utils import secure_filename


# from saiquery import SaiHiTech

upload_location = 'F:\Auribises\pythonProject\saihitechfuels\static'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

web_app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = upload_location

app = Flask("SaiHiTech")
db_Database = Database()



@app.route("/")
def add_detail():
    return render_template("bpclvoucher.html")


@app.route("/logs")
def view_all_health_logs():
    view_data_object = SaiHiTech()
    sql = view_data_object.fetch_sql_command()
    rows = db_Database.read(sql)
    return render_template("bpclview.html", result=rows)


@app.route("/save", methods=["POST"])
def save_data():
    # print("Save health Data Executed...")

    form_data_object = SaiHiTech(name=request.form['name'],
                                 mobile=request.form['mobile'],
                                 vehicle=request.form['vehicle'],
                                 image=request.form['image'],
                                 )

    # print(form_data_object)
    sql = form_data_object.insert_sql_command()
    # print("SQL IS:", sql)
    db_Database.write(sql)
    # return '<div class="alert alert-success" style="color:red; text-align:center;"><strong>SUCCESS!</strong> Thank you for fueling with us.</div>'
    return messagebox.showinfo("Title", "Message")
#
# @app.route("/uploader", methods=["POST"])
# def uploader():
#     if (request.method == 'POST'):
#         f = request.files['file1']
#         f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
#         return "uploaded Success"


def main():
    app.run()

if __name__ == "__main__":
    app.debug = True
    main()
    # app.run(debug=True)



# picFolder = os.path.join('static')
# app.config['UPLOAD_FOLDER'] = picFolder


# @app.route("/")
# def index():
#     pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'bpcl.jpg')
#     return render_template("saiform.html", user_image = pic1)

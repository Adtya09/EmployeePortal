from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "Employee Portal Basic"
heading = "Insert and read operation"

myclient = MongoClient("mongodb://127.0.0.1:27017")  # host uri
database = myclient.mymongodb
mycoll = database.employeeportalDemo


@app.route("/", methods=['GET'])
def home():
    return render_template("InsertEmployee.html")


@app.route("/getEmployee", methods=['GET', 'POST'])
def getEmployee():
    name = request.form.get("searchbar")
    print(name)
    cursor = mycoll.find()
    data = []
    for record in cursor:
        del (record['_id'])
        if record['name'] == name:
            data.append(record)
    print(data)
    return render_template("viewEmployees.html", data=data)


@app.route("/viewEmployees", methods=['GET'])
def showEmployeeData():
    cursor = mycoll.find()
    data = []
    for record in cursor:
        del (record['_id'])
        data.append(record)
    print(data)
    return render_template("viewEmployees.html", data=data)


@app.route("/insertEmployee", methods=['POST', 'GET'])
def insertEmployeeData():
    fname = request.form.get('First Name')
    lname = request.form.get('Last Name')
    fullname= fname + " " + lname
    gender = request.form.get('optradio')
    doj = request.form.get('date')
    employed = request.form.get('selected')
    record = {"name": fullname, "gender": gender, "doj": doj, "employed": employed}
    mycoll.insert_one(record)
    print("Successfully Inserted!!!")
    return redirect("/")


if __name__ == "__main__":
    app.run()

from flask import Flask
from datetime import datetime
#from flask import os
from flask import render_template, request, json
import csv
from csv import writer 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/form/")
def form():
    return render_template("form.html")
 
@app.route("/data/", methods = ['POST', 'GET'])
def data():

    companies_list = []

    companies_headers = []

    filename = ("static/companycitystate.csv")

    sortchk = request.form.get("SortFilter")
    filterchk = request.form.get("CompFilter")
    companychk = request.form.get("Company")
    citychk = request.form.get("City")
    statechk = request.form.get("State")

    if filterchk == '' and companychk != '' and citychk != '' and statechk != '':
        companies_csvrow = [companychk,citychk,statechk]
        with open(filename, 'a+', newline='') as companies:
            csv_writer = writer(companies)
            csv_writer.writerow(companies_csvrow)
        with open(filename, newline = '') as companies:
            company_reader = csv.DictReader(companies)
            companies_headers = company_reader.fieldnames
            for company in company_reader:
                companies_list.append(dict(company))
        companies_sublist = [company for company in companies_list]

    if filterchk == '*':
        with open(filename, newline = '') as companies:                                                                                          
            company_reader = csv.DictReader(companies)
            companies_headers = company_reader.fieldnames
            for company in company_reader:
                companies_list.append(dict(company))
        companies_sublist = [company for company in companies_list]

    if filterchk != '' and filterchk != '*':
        with open(filename, newline = '') as companies:                                                                                          
            company_reader = csv.DictReader(companies)
            companies_headers = company_reader.fieldnames
            for company in company_reader:
                companies_list.append(dict(company))
        companies_sublist = [company for company in companies_list if filterchk in(company['Company'])]

    if sortchk == "desc":
        companies_sublist.sort(key=lambda x: x.get('Company'), reverse=True)
    else:
        companies_sublist.sort(key=lambda x: x.get('Company'))
    
    return render_template("data2.html", len = len(companies_sublist), CompaniesFiltered = companies_sublist)

    if request.method == 'GET':
        return f"The URL /data is not accessed directly. Use '/form' to submit your data by form"
    if request.method == 'POST':
        form_data = request.form
        return render_template("data.html",form_data = form_data)
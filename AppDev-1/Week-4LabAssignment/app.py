from flask import Flask 
from flask import render_template
from flask import request
import csv
import matplotlib.pyplot as plt
app = Flask(__name__)

students = {}
courses= {}

def update_dict(dict_name, primary_id, secondary_id, marks):
    if primary_id in dict_name.keys():
        dict_name[primary_id][secondary_id] = marks
    else:
        dict_name[primary_id]={}
        dict_name[primary_id][secondary_id] = marks

with open('data.csv') as csv_file:
    dict_file = csv.DictReader(csv_file)
    for row in dict_file:
        update_dict(courses, int(row[' Course id']), int(row['Student id']), int(row[' Marks']))
        update_dict(students,  int(row['Student id']), int(row[' Course id']), int(row[' Marks']))

@app.route("/", methods = ["Get","POST"])
def index():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        try:
            choice = request.form["ID"]
            id_value = int(request.form["id_value"])
            if choice=="student_id":
                # Generating details for student details
                student_details = students[id_value].items()
                return render_template("student.html",student_id = id_value, student_details = student_details, total_marks_data = sum(students[id_value].values()))

            elif choice=="course_id":
                course_details = courses[id_value].values()

                #Generating histogram
                plt.hist(course_details, bins = 10)
                plt.xlabel("Marks")
                plt.ylabel("Frequency")
                plt.savefig("static/course_histogram.png")

                #Filling Templates
                maximum_marks = max(course_details)
                average_marks = (sum(course_details)/len(course_details))
                return render_template("course.html",average_marks= average_marks, maximum_marks = maximum_marks)

        except:
            # Error Template
            return render_template("error.html")

@app.errorhandler(Exception)
def handle_exception(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run()
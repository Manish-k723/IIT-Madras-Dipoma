import sys
import csv
from jinja2 import Template
import matplotlib.pyplot as plt

students = {}
courses = {}

def dict_update(dictionary_name, student_id, course_id, marks):
    if student_id in dictionary_name.keys():
        dictionary_name[student_id][course_id] = marks
    else:
        dictionary_name[student_id] = {}
        dictionary_name[student_id][course_id] = marks


with open('data.csv', 'r') as data_file:
    f = csv.DictReader(data_file)
    line_count = 0
    for row in f:
        if line_count>=0:
            dict_update(courses, int(row[' Course id']),
                        int(row['Student id']), int(row[' Marks']))
            dict_update(students, int(row['Student id']),
                        int(row[' Course id']), int(row[' Marks']))
        line_count+=1

#Generating Student Template
students_template = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>IIT Madras</title>
  </head>
  <body>
    <h1 class="mainTitle">Student Details</h1>
    <table frame= "box" rules = "all">
      <tr>
        <th>Student id</th>
        <th>Course id</th>
        <th>Marks</th>
      </tr>
      {% for sub_id, marks in students_details %}
      <tr>
          <td>{{ student_id }}</td>
          <td>{{ sub_id }}</td>
          <td>{{ marks }}</td>
      </tr>
      {% endfor %}
      <tr>
        <td colspan="2" style="text-align: center">Total Marks</td>
        <td>{{ total_marks }}</td>
      </tr>
    </table>
  </body>
</html>
'''

#Generating Course Template
course_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IIT Madras</title>
</head>
<body>
    <h1>Course Details</h1>
    <table frame = "box" rules = "all">
        <tr>
            <th>Average Marks</th>
            <th>Maximum Marks</t>
        </tr>
        <tr>
            <td>{{Average_marks}}</td>
            <td>{{Maxium_marks}}</td>
        </tr>
    </table>
    <img src="course_histogram.png" alt="course_histogram" />
</body>
</html>
'''

#Generating Error Template
error_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IIT Madras</title>
</head>
<body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
        
    </table>
</body>
</html>
'''

arg_option = sys.argv[1]
arg_id = int(sys.argv[2])

try:

  if arg_option == '-c':

    # ----Generate Histogram----
    plt.hist(courses[arg_id].values(), bins=10)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig('course_histogram.png')

    # ----Generate Course details template
    template = Template(course_template)
    html_out = template.render(Average_marks=((sum(courses[arg_id].values())) /
                                          len(courses[arg_id].values())),
                               Maxium_marks=max(courses[arg_id].values()))
    html_outfile = open('output.html', 'w')
    html_outfile.write(html_out)
    html_outfile.close()

  elif arg_option == '-s':

    # ----Generate Student details template----
    template = Template(students_template)
    html_out = template.render(students_details=students[arg_id].items(),
                               student_id=arg_id,
                               total_marks=sum(students[arg_id].values()))
    html_outfile = open('output.html', 'w')
    html_outfile.write(html_out)
    html_outfile.close()

except:

  # ----Generating Error template----
  html_outfile = open('output.html', 'w')
  html_outfile.write(error_template)
  html_outfile.close()

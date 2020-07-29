#!/Python/Python38/python
import cgi
import sqlite3
import os
import http.cookies as Cookie
import time

def printHeader(title):

    print("Content-type: text/html")
    print("")
    print("""<html><head>
    <title>Internship</title>
          <link rel="stylesheet" type="text/css" href="style.css"></head><body>""")
    print("""<div class="tablebox"><h1>Internships</h1>""")
def printFooter():
    print("</body></html>")

printHeader("List")
form=cgi.FieldStorage()
keyword=form["keyword"].value
print("""<table class="content-table "><thead><tr><th>Company Name</th><th>Position Name</th><th>Description</th><th>Expectation</th><th>Deadline</th></tr></thead>
<tbody>""")
conn=sqlite3.connect("internship.db")
c=conn.cursor()
c.execute("SELECT companyName,positioName,description,expectations,deadline FROM internships WHERE positioName LIKE '?%' OR description LIKE '?%' OR expectations LIKE '?%'",(keyword,keyword,keyword,))
rows = c.fetchall()
for row in rows:
    print("<tr>")
    for col in row:
        print("<td>{}</td>".format(col))
    print("</tr>")
print("""</tbody>
</table>""")
printFooter()

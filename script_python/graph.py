import pygal
import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('/home/arthur/adminsys/DB/info.db')
c = conn.cursor()

# Get the data from the database

c.execute('SELECT * FROM infopc;')
data = c.fetchall()


dates = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in data]


# keep only hours and minutes
dates = [date.strftime("%M") for date in dates]

ram_usage = []

for row in data:
    ram_usage.append(row[3])

# Create a line chart on a scale of 0-100
line_chart = pygal.Line()
line_chart.title = 'RAM usage'
line_chart.x_labels = map(str, dates)
line_chart.y_labels = map(int, range(0, 101, 10))
line_chart.add('RAM usage', ram_usage)
line_chart.render_to_file('/var/www/html/img/graphram.svg')

cpu_usage = []

for row in data:
    cpu_usage.append(row[1])

line_chart = pygal.Line()
line_chart.title = 'CPU usage'
line_chart.x_labels = map(str, dates)
line_chart.y_labels = map(int, range(0, 101, 10))
line_chart.add('CPU usage', cpu_usage)
line_chart.render_to_file('/var/www/html/img/graphcpu.svg')

disk_usage = []

for row in data:
    disk_usage.append(row[2])
    
line_chart = pygal.Line()
line_chart.title = 'Disk usage'
line_chart.x_labels = map(str, dates)
line_chart.y_labels = map(int, range(0, 101, 10))
line_chart.add('Disk usage', disk_usage)
line_chart.render_to_file('/var/www/html/img/graphdisk.svg')

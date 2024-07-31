# Script
Hi, All. This repository includes all qwiklabs assessments code to finish "Automating Real-World Task With Python" Course.

## Module 1: Scale and convert images using PIL
### Description
Create script that uses PIL to perform the following operations:

- Iterate through each file in the folder
- For each file:
  1. Rotate the image 90° clockwise
  2. Resize the image from 192x192 to 128x128
  3. Save the image to a new folder in .jpeg format

## Module 2: Processing Text Files with Python Dictionaries and Uploading to Running Web Service
### Description
Create a Python script that uploads all the feedback stored in this folder to the company's website, without having to turn it into a dictionary one by one.

The script should now follow the structure:
- List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
- Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
- Upload the dictionary to Django REST API with requests module and POST method to make a request to http://<corpweb-external-IP>/feedback
- Make sure an error message isn't returned.

## Module 3: Automatically Generate a PDF and sending it by E-mail
### Description
Update the script cars.py which a part of the script is already done, where it calculates the car model
with the most revenue. 

The updated script should include the following objectives:
- Calculate the car model which had the most sales.
- Calculate the most popular car_year across all car make/models.
- Send the report using the report.generate() function within the main function.
- The report should be named as cars.pdf, and placed in the folder /tmp/.
- The PDF should contain:
  1. A summary paragraph which contains the most sales/most revenue/most popular year values worked out in the previous step.
  2. A table which contains all the information parsed from the JSON file, organised by id_number. The car details should be combined into one column in the form <car_make> <car_model> (<car_year>).
- Send the PDF report through email using emails.generate() and emails.send() function with following details:
  1. From: automation@example.com
  2. To: student@example.com
  3. Subject line: Sales summary for last month
  4. E-mail Body: The same summary from the PDF, but using \n between the lines
  5. Attachment: Attach the PDF path i.e. generated in the previous step

Optional Challenge:
- Sort the list of cars in the PDF by total sales. (DONE)
- Create a pie chart for the total sales of each car made. (DONE)
- Create a bar chart showing total sales for the top 10 best selling vehicles using the ReportLab Diagra library. Put the vehicle name on the X-axis and total revenue (remember, price * total sales!) along the Y-axis.

## Module 4: Automate updates to catalog information
### Description
Create a Python script that will process the images and descriptions and then update company's online website to add the new products.

When the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

Basically, use previous code from module 1 to module 3 + health check script to finish this task
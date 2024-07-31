#!/usr/bin/env python3

import sys
import emails
import reports
import os
from datetime import datetime

def format_title():
  """Format title for pdf"""
  today_day = datetime.now().day
  today_month = datetime.now().strftime("%B")
  today_year = datetime.now().year
  return "Processed Update on {} {}, {}".format(today_month, today_day, today_year)

def process_data(src_dir):
  """Processed data from text files
  """
  paragraph = []
  for file in os.listdir(src_dir):
    f = os.path.join(src_dir, file)
    with open(f) as texts:
        lines = texts.readlines()
        text = "name: {}weight: {}".format(lines[0].replace('\n', '<br/>'), lines[1].replace('\n', '<br/>'))
        paragraph.append(text)

  return paragraph

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  src_dir = "supplier-data/descriptions/"
  paragraph = process_data(src_dir)
  paragraph_with_blankline = '<br/>'.join(paragraph)
  print(paragraph_with_blankline)

  # turn this into a PDF report
  reports.generate_report("/tmp/processed.pdf", format_title(), paragraph_with_blankline)

  # send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
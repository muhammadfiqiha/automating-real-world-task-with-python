#!/usr/bin/env python3

import shutil, psutil, os, socket, emails, sys

# Check cpu usage is over 80%
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

# Check disk usage is lower than 20%
def check_disk_usage():
    du = psutil.disk_usage('/')
    free = du.free / du.total * 100
    return free < 20

# Check available memory is less than 100 MB
def check_available_memory():
    available_memory = psutil.virtual_memory().available
    available_memory_mb = available_memory / 1024 ** 2
    return available_memory_mb < 100

# Check if hostname 'localhost' cannot be resolved to 127.0.0.1
def check_localhost():
    ip_addr_localhost = socket.gethostbyname('localhost')
    return ip_addr_localhost != '127.0.0.1'

# Send email if there is error from the system
def send_email(subject):
    sender = "automation@example.com"
    receiver = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_report(sender, receiver, subject, body)
    emails.send_email(message)

def main(argv):
    if check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        send_email(subject)
    
    if check_disk_usage():
        subject = "Error - Available disk space is less than 20%"
        send_email(subject)
    
    if check_available_memory():
        subject = "Error - Available memory is less than 100MB"
        send_email(subject)
    
    if check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        send_email(subject)

if __name__ == "__main__":
  main(sys.argv)
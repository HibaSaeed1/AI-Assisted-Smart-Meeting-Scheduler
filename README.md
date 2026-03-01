# AI Assisted Smart Meeting Scheduler

## Description

This project is a Smart Meeting Scheduler developed using FastAPI.  
It helps users find suitable meeting times based on participant availability.

The system automatically suggests the best available time slots and prevents double booking.

---

## Problem Understanding

When scheduling meetings with multiple people, it becomes difficult to find a common free time. Time conflicts may occur, or meetings may get double booked.

The goal of this project was to build a system that can:

- Check availability of participants  
- Suggest the best meeting time  
- Avoid already booked slots  

---

## Approach

I used a simple rule-based approach instead of machine learning.

The system works as follows:

- It creates predefined time slots for 3 participants  
- It checks how many participants are free in each slot  
- It gives extra priority to morning time slots  
- It removes already booked slots from the list  
- It shows ranked available slots on the web page  

This approach makes the system behave like a smart scheduler.

---

## Features

- User login simulation  
- Participant availability simulation  
- Automatic meeting time suggestion  
- Slot ranking based on availability  
- Conflict prevention (no double booking)  
- Web interface using HTML and CSS  
- Simulated email message in terminal  

---

## Technologies Used

- Python  
- FastAPI  
- HTML  
- CSS  
- Uvicorn  

---

## Challenges Faced

### Google Calendar Integration

I tried connecting the project with Google Calendar, but I faced configuration and authentication issues. Because of that, I implemented a local simulated scheduling system instead.

### Installation Issues in Terminal

Initially, there were problems while installing packages and running the server. I solved this by using:

    python -m pip install -r requirements.txt

### Internal Server Error

At one stage, the project showed an internal server error due to routing and logic mistakes. After checking the error logs in the terminal, I corrected the function logic and fixed the issue.

---

## What I Implemented Myself

- Slot generation logic  
- Smart scoring system  
- Conflict detection logic  
- Booking functionality  
- Session handling  
- Frontend integration with backend  
- Error debugging and fixing  

---

## How to Run

### Install Requirements

    python -m pip install -r requirements.txt

### Run Server

    python -m uvicorn main:app --reload

### Open in Browser

    http://127.0.0.1:8000

---

## Author

Hiba Saeed

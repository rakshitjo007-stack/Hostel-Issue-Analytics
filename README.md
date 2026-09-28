# Hostel Issue Management System

## Introduction
The Hostel Issue Management System is a Python-based application designed to help hostel students report maintenance issues and allow administrators to manage those issues.

## Problem Statement
In a hostel, students may face problems related to plumbing, electrical systems, cleaning, furniture, and other facilities. A simple system is needed to record these issues and allow the administration to track and update their status.

## Objectives
- Allow students to register and log in.
- Allow students to report hostel issues.
- Generate a unique ticket ID for each issue.
- Allow students to view their reported issues.
- Allow administrators to view all reported issues.
- Allow administrators to update issue status.
- Store issue information permanently using JSON.

## Main Features
- Student registration and login
- Admin login
- Issue reporting
- Issue categorization
- Priority selection
- Ticket generation
- Issue status management
- Permanent JSON storage

## Technologies Used
- Python
- JSON
- Git and GitHub

## Issue Status
- Pending
- In Progress
- Resolved

## Project Structure

```text
Hostel-Issue-Analytics/
├── main.py
├── user.py
├── issue.py
├── storage.py
├── data/
│   └── issues.json
└── README.md
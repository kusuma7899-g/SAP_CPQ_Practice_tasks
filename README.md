🚀 SAP CPQ Automation Practice Projects

This repository contains multiple hands-on automation and integration tasks implemented in SAP CPQ using IronPython scripting, REST APIs, UI customization, and Excel integration.

The objective of this repository is to demonstrate real-time CPQ configuration logic, dynamic pricing, external integrations, and automation capabilities.

📌 Implemented Tasks Overview
1️⃣ Broadband Pricing & Contract Automation

Implemented dynamic pricing logic using custom SQL tables

Fetched bandwidth and tier-based rates

Generated month-wise billing entries based on contract duration

Automated container row creation dynamically

Ensured pricing updates when attributes change

✔ Technologies Used: IronPython, SQL Helper, Containers, Product Attributes

2️⃣ Movie API Integration (External REST API)

Integrated external movie data using REST API

Developed custom button with modal popup

Passed filters (media type, time window, genre) to backend

Used cpq.server.executeScript for backend communication

Displayed API response dynamically in UI

✔ Technologies Used: REST API, JavaScript, Knockout.js, IronPython

3️⃣ Excel to Container Automation

Read structured Excel data using Param.Workbook

Extracted data dynamically from Sheet1

Skipped empty rows with validation logic

Auto-populated product containers

Enabled bulk upload of product data

✔ Technologies Used: Workbook API, Containers, IronPython

4️⃣ Excel-Based Sub-Product Creation

Dynamically created child products from Excel

Assigned Part Number formulas programmatically

Populated product-level attributes

Automated office essentials configuration setup

Cleared and rebuilt container dynamically

✔ Technologies Used: Product Templates, Attributes API, Container API

5️⃣ Excel-Driven Attribute Auto Selection

Read brand and color values from Excel

Validated against predefined lists

Automatically selected product attributes

Stopped processing after first valid record

Implemented controlled configuration logic

✔ Technologies Used: Attribute Selection API, Data Validation

6️⃣ Custom Table REST API Integration

Implemented OAuth 2.0 authentication

Retrieved access token dynamically

Performed GET operation with filter query

Inserted records using POST method

Deleted records using record key

✔ Implemented full CRUD operations on Custom Tables
✔ Used dynamic base URL for environment flexibility
✔ Structured reusable REST architecture

🏗 Technical Highlights

IronPython scripting

Dynamic pricing logic

Custom Table SQL integration

REST API integration (GET / POST / DELETE)

OAuth authentication

JSON handling

Container automation

Excel-based data processing

UI modal customization

Error handling & validation logic

🔐 Security Best Practices

Avoid hardcoding credentials

Use dynamic instance URLs

Implement proper token validation

Handle API errors securely

Do not commit sensitive information to GitHub

🎯 Learning Outcomes

Through these tasks, I gained practical experience in:

SAP CPQ product configuration

Advanced scripting automation

Real-time pricing logic implementation

External system integration

Structured REST architecture

Data-driven configuration management

📌 Purpose of Repository

This repository serves as:

Practice implementation portfolio

Demonstration of CPQ automation skills

Interview reference material

Hands-on learning documentation

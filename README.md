# AI-Powered Tea Leaf Disease Diagnosis System

## Project Description
This project focuses on the development of an AI-powered system to diagnose diseases in tea leaves using Convolutional Neural Networks (CNNs) and a user-friendly web interface. The application is built to help tea farmers and agronomists quickly and accurately identify diseases by analyzing uploaded images of tea leaves. The system utilizes a VGG16-based CNN model, trained on a comprehensive dataset, to provide real-time diagnostic results and suggestions.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [How to Use](#how-to-use)
- [Dataset](#dataset)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

## Features
- **Disease Detection:** Uses a trained CNN model to detect and classify common tea leaf diseases.
- **User-Friendly Web Interface:** Simple web interface allowing users to upload images and view diagnosis results.
- **Real-Time Feedback:** Offers fast and reliable results with suggestions on disease management.
- **Secure Data Storage:** Stores images and diagnostic history in a secure and organized manner.
- **Scalable Design:** Designed to handle multiple concurrent users and large datasets.
- **Reporting and Analysis:** Logs and tracks user submissions for future reference and performance evaluation.

## Technology Stack
The system uses a variety of tools and frameworks:

- **Backend:** Python, Flask, TensorFlow  
- **Frontend:** HTML, CSS, JavaScript (Flask Templates)  
- **Machine Learning Framework:** TensorFlow  
- **Database:** SQL (for logging and user management)  
- **Deployment:** Docker for containerization  
- **Version Control:** Git  
- **Testing Tools:** Selenium, Postman, PyTest  

## Project Structure
The project is organized into the following folders:

- **`/static`:** Contains static files like images, CSS, and JavaScript.  
- **`/templates`:** HTML templates for the web pages.  
- **`/models`:** Pre-trained and fine-tuned AI models.  
- **`/data`:** Datasets used for training and testing.  
- **`/logs`:** Log files for tracking user activities and errors.  
- **`app.py`:** Main Flask application file.  

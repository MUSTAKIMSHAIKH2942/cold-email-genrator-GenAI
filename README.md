## 📧 Cold Mail Generator
The Cold Mail Generator is a web application that allows users to generate customized cold emails based on job descriptions scraped from provided URLs. The app utilizes a natural language model to extract job details and generates a tailored email response for business outreach.
![Architecture Pic](https://github.com/MUSTAKIMSHAIKH2942/cold-email-genrator-GenAI/blob/main/project-genai-cold-email-generator/imgs/architecture.png)
## Features
Automated Cold Email Generation: Generate professional emails based on job listings.
Job Extraction: Automatically extracts job role, experience, skills, and description from a provided job URL.
Link Integration: Adds relevant portfolio links from a predefined list based on job requirements.
Error Handling: Displays user-friendly messages in case of errors.


## Tech Stack
Flask: Backend server to handle requests and serve the application.
JavaScript (Fetch API): For handling asynchronous data submission and response display.
HTML & CSS: Frontend structure and styling.
Prerequisites
Python 3.x
pip (Python package installer)
## Installation

Clone the Repository:
git clone https://github.com/Mustakimshaikh2942/cold-mail-generator.git
cd cold-mail-generator

## Install the Required Packages:

pip install -r requirements.txt

Environment Setup: Create a .env file in the project directory to store API keys and other sensitive information. For instance:

makefile

GROQ_API_KEY=your_groq_api_key_here


Set Up the Portfolio Data: Place your my_portfolio.csv file under app/resource/. This file should contain your tech stack and related links.

Project Structure
![Directory Structure Pic](https://github.com/MUSTAKIMSHAIKH2942/cold-email-genrator-GenAI/blob/main/project-genai-cold-email-generator/imgs/file_directory.png)


## Usage
 Run the Flask Application:

python app.py
Access the Web App: Open your browser and go to http://127.0.0.1:5000.

Generate an Email:

Enter the URL of a job listing in the input field.
Click on "Generate Email" to receive a personalized cold email tailored to the job description.
API Key Setup
Ensure that your API key for the language model (e.g., GROQ) is stored in the .env file. This will enable the app to connect to the language model for job extraction and email generation.

Example .env File

GROQ_API_KEY=your_groq_api_key_here

Troubleshooting
Missing File Errors: Ensure my_portfolio.csv is placed in the correct folder (app/resource/).
API Errors: Double-check your API key in the .env file. Confirm that your key is active and has the necessary permissions.

Contributing
Feel free to submit pull requests or open issues to improve this project.

## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   python app.py
   ```
## Input
![Input form Pic](https://github.com/MUSTAKIMSHAIKH2942/cold-email-genrator-GenAI/blob/main/project-genai-cold-email-generator/imgs/input_email.png)

## Output
![output form Pic](https://github.com/MUSTAKIMSHAIKH2942/cold-email-genrator-GenAI/blob/main/project-genai-cold-email-generator/imgs/output_email.png)

   

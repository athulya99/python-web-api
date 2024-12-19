Python Flask Web App with Azure Deployment
A simple Flask web application that displays a "Hello, LIVE DEMO!!!" message, deployed to Azure Web Apps using GitHub Actions for CI/CD.
Description
This project demonstrates a basic Flask web application with automated deployment to Azure Web Apps using GitHub Actions. The application consists of a single endpoint that returns a greeting message.
Prerequisites

Python 3.12
Azure subscription
GitHub account
Azure CLI (for local testing with Azure)

Project Structure

├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .github/workflows   # GitHub Actions workflow files
└── README.md          # This file
Local Development

Create and activate a virtual environment:

bashCopypython -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The application will be available at http://localhost:5000

Deployment
The application is automatically deployed to Azure Web Apps through GitHub Actions when changes are pushed to the main branch. The deployment process includes:

Building the Python application
Creating a deployment package
Authenticating with Azure
Deploying to Azure Web App service

Azure Configuration
To deploy this application, you need to configure the following secrets in your GitHub repository's settings (Settings > Secrets and Variables > Actions):

AZUREAPPSERVICE_CLIENTID - Your Azure App Service client ID
AZUREAPPSERVICE_TENANTID - Your Azure tenant ID
AZUREAPPSERVICE_SUBSCRIPTIONID - Your Azure subscription ID

To obtain these values:

Log in to the Azure Portal
Navigate to your App Service
Go to Settings > Configuration
Find these values in your App Service configuration

⚠️ Security Note: Never commit these secrets directly to your repository or include them in your README file. Always use GitHub Secrets to store sensitive information.
Dependencies

Flask==2.3.2
gunicorn==23.0.0

CI/CD Pipeline
The GitHub Actions workflow includes:

Setting up Python 3.12
Installing dependencies
Creating a deployment package
Authenticating with Azure
Deploying to Azure Web Apps

The deployment is triggered automatically on:

Push to main branch
Manual trigger (workflow_dispatch)

Contributing

Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Open a Pull Request

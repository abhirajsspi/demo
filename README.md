# My Web App

This is a basic web application built with Express.js, a Node.js web framework. The application has two routes:

- `/`: The root route that displays a welcome message.
- `/about`: The about route that displays information about the application.

## Prerequisites

- Node.js 16.x
- Git
- An AWS account

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git






   CI/CD Pipeline
This project includes a GitHub Actions workflow for Continuous Integration and Continuous Deployment (CI/CD). The workflow is defined in the .github/workflows/ci-cd.yml file.
The pipeline has two jobs:

Test: This job runs on every push to the main branch. It checks out the repository code, sets up Node.js, installs dependencies, and runs the unit tests.
Deploy: This job runs only if the test job is successful. It checks out the repository code, sets up Node.js, installs dependencies, builds the application, and deploys the application to an AWS Lambda function.

To set up the pipeline, you need to create the following GitHub secrets in your repository:

AWS_ACCESS_KEY_ID: Your AWS access key ID.
AWS_SECRET_ACCESS_KEY: Your AWS secret access key.
AWS_REGION: The AWS region where your resources are located.

You also need to have an AWS Lambda function named my-web-app set up in your AWS account.
Once these secrets are set, the pipeline will automatically run on every push to the main branch, and if the tests pass, the application will be deployed to your AWS Lambda function.
CI/CD Process and Tool Choices
The CI/CD process in this project involves the following steps:

Continuous Integration (CI): On every push to the main branch, the GitHub Actions workflow checks out the repository code, sets up the Node.js environment, installs dependencies, and runs the unit tests. This step ensures that the code changes do not introduce any new bugs or break existing functionality.
Continuous Deployment (CD): If the unit tests pass in the CI step, the workflow proceeds to build the application, package it as a ZIP file, and deploy the package to an AWS Lambda function.

The tools used in this CI/CD process are:

GitHub Actions: A powerful workflow automation tool provided by GitHub. It allows defining custom workflows for various events, such as code pushes, pull requests, or scheduled tasks.
AWS Lambda: A serverless computing service provided by AWS, which allows running code without provisioning or managing servers.

These tools were chosen for the following reasons:

GitHub Actions: It is tightly integrated with GitHub, making it easy to set up and manage workflows. It also provides a vast library of pre-built actions for various tasks, reducing the need for custom scripts.
AWS Lambda: It offers a cost-effective and scalable solution for running applications without managing underlying infrastructure. It automatically scales based on incoming traffic, making it suitable for applications with varying workloads.

This setup leverages the serverless architecture of AWS Lambda, allowing for easy deployment and scaling of the application without managing servers or infrastructure. It can be scaled for larger applications by adding more Lambda functions, utilizing other AWS services like API Gateway for API management, and leveraging AWS Step Functions for orchestrating complex workflows

import subprocess
import os

# Get the project name from the user
project_name = input("Enter the name of your React project: ")

# Create a new React project
subprocess.run(['npx', 'create-react-app', project_name])

# Change to the project directory
os.chdir(project_name)

# Install additional dependencies
subprocess.run(['npm', 'install', 'axios', 'react-router-dom'])

# Start the development server
subprocess.run(['npm', 'start'])


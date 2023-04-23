import subprocess
import os
import click

@click.command()
def install_django():
    """
    This script creates a Django project and app, creates a superuser, and runs database migrations.
    """
    click.clear()

    click.echo("Welcome to the Django installation wizard!\n")

    project_name = click.prompt("Enter the name of your Django project")
    app_name = click.prompt("Enter the name of your Django app")

    click.clear()

    click.echo(f"Creating Django project: {project_name}")
    subprocess.run(['django-admin', 'startproject', project_name])

    click.echo(f"Creating Django app: {app_name}")
    subprocess.run(['python', f'{project_name}/manage.py', 'startapp', app_name])

    click.clear()

    click.echo("Creating superuser:")
    username = click.prompt("Enter the superuser username")
    email = click.prompt("Enter the superuser email")
    password = click.prompt("Enter the superuser password", hide_input=True, confirmation_prompt=True)
    
    click.echo("Running database migrations...")
    subprocess.run(['python', f'{project_name}/manage.py', 'makemigrations'])
    subprocess.run(['python', f'{project_name}/manage.py', 'migrate'])
  
    click.clear()
    
    click.echo("Creating superuser...")
    input_data = f"{username}\n{email}\n{password}\n{password}\n".encode('utf-8')
    #subprocess.run(['python', f'{project_name}/manage.py', 'createsuperuser', '--no-input'], input=input_data)
    #subprocess.run(['python', f'{project_name}/manage.py', 'createsuperuser', '--no-input', '--username', username], input=input_data)    
    subprocess.run(['python', f'{project_name}/manage.py', 'createsuperuser', '--no-input', '--username', username, '--email', email], input=input_data)

    
    click.echo("\nCongratulations! Django has been successfully installed!")

if __name__ == '__main__':
    install_django()


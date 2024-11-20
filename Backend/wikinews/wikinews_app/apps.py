from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command
import subprocess


class WikinewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wikinews_app'

    def ready(self):
       

        # Path to your log file
        log_file_path = r'C:\Users\naikn\OneDrive\Desktop\Repos\WikipediaNewsArticlesAnalysis\Backend\wikinews\wikinews_app\logs\producer_logs.log'

        # Get the root of your project (adjust if necessary)
        project_root = r'C:\Users\naikn\OneDrive\Desktop\Repos\WikipediaNewsArticlesAnalysis\Backend\wikinews'

        # Open log file in append mode so logs are not overwritten
        with open(log_file_path, 'a') as log_file:
            process = subprocess.Popen(
                ['python', r'C:\Users\naikn\OneDrive\Desktop\Repos\WikipediaNewsArticlesAnalysis\Backend\wikinews\wikinews_app\Algos\Producer.py'],
                stdout=log_file,  # Redirect standard output
                stderr=log_file,  # Redirect standard error
                universal_newlines=True,  # Ensure text mode
                cwd=project_root  # Set the working directory to your project root
            )
            process.communicate() 
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Set the environment variable to point to the specific settings file (e.g., development)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurance_project.settings.development')

def main():
    """Run administrative tasks."""
    # NOTE: The line setting DJANGO_SETTINGS_MODULE has been removed from here.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
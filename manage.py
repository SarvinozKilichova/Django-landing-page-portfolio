#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    from django.core.management import execute_from_command_line
 
    execute_from_command_line(sys.argv)



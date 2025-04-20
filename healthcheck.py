#!/usr/bin/env python3
"""
Health check script for PDFMathTranslate service.
Tests if the web server is responding and the UI elements are present.
"""

import sys
import requests
from urllib.parse import urljoin
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("healthcheck")

# URL to check
BASE_URL = "http://localhost:7860"

def check_server_health():
    """Check if the server is up and running with the expected UI elements."""
    try:
        # Get the main page
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()  # Will raise an exception for 4XX/5XX responses
        # Check if the response contains expected content from the UI
        expected_elements = [
            "PDFMathTranslate",  # Title should be present
            "Translate",         # Button should be present
            "Service"            # Service dropdown should be present
        ]
        
        for element in expected_elements:
            if element not in response.text:
                logger.error(f"Expected UI element '{element}' not found in response")
                return False
        
        logger.info("Health check passed: Server is up and UI elements are present")
        return True
        
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Health check failed: {str(e)}")
        return False

if __name__ == "__main__":
    if check_server_health():
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Failure
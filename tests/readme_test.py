import re

def test_server_integration_section_exists():
    """Verify that the Server Integration section exists in the README."""
    with open('readme.md', 'r') as readme:
        content = readme.read()
        
    # Check for main Server Integration section
    assert '## Server Integration' in content, "Server Integration section is missing"

def test_server_integration_section_structure():
    """Validate the structure of the Server Integration section."""
    with open('readme.md', 'r') as readme:
        content = readme.read()
        
    # Check for key subsections
    subsections = [
        '### Overview',
        '### Connection Configuration',
        '### Authentication',
        '### Connection Examples',
        '### Troubleshooting',
        '### Best Practices'
    ]
    
    for section in subsections:
        assert section in content, f"Missing subsection: {section}"

def test_connection_examples():
    """Verify presence of connection code examples."""
    with open('readme.md', 'r') as readme:
        content = readme.read()
        
    # Check for code blocks in multiple languages
    assert '```python' in content, "Python connection example missing"
    assert '```javascript' in content, "JavaScript connection example missing"

def test_authentication_methods():
    """Ensure multiple authentication methods are documented."""
    with open('readme.md', 'r') as readme:
        content = readme.read()
        
    authentication_methods = [
        'API Key Authentication',
        'OAuth 2.0'
    ]
    
    for method in authentication_methods:
        assert method in content, f"Authentication method '{method}' not documented"
import re

def extract_emails(file_path, output_path='extracted_emails.txt'):
    """
    Extract unique email addresses from a large file and save to a text file.
    
    :param file_path: Path to the input file
    :param output_path: Path to save extracted emails
    :return: Set of unique email addresses
    """
    # Regular expression for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Set to store unique emails to avoid duplicates
    unique_emails = set()
    
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Find all email addresses in the content
        emails = re.findall(email_pattern, content)
        
        # Add to the set of unique emails
        unique_emails.update(emails)
    
    # Save emails to a text file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for email in sorted(unique_emails):
            output_file.write(email + '\n')
    
    # Print summary
    print(f"Found {len(unique_emails)} unique email addresses")
    print(f"Emails saved to {output_path}")
    
    return unique_emails

# Example usage
file_path = 'your_large_file.json'
extracted_emails = extract_emails(file_path)

# Optional: print emails to console
print("\nExtracted Emails:")
for email in sorted(extracted_emails):
    print(email)

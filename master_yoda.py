# Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    return ' '.join(text.split()[::-1])

# Check
master_yoda('I am home')

# Check
master_yoda('We are ready')
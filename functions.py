# def greet(person):
#     return f"Hello, {person}"


# def divide(a,b):
#     if type(a) is int and type(b) is int:
#         return a/b
#     return 'a and b must be int'




def send_email(to_email, from_email, subject, body):
    email = f"""
    to: {to_email}
    from: {from_email}
    subject: {subject}
    _____________________
    body: {body}
"""
    print(email)


send_email(subject="meow", to_email="bluemeow@gmail.com", from_email="Casey@maritime.com", body="Hi Blue you are a cat")
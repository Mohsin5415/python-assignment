# Can one block of except statements handle multiple exception? 

try:
    name = 'Bob'
    name += 5
except (NameError, TypeError) as error:
    print(error)
    rollbar.report_exc_info()
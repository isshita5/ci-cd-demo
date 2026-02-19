output = "Hello CI/CD"
print(output)

if output != "Hello CI/CD":
    raise Exception("Test failed")

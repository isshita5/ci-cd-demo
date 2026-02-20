output = "Hello CI/CD1"
print(output)

if output != "Hello CI/CD":
    raise Exception("Test failed")

def main():
    s = snake_case (input("camelCase : "))
    print (s)

def snake_case (camel) :
    for c in camel :
        if c.isupper() == True:
            camel = camel.replace (c, "_" + c.lower())
    return camel


main()

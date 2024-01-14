def convert ():
        text = input()
        emoji = text.replace(":)", "🙂").replace(":(", "🙁")
        return emoji


def main():
     print(convert())


main()

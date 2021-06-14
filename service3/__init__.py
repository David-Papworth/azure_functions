import logging
import string, random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    setence = ""
    num = 0
    while (num < 6):
        if num<5:
            letter = random.choice(string.ascii_letters)
            setence += letter
            num += 1
        else:
            num = 6
            return func.HttpResponse(f"{setence}")
    

import click
import random
import string

dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu', 'a':'alpha', 'b':'bravo','c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf',"h":"hotel", 'i':'india', 'j':'juliet', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'xray', 'y':'yankee', 'z':'zulu', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '0':'0'}


@click.command()
@click.option('--num', is_flag=True, help='Use this to include 0-9 characters')
@click.option('--special',is_flag=True, help="Use this to allow special characters ex: {} [] - ? /\ +")
@click.option('--length', default=10, help='Use to change password length. Default and minimum is 10')

def generate(length, num, special):
    if(length < 10):
        click.echo("Minimum length is 10")
        length = 10
    if(num):
        if(special):
            click.echo(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits, k=length)))
            exit()
        vanilla_num_temp = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
        click.echo(vanilla_num_temp)
        click.echo(" ".join(map(dictionary.get,vanilla_num_temp)))
        exit()
    elif(special):
            click.echo(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.punctuation, k=length)))
            exit()

    vanilla_temp = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))
    click.echo(vanilla_temp)
    click.echo(" ".join(map(dictionary.get,vanilla_temp)))

if __name__ == '__main__':
    generate()

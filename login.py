import requests
import getpass

def login_zendesk(b_url,user,pwd):

    print('\n')
    print('                 ** Signing into Zendesk **                  ')
    print('\n')


    url = b_url+'users.json'

    #Authenticating user
    response = requests.get(url, auth=(user,pwd))
    if response.status_code == 200:
        data = response.json()
        user_name = data['users'][0]['name']

        print(' ########################################################################','\n',
        '#                           ZENDESK TICKET VIEWER                      #','\n',
        '########################################################################','\n'
        )

        print('\n','Welcome ' +user_name+ '!')
        return()
    else:
        print('status:',response.status_code,'Login authorization failed! Please check your login credentials and try again!')
        exit()

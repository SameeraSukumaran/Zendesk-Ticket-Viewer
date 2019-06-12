import requests

#for not displaying the token when being entered we are importing getpass
import getpass
import login
import forPagination
import singleTkt

subdomain = input ("Please enter your subdomain: ")
usr = input ('Please enter your login email: ')
user = usr + '/token'
pwd = getpass.getpass('please enter your API token: ')

#baseURL
b_url='https://'+subdomain+'.zendesk.com/api/v2/'
login.login_zendesk(b_url,user,pwd)
i=1
while i:
    print('\n','Please enter your choice:'+'\n'+'1. List all my tickets'+'\n'+'2. Display details for a ticket id' +'\n'+'3. Exit Ticket Viewer'+'\n')
    choice = input()
    if choice == '1':
        forPagination.pagination_zendesk(b_url,user,pwd)
    elif choice == '2':
        id_t = input('Please enter the Ticket ID: ')
        singleTkt.singleView(b_url,user,pwd,id_t)
    elif choice == '3':
        print('Exiting from Zendesk Ticket Viewer! Have a nice day!')
        exit()
    else:
        print('\n')
        print('Invalid choice! Please enter number from the above displayed choices!!')

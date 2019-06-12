import login
import getpass
import requests
import forPagination
import singleTkt

# Hard coded user cred for testing. To be removed
'''
subdomain = 'stardustsupport'
user = 'sam.era272@gmail.com'
pwd = 'IntSam@2019'
'''

subdomain = input ("Please enter your subdomain: ")
usr = input ('Please enter your login email: ')
user = usr + '/token'
pwd = getpass.getpass('please enter your API token: ')

b_url='https://'+subdomain+'.zendesk.com/api/v2/'
login.login_zendesk(b_url,user,pwd)



i=1
while i:
    print('\n','Please enter your choice:'+'\n'+'1. List all my tickets'+'\n'+'2. Display details for a ticket id' +'\n'+'3. Exit Ticket Viewer'+'\n')
    choice = input()
    #stv = input('2.Single Ticket View')
    #ext = input('3.Exit')

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

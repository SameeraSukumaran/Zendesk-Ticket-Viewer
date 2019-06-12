import requests

def singleView(b_url,user,pwd,id):

    '''
    #defining request parameters
    url = 'https://stardustsupport.zendesk.com/api/v2/tickets/'+str(id)+'.json'
    user = 'sam.era272@gmail.com'
    pwd = 'IntSam@2019'
    '''

    url = b_url + 'tickets/'+str(id)+'.json'

    #invoking the http get method
    response = requests.get(url, auth=(user,pwd))

    #check for status other than success
    if response.status_code == 400 or response.status_code == 404:
    	print('Record not found, Please enter a valid Ticket ID!')
    	return()
    elif response.status_code >= 500:
        print('status:',response.status_code,'Server temporarily unavailable,Please try again later!')
        return()

    # fetching ticket data

    data = response.json()
    #print('Id = ' + str(data['ticket']['id']))
    print(
    'TICKET_ID = ',data['ticket']['id'],'\n',
    'CREATED_AT = ',data['ticket']['created_at'],'\n',
    'SUBJECT = ',data['ticket']['subject'],'\n',
    'PRIORITY = ',data['ticket']['priority'],'\n',
    'STATUS = ',data['ticket']['status'],'\n',
    'DESCRIPTION = {','\n',(data['ticket']['description']),'\n',
    '}')

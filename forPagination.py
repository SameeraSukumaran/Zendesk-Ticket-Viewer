import requests
#Function for displaying the tickets list with pagination of 25 tickets per view
def pagination_zendesk(b_url,user,pwd):

    url = b_url + 'tickets.json?per_page=25&sort_by=created_at'
    response = requests.get(url, auth=(user,pwd))

    #handling of error response codes
    if response.status_code >= 500:
        print('status:',response.status_code,'Server temporarily unavailable,Please try again later!')
        return()
    elif response.status_code == 400 or response.status_code == 404:
        print('status:',response.status_code,'Record not found')
        return()

    #obtaining the response into data
    data = response.json()

    #saving the ticket count in f
    f=data['count']
    print('\n')
    print('*****There are a total of '+str(f)+' tickets in your account*****')
    print('\n')
    print('-----------------------------------Ticktets list---------------------------------------------')
    print('Id	|	   created_at	        |	 status	|	Ticket Summary')
    print('---------------------------------------------------------------------------------------------')

    #for the first pagination
    if data['previous_page'] is None:
        for tkts in data['tickets']:
            print(tkts['id'],'	|	',tkts['created_at'],'	|	',tkts['status'],'	|	',tkts['subject'])
    n = 0
    while data['next_page'] is not None:
        n = n+1
        print('----------------------------------------[Page '+str(n)+']--------------------------------------------------')
        print('\n')
        ans = input('Do you want to view the next page? Please enter Y or N ')
        if ans.upper() == 'Y':
            url = data['next_page'] + 'sort_by=created_at'
            response = requests.get(url, auth=(user,pwd))
            if response.status_code >= 500:
                print('status:',response.status_code,'Server temporarily unavailable,Please try again later!')
                return()
            elif response.status_code == 400 or response.status_code == 404:
                print('status:',response.status_code,'Record not found')
                return()
            data = response.json()
            for tkts in data['tickets']:
                print(tkts['id'],'	|	',tkts['created_at'],'	|	',tkts['status'],'	|	',tkts['subject'])
        elif ans.upper() == 'N':
            print('Cheers lets exit then!')
            return()
        else:
            print('Invalid input! Please enter Y or N')
            return()

    #for ticket count being greater that 25 and multiple of 25
    if((f>25) and (f%25==0)):
        k = (f//25)
        print('----------------------------------------[Page '+str(k)+']--------------------------------------------------')
        print('\n')
        print('****************************************[End of tickets]***************************************************')
    #for ticket count not multiple of 25    
    else:
        k = (f//25)+1
        print('----------------------------------------[Page '+str(k)+']--------------------------------------------------')
        print('\n')
        print('****************************************[End of tickets]***************************************************')

# Zendesk-Ticket-Viewer
For Zendesk Internship Project

# Project Description

Zendesk-Ticket-Viewer is a CLI ticket viewer which has the following functionalities:
  Loging into the zendesk user's account.
  Requesting Ticket list view with pagination upto 25 tickets per page.
  Viewing a single ticket.

# Prerequisites:

Please make sure you have zendesk account.

Please make sure you have tickets in your account.If not please use the below link via postman get with basic auth and your userid(email id) and password(API token) using your credentials to populate your account with 100 tickets

https://yoursubdomain.zendesk.com/api/v2/imports/tickets/create_many.json

Keep your Subdomain Name,Email id for zendesk account and API token handy.

API token can be obtained from the Support admin interface at Admin > Channels > API.

Go to your Mac Terminal

Make sure Python3 has been installed in your system by running the following:
$python3 --version   
you need to see the version of python3

# Installation
Install requests library using python packet manager
$pip3 install requests

Create a folder zendeskTicketViewer

Run the below commands to create zendeskTicketViewer directory and change directory to zendeskTicketViewer
  
  $mkdir zendeskTicketViewer
  $cd zendeskTicketViewer
  
Save all the files[login.py,singleTkt.py,forPagination.py and ticketViewerWrapper.py] from Zendesk-Ticket-Viewer repository into ZendeskTicketViewer folder

# Happy path Testing 

$python3 ticketViewerWrapper.py

please enter your subdomain:YOUR_SUBDOMAIN_NAME

please enter your login email:YOUR_EMAIL_ID

please enter your API token:YOU_CAN_COPY_PASTE_YOUR_TOKEN
if valid credentials you will login successfully into zendesk ticket viewer


Please enter your choice:
1. List all my tickets
2. Display details for a ticket id
3. Exit Ticket Viewer

For choice 1
*****There are a total of n tickets in your account*****
 and the tickets in your account will be displayed with 25 tickets per page.
 For viewing the next page enter Y when prompted,else enter N.
 
For choice 2
Please enter the Ticket ID:ENTER_VALID_TICKET_ID
The details of the ticket with ID provided will be displayed!

For choice 3
Exit successfully.























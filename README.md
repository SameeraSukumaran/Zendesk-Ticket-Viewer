# Zendesk-Ticket-Viewer
For Zendesk Internship Project

# Project Description

Zendesk-Ticket-Viewer is a CLI ticket viewer which has the following functionalities:
  Loging into the zendesk user's account.
  Requesting Ticket list view with pagination upto 25 tickets per page.
  Viewing a single ticket.

# Prerequisites:

Make sure you have zendesk account.
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

# Testing 

$python3 ticketViewerWrapper.py
$please enter your subdomain:YOUR_SUBDOMAIN_NAME
$please enter your login email:YOUR_EMAIL_ID
$please enter your API token:YOU_CAN_COPY_PASTE_YOUR_TOKEN























import requests
from bs4 import BeautifulSoup
from gi.repository import GLib, Notify, GdkPixbuf
import time
from twilio.rest import Client

#using email alerts disbanded for security reasons
#forced to use text message alerts, via twilio

account_sid = "insert account_sid as obtained from twilio"
auth_token = "insert auth_token as obtained from twilio"

client = Client(account_sid, auth_token)
string1='<a class="button button--quidel button--round-s center-block">Buy Tickets <br/> <span class="button-inner-text center-block">Coming soon</span></a>'
f=0
while True:
	Notify.init("Status")
	r=requests.get('https://in.pycon.org/2018/#home')
	soup=BeautifulSoup(r.text, 'html.parser')
	
	string2=str(soup.find_all('a',class_='button button--quidel button--round-s center-block')[0])

	if (string1==string2):
		body="Link not Active"
	else:
		body="Link Active"
		response = client.messages.create(to= "+919875449228",from_= "+15622685503",body= "Pycon Tickets up for sale")
		f=1
	summary="PyCon 2018"
	time.sleep(90)
	notification=Notify.Notification.new(summary,body)
	image=GdkPixbuf.Pixbuf.new_from_file("/home/indraneel/Desktop/pycon.jpg")
	notification.set_icon_from_pixbuf(image)
	notification.set_image_from_pixbuf(image)
	notification.set_urgency(1)
	notification.show()
	time.sleep(5)
	notification.close()
	if(f==1):
		break;

Notify.uninit()


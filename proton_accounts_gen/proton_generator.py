from selenium import webdriver
import random
import string
import time

#Login and password generator
def get_random_string(length=12):
    ascii = string.ascii_letters
    str = ''.join(random.choice(ascii) for i in range(length))
    return str

def has_page_loaded_check(driver):
    try:
        elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form')
        print("Registration form loaded")
        time.sleep(5)
        return
    except:
        has_page_loaded_check(driver) #check again

def save_pass_to_file(login, password, filename='proton_acc.txt'):
    with open(filename,'a') as f:
        f.write(f"{login}:{password}")

def create_account(proton_register_url="https://account.protonvpn.com/signup?plan=free&currency=EUR&language=en"):

    #running on geckodriver
    driver = webdriver.Firefox()

    driver.get(proton_register_url)
    has_page_loaded_check(driver) #Wait until page load


    #Login and password
    login = get_random_string() #login 
    password = get_random_string() #password

    print(f"Generated login: {login}\nGenerated password: {password}")

    #Fill login (its via additional iframe)
    username_iframe = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/iframe')
    driver.switch_to.frame(username_iframe)
    form_username_elem = driver.find_element_by_id('email')

    form_username_elem.click()
    form_username_elem.clear()
    form_username_elem.send_keys(login)

    driver.switch_to.default_content()

    #Fill password x2
    form_password_elem = driver.find_element_by_xpath('//*[@id="password"]')
    form_password_repeat_elem = driver.find_element_by_xpath('//*[@id="repeat-password"]')
    
    form_password_elem.click()
    form_password_elem.clear()
    form_password_elem.send_keys(password)

    form_password_repeat_elem.click()
    form_password_repeat_elem.clear()
    form_password_repeat_elem.send_keys(password)

    try:
        #Sometimes it asks for recovery email
        form_email_elem = driver.find_element_by_xpath('//*[@id="recovery-email"]')
        recovery_email = get_random_string()+"@xyz.com"#random email
        
        form_email_elem.click()
        form_email_elem.clear()
        form_email_elem.send_keys(recovery_email)
    except:
        print("Recovery email input not found - continuing")

    #Submitting form
    time.sleep(2) #wait a while
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button').click()

    print("Form submitted now make the verification")

    #Captcha loop
    while True:
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/header/div/ul/li[3]/button/span[1]/span')
            if(elem.text==login):
                break
        except:
            print('Waiting for verification...')
            time.sleep(5)
    
    save_pass_to_file(login, password)
    print(f"Account '{login}' created" )
    driver.close()

if(__name__=="__main__"):
    n = int(input("Enter a number of accounts needed: "))
    for i in range(n):
        create_account()
        time.sleep(1)


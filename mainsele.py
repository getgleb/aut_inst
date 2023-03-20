from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from useragent1.main import user_agent
from config import log1, pass1
from selenium.webdriver.common.keys import Keys
except1 = 0
global infosess1
global log1
global pass1
#фон
#option.headless = True

# browser.get('https://ciox.ru/check-user-agent')

cookies_ = '/html/body/div[4]/div/div/div[3]/div[2]/button'
log_xpath = '/html/body/div[1]/section/main/article/div/div/div[2]/form/div[1]/div[3]/div/label/input'
pass_xpath = '/html/body/div[1]/section/main/article/div/div/div[2]/form/div[1]/div[4]/div/label/input'
enter_butt = '/html/body/div[1]/section/main/div[1]/div/div/div[2]/form/div[1]/div[6]/button/div'
nnow_butt = '/html/body/div[1]/section/main/div/div/div/button'
nnow_butt2 = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'
subs_butt = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div'
# /html/body/div[4]/div/div/button[1]
log_2 = '/html/body/div[1]/section/main/article/div/div/div[2]/form/div[1]/div[4]/div/label/input'
pass_2 = '/html/body/div[1]/div/div/section/main/article/div/div/div[2]/form/div[1]/div[4]/div/label/input'
objject = 'div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm'

except1 = 0
global infosess1
print('__________________________________________________________________')
print(user_agent)
print('__________________________________________________________________')
option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
# option.set_preference('general.useragent.override', f'{user_agent}')
option.set_preference('general.useragent.override', user_agent)
# фон
# option.headless = True


browser = webdriver.Firefox(options=option)
browser.get('http://instagram.com/')
time.sleep(4)

def protect():
    # browser.get('https://ciox.ru/check-user-agent')
    # infosess = 0
    # infosess1 = 0
    while True:
        try:
            ex_cookie()
            ex_enter()

        except:
            ex_enter()

        finally:
            # if bool(infosess) == 1:
            #     log_form = browser.find_element(By.XPATH, cookies_).click()
            # elif bool(infosess1) == 1:
            #     log_form = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div/div/div[2]/div[3]/button[1]').click()
            #     log_form = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/article/div/div/div[2]/form/div[1]/div[3]/div/label/input').send_keys(
            #         log1)
            #     time.sleep(1)
            #     pass_form = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/section/main/article/div/div/div[2]/form/div[1]/div[4]/div/label/input').send_keys(
            #         pass1)
            # else:
                # infosess = browser.find_element(By.CSS_SELECTOR, 'div._7UhW9.xLCgt.MMzan._0PwGv.uL8Hv.l4b0S')
            if except1 == 0:
                print('провалился if')
                time.sleep(1)
                log_form = browser.find_element(By.XPATH, log_xpath).send_keys(log1)
                # time.sleep(1)
                pass_form = browser.find_element(By.XPATH, pass_xpath).send_keys(pass1)
                time.sleep(2)
                enter = browser.find_element(By.XPATH, enter_butt).click()
                time.sleep(5)
                nnow = browser.find_element(By.XPATH, nnow_butt).click()
                time.sleep(1)
                # nnow = browser.find_element(By.XPATH, nnow_butt2).click()
                name = input('Введите ник в инстаграмме: ')
                browser.get(f'http://instagram.com/{name}/')
                time.sleep(1)
                nnow = browser.find_element(By.XPATH, subs_butt).click()
                # position: relative; display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px;
                # searchsubs = browser.f
                time.sleep(5)

                time.sleep(5)
                # objject1 = browser.find_element(By.XPATH, objject).click()
                # searchsubs.send_keys(Keys.END)
                searchsubs = browser.find_elements(By.CSS_SELECTOR, 'div._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm')
                time.sleep(5)
                browser.execute_script("window.scrollBy(0,9000)", "")
                time.sleep(10)
                # browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
                # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print(len(searchsubs))
                for subs in searchsubs:
                    print(subs.text)
            else:
                print('провалился else')
                enter = browser.find_element(By.XPATH, enter_butt).click()
                time.sleep(5)
                nnow = browser.find_element(By.XPATH, nnow_butt).click()
                time.sleep(1)
                nnow = browser.find_element(By.XPATH, nnow_butt2).click()
                name = input('Введите ник в инстаграмме: ')
                browser.get(f'http://instagram.com/{name}/')
                time.sleep(1)
                nnow = browser.find_element(By.XPATH, subs_butt).click()
                # position: relative; display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px;
                # searchsubs = browser.f
                time.sleep(5)
                searchsubs = browser.find_elements(By.CSS_SELECTOR, 'div._ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm')
                #
                time.sleep(5)
                objject = browser.find_element(By.XPATH, 'div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm').click()
                # searchsubs.send_keys(Keys.END)
                time.sleep(5)
                browser.execute_script("window.scrollBy(0,100)", "")
                time.sleep(10)
                # browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
                # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                k = time.sleep(5)
                for sec in k:
                    print(sec)
                    print(len(searchsubs))
                    for subs in searchsubs:
                        print(subs.text)
    time.sleep(25)
    browser.quit()
# browser.save_screenshot('1.png')
# browser.refresh()

def ex_cookie():
    # kykи
    infosess = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div[2]/div[1]/h2').text
    # infosess = 1
    # print(infosess)
    print(f'infosess = {infosess}')
    log_form = browser.find_element(By.XPATH, cookies_).click()
    time.sleep(4)

def ex_enter():
    infosess1 = browser.find_element(By.XPATH,
                                     '/html/body/div[1]/section/main/article/div/div/div[2]/div[1]/div').text
    # print(infosess1)
    print(f'infosess1 = {infosess1}')
    time.sleep(3)
    log_form = browser.find_element(By.XPATH,
                                    '/html/body/div[1]/section/main/article/div/div/div[2]/div[3]/button[1]').click()
    pass_form = browser.find_element(By.XPATH, log_2).send_keys(log1)
    time.sleep(1)
    pass_form = browser.find_element(By.XPATH, pass_2).send_keys(pass1)
    except1 = 1
    time.sleep(4)

def main():
    protect()

if __name__ == '__main__':
    main()

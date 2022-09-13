rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from playsound import playsound
from csv import writer


lower_lim, upper_lim = map(int, input("enter the limits: ").split())
final_upper_lim = upper_lim+1
options = Options()
options.add_argument("--headless")
# options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/jarvis/pymycod/chromedriver")

driver.get("https://stimulate.icsi.edu/memTemp/MemberSearch")
wait = WebDriverWait(driver,10)
element1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="SearchCriteriaId"]/div/div/div[1]/div[3]/div/div/div/select')))
element1.click()
# element2_acs = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SearchCriteriaId"]/div/div/div[1]/div[3]/div/div/div/select/option[2]')))
# element2_acs.click()
element2_fcs = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SearchCriteriaId"]/div/div/div[1]/div[3]/div/div/div/select/option[3]')))
element2_fcs.click()
# element3_acs = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SearchCriteriaId"]/div/div/div[1]/div[4]/div/div/div/input[3]')))
# element3_acs.click()
# element3_acs.send_keys("1")

f_object = open("csvinfo/1-1000_fcs_icsi_member.csv","a+",newline='')
writer_object = writer(f_object)


# name_of_members=[]
# org_of_members=[]
# email_of_members=[]
# phone_of_members=[]
# city_of_members = []
list_of_writing_one_by_one = []
for i in range(lower_lim,final_upper_lim):

    element3_fcs = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SearchCriteriaId"]/div/div/div[1]/div[4]/div/div/div/input[3]')))
    element3_fcs.click()
    element3_fcs.send_keys(i)
    ele_button = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SearchCriteriaId"]/div/div/div[2]/div/button')))
    ele_button.click()
    print(i)
    try:
        name =  wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div/div[4]/div/div/div/table/tbody/tr/td[2]'))).text
        organization =  wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div/div[4]/div/div/div/table/tbody/tr/td[3]'))).text
        email =  wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div/div[4]/div/div/div/table/tbody/tr/td[9]'))).text
        phone =  wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div/div[4]/div/div/div/table/tbody/tr/td[10]'))).text
        city = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div/div/div[4]/div/div/div/table/tbody/tr/td[8]'))).text
    except Exception as error:
        name = "nun"
        organization = "nun"
        email = "nun"
        phone = "nun"
        city = "nun"
        continue

    list_of_writing_one_by_one.append(name)
    list_of_writing_one_by_one.append(organization)
    list_of_writing_one_by_one.append(email)
    list_of_writing_one_by_one.append(phone)
    list_of_writing_one_by_one.append(city)
    writer_object.writerow(list_of_writing_one_by_one)
    list_of_writing_one_by_one.clear()

    # name_of_members.append(name)
    # org_of_members.append(organization)
    # email_of_members.append(email)
    # phone_of_members.append(phone)
    # city_of_members.append(city)
# new_csv = pd.DataFrame({"name" : name_of_members, "organization": org_of_members, "email": email_of_members,"phone number": phone_of_members,"city":city_of_members})
# new_csv.to_csv(f"csvinfo/{lower_lim}-{upper_lim}_fcs_icsi_member.csv")


print("done!!!!!!")
f_object.close()
playsound("sbeep.mp3")






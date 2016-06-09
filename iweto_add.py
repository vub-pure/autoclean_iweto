from selenium import webdriver
import unittest

username = input("Username: ")
password = input("Password: ")

# set up initial connection and login
driver = webdriver.Firefox()
driver.implicitly_wait(30)
# driver.maximize_window()
driver.get("https://cris.cumulus.vub.ac.be/admin/login.xhtml")
username_field = driver.find_element_by_id("j_username_input_field")
username_field.clear()
username_field.send_keys(username)
password_field = driver.find_element_by_id("j_password_input_field")
password_field.clear()
password_field.send_keys(password)
password_field.submit()

# choose environment
env = ''
while not env:
    env_flag = input("Choose environment: [T]est, [U]at, [P]roduction: \n").lower()
    if env_flag == "t":
        env = 'ADD URL TO TEST ENV HERE'
    elif env_flag == "u":
        env = 'ADD URL TO UAT HERE'
    elif env_flag == "p":
        env = 'ADD URL TO PROD HERE'
    else:
        print("Invalid environment")


with open(ADD LINK TO INPUT FILE HERE) as f:
    d = dict(csv.reader(f, delimiter='\t'))

od = collections.OrderedDict(sorted(d.items()))

for k, v in od.items():
    # navigate to award screen
    driver.get("BASE_DOMAIN_HERE/editor/dk/atira/pure/modules/unifiedprojectmodel/external/model/award/editor/awardeditor.xhtml?id=" + k)
    # switch to edit mode
    edit_button = driver.find_element_by_class_name("editor_editlayout_button")
    edit_button.click()
    # focus on the button - messy
    driver.find_element_by_xpath("//div[@class='pure_fieldset_content pure_fieldset_content_indent']/div/div[5]/div/div[1]/div[2]/a").send_keys('/t')
    # click the fin-code button
    fin_code_button = driver.find_element_by_xpath("//div[@class='pure_fieldset_content pure_fieldset_content_indent']/div/div[5]/div/div[1]/div[2]/a")
    fin_code_button.click()
    # choose right fin-code from list
    fin_code_select = driver.find_element_by_xpath("//span[contains(text(),'" + v[:4] + "')]")
    fin_code_select.click()
    driver.find_element_by_xpath("//span[text()='Save']").click()



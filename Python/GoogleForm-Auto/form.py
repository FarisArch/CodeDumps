from selenium import webdriver
import time,random

driver = webdriver.Firefox(executable_path="/home/faris/Documents/work/geckodriver")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfQ1EBcvo4R6m-9pTolChrmpF4wCmHyrMUzNnTZ3RzIfgT8ug/viewform?vc=0&c=0&w=1&flr=0")

for i in range(101):
    male =driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")
    female = driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox.exportInnerBox")
    nameInput = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput.exportInput")

    genders = [male[0],male[1]]
    ages = [male[2],male[3],male[4],male[5],male[6],male[7]]
    updates = [male[8],male[9],male[10],male[11],male[12],male[13],male[14],male[15],male[16],male[17],male[18]]
    mediums = [female[0],female[1],female[2],female[3],female[4],female[5],female[6]]
    satisfics = [male[19],male[20],male[21],male[22],male[23]]
    efforts = [female[8],female[9],female[10],female[11],female[12],female[13],female[14]]

    money = random.randint(20,40)
    santize = random.randint(1,10)
    N = random.randint(1,4)

    gender = random.choice(genders)
    gender.click()

    age = random.choice(ages)
    age.click()

    update = random.choice(updates)
    update.click()

    nameInput[0].send_keys(money)
    nameInput[1].send_keys(santize)

    medium = random.sample(mediums, k=N)
    for med in medium:
        med.click()

    satisfy = random.choice(satisfics)
    satisfy.click()

    effort = random.sample(efforts,k=N)
    for eff in effort:
        eff.click()

    button = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
    button.click()

    resubmit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    resubmit.click()
print(i)
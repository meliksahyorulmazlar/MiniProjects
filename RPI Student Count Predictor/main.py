import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests,lxml
from bs4 import BeautifulSoup


class RPI:
    def __init__(self):
        self.start_webdriver()
        self.gather_semesters()
        self.run()

    # The following method will start the selenium webdriver
    def start_webdriver(self)->None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)


    # The following method will get all the semesters
    def gather_semesters(self)->None:
        self.driver.get('https://quacs.org')
        while True:
            try:
                semester_click = self.driver.find_element(By.ID,'__BVID__17__BV_toggle_')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                semester_click.click()
                break
        semesters = self.driver.find_elements(By.CLASS_NAME,'dropdown-item')
        self.semesters = [s.text.replace(" ","").lower() for s in semesters if s.text]

    # The following method will print all the semesters
    def print_semesters(self):
        text = ""
        i = 0
        for s in self.semesters:
            text += f"{s}  "
            i += 1
            if i % 10 == 0:
                text += "\n\n"
        print(text)

    # The following method will print all the arguments
    def print_instructions(self):
        print("print-This instruction will print all the semesters")
        print("exit-This instruction will exit the program")
        print("Semester instructions:")
        print("a particular semester-This method will print all the departments")
        print("departments-This instruction will print all the departments")
        print("ALL-This instruction will calculate all the departments ")
        print("leave-This instruction will let you come back to the introduction")

    #This will method will return all the departments for a particular semester
    def print_semester_departments(self,semester)->list:
        site = f"https://quacs.org/{semester}/#/"
        self.driver.get(site)
        while True:
            try:
                departments = self.driver.find_elements(By.CLASS_NAME,'department-link')
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                departments = [(d.get_attribute('href').split("/")[-1],d.text) for d in departments]
                text = ""
                for d in departments:
                    text += f"{d[1]} \n\n"
                print(text)
                return [d[0] for d in departments]

    # The following method will print a particular department for a given semester
    def print_semester_department(self,semester,department):
        site = f"https://quacs.org/{semester}/#/department/{department}"
        self.driver.get(site)
        time.sleep(0.1)
        soup = BeautifulSoup(self.driver.page_source,'lxml')
        spans = soup.find_all('span',title=True,class_='padding-left')
        total_students = 0
        total_space = 0
        for span in spans:
            if "seat" in span.text:
                fraction = span.text.split()[0].split("/")
                students = int(fraction[0])
                space = int(fraction[1])
                students = space-students
                total_students += students
                total_space += space
                print(students,space,fraction)
        print(f"Total students: {total_students} Total seats: {total_space}")
        return total_students,total_space

    #This will run the code
    def run(self):
        while True:
            user_input = input('give a prompt or write instructions to get instructions.\n')
            if user_input == "exit":
                break
            elif user_input == "print":
                self.print_semesters()
            elif user_input == "instructions":
                self.print_instructions()
            elif user_input in self.semesters:
                departments = self.print_semester_departments(user_input)
                while True:
                    department_input = input("Give a semester prompt")
                    if department_input == "leave":
                        break
                    elif department_input in departments:
                        self.print_semester_department(user_input,department_input)
                    elif department_input == "ALL":
                        total_students = 0
                        total_space = 0
                        for department in departments:
                            print(department)
                            result = self.print_semester_department(user_input,department)
                            total_students += result[0]
                            total_space += result[1]
                        print(f"Total students: {total_students} Total seats: {total_space}")

if __name__ == "__main__":
    rpi = RPI()
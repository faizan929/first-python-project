from bs4 import BeautifulSoup

with open('home.html','r') as op: #this will open the file named home.html and we used op as an anlias so it is like we are opening home.html and then 'r' method says we can read and stores it to op, we applied read method on op therefore the content of op(i.e., the content of home.html) will get stored in the variable named "content" (below) # 'r' is the parser method

    content=op.read()
    # print(content) # this will print what is the html file
    
    #creating an instance of the BeautifulSoup
    soup=BeautifulSoup(content,'lxml') # lxml is the parser method # content: mention the file that we want to scrap
    # print(soup.prettify())  using a method on the instance (instances are real world object created from classes
    # (abstract))

    # to get the info we use different methodes
    # e.g to get h5 tags from the file
    # tags=soup.find('h5') # we got the output of h5 tag even tho there are multiple h5 tags, it is because this method 
    # finds the first h5 tag and then stops the execution
    course_html_tags=soup.find_all('h5') # searches all
    # print(tags)
    # print(course_html_tags)
    # for course in course_html_tags:
    #     print(course.text)  this will print course present in html tags

    course_cards=soup.find_all('div', class_='card') #why underscore? because class is a built-in in python in
     # order to differentiate between python's built-in and html's class
    for course in course_cards:
        #  print(course)
         course_name=course.h5.text
         course_price=course.a.text.split()[-1]
         print(f"The course {course_name} costs {course_price}")
        #  print(course_price)
   
        #  print(course_cards)
    # for course in course_cards:
    #     # course_text=course.h5.text
    #     # course_price=course.a.text
    #     # print(course_text)
    #     # print(course_price)
    #     # # print(course.h5)
    #     title_cards=course.find('h5',class_="card-title")
    #     price_cards=course.find('a',class_="btn btn-primary")
    #     # print(title_cards)
    #     # print(price_cards)
    #     course_text=title_cards.text.strip() if title_cards else None
    #     course_price=price_cards.text.strip() if price_cards else None
    #     print(course_text)
    #     print(course_price)

        
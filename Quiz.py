import mysql.connector
from pwinput import pwinput

db=mysql.connector.connect(host="localhost",
                           user="root",
                           password="0312",
                           database="admin")

cursor=db.cursor()

def admin_authentication(admin_username,admin_password):
    # print("hi")
    try:
        query="SELECT COUNT(*) FROM admindetails WHERE admin_username=%s AND admin_password=%s"
        cursor.execute(query,(admin_username,admin_password))
        result=cursor.fetchone()
        if result[0]==1:
            print("Authentication successfully")
            print("====================================")
            while True:
                print("Menu for the Admin")
                print("====================================")
                print("1.Create Question")
                print("2.Delete Question")
                print("3.Logout")
                print("====================================")
                admin_choice=input("select an appropriate opton")

                if admin_choice=="1":
                    create_question()
                elif admin_choice=="2":
                    delete_question()
                elif admin_choice=="3":
                    print("Bye!")
                break
        else:
            print("Authentication failed")
    
    except mysql.connector.Error as e:
        print("Error",e)

def student_authentication(student_id,student_username,student_password):
    try:
        query1="SELECT COUNT(*) FROM studentdetails WHERE student_username=%s AND student_password=%s"
        cursor.execute(query1,(student_username,student_password))
        result=cursor.fetchone()
        if result[0]==1:
            print("Student Authentication successfully")
            print("====================================")
            while True:
                print("Menu for the Student")
                print("====================================")
                print("1. Take Quiz")
                print("2. Logout")
                print("====================================")
                student_choice=input("select an appropriate opton")

                if student_choice=="1":
                    TakeQuiz(student_id)
                elif student_choice=="2":
                    break
        else:
            print("Authentication failed")
    
    except mysql.connector.Error as e:
        print("Error",e)

def create_question():
    questions=input("Enter the question")
    option1=input("Enter the option 1")
    option2=input("Enter the option 2")
    option3=input("Enter the option 3")
    option4=input("Enter the option 4")
    correct_option=input("Enter the correct option (1/2/3/4)")

    insertquery="INSERT INTO question(questions,option1,option2,option3,option4,correctoption) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(insertquery,(questions,option1,option2,option3,option4,correct_option))
    db.commit()
    print("Question added successfully")
    choice=input("Do you want to add a question(yes/no)?")
    if choice=="yes":
        create_question()
    else:
        print("Bye! Thankyou...")

def delete_question():
    confirmation=input("Are you sure you want to delete all the questions(yes/no)")
    if confirmation=="yes":
        deletequery="DELETE FROM question"
        cursor.execute(deletequery)
        db.commit()
        print("All the questions have been deleted")

def TakeQuiz(student_id):
    cursor.execute("SELECT * FROM question")
    result=cursor.fetchall()
    score=0

    for i in result:
        questions,option1,option2,option3,option4,correct_option=i
        print("Questions:"+questions)
        print("1."+option1)
        print("2."+option2)
        print("3."+option3)
        print("4."+option4)
        student_answer=input("Enter your answer(1/2/3/4)")
        
        if student_answer==correct_option:
            score+=1
        
        score_query="INSERT INTO scores(student_id,score) VALUES(%s,%s)"
        cursor.execute(score_query,(student_id,score))
        db.commit()
        print("Quiz completed! Your score"+str(score))

while True:
    print("Welcome to the quiz game")
    print("====================================")
    print("1. Admin")
    print("2. Student")
    print("3. exit")
    print("====================================")
    select=input("Enter the appropriate authentication")

    if select=="Admin":
        admin_username=input("enter the appropriate admin username")
        admin_password=pwinput("enter the appropriate admin password",'*')
        admin_authentication(admin_username,admin_password)
        # create_question()
    
    elif select=="Student":
        student_id=input("enter the appropriate Student id")
        student_username=input("enter the appropriate Student username")
        student_password=pwinput("enter the appropriate Student password",'*')
        student_authentication(student_id,student_username,student_password)
        # TakeQuiz(student_id)

    elif select=="exit":
        print("Bye!")
        break
    else:
        print("Invalid option selected")



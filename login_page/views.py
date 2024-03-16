from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages
em=''
pw=''
name=''
# Create your views here.
def login(request):
    global em,pw
    if request.method == "POST":
        connect_to_sql=sql.connect(host="localhost",user="root",password="Ram#098765",database="DHR_Automation")  ### connecting to mysql database
        cursor=connect_to_sql.cursor()
        data_to_store=request.POST    #### Storing the data in the variable
        
        for key,value in data_to_store.items():
            if key =="email":
                em = value
            if key =="password":
                pw = value
             

        mysql_command = "SELECT email, first_name FROM users WHERE email=%s AND password=%s"
        cursor.execute(mysql_command, (em, pw))
        # user_data = cursor.fetchone()
        # if user_data:  # If user exists
        #     email, username = user_data
        #     request.session['first_name'] = username  # Store the username in the session
        #     return redirect('SMT_DHR_page.html')  # Redirect to SMT DHR page
        # else:
        #     messages.error(request, 'Invalid email or password')
        #     return render(request, 'login_page.html')
        return_data=tuple(cursor.fetchall()) #### storing the return data in the tuple form
        if return_data==():  ### checking that return data is matched or not 
            return render(request,'error.html') ###if not match
        else:
            return redirect('http://localhost:8000/SMT-DHR/')#### if it is match
        
    return render(request,'login_page.html')

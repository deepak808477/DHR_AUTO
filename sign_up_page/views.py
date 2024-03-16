from django.shortcuts import render,redirect
import mysql.connector as sql
fn=''
ln=''
des=''
em=''
pw=''

# Create your views here.
def signup(request):
    global fn,ln,des,em,pw
    if request.method=="POST":
        connect_to_sql=sql.connect(host="localhost",user="root",password="Ram#098765",database="DHR_Automation")  ### connecting to mysql database
        cursor=connect_to_sql.cursor()
        data_to_store=request.POST    #### Storing the data in the variable
        for key,value in data_to_store.items():
            if key =="first_name":
                fn=value
            if key =="last_name":
                ln=value
            if key =="desg":
                des=value
            if key =="email":
                em=value
            if key =="password":
                pw=value

        mysql_command="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,des,em,pw)  #### command for inserting the data to the database
        cursor.execute(mysql_command)
        connect_to_sql.commit()  ###saving to mysql
    # return redirect('http://localhost:8000/signup/')
    return render(request,'sign_up_page.html')



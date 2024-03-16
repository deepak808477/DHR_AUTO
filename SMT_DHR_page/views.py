from django.shortcuts import render, redirect
import mysql.connector as sql

def SMT(request):
    global d, dn, q, pn, nob, tl, ln, name
    if request.method == "POST":
        connect_to_sql = sql.connect(host="localhost", user="root", password="Ram#098765", database="DHR_Automation")
        cursor = connect_to_sql.cursor()
        data_to_store = request.POST
        for key, value in data_to_store.items():
            if key == "date":
                d = value
            if key == "DHR_no.":
                dn = value
            if key == "qty":
                q = value
            if key == "prod_name":
                pn = value
            if key == "no._of_boards":
                nob = value
            if key == "total_lot":
                tl = value
            if key == "lot_no.":
                ln = value

        mysql_command = "INSERT INTO DHR_SMT_data VALUES('{}','{}','{}','{}','{}','{}','{}')".format(d, dn, q, pn, nob, tl, ln)
        cursor.execute(mysql_command)
        connect_to_sql.commit()

    

    return render(request, 'SMT_DHR_page.html')




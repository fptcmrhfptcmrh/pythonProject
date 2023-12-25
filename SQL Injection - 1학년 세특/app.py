from flask import Flask,render_template,request
import sqlite3,os
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
  con=sqlite3.connect('database.db')
  cur=con.cursor()
  try:
    con.execute("DELETE FROM LoginInfo").rowcount
  except:
    cur.execute("CREATE TABLE IF NOT EXISTS LoginInfo(Id TEXT, Password TEXT)")
  cur.execute("INSERT INTO LoginInfo Values('guest','guest')")
  cur.execute("INSERT INTO LoginInfo Values('admin','afsd2747')")
  con.commit()
  if request.method=='POST':
    id=request.form["id"]
    pswd=request.form["pswd"]
    print(id,pswd)
    tf="-"
    cur.execute("SELECT * From LoginInfo where Id='%s' and password='%s'"%(id,pswd))
    if len(cur.fetchall())==0:  tf="login fail"
    else: tf="login success"
    print(tf)
  cur.close()
  con.close()
  return render_template('index.html',id=id,pswd=pswd)
if __name__=='__main__':
  app.run(debug=True)
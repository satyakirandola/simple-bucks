from flask import Flask,request
app=Flask(__name__)
@app.route("/send")
def msg():
  mail=request.args.get("mail")
  amt=request.args.get("amt")
  msg="hello"
  return msg
if __name__=="__main__":
  app.run()

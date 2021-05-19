from flask import Flask,request
app=Flask(__name__)
@app.route("/send")
def msg():
  mail=request.args.get("mail")
  amt=request.args.get("amt")
  import telepot
  bot=telepot.Bot("1810918140:AAEDH8WcSw3FVgI_93Yp9cJcTPUIZ58ODFg")
  msg="hello"
  bot.sendMessage(1113599535,msg)
  return "200"
if __name__=="__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)

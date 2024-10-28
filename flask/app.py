from flask import Flask

app=Flask("whatsapp")

@app.route("/",methods=["GET"])
def home():
    return """<h1> welcome to caliculator </h1>
    <h2 >Note: type this in search url</h2>
    <h2>for addition = type(/calc/add/num1/num2)</h2>
    <h2>for substrction = type(/calc/sub/num1/num2)</h2>
    <h2>for multiplication = type(/calc/mul/num1/num2)</h2>
    <h2>for division = type(/calc/div/num1/num2)</h2>"""

@app.route("/status",methods=["GET"])
def status():
    return "status menu"


@app.route("/add/<num1>/<num2>",methods=["GET"])
def add(num1,num2):
    return f"{num1}+{num2}={int(num1)+int(num2)}"

@app.route("/sub/<num1>/<num2>",methods=["GET"])
def sub(num1,num2):
    return f"{num1}-{num2}={int(num1)-int(num2)}"

@app.route("/mul/<num1>/<num2>",methods=["GET"])
def mul(num1,num2):
    return f"{num1}*{num2}={int(num1)*int(num2)}"

@app.route("/div/<num1>/<num2>",methods=["GET"])
def div(num1,num2):
    if int(num2)==0:
        return "numeric error : divisor must not be zero"
    else :
        return f"{num1}/{num2}={int(num1)/int(num2)}"

@app.route("/calc/<opr>/<num1>/<num2>")
def calc(opr,num1,num2):
    if opr=="add" :
        return f"{num1}+{num2}={int(num1)+int(num2)}"
    elif opr=="sub":
        return f"{num1}-{num2}={int(num1)-int(num2)}"
    elif opr=="mul":
        return f"{num1}*{num2}={int(num1)*int(num2)}"
    elif opr=="div":
        if int(num2)==0:
            return "numeric error : divisor must not be zero"
        else :
            return f"{num1}/{num2}={int(num1)/int(num2)}"
    else:
        return "unknown operation"

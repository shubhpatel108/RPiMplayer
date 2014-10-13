import os
from bottle import route, run

host = '0.0.0.0'

def update_state(cmd):
    if cmd == "p":
        os.system("cmus-remote -u")
    elif cmd == "vi":
        os.system("cmus-remote -v +10%")
    elif cmd == "vd":
        os.system("cmus-remote -v -10%")
    elif cmd == "next":
        os.system("cmus-remote -n")
    elif cmd == "prev":
        os.system("cmus-remote -r")
    elif cmd == "stop":
        os.system("cmus-remote -s")

def html_for_button(name, cmd):
    result = " <input type='button' class='cus_but' onClick='changed(" + "\""+cmd + "\""+")' value='" + name + "'/>\n"
    return result

def html_for_info():
    os.system("cmus-remote -Q > info.text")
    f = open("info.text")
    for x in range(0, 5):
        line = f.readline()
    album = f.readline()
    title = f.readline()
    if "album" in album:
        result = "<p class='info'> Album:" + str(album[9:]) + "</p>\n"
        result += "<p class='info'> Title:" + str(title[9:]) + "</p>"
    else:
        result = ""
    return result

@route('/')
@route('/<cmd>')
def index(cmd="n"):
    print(cmd)
    if cmd != "n":
        update_state(cmd)
    response = "<script>\n"
    response += "function changed(cmd)\n"
    response += "{\n"
    response += "console.log(cmd);\n"
    response += "  window.location.href= '/' + cmd\n"
    response += "}\n"
    response += "</script>\n"
    response += "<style>"
    response += ".cus_but {"
    response += "width:80%;"
    response += "margin-left:10%;"
    response += "margin-right:10%;"
    response += "margin-top:20px;"
    response += "height:250px;"
    response += "font-size:60;"
    response += "}"
    response += ".info {font-size:60;}"
    response += "</style>"
    
    response += html_for_info()
    response += html_for_button("Play/Pause", "p")
    response += html_for_button("Stop", "stop")
    response += html_for_button("Vol +", "vi")
    response += html_for_button("Vol -", "vd")
    response += html_for_button("Next", "next")
    response += html_for_button("Prev", "prev")
    return response

run(host=host, port=4000)
import os
from bottle import route, run

host = '0.0.0.0'

def update_state(cmd):
	if cmd == "p":
		print "yoyo"
		os.system("cmus-remote -u")

def html_for_button(name, cmd):
    result = " <input type='button' onClick='changed(" + "\""+cmd + "\""+")' value='" + name + "'/>"
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
    
    response += html_for_button("Play/Pause", "p") 
    return response

run(host=host, port=4000)
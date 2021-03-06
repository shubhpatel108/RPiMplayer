import os
from bottle import route, run
import video_control as vc

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
    response += html_for_button("Play/Pause", "cmus-p")
    response += html_for_button("Stop", "cmus-stop")
    response += html_for_button("Vol +", "cmus-vi")
    response += html_for_button("Vol -", "cmus-vd")
    response += html_for_button("Next", "cmus-next")
    response += html_for_button("Prev", "cmus-prev")
    return response



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

def main_index_page():
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
    response += html_for_button("MUSIC", "cmus-index")
    response += html_for_button("VIDEO", "video-index")
    return response




@route('/')
@route('/<cmd>')
def index(cmd="n"):
    os.system("mkfifo /tmp/pipe")
    print(cmd)
    if cmd != "n":
	toks = cmd.split('-')
	if len(toks)>1 and toks[0]=="cmus":
        	return update_state(toks[1])
	elif toks[0]=="video":
		return vc.video_controller(cmd)
    else:
	return main_index_page()
    

run(host=host, port=5000)
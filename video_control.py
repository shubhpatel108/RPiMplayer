import subprocess, os, time, sys, select

debug = True
fifo = "/tmp/omxcmd"

def omx_send_control(char,fifo):
	command="echo -n " + char + ">" + fifo
	if debug: print "To omx: " + command
        os.system(command)


def child_wait_for_terminate(proc):
	while proc.poll()!= None:
    		time.sleep(0.1)
	if debug: print 'Child terminated'


def omx_play(omxoptions, track):


    def keyboard_poll():
        i,o,e = select.select([sys.stdin],[],[],0)
        for s in i:
            if s == sys.stdin:
                input = sys.stdin.readline().rstrip()
                return input
        return None


    def child_start(cwd):

        proc=subprocess.Popen([cwd + '/omxchild.sh'], shell=False, \
              stderr=subprocess.PIPE, \
              stdout=subprocess.PIPE, \
              stdin=subprocess.PIPE)
        pid = proc.pid
        if debug: print "PID: ", pid
        
        while proc.poll()!= None:
            time.sleep(0.1)
        if debug: print 'Subprocess ',pid," started"
        return proc

    def child_running(proc):
            if proc.poll() != None:
                return False
            else:
                return True



    def child_send_command (command, proc ):
        if debug: print "To child: "+ command
        proc.stdin.write(command)

    def child_get_status():
        opp=proc.stdout.readline()
        print "From child:  " + opp


    cwd= os.getcwd()
    

    if os.path.exists (fifo): os.system("rm " + fifo )
    os.system("mkfifo " + fifo )

    proc=child_start(cwd)

    child_send_command("track " + omxoptions + " " + track + "\n", proc )

    omx_send_control('.',fifo)

    return



def update_video_state(key):
		if key != '':
			if key=="vi":
				key="+"
			elif key=="vd":
				key="-"
			omx_send_control(key,fifo)
			if key == 'q':
				child_wait_for_terminate(proc)
				os.system("rm " + fifo)
			return




def check_runnable():
    # current working directory
    cwd= os.getcwd()
    
    path = cwd + "/omxchild.sh"
    if os.path.exists(path) == False:
	print "omxchild.sh not found, download from github"
        sys.exit()
    command = "chmod +x " + path
    os.system(command) 


        
videodir ="/home/pi/omp/"
debug = False


def html_for_button(name, cmd):
    result = " <input type='button' class='cus_but' onClick='changed(" + "\""+cmd + "\""+")' value='" + name + "'/>\n"
    return result



def video_controller(cmd):
	    check_runnable()
	    print(cmd)
	    toks = cmd.split('-')
	    if len(toks)>1 and toks[1]=="index":
		while True:
			track = "tl.mp4"
			omx_play("-olocal", videodir + track)
	    else:
        	update_video_state(cmd)
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
	    
	    response += html_for_button("Play/Pause", "video-p")
	    response += html_for_button("Quit", "video-q")
	    response += html_for_button("Vol +", "video-vi")
	    response += html_for_button("Vol -", "video-vd")
	    response += html_for_button("Prev Chap", "video-i")
	    response += html_for_button("Next Chap", "video-o")
	    response += html_for_button("Seek forward", "video-^[[C")
	    response += html_for_button("Next Chap", "video-^[[D")
	    return response


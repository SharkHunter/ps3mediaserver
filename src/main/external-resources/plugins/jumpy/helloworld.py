import sys, jumpy

if len(sys.argv) == 1:
	# initial call
	print "hello"
	pms.addItem(PMS_FOLDER, "Hello", [sys.argv[0], "hello"], "")

elif sys.argv[1] == "hello":
	# user clicked on the 'Hello' folder
	print "world"
	pms.addItem(PMS_VIDEO, "W", "world.mpg", "")
	pms.addItem(PMS_VIDEO, "O", "world.mpg", "")
	pms.addItem(PMS_VIDEO, "R", "world.mpg", "")
	pms.addItem(PMS_VIDEO, "L", "world.mpg", "")
	pms.addItem(PMS_VIDEO, "D", "world.mpg", "")



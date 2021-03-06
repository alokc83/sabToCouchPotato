#!/usr/bin/env python

import sys
import autoProcessMovie 

# SABnzbd
if len(sys.argv) == 8:
# SABnzbd argv:
# 1 The final directory of the job (full path)
# 2 The original name of the NZB file
# 3 Clean version of the job name (no path info and ".nzb" removed)
# 4 Indexer's report number (if supported)
# 5 User-defined category
# 6 Group that the NZB was posted in e.g. alt.binaries.x
# 7 Status of post processing. 0 = OK, 1=failed verification, 2=failed unpack, 3=1+2
	print "Script triggered from SABnzbd, starting autoProcessMovie..."
	autoProcessMovie.process(sys.argv[1], sys.argv[2], sys.argv[7])

# NZBGet
elif len(sys.argv) == 3:
# NZBGet argv: 
# 1  The final directory of the job (full path) 
# 2  The original name of the NZB file 
# From NZBGet only successful downloads are triggered so status is set to "0"
	print "Script triggered from NZBGet, starting autoProcessMovie..."
	
	autoProcessMovie.process(sys.argv[1], sys.argv[2], 0)

else:
	print "Invalid number of arguments received from client." 
	print "Running autoProcessMovie as a manual run..."
	autoProcessMovie.process('Manual Run', 'Manual Run', 0)

# windgrabber
A Python module for grabbing screenshots of windows using their window name.

First you need to start by creating a WindowCamera class
and pass it the name of the window you're trying to caputure.
e.g. 'Steam'

Make sure the window is on your main monitor if you have multiple, or it'll return a black screen.

Then call the "grab" method on the object, and
then it'll return a PIL Image object.

You can also use the show_window method to unminimze the window and bring it to the front.

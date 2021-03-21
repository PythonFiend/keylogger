# Keylogger
This program listens and records every keystroke on the victims computer and then emails it to you, the attacker. It is comprised of three parts:

1. A functions that creates keyboard instance of listener object that uses the pynput module
2. A function that processes the input keystrokes making it more readable, by adding spaces instead of recording Key.backspace, or adding "" instead of Key.shift when the user presses the shift key to capitalize words, etc.
3. A function that reports and sends the email to the attacker. Currently the interval between email is set to 20 seconds, but that can be changed in the keylogge_main.py file. It currently uses outlook configuration, so all you have to do is add your own credentials and it should work right off the bat. However, you might have to set up outlook to accept connection from "untrusted devices." This also works with gmail, but the server settings must be changed accordingly,

How to use it:

1. Run keylogger_main.py from command line.
2. Start typing
3. Wait for emails to start arriving with the reports. 

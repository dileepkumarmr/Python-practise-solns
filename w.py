import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	# Get address from command line.

	print(len(sys.argv))
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard.
	addr="870 Valencia St, San Francisco, CA 94110"
	pyperclip.copy(addr)
	address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

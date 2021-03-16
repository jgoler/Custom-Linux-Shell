import signal, os

def handler(signum, frame):
	print('Signal handler called with signal', signum)


signal.signal(signal.SIGCONT, handler)
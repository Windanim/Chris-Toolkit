import os
from datetime import datetime
from threading import Timer

# Clears the console, regardless of the current operating system
def clearConsole(): return os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# Prints a simple page break break in the console
def pageBreak(): return print('\n---\n')

# Sets the title of the current window
def setWindowTitle(title): os.system("title " + str(title))

# Returns a string containing the current date and time
def returnCurrentDayTimeString(): return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")

# Prints a and-of-script declaration to the console that contains the current date and time
def declareScriptEnd(): return print(datetime.strftime(datetime.now(), "Current script iteration completed at %H:%M:%S on %Y/%m/%d.\nOn to the next!"))

# Loops the provided function every [interval] seconds
class functionLooper(object):

    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        # Runs an initial rendition of the function
        self.function(*self.args, **self.kwargs)
        # Begins the actual loop
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
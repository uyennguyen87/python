_HEADER = '\033[95m'
_OKBLUE = '\033[94m'
_OKGREEN = '\033[92m'
_WARNING = '\033[93m'
_FAIL = '\033[91m'
_ENDC = '\033[0m'
_BOLD = '\033[1m'
_UNDERLINE = '\033[4m'

def green(str):
    print _OKGREEN, str, _ENDC

def blue(str):
    print _OKBLUE, str, _ENDC

def header(str):
    print _HEADER, str, _ENDC

def warning(str):
    print _WARNING, str, _ENDC

def fail(str):
    print _FAIL, str, _ENDC





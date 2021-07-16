import traceback
from datetime import datetime

try:
    print(6 / 0)
except ZeroDivisionError:
    fullTraceback = str(traceback.format_exc())
    print({'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'level': 'error', 'traceback': fullTraceback})

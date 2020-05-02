#Constants

import inspect
URL ="https://opensource-demo.orangehrmlive.com/"
Username ="Admin"
Password ="admin123"


def whoami():
    return inspect.stack()[1][3]

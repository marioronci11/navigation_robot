import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mariocool11/nav_robot_wsp/install/nav_robot_simulation'

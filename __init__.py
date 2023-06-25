import sys
sys.path.append('./io')
sys.path.append('./noiseCanceling')
sys.path.append('./recordMusic')
sys.path.append('./singingMusic')
sys.path.append('./splitingMusic')

import singingIO


print("singing_supporter is running...")
singingIO.execute()

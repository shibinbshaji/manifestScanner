import re
import sys

test_list = ["android:debuggable=\"true\"", "android:allowBackup=\"false\""]

###implement permissions list
##test_permission_list = ["android:name="android.permission.SEND_SMS"]

file1 = open(sys.argv[1],"r+")

test_str = file1.read()

res = [sub for sub in test_list if re.search(sub, test_str)]

###For permissions list
###res2 = [sub for sub in test_list if re.search(sub, test_permission_list)]

print("Possible entry points:")
print(res)

##print(str)

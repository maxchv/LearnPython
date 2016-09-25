import re
p = re.compile(r'[a-zA-Z0-9-.]+@[a-zA-Z0-9-.]+?\.[a-zA-Z0-9.-]+')
test_str = u"мой электронный адрес shaptala@itstep.org.ua ljakljfal;ksjklea .\nmaxshaptala@gmail.com\n@testtest.com\n"
 
m = re.findall(p, test_str)

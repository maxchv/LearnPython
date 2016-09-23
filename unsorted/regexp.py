https://regexone.com/
http://regex.alf.nu
##A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
##Following are the criteria for checking the password:
##1. At least 1 letter between [a-z]
##2. At least 1 number between [0-9]
##1. At least 1 letter between [A-Z]
##3. At least 1 character from [$#@]
##4. Minimum length of transaction password: 6
##5. Maximum length of transaction password: 12
##Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
##Example
##If the following passwords are given as input to the program:
##ABd1234@1,a F1#,2w3E*,2We3345
##Then, the output of the program should be:
##ABd1234@1

-----------------

Enter a regexp that matches all the items in the first column (positive examples) but none of those in the second (negative examples). When you press "submit", you will see what matched.
Regexp:	
Positive 	Negative
pit
spot		pt
spate		Pot
slap two	peat
respite		part
	
------------------

Enter a regexp that matches all the items in the first column (positive examples) but none of those in the second (negative examples). 
Positive 	Negative
			aleht
rap them	happy them
tapeth		tarpth
apth		Apt
wrap/try	peth
sap tray	tarreth
87ap9th		ddapdg
apothecary	apples
			shape the	

------------

Enter a regexp that matches all the items in the first column (positive examples) but none of those in the second (negative examples)

Positive 	Negative
affgfking	fgok
rafgkahe	a fgk
bafghk		affgm
baffgkit	afffhk
affgfking	fgok
rafgkahe	afg.K
bafghk		aff gm
baffg kit	afffhgk

--------------



1 Which of the following matches regexp /a(ab)*a/

 

1)      abababa

2)      aaba

3)      aabbaa

4)      aba

5)      aabababa

 

2 Which of the following matches regexp /ab+c?/

 

1)      abc

2)      ac

3)      abbb

4)      bbc

 

3 Which of the following matches regexp /a.[bc]+/

 

1)      abc

2)      abbbbbbbb

3)      azc

4)      abcbcbcbc

5)      ac

6)      asccbbbbcbcccc

 

4 Which of the following matches regexp /abc|xyz/

 

1)      abc

2)      xyz

3)      abc|xyz

 

5 Which of the following matches regexp /[a-z]+[\.\?!]/

 

1)      battle!

2)      Hot

3)      green

4)      swamping.

5)      jump up.

6)      undulate?

7)      is.?

 

6 Which of the following matches regexp /[a-zA-Z]*[^,]=/

 

1)      Butt=

2)      BotHEr,=

3)      Ample

4)      FIdDlE7h=

5)      Brittle =

6)      Other.=

 

7 Which of the following matches regexp /[a-z][\.\?!]\s+[A-Z]/

(\s matches any space character)

1)      A. B

2)      c! d

3)      e f

4)      g.   H

5)      i?  J

6)      k L

 

8 Which of the following matches regexp /(very )+(fat )?(tall|ugly) man/

 

1)      very fat man

2)      fat tall man

3)      very very fat ugly man

4)      very very very tall man

 

9 Which of the following matches regexp /<[^>]+>/

 

1)      <an xml tag>

2)      <opentag> <closetag>

3)      </closetag>

4)      <>

5)      <with attribute=”77”>
	











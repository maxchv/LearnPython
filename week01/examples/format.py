>>> template = '{}, {} and {}' 
>>> template.format('spam', 'ham', 'eggs')
'spam, ham and eggs'
>>> template = "{0}, {1} and {2}"			# Порядковые номера позиционных аргументов 
>>> template.format('spam', 'ham', 'eggs')
'spam, ham and eggs'
>>> template.format('ham', 'spam', 'eggs')
'ham, spam and eggs'
>>> template = "{1}, {0} and {2}"			
>>> template.format('spam', 'ham', 'eggs')
'ham, spam and eggs'
>>> template = "{motto}, {pork} and {food}"	# Имена именованных аргументов 
>>> template.format(motto="spam", pork="ham", food="eggs")
'spam, ham and eggs'
>>> template.format(motto="ham", pork="spam", food="eggs")
'ham, spam and eggs'
>>> template = '{motto}, {0} and {food}'	# # Оба варианта 
>>> template.format("ham", motto="spam", food="eggs")
'spam, ham and eggs'

def bmi(height, mass):
    idx = mass / height ** 2
    msg = ''
    if idx < 16:
        msg = 'Выраженный дефицит массы тела'
    elif idx < 18.5:
        msg = 'Недостаточная(дефицит) масса тела'
    elif idx < 25:
        msg = 'Норма'
    elif idx < 30:
        msg = 'Избыточная масса тела(предожирение)'
    return idx, msg

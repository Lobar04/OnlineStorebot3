def lotin_l(a):
    d = ''
    b = {' ':' ',
         'й':'y',
         'ц':'ts',
         'у':'u',
         'к':'k',
         'е':'e',
         'н':'n',
         'г':'g',
         'ш':'sh',
         'щ':'sh',
         'з':'z',
         'х':'x',
         'ъ':"'",
         'ф':'f',
         'ы':'i',
         'в':'v',
         'а':'a',
         'п':'p',
         'р':'r',
         'о':'o',
         'л':'l',
         'д':'d',
         'ж':'dj',
         'э':'e',
         'я':'ya',
         'ч':'ch',
         'с':'s',
         'м':'m',
         'и':'i',
         'т':'t',
         'ь':'',
         'б':'b',
         'ю':'yu',
         'ё':'yo'
         }
    if a is not None:
        for j in a:
            for i in b:
                if i.lower()==j and i.isupper():
                    d+=b[i].upper()
                elif i==j:
                    d+=b[i]
    if d!='':
         return d
    else:
         return a


def to_lower(a):
    c = ''
    for i in a:
        if i.isalpha():
            c+=i.lower()
        else:
            c+=i


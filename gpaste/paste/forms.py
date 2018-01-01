from datetime import datetime, timedelta

languageBox = [
        'Apache',
        'Bash',
        'C#',
        'C++',
        'CSS',
        'CoffeeScript',
        'Diff',
        'HTML',
        'HTTP',
        'Ini',
        'JSON',
        'Java',
        'JavaScript',
        'Makefile',
        'Markdown',
        'Nginx',
        'Obj-C',
        'PHP',
        'Perl',
        'Python',
        'Ruby',
        'SQL',
        'Shell',
        ]

expirationDate = [
        'Burn After Reading',
        '10 Minutes',
        '1 Hour',
        '1 Day',
        '7 Days',
        '1 Month',
        ]

def expiryDateAndType(expiration):
    burnAfterReading = False
    date = datetime.now()

    if expiration == 'Burn After Reading':
        burnAfterReading = True
        date += timedelta(weeks=3) 

    elif expiration == '10 Minutes':
        date += timedelta(minutes=10)

    elif expiration == '1 Hour':
        date += timedelta(hours=1)

    elif expiration == '1 Day':
        date += timedelta(days=1)

    elif expiration == '7 Days':
        date += timedelta(days=7)

    elif expiration == '1 Month':
        date += timedelta(days=31)

    else:
        date += timedelta(days=7)

    return burnAfterReading, date

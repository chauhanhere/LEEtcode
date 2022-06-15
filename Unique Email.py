#929
def email(s):
    unique=set()
    for i in s:
        local,domain=i.split('@')
        local=local.split('+')[0]
        local=local.replace('.','')
        unique.add((local,domain))
    return len(unique)
print(email(["test.email+alex@abc.com","test.e.mail+bob.cathy@abc.com","testemail+david@ab.c.com"]))

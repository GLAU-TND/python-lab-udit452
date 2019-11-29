class Myexpection(Exception):
    def __init__(self,v):
        def __init__(self,v):
            self.v=v
        def __str__(self):
            print(v)
def xyz(i,j):

    if(i+j>=150):
        print(i+j)
    else:
        raise Myexpection('Custom Exception Occurred')


i=int(input())
j=int(input())
xyz(i,j)

'''A1=input("A1")
A2=input("A2")
A3=input("A3")
B1=input("B1")
B2=input("B2")
B3=input("B3")
C1=input("C1")
C2=input("C2")
C3=input("C3")
print(A1+"|"+A2+"|"+A3+"\n----------\n"+B1+"|"+B2+"|"+B3+"\n------------\n"+C1+"|"+C2+"|"+C3)'''
score=0
print("Type ''a'', ''b'', or ''c''(Case sensitive) to go to a game: ")
d=input()
import random
if(d=="a"):
    print("Thanos Snap")
    f=input("Type anything to see if you'll be snapped out of existance: ")
    g=round(random.randint(0,1))
    if(g==0):print("Thanos will spare you") 
    if(g==1):print("Thanos will snap you out of existince")
    print(score)
if(d=="b"):
    print("Lottery Ticket")
    h=input("Type anything to start")
    s=input(("Enter a Wager: "))
    i=input(("Enter a Number  between 1-20: "))
    j=input(("Enter a Number between 1-20: "))
    k=input(("Enter a Number between 1-20: "))
    l=input(("Enter a Number between 1-20: "))
    m=input(("Enter a Number between 1-20: "))
    n=random.randint(1,20)
    o=random.randint(1,20)
    p=random.randint(1,20)
    q=random.randint(1,20)
    r=random.randint(1,20)
    if(n==i): score=score+s
    if(o==i): score=score+s
    if(p==i): score=score+s
    if(r==i): score=score+s
    if(q==i): score=score+s
    if(n==j): score=score+s
    if(o==j): score=score+s
    if(p==j): score=score+s
    if(q==j): score=score+s
    if(r==j): score=score+s
    if(n==k): score=score+s
    if(o==k): score=score+s
    if(p==k): score=score+s
    if(q==k): score=score+s
    if(r==k): score=score+s
    if(n==l): score=score+s
    if(o==l): score=score+s
    if(p==l): score=score+s
    if(r==l): score=score+s
    if(q==l): score=score+s
    if(o==m): score=score+s
    if(p==m): score=score+s
    if(q==m): score=score+s
    if(r==m): score=score+s
    print("Winning Numbers")
    print(n)
    print(o)
    print(p)
    print(q)
    print(r)
    print("$ Won:")
    print(score)
'''Repeat without restarting the terminal'''
print("Type ''a'', ''b'', or ''c'' to go to a game: ")
d=input()
'''if any(c in someList for c in ("a", "á", "à", "ã", "â")):'''

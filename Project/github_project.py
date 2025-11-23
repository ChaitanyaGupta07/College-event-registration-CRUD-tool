events = []
regs = []

while True:
    print("\n1 Add Event 2 Show Events 3 Delete Event")
    print("4 Register 5 Show Regs    6 Delete Reg 0 Exit")
    c = input("choose option: ")

    if c=="1":
        nm = input("Event name :")
        events.append(nm)
        print("added event")

    elif c=="2":
        if len(events)==0:
            print("no events yet")
        else:
            for i,eve in enumerate(events):
                print(i , eve)

    elif c=="3":
        for i,e in enumerate(events):
            print(i,e)
        x = input("enter no:")
        if x.isdigit():
            x = int(x)
            if x < len(events):
                events.pop(x)
                print("event deleted")
            else:
                print("wrong index")
        else:
            print("enter number only")

    elif c=="4":
        for i,e in enumerate(events):
            print(i , e)
        evn = input("event no :")
        if evn.isdigit():
            evn = int(evn)
            if evn < len(events):
                n = input("name : ")
                regtxt = n + " - " + events[evn]
                regs.append(regtxt)
                print("done registering")
            else:
                print("not in list")
        else:
            print("enter valid no")


    elif c=="5":
        if len(regs)==0:
            print("no regs found")
        else:
            for i,r in enumerate(regs):
                print(i , r)

    elif c=="6":
        for i,r in enumerate(regs):
            print(i , r)
        d = input("no:")
        if d.isdigit():
            d = int(d)
            if d < len(regs):
                regs.pop(d)
                print("deleted")
            else:
                print("wrong num")
        else:
            print("enter number")

    elif c=="0":
        break

    else:
        print("wrong choice try again")
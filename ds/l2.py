def addcourse(courses):
    code=input("Enter course code:")
    if code in courses:
        print("Duplicate courses not allowed")
        return
    name=input("Enter course name:")
    fauclty=input("Enter faculty name:")
    noOfregs=int(input("Enter no of regs:"))
    courses[code]=[name,fauclty,noOfregs]


def dispallcourse(courses):
    if len(courses)==0:
        print("No courses")
        return 
    print("Courses are:")
    for code,[name,fauclty,noOfregs]in courses.items():
        print(code,' ',name,' ',fauclty,' ',noOfregs)
        
def dispcourse(courses):
    if len(courses)==0:
        print("No courses")
        return
    code=input("Enter course code:")
    if code in courses:
        print(courses[code][0],courses[code][1],courses[code][2])
    else:
        print("No course with code",code,"is present")
def highnoOfregs(courses):
    if len(courses)==0:
        print("No courses")
        return
    regs=[]
    for details in courses.values():
        regs.append(details[2])
    maxregs=max(regs)
    print("max no of regs:",maxregs)
    print("course with max no of regs:")
    for code,[name,faculty,noOfregs] in courses.items():
        if maxregs==noOfregs:
            print(name)
    
def main():
    courses={}
    while True:
        print("\n 1.addcourse 2.dispallcourses 3.dispcourse 4.highnoOfregs")
        opt=int(input("Enter option:"))
        if opt==1:
            addcourse(courses)
        elif opt==2:
            dispallcourse(courses)
        elif opt==3:
            dispcourse(courses)
        elif opt==4:
            highnoOfregs(courses)
        elif opt==5:
            break
        else:
            print("incorrect choice")

if __name__=='__main__':
    main()
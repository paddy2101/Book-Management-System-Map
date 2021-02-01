library={}

menu={1:"CREATE LIBRARY",2:"GET BOOK DETAILS",3:"ADD NEW BOOK",4:"NO OF BOOKS IN STOCK",5:"EXIT"}

def addBook():
    bookName = input("Enter Book Name : ")
    auther = input("Enter Auther : ")
    price = input("Enter Price : ")
    tempDis={'auther':auther,'price':price}
    library[bookName]=tempDis

def printBookDetails(bname):
    
    if(library.get(bname) == None ):
        print("Book Not Available")
    else:
        print("Book Details Are : ")
        print("Book Name : ",bname)
        print("Auther : ",library.get(bname)["auther"])
        print("Price : ",library.get(bname)["price"])
    
if __name__=="__main__": 
    ch = 0
    while(ch!=5):
        print("*******MENU*******")
        for key, value in menu.items():
            print(key, '->', value)
        ch=int(input("Enter Your Choise : "))
        if ch == 1:
            n=int(input("Enter No Of Book Do You Want To Add : "))
            for i in range(n):
                addBook();
            print("Library Created")
        elif ch ==2:
            bname = input("Enter Book Name : ")
            printBookDetails(bname)
        elif ch ==3:
            if not library:
                print("Library Is Not yet created")
            else:
                n=int(input("Enter How Many New Book Do You Want To Add : "))
                for i in range(n):
                    addBook()
                print("All Book Added")
        elif ch == 4:
            if(len(library) == 0):
                print("Library Is Not yet created")
            else :
                print("Book In Stock : ",len(library))
file = open("mysquad.txt", "w")
file.write("My favorite Football team is :Bangladesh")
file.close()

player = ["Zico","Rana","Rahmat","Tariq","Zamal","Mahbub"]


file = open("mysquad.txt" ,"a")
file.write("\n1 ==> Mahbub")
file.write("\n3 ==> Zamal")
file.write("\n5 ==> Tariq")
file.write("\n7 ==> Rahmat")
file.write("\n9 ==> Rana")
file.write("\n11 ==> Zico")
file.close()
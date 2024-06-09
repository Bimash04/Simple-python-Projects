rent= int (input("Enter your room rent ="))
grocery= int (input("Enter your room grocery ="))
electricityBill=  int (input("Enter your room electricity bill you paid ="))
electricityChargePerUnit= int (input("Enter the charge per unit"))  
person= int (input("Enter the person you are living on room"))

totalElectricity= electricityBill * electricityChargePerUnit
            
BillGenerated= (grocery+rent+totalElectricity) // person


print("Each person has to bay =", BillGenerated)
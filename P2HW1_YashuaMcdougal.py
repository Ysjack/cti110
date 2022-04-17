  # This assignment involves using a program calculate subtotal, sales tax and overall total requests prices for five purchased items
    # 4/16/2022
    # CTI-110 P2HW1 - Total Purchases
    # Yashua Mcdougal
    #
sales_tax =7 
t1=float(input("Enter the price of first item:"))
t2=float(input("Enter the price of second item:"))
t3=float(input("Enter the price of third item:"))
t4=float(input("Enter the price of four item:"))
t5=float(input("Enter the price of five item:"))
subtotal =t1+t2+t3+t4+t5 
print("The subtotal of the sale:",subtotal)
salestax = subtotal * sales_tax 
amountofsalestax = "{:.2f}".format(salestax) 
print("The sales tax is:",amountofsalestax)
Total = subtotal + salestax 
total_new = "{:.2f}".format(Total)
print("Total:",total_new)

# This is a  python program to calculate the total amount of money each person should give as a share in monthly Bill
# It consists of Hostel/Flat Bill
# Total amount of food ordered
# Total Electricit spent
# Charge per unit of electricity
# Number of persons to share the Bill

rent = int(input("Enter you hostel/flat rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity_spend = int(input("Enter the total of electricity spent: "))
charge_per_unit = float(input("Enter the charge per unit: "))
persons = int(input("Enter the number of persons living in room or flat: "))


total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) / persons

print("Each person will pay:" ,output)

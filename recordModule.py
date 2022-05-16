
import varModule as var
import homeModule as home

# RECORD FUNCTION
def Record():
	
	# checks if any record exists or not
	if var.phno!=[]:
		print("	 *** HOTEL RECORD ***\n")
		print("| Name \t | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,var.i):
			print("|",var.name[n],"\t |",var.phno[n],"\t|",var.add[n],"\t|",var.checkin[n],"\t|",var.checkout[n],"\t|",var.room[n],"\t|",var.price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		print("No Records Found")
	n = int(input("0-BACK\n ->"))
	if n == 0:
		home.Home()
		
	else:
		exit()
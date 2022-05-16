import varModule as var
import homeModule as home
# PAYMENT FUNCTION			
def Payment():
	
	ph=str(input("Phone Number: "))
	global i
	f=0
	
	for n in range(0,var.i):
		if ph==var.phno[n] :
			
			# checks if payment is
			# not already done
			if var.p[n]==0:
				f=1
				print(" Payment")
				print(" --------------------------------")
				print(" MODE OF PAYMENT")
				
				print(" 1- Credit/Debit Card")
				print(" 2- Paytm/PhonePe")
				print(" 3- Using UPI")
				print(" 4- Cash")
				x=int(input("-> "))
				print("\n Amount: ",(var.price[n]*var.day[n])+var.rc[n])
				print("\n		 Pay For AnCasa")
				print(" (y/n)")
				ch=str(input("->"))
				
				if ch=='y' or ch=='Y':
					print("\n\n --------------------------------")
					print("		 Hotel AnCasa")
					print(" --------------------------------")
					print("			 Bill")
					print(" --------------------------------")
					print(" Name: ",var.name[n],"\t\n Phone No.: ",var.phno[n],"\t\n Address: ",var.add[n],"\t")
					print("\n Check-In: ",var.checkin[n],"\t\n Check-Out: ",var.checkout[n],"\t")
					print("\n Room Type: ",var.room[n],"\t\n Room Charges: ",var.price[n]*var.day[n],"\t")
					print(" Restaurant Charges: \t",var.rc[n])
					print(" --------------------------------")
					print("\n Total Amount: ",(var.price[n]*var.day[n])+var.rc[n],"\t")
					print(" --------------------------------")
					print("		 Thank You")
					print("		 Visit Again :)")
					print(" --------------------------------\n")
					var.p.pop(n)
					var.p.insert(n,1)
					
					# pops room no. and customer id from list and
					# later assigns zero at same position
					var.roomno.pop(n)
					var.custid.pop(n)
					var.roomno.insert(n,0)
					var.custid.insert(n,0)
					
			else:
				
				for j in range(n+1,i):
					if ph==var.phno[j] :
						if var.p[j]==0:
							pass
						
						else:
							f=1
							print("\n\tPayment has been Made :)\n\n")
	if f==0:
		print("Invalid Customer Id")
		
	n = int(input("0-BACK\n ->"))
	if n == 0:
		home.Home()
	else:
		exit()
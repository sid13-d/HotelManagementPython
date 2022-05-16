import varModule as var
import homeModule as homee

# RESTAURANT FUNCTION
def restaurant():
	ph=int(input("Customer Id: "))
	global i
	f=0
	r=0
	for n in range(0,var.i):
		if var.custid[n]==ph and var.p[n]==0:
			f=1
			print("-------------------------------------------------------------------------")
			print("						 Hotel AnCasa")
			print("-------------------------------------------------------------------------")
			print("						 Menu Card")
			print("-------------------------------------------------------------------------")
			print("\n BEVARAGES							 26 Dal Fry................ 140.00")
			print("----------------------------------	 27 Dal Makhani............ 150.00")
			print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
			print(" 2 Masala Tea.............. 25.00")
			print(" 3 Coffee.................. 25.00	 ROTI")
			print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
			print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
			print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
			print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
			print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
			print(" 9 Cheese Toast Sandwich... 70.00")
			print(" 10 Grilled Sandwich........ 70.00	 RICE")
			print("									 ----------------------------------")
			print(" SOUPS								 33 Plain Rice.............. 90.00")
			print("----------------------------------	 34 Jeera Rice.............. 90.00")
			print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
			print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
			print(" 13 Veg. Noodle Soup....... 110.00")
			print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
			print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
			print("									 37 Plain Dosa............. 100.00")
			print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
			print("----------------------------------	 39 Masala Dosa............ 130.00")
			print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
			print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
			print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
			print(" 19 Palak Paneer........... 120.00")
			print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
			print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
			print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
			print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
			print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
			print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
			print("Press 0 -to end ")
			ch=1
			while(ch!=0):
				
				ch=int(input(" -> "))
				
				# if-elif-conditions to assign item
				# prices listed in menu card
				if ch==1 or ch==31 or ch==32:
					rs=20
					r=r+rs
				elif ch<=4 and ch>=2:
					rs=25
					r=r+rs
				elif ch<=6 and ch>=5:
					rs=30
					r=r+rs
				elif ch<=8 and ch>=7:
					rs=50
					r=r+rs
				elif ch<=10 and ch>=9:
					rs=70
					r=r+rs
				elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
					rs=110
					r=r+rs
				elif ch<=19 and ch>=18:
					rs=120
					r=r+rs
				elif (ch<=26 and ch>=20) or ch==42:
					rs=140
					r=r+rs
				elif ch<=28 and ch>=27:
					rs=150
					r=r+rs
				elif ch<=30 and ch>=29:
					rs=15
					r=r+rs
				elif ch==33 or ch==34:
					rs=90
					r=r+rs
				elif ch==37:
					rs=100
					r=r+rs
				elif ch<=41 and ch>=39:
					rs=130
					r=r+rs
				elif ch<=46 and ch>=43:
					rs=60
					r=r+rs
				elif ch==0:
					pass
				else:
					print("Wrong Choice..!!")
			print("Total Bill: ",r)
			
			# updates restaurant charges and then
			# appends in 'rc' list
			r=r+var.rc.pop(n)
			var.rc.append(r)
		else:
			pass
	if f == 0:
		print("Invalid Customer Id")
	n=int(input("0-BACK\n ->"))
	if n==0:
		homee.Home()
	else:
		exit()
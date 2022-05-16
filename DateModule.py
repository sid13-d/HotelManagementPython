# Function used in booking
import bookingModule as booking
import varModule as var

def date(c):
	
	if c[2] >= 2019 and c[2] <= 2022:
		
		if c[1] != 0 and c[1] <= 12:
			
			if c[1] == 2 and c[0] != 0 and c[0] <= 31:
				
				if c[2]%4 == 0 and c[0] <= 29:
					pass
				
				elif c[0]<29:
					pass
				
				else:
					print("Invalid date\n")
					var.name.pop(var.i)
					var.phno.pop(var.i)
					var.add.pop(var.i)
					var.checkin.pop(var.i)
					var.checkout.pop(var.i)
					booking.Booking()
			
			
			# if month is odd & less than equal
			# to 7th month
			elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
				pass
			
			# if month is even & less than equal to 7th
			# month and not 2nd month
			elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
				pass
			
			# if month is even & greater than equal
			# to 8th month
			elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
				pass
			
			# if month is odd & greater than equal
			# to 8th month
			elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
				pass
			
			else:
				print("Invalid date\n")
				var.name.pop(var.i)
				var.phno.pop(var.i)
				var.add.pop(var.i)
				var.checkin.pop(var.i)
				var.checkout.pop(var.i)
				booking.Booking()
				
		else:
			print("Invalid date\n")
			var.name.pop(var.i)
			var.phno.pop(var.i)
			var.add.pop(var.i)
			var.checkin.pop(var.i)
			var.checkout.pop(var.i)
			booking.Booking()
			
	else:
		print("Invalid date\n")
		var.name.pop(var.i)
		var.phno.pop(var.i)
		var.add.pop(var.i)
		var.checkin.pop(var.i)
		var.checkout.pop(var.i)
		booking.Booking()
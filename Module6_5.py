



#Problem 5
#Have the user to enter number of concert tickets. The price per ticket
#depends on the volume (see below). Display the number of tickets, price
#per ticket and the total cost (number of tickets x Price Per Ticket).
#Quantity Price Per Ticket
#>=25 $50
#10 to 24 $60
#5 to 9 $70
#Less 5 $75

ticket_number = float(input("Please enter number of concert tickets: "))
ticket_price = float(50 if ticket_number >= 25 
                      else 60 if (ticket_number >= 10 and ticket_number <= 24)
                      else 70 if (ticket_number >= 5 and ticket_number <= 9 ) else 75)
ticketp_total = ticket_number * ticket_price



print(f"Number of tickets: {ticket_number:.0f}")
print(f"Price per ticket: ${ticket_price:.2f}")
print(f"Total ticket cost: {ticketp_total:.2f}")

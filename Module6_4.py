#Problem 4
#Enter a principle amount of a CD and year to maturity of CD. Determine
#the interest rate based on the amount of the principle and maturity (see
#below). Calculate first year interest (principle x interest rate). Display
#principle, interest rate and the interest amount for first year.
#Principle Years to Maturity Interest Rate
#>$100,000 5 6%
#$50,000 to $100,000 10 5%
#$50,000 to $100,000 5 4%
#Any other principle and years 2%

principle_amt = float(input("Please enter principle amount: "))
CD_years = float(input("CD Years to Maturity: "))
interest_rate = float(.06 if (principle_amt > 100000 and CD_years == 5)
                      else .05 if (principle_amt >= 50000 and principle_amt <= 100000 and CD_years == 10)
                      else .04 if (principle_amt >= 50000 and principle_amt <= 100000 and CD_years == 5) else .02)

rate_converted = interest_rate * 100
yearone_interest = principle_amt * interest_rate


print(f"Principle Amount: ${principle_amt:.2f}")
print(f"Interest Rate: {rate_converted}%")
print(f"First Year Interest:${yearone_interest:.2f}")




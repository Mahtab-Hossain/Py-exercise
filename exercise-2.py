#income tex calculator code with 
input_income = int(input("Enter the salary : "))
tax_payable =0
def tax_calculator():
    if input_income <= 10000 and input_income <=20000:
        tax_payable = 0
    elif input_income <=30000:
        
        tax_on_first_10k =input_income-10000
        tax_payable = tax_on_first_10k*20/100 #tax on 10% 
    else:
        tax_payable = 0
        tax_payable = 10000 * 10/100
        tax_payable = 20000 * 20/100
        tax_payable +=(input_income-30000)*30/100
print("you need to pay ",tax_payable," tax")
#  Program created by: Patrick Layman @ 8PM, July 24th 2023.
#  The purpose of the program is to enable a real estate company to track and identify information
#  Regarding their customers file information and make it easily accessible://

#  Import libraries://
import datetime
import FormatValues as FV
from tqdm import tqdm
import time

CurDate = datetime.datetime.now()

#  Identify program constants from the .dat file

f = open("OSICDef.dat", "r")

NEXT_POL_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISC = float(f.readline())
EXT_LIAB_COST = float(f.readline())
GLASS_COV_COST = float(f.readline())
LOAN_CAR_COV_COST = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())

f.close()

#  Main Program & Program Inputs://

while True:

    CustFirstName = input("Enter the client's first name (or 'End' to quit):                        ").title()

    if CustFirstName == "End":
        break
    CustLastName = input("Enter the customer's last name:               ").title()
    CustAddress = input("Enter the customer's street address            ").title()
    CustCity = input("Enter the customer's city of residence:           ").title()

    ProvLst = ['NL', 'QC', 'NB', 'NS', 'PE', 'ON', 'MB', 'SK', 'AB', 'BC']

    while True:
        Prov = input("Enter the customer's province of residence: ").upper()

        if Prov in ProvLst and len(Prov) == 2:
            print("Valid province entered:", Prov)
            break
        else:
            print("Error - Province must be two characters and a valid province!")

    PostalCode = input("Enter the customer's postal code:                   ").upper()
    PhoneNum = input("Enter the customer's 10 digit phone number:                    ")
    NumCarsIns = int(input("Enter the total number of vehicles to be insured:   "))

    while True:
        ExtLiabilityCov = input("Would you like extra liability coverage up to $1,000,000? Enter Y for Yes or N for No:").upper()
        if len(ExtLiabilityCov) != 1:
            print("Error - Answer must be Y or N")
        else:
            if ExtLiabilityCov == "Y":
                ExtLiabilityCov = "Yes"
                break
            elif ExtLiabilityCov == "N":
                ExtLiabilityCov = "No"
                break

    while True:
        OptGlassCov = input("Would you like glass coverage? Enter Y for Yes or N for No:").upper()
        if len(OptGlassCov) != 1:
            print("Error - Answer must be Y or N")
        else:
            if OptGlassCov == "Y":
                OptGlassCov = "Yes"
                break
            elif OptGlassCov == "N":
                OptGlassCov = "No"
                break

    while True:
        OptLoanerCar = input("Would you like loaner car coverage? Enter Y for Yes or N for No:").upper()
        if len(OptLoanerCar) != 1:
            print("Error - Answer must be Y or N")
        else:
            if OptLoanerCar == "Y":
                OptLoanerCar = "Yes"
                break
            elif OptLoanerCar == "N":
                OptLoanerCar = "No"
                break

    PaymentOptionLst = ['Full', 'Monthly']

    while True:

        PaymentOption = input("Enter how you would like to pay (Full or Monthly):           ").title()
        if PaymentOption in PaymentOptionLst:
            print(f"Valid response entered, {PaymentOption}!                                ")
            break
        else:
            print("Error - Invalid payment option!                                          ")

    #  Calculations://

    InsurancePrem = 0

    if NumCarsIns == 1:
        InsurancePrem = BASIC_PREMIUM

    if NumCarsIns >= 2:
        InsurancePrem = (NumCarsIns - 1) * (BASIC_PREMIUM - (BASIC_PREMIUM * ADD_CAR_DISC)) + BASIC_PREMIUM

    ExtLiabilityCost = 0

    if ExtLiabilityCov == "Yes":
        ExtLiabilityCost = EXT_LIAB_COST

    if ExtLiabilityCov == "No":
        ExtLiabilityCost = 0

    GlassCoverageCost = 0

    if OptGlassCov == "Yes":
        GlassCoverageCost = GLASS_COV_COST

    if OptGlassCov == "No":
        GlassCoverageCost = 0

    LoanerCarCost = 0

    if OptLoanerCar == "Yes":
        LoanerCarCost = LOAN_CAR_COV_COST

    if OptLoanerCar == "No":
        LoanerCarCost = 0

    TotExtraCost = ExtLiabilityCost + GlassCoverageCost + LoanerCarCost

    TotInsurancePrem = InsurancePrem + TotExtraCost

    SalesTax = TotInsurancePrem * HST_RATE

    TotPremCost = TotInsurancePrem + SalesTax

    PaymentTotal = 0

    if PaymentOption == 'Full':
        PaymentTotal = TotPremCost

    if PaymentOption == 'Monthly':
        PaymentTotal = (TotPremCost + PROC_FEE) / 8

    NextMonth = CurDate.replace(month=CurDate.month + 1)
    NextPayment = NextMonth.replace(day=1)
    NextPayment = NextPayment.strftime("%Y-%m-%d")

    #  Write the information to a file://

    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POL_NUM}, ")
    f.write(f"{FV.FDateM(CurDate)}, ")
    f.write(F"{CustFirstName} {CustLastName}, ")
    f.write(f"{CustAddress}, {CustCity}, {Prov}, {PostalCode}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{NumCarsIns}, ")
    f.write(f"{ExtLiabilityCov}, {OptGlassCov}, {OptLoanerCar}, ")
    f.write(f"{PaymentOption}, ")
    f.write(f"{InsurancePrem}\n")
    f.close()

    #  Add any necessary counters before rewriting back to defaults file.

    NEXT_POL_NUM += 1

    f = open("OSICDef.dat", "w")
    f.write(f"{NEXT_POL_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{ADD_CAR_DISC}\n")
    f.write(f"{EXT_LIAB_COST}\n")
    f.write(f"{GLASS_COV_COST}\n")
    f.write(f"{LOAN_CAR_COV_COST}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROC_FEE}\n")
    f.close()

    print()
    print()
    print("Saving data - please wait")
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Data successfully saved ...")
    time.sleep(1)

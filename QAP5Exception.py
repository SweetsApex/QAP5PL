# Import required libraries
import datetime
import FormatValues as FV
CurDate = FV.FDateM(datetime.datetime.now())

#  Pulling information from the defaults file://

f = open("Defaults.dat", "r")

EXT_LIAB_COST = float(f.readline())
GLASS_COV_COST = float(f.readline())
LOAN_CAR_COV_COST = float(f.readline())

f.close()

print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY PAYMENT LISTING AS OF {CurDate}")
print()
print("POLICY  CUSTOMER              TOTAL                     TOTAL       MONTHLY")
print("NUMBER  NAME                 PREMIUM       HST          COST        PAYMENT")
print("="*75)

#  Identifying variables to be used in calculations://

LiabInsCost = 0
GlassCovCost = 0
LoanerCarCost = 0
InvNum = 0
CustName = 0
PolicyDate = 0
InsPremium = 0
ExtraCost = 0
TotalPremium = 0
TotalPolicies = 0
CompleteInsPremium = 0
CompleteExtraCost = 0
CompleteTotalPremium = 0
MonthlyPayment = 0
CompleteMonthlyPayment = 0
CompleteTaxTotal = 0

#   Grabbing information from the Policy main file://

f = open("Policies.dat", "r")

for PoliciesData in f:

    InvLine = PoliciesData.split(",")

    InvNum = int(InvLine[0].strip())
    PolicyDate = InvLine[1].strip()
    CustName = InvLine[2].strip()
    CustPhoneNum = InvLine[7].strip()
    NumCars = float(InvLine[8].strip())
    LiabIns = InvLine[9].strip()
    GlassCov = InvLine[10].strip()
    LoanerCar = InvLine[11].strip()
    PaymentOption = InvLine[12].strip()
    InsPremium = float(InvLine[13].strip())

    #   Program calculations://
    if PaymentOption == "Monthly":

        if LiabIns == "Yes":
            LiabInsCost = EXT_LIAB_COST
        if LiabIns == "No":
            LiabInsCost = 0

        if GlassCov == "Yes":
            GlassCovCost = GLASS_COV_COST
        if GlassCov == "No":
            GlassCovCost = 0

        if LoanerCar == "Yes":
            LoanerCarCost = LOAN_CAR_COV_COST
        if LoanerCar == "No":
            LoanerCarCost = 0

        ExtraCost = LiabInsCost + GlassCovCost + LoanerCarCost

        TotalPremium = InsPremium + ExtraCost

        HST = TotalPremium * 0.15

        TotalCost = TotalPremium + HST

        MonthlyPayment = (TotalCost + 39.99) / 12

        #   Add any counters or totals://

        CompleteInsPremium += InsPremium
        CompleteExtraCost += ExtraCost
        CompleteTotalPremium += TotalPremium
        TotalPolicies += 1
        CompleteMonthlyPayment += MonthlyPayment
        CompleteTaxTotal += HST

        #   Finalized print statements://

        print(f"{InvNum:>4d}  {CustName:<20s}   {FV.FDollar2(TotalPremium):>9s} {FV.FDollar2(HST):>9s}      {FV.FDollar2(TotalCost):>9s}  {FV.FDollar2(MonthlyPayment):>9s}")
f.close()
print("="*75)
print(f"Total Policies: {TotalPolicies:<3d}         {FV.FDollar2(CompleteInsPremium):>10s}  {FV.FDollar2(CompleteTaxTotal):>9s}    {FV.FDollar2(CompleteTotalPremium):>9s}  {FV.FDollar2(CompleteMonthlyPayment)}")

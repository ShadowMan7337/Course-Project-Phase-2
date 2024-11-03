#Joshua Martin CIS261 Project Phase 2

from datetime import datetime, timedelta 

def getEmpName():
    empName = input("Enter Employee Name:  ")
    return empName

def getHoursWorked():
    HoursWorked = float(input("Enter Hours:  "))
    return HoursWorked

def getHourlyRate():
    HourlyRate = float(input("Enter Hourly Rate:  "))
    return HourlyRate

def getTaxRate():
    TaxRate = float(input("Enter Tax Rate:  "))
    return TaxRate 

def CalcTaxAndNet(HoursWorked, HourlyRate, TaxRate):
    gPay = HoursWorked * HourlyRate
    incomeTax = gPay * TaxRate 
    netPay = gPay - incomeTax 
    return gPay, incomeTax, netPay

def printInfo(empName, HoursWorked, HourlyRate, gPay, TaxRate, incomeTax, netPay):
    print(empName, f"{HoursWorked:,.2f}", f"{HourlyRate:,.2f}", f"{gPay:,.2f}", f"{TaxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}") 

def printTotals(totals):
    if totals['totalEmployees'] == 0:
        print("\nNo employees were entered.")
        return
    print(f"\nTotal Number of Employees: {totals['totalEmployees']}")
    print(f"\nTotal Hours: {totals['totalHours']:,.2f}")
    print(f"\nTotal Gross Pay: {totals['totalGrossPay']:,.2f}")
    print(f"\nTotal Tax: {totals['totalTax']:,.2f}")
    print(f"\nTotal Net Pay: {totals['totalNetPay']:,.2f}")

def get_hours_worked_between_dates(start_date, end_date):
    total_hours = 0.0
    current_date = start_date

    while current_date <= end_date:
        hours = float(input(f"Enter hours worked on {current_date.strftime('%Y-%m-%d')}: "))
        total_hours += hours
        current_date += timedelta(days=1)
    
    return total_hours

# Employee List
def employee_list():
    e_list = [getEmpName, getHourlyRate, getTaxRate, get_hours_worked_between_dates]
    print(e_list)

if __name__ == "__main__":
    totals = {
        'totalEmployees': 0,
        'totalHours': 0.00,
        'totalGrossPay': 0.00,
        'totalTax': 0.00,
        'totalNetPay': 0.00
    }

    while True:
        empName = getEmpName()
        if empName.upper() == 'END':
            break

        # Get date range for hours worked
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        end_date_str = input("Enter end date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        
        # Calculate total hours worked in the given date range
        hours = get_hours_worked_between_dates(start_date, end_date)
        
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        gPay, incomeTax, netPay = CalcTaxAndNet(hours, hourlyRate, taxRate)

        printInfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)

        # Update the totals in the dictionary
        totals['totalEmployees'] += 1
        totals['totalHours'] += hours
        totals['totalGrossPay'] += gPay
        totals['totalTax'] += incomeTax
        totals['totalNetPay'] += netPay

    printTotals(totals)

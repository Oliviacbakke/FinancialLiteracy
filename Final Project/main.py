import matplotlib.pyplot as plt
# Important Numbers
savings_initial = 5000
debt_initial = 30100
mortgage_initial = 0
checking_initial = 0
annual_salary = 61000
rent = 850
house_price = 175000
bank_savings_return = 1.01
mutual_savings_return = 1.07
debt_interest = 1.2
debt_payed = 0
mortgage_payed = 0
minimum_debt_payment = 0.03
loan_initial = 0
year_initial = 0
dog_cost = 1000
dog_expenses = 500
dog_emergency = 1000

class Person:
    def __init__(self, name, is_literate):
        # Initializes Person attributes
        self.name = name
        self.is_literate = is_literate
        self.savings = savings_initial
        self.checking = checking_initial
        self.debt = debt_initial
        self.debt_payed = debt_payed
        self.mortgage = mortgage_initial
        self.mortgage_payed = mortgage_payed
        self.loan = loan_initial
        self.year = year_initial
        self.has_house = False
        self.has_dog = False
        self.has_had_dog = False
        self.years_with_dog = year_initial


    def get_wealth(self):
        # Returns the total wealth of the person
        return self.savings + self.checking - self.debt - self.loan

    def annual_to_accounts(self):
        # Adds money to checking and savings accounts
        self.checking = self.checking + annual_salary*.3
        self.savings += annual_salary*.2

    def annual_interest(self):
        # Gives annual interest to money in savings account
        if self.is_literate:
            self.savings = self.savings * mutual_savings_return
        else:
            self.savings = self.savings * bank_savings_return

    def monthly_debt(self):
        # Calculates the monthly debt that is owed
        if self.is_literate:
            extra_payment = 15
        else:
            extra_payment = 1
        payment = min((self.debt * minimum_debt_payment) + extra_payment, self.debt)
        self.debt -= payment
        self.debt_payed += payment

        if self.checking >= payment:
            self.checking -= payment
        else:
            remaining = payment - self.checking
            self.checking = 0
            self.savings -= remaining


    def monthly_rent(self):
        # Takes the monthly rent out of the checking account
        self.checking -= rent


    def can_buy_house(self):
        # Tells whether the person can buy the house, and from there buys the house
        if self.has_house:
            return
        if self.is_literate:
            if self.checking >= house_price * .2:
                self.has_house = True
                self.buy_house()
        else:
            if self.checking >= house_price * .05:
                self.has_house = True
                self.buy_house()

    def buy_house(self):
        # Buys a house and sets the mortgage
        interest = 1
        if self.is_literate:
            self.checking -= house_price*.2
            self.loan = house_price*.8
            interest = .045
        else:
            self.checking -= house_price*.05
            self.loan = house_price*.95
            interest = .05
        self.has_house = True
        N = 360
        i = interest / 12
        D = (((i+1)**N) - 1) / (i*((1+i)**N))
        monthly_payment = self.loan / D
        self.mortgage = monthly_payment
        self.years_renting = self.year

    def mortgage_payment(self):
        # Pays the mortgage
        if self.mortgage > 0 and self.year < 31:
            if self.mortgage < self.checking:
                self.checking -= self.mortgage
            else:
                self.savings -= self.mortgage
        self.loan -= self.mortgage
        self.mortgage_payed += self.mortgage

    def buy_dog(self):
        # Buys a dog
        if self.has_dog:
            return
        if self.has_house:
            self.has_dog = True

    def pay_for_dog(self):
        # Pays for the dog, both regular expenses and emergency payments
        if self.has_had_dog:
            return
        if self.has_dog:
            if dog_expenses < self.checking:
                self.checking -= dog_expenses
            else:
                self.savings -= dog_expenses
            if self.years_with_dog % 3 == 0:
                if dog_emergency < self.checking:
                    self.checking -= dog_emergency
                else:
                    self.savings -= dog_emergency
            self.years_with_dog += 1
            if self.years_with_dog % 12 == 0:
                self.has_dog = False
                self.has_had_dog = True

    def run_a_year(self):
        # Runs a year
        self.annual_to_accounts()
        for i in range(12):
            if not self.has_house:
                self.monthly_rent()
            if self.debt > 0:
                self.monthly_debt()
            if self.has_house:
                self.mortgage_payment()
        self.can_buy_house()
        self.buy_dog()
        self.pay_for_dog()
        self.debt *= debt_interest
        self.annual_interest()
        self.year += 1



class Simulation:
    def __init__(self, Person, years=40):
        # Initializes Simulation attributes
        self.person = Person
        self.years = years
        self.lst = []
        self.years_in_debt = years
        self.years_renting = years

    def run(self):
        # Runs the person through the years, returns list of wealth
        lst = []
        for i in range(0, self.years+1):
            self.person.run_a_year()
            lst.append(self.person.get_wealth())
            if self.person.debt <= 0 and self.years_in_debt == self.years:
                self.years_in_debt = i + 1
            if self.person.has_house and self.years_renting == self.years:
                self.years_renting = i + 1
        self.lst = lst
        if self.person.debt <= 0 and self.years_in_debt == 0:
            self.years_in_debt = i + 1
        if self.person.has_house and self.years_renting == 0:
            self.years_renting = i + 1
        return lst

    def summary(self):
        # Returns a dictionary with final numbers
        dict = {}
        dict['final_wealth'] = self.lst[-1]
        dict['years_in_debt'] = self.years_in_debt
        dict['total_debt_paid'] = self.person.debt_payed
        dict['total_mortgage_paid'] = self.person.mortgage_payed
        dict['final_debt'] = self.person.debt
        return dict

def plot_wealth(fl_wealth_history, nfl_wealth_history, filename="wealth_over_time.png"):
    # Plots the wealth into a graph
    years = range(len(fl_wealth_history))
    plt.plot(years, fl_wealth_history, label="Financially Literate")
    plt.plot(years, nfl_wealth_history, label="Financially Illiterate")
    plt.title("Financially Literate vs Financially Illiterate")
    plt.xlabel("Years")
    plt.ylabel("Wealth")
    plt.legend()
    plt.savefig(filename)

def run_tests():
    # Tests all of the methods of Person and tests Simulation

    # Tests for Person method annual_to_accounts()
    fn_name = "annual_to_accounts"
    fl = Person('fl', True)
    fl.annual_to_accounts()
    result = fl.checking
    expected = 18300
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.savings
    expected = 17200
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.annual_to_accounts()
    result = nfl.checking
    expected = 18300
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = nfl.savings
    expected = 17200
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl.annual_to_accounts()
    result = nfl.checking
    expected = 36600
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = nfl.savings
    expected = 29400
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method annual_interest()
    fn_name = "annual_interest"
    fl = Person('fl', True)
    fl.annual_interest()
    result = fl.savings
    expected = 5350
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.annual_interest()
    result = nfl.savings
    expected = 5050
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl.annual_to_accounts()
    nfl.annual_interest()
    result = nfl.savings
    expected = 17422.5
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method monthly_debt()
    fn_name = "monthly_debt"
    fl = Person('fl', True)
    fl.annual_to_accounts()
    for i in range(12):
        fl.monthly_debt()
    result = int(fl.checking)
    expected = 8931
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.savings
    expected = 17200
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.annual_to_accounts()
    for i in range(12):
        nfl.monthly_debt()
    result = int(nfl.checking)
    expected = 9074
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = nfl.savings
    expected = 17200
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl.checking = 10
    for i in range(12):
        nfl.monthly_debt()
    result = int(nfl.savings)
    expected = 10808
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = nfl.checking
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method monthly_rent()
    fn_name = "monthly_rent"
    fl = Person('fl', True)
    fl.annual_to_accounts()
    for i in range(12):
        fl.monthly_rent()
    result = fl.checking
    expected = 8100
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.annual_to_accounts()
    for i in range(12):
        nfl.monthly_rent()
    result = nfl.checking
    expected = 8100
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl.annual_to_accounts()
    for i in range(12):
        nfl.monthly_rent()
    result = nfl.checking
    expected = 16200
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method can_buy_house()
    fn_name = "can_buy_house"
    fl = Person('fl', True)
    fl.checking = 36000
    fl.can_buy_house()
    result = fl.has_house
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.can_buy_house()
    result = nfl.has_house
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl.annual_to_accounts()
    nfl.annual_to_accounts()
    nfl.can_buy_house()
    result = nfl.has_house
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method buy_house()
    fn_name = "buy_house"
    fl = Person('fl', True)
    fl.checking = 36000
    fl.buy_house()
    result = int(fl.mortgage)
    expected = 709
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.checking
    expected = 1000
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.loan
    expected = 140000
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.checking = 9000
    nfl.buy_house()
    result = int(nfl.mortgage)
    expected = 892
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = nfl.checking
    expected = 250
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = nfl.loan
    expected = 166250
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method mortgage_payment()
    fn_name = "mortgage_payment"
    fl = Person('fl', True)
    fl.checking = 45000
    fl.savings = 10000
    fl.buy_house()
    for i in range(12):
        fl.mortgage_payment()
    result = int(fl.checking)
    expected = 1487
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    for i in range(12):
        fl.mortgage_payment()
    result = int(fl.savings)
    expected = 2906
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.checking = 20000
    nfl.savings = 11000
    nfl.buy_house()
    for i in range(12):
        nfl.mortgage_payment()
    result = int(nfl.checking)
    expected = 540
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    for i in range(12):
        nfl.mortgage_payment()
    result = int(nfl.savings)
    expected = 290
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method buy_dog()
    fn_name = "buy_dog"
    fl = Person('fl', True)
    fl.checking = 36000
    fl.buy_house()
    fl.buy_dog()
    result = fl.has_dog
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nfl.checking = 9750
    nfl.buy_house()
    nfl.buy_dog()
    result = fl.has_dog
    expected = True
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    fl = Person('fl', True)
    fl.checking = 36000
    fl.buy_dog()
    result = fl.has_dog
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method pay_for_dog()
    fn_name = "pay_for_dog"
    fl = Person('fl', True)
    fl.checking = 38500
    fl.buy_house()
    fl.buy_dog()
    fl.pay_for_dog()
    result = fl.checking
    expected = 2000
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    fl.years_with_dog = 3
    fl.pay_for_dog()
    result = fl.checking
    expected = 500
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    fl.years_with_dog = 11
    fl.pay_for_dog()
    result = fl.has_dog
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for Person method run_a_year()
    fn_name = "run_a_year"
    fl = Person('fl', True)
    fl.run_a_year()
    result = fl.checking
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = int(fl.savings)
    expected = 17046
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.has_house
    expected = False
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.mortgage
    expected = 0
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = int(fl.debt)
    expected = 24877
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = int(fl.debt_payed)
    expected = 9368
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    result = fl.year
    expected = 1
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message



    # Tests for class Simulation
    fn_name = "Simulation"
    fl = Person('fl', True)
    flsimulation = Simulation(fl, 1)
    result = [int(x) for x in flsimulation.run()]
    expected = [-7831, 11094]
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message

    nfl = Person('nfl', False)
    nflsimulation = Simulation(nfl, 1)
    result = [int(x) for x in nflsimulation.run()]
    expected = [-8814, 8296]
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message


    nflsimulation = Simulation(nfl, 1)
    nflsimulation.run()
    result = [int(x) for x in nflsimulation.summary().values()]
    expected = [44545, 1, 28616, 0, 14427]
    error_message = f'while testing {fn_name}, expected {expected} got {result}'
    assert expected == result, error_message


if __name__ == "__main__":
    run_tests()
    fl = Person("fl", True)
    nfl = Person("nfl", False)
    sim_fl = Simulation(fl, years=40)
    sim_nfl = Simulation(nfl, years=40)
    fl_wealth_history = sim_fl.run()
    nfl_wealth_history = sim_nfl.run()
    plot_wealth(fl_wealth_history, nfl_wealth_history)
    summary_fl = sim_fl.summary()
    summary_nfl = sim_nfl.summary()
    print(
        f"RESULT "
        f"fl_final_wealth={summary_fl['final_wealth']} "
        f"nfl_final_wealth={summary_nfl['final_wealth']} "
        f"fl_years_in_debt={summary_fl['years_in_debt']} "
        f"nfl_years_in_debt={summary_nfl['years_in_debt']} "
        f"fl_total_debt_paid={summary_fl['total_debt_paid']} "
        f"nfl_total_debt_paid={summary_nfl['total_debt_paid']} "
        f"fl_total_mortgage_paid={summary_fl['total_mortgage_paid']} "
        f"nfl_total_mortgage_paid={summary_nfl['total_mortgage_paid']}")

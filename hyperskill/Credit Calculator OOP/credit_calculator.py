import math


class CreditCalculator:
    def __init__(self):
        self.principal = 0.0    # credit principal
        self.payment = 0.0      # monthly payment
        self.months_cnt = 0.0   # count of the period
        self.interest = 0.0     # monthly interest rate
        self.target = 'n'       # calculation target

    def setup(self):
        self.target = input('What do you want to calculate?\n'
                            'type "n" - for count of months,\n'
                            'type "a" - for annuity monthly payment,\n'
                            'type "p" - for credit principal:\n')

    def set_principal(self):
        self.principal = float(input('Enter credit principal:\n'))

    def set_payment(self):
        self.payment = float(input('Enter monthly payment:\n'))

    def set_interest(self):
        self.interest = float(input('Enter credit interest:\n')) / 1200

    def set_periods(self):
        self.months_cnt = float(input('Enter count of periods:\n'))

    def get_period(self):
        self.set_principal()
        self.set_payment()
        self.set_interest()
        self.months_cnt = math.ceil(math.log(
            self.payment / (self.payment - self.interest * self.principal),
            1 + self.interest))
        print(f'You need {self.months_to_years()} to repay the credit!')

    def get_ann_payment(self):
        self.set_principal()
        self.set_periods()
        self.set_interest()
        self.payment = self.principal * (
            (self.interest * (1 + self.interest)**self.months_cnt) /
            ((1 + self.interest)**self.months_cnt - 1)
            )
        print(f'Your annuity payment = {math.ceil(self.payment)}!')

    def get_principal(self):
        self.set_payment()
        self.set_periods()
        self.set_interest()
        self.principal = self.payment / (
            (self.interest * (1 + self.interest)**self.months_cnt) /
            ((1 + self.interest)**self.months_cnt - 1)
            )
        print(f'Your credit principal = {math.floor(self.principal)}!')

    def months_to_years(self):
        result = ''
        years = self.months_cnt // 12
        months = self.months_cnt % 12

        if years:
            result += f'{years} year'
            if years % 10 != 1 or years == 11:
                result += 's'

        if years and months:
            result += ' and '

        if months:
            result += f'{months} month'
            if months > 1:
                result += 's'
        return result

    def calculate(self):
        if self.target == 'n':
            self.get_period()
        elif self.target == 'a':
            self.get_ann_payment()
        elif self.target == 'p':
            self.get_principal()
        else:
            print('Command unknown')

    def run(self):
        self.setup()
        self.calculate()


calculator = CreditCalculator()
calculator.run()

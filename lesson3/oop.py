class Company:
    def __init__(self, name, prof_orient, month_profit=0, comp_value=0):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Short company name')
        self.prof_orient = prof_orient
        self.month_profit = abs(float(month_profit))
        self.comp_value = abs(float(comp_value))
        if self.comp_value > 10:
            raise ValueError('This company is too small')

    def year_profit(self):
        return print(self.month_profit*12)

    def __repr__(self):
        return f'<Company name: {self.name}, Company profile: {self.prof_orient}, Company value: {self.comp_value}>'

class Self_employed(Company):
    def __init__(self, name_director, prof_orient, month_profit=0, comp_value=0):
        super().__init__(name_director, prof_orient, month_profit, comp_value)
        self.name_director = name_director

    def __repr__(self):
        return f'<Director name: {self.name}, Company profile: {self.prof_orient}, Company value: {self.comp_value}>'

    def get_nameDirector(self):
        return f'<Name director this company {self.name_director}>'

company1 = Company('LearnPython', 'Building', 100)
print(company1.__repr__())

company1.year_profit()
self_employed1 = Self_employed('Grigory', 'Building')
print(Self_employed.get_nameDirector(self_employed1))

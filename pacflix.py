from tabulate import tabulate

class User:
    def __init__(self, data):
        self.data = data
        self.username = None
        self.current_plan = None
        self.current_duration_plan = None
        self.refferal_code = None
    
    def set_data(self, username, current_plan, current_duration_plan, refferal_code):
        self.username = username
        self.current_plan = current_plan
        self.current_duration_plan = current_duration_plan
        self.refferal_code = refferal_code
        
    def get_data(self, username):
        result = None
        
        for key, value in self.data.items():
            if key.lower() == username.lower():
                result = (key, value[0], value[1], value[2])
                break
        
        return result
    
    def check_benefit(self):
        pacflix_plan_value = [
            ['True', 'True', 'True', 'Can Stream'], 
            ['True', 'True', 'True', 'Can Download'],
            ['True', 'True', 'True', 'Has SD'],
            ['False', 'True', 'True', 'Has HD'],
            ['False', 'False', 'True', 'Has UHD'],
            [1, 2, 4, 'Number of Devices'],
            [
                '3rd party movie', 
                'Basic Plan + Sport Streaming', 
                'Standard Plan + PacFlix Original Series and Movie', 
                'Content'
            ],
            [120_000, 160_000, 200_000, 'Price']
        ]
        
        pacflix_plan_header = [
            'Basic Plan', 
            'Standard Plan', 
            'Premium Plan',
            'Services'
        ]
        
        print('PacFlix Plan List:')
        print(tabulate(pacflix_plan_value, pacflix_plan_header))
    
    def check_plan(self, username):
        for key, value in self.data.items():
            if key.lower() == username.lower():
                self.set_data(key, value[0], value[1], value[2])
                break
        
        if self.current_plan == 'Basic Plan':
            pacflix_plan_value = [
                ['True', 'Can Stream'], 
                ['True', 'Can Download'],
                ['True', 'Has SD'],
                ['False','Has HD'],
                ['False', 'Has UHD'],
                [1, 'Number of Devices'],
                ['3rd party movie', 'Content'],
                [120_000, 'Price']
            ]

            pacflix_plan_header = [
                'Basic Plan', 
                'Services'
            ]
            
            print(tabulate(pacflix_plan_value, pacflix_plan_header))
        elif self.current_plan == 'Standard Plan':
            pacflix_plan_value = [
                ['True', 'Can Stream'], 
                ['True', 'Can Download'],
                ['True', 'Has SD'],
                ['True', 'Has HD'],
                ['False', 'Has UHD'],
                [2, 'Number of Devices'],
                ['Basic Plan + Sport Streaming', 'Content'],
                [160_000, 'Price']
            ]

            pacflix_plan_header = [
                'Standard Plan', 
                'Services'
            ]

            print(tabulate(pacflix_plan_value, pacflix_plan_header))
        elif self.current_plan == 'Premium Plan':
            pacflix_plan_value = [
                ['True', 'Can Stream'], 
                ['True', 'Can Download'],
                ['True', 'Has SD'],
                ['True', 'Has HD'],
                ['True', 'Has UHD'],
                [4, 'Number of Devices'],
                [
                    'Standard Plan + PacFlix Original Series and Movie', 
                    'Content'
                ],
                [200_000, 'Price']
            ]

            pacflix_plan_header = [
                'Premium Plan',
                'Services'
            ]

            print(tabulate(pacflix_plan_value, pacflix_plan_header))
        elif not self.current_plan:
            print('Username tidak ditemukan!')
        
    def upgrade_plan(self, username, new_plan):
        for key, value in self.data.items():
            if key.lower() == username.lower():
                self.set_data(key, value[0], value[1], value[2])
                break
        
        if self.current_duration_plan >= 13:
            if not self.current_plan:
                print('Username tidak ditemukan!')
            elif self.current_plan.lower() and new_plan.lower() == self.current_plan.lower():
                print(f'Anda tidak bisa upgrade ke plan yang sama!')
            elif self.current_plan.lower() and new_plan.lower() == 'standart plan':
                total = 160_000 - (160_000 * 0.05)
                print(f'Bayar {total} untuk upgrade ke standart')
            elif self.current_plan.lower() and new_plan.lower() == 'premium plan':
                total = 200_000 - (200_000 * 0.05)
                print(f'Bayar {total} untuk upgrade ke premium')
            
        elif  self.current_duration_plan < 13:
            if not self.current_plan:
                print('Username tidak ditemukan!')
            elif self.current_plan.lower() and new_plan.lower() == self.current_plan.lower():
                print(f'Anda tidak bisa upgrade ke plan yang sama!')
            elif self.current_plan.lower() and new_plan.lower() == 'standart plan':
                total = 160_000
                print(f'Bayar {total} untuk upgrade ke standart')
            elif self.current_plan.lower() and new_plan.lower() == 'premium plan':
                total = 200_000
                print(f'Bayar {total} untuk upgrade ke premium')

class NewUser:
    def __init__(self, data):
        self.data = data
        self.username = None
        self.current_plan = None
        self.current_duration_plan = None
        self.refferal_code = None
        
    def add_user(self, username):
        for key, value in self.data.items():
            if key.lower() == username.lower():
                print('Username sudah ada!')
                break
                
        self.data[username] = [None, None, None]
        
    def get_refferal_code(self):
        result = []
        for key, value in self.data.items():
            result.append(value[2])
            
        return result
        
    def pick_plan(self, username, new_plan, refferal_code):
        for key, value in self.data.items():
            if key.lower() == username.lower():
                self.current_duration_plan = 0
                self.refferal_code = "faizal_icikiwir-123"
                break
        
        refferals = self.get_refferal_code()
        code = None
        total = None
        
        for refferal in refferals:
            if refferal_code == refferal:
                code = refferal
                
        if code and new_plan.lower() == "basic plan":
            total = 120_000 - (120_000 * 0.04)
            self.current_plan = new_plan
            print(f'Bayar {total} untuk plan {new_plan.capitalize()}')
        elif code and new_plan.lower() == "standart plan":
            total = 160_000 - (160_000 * 0.04)
            self.current_plan = new_plan
            print(f'Bayar {total} untuk plan {new_plan.capitalize()}')
        elif code and new_plan.lower() == "premium plan":
            total = 200_000 - (200_000 * 0.04)
            self.current_plan = new_plan
            print(f'Bayar {total} untuk plan {new_plan.capitalize()}')
        elif not code:
            print("Refferal code error!")
        else:
            print("Plan tidak ditemukan!")


if __name__ == "__main__":
    data = {
        # username: [plan, bulan, refferal]
        "Shandy": ["Basic Plan", 12, "shandy-2134"],
        "Cahya": ["Standard Plan", 24, "cahya-abcd"],
        "Ana": ["Premium Plan", 5, "ana-2f9g"],
        "Bagus": ["Basic Plan", 11, "bagus-9f92"]
    }
    
    # Load semua data
    user_1 = User(data)

    # Set data dari luar
    user_1.set_data("Shandy", 12, "Basic Plan", "shandy-2134")
    
    print(user_1.username, user_1.current_duration_plan, user_1.current_plan)
    print(user_1.get_data('Shandy'))
    
    print("----------- TEST CASE 1 -----------")
    user_2 = User(data)
    user_2.check_benefit()
    
    print("----------- TEST CASE 2 -----------")
    user_2.check_plan('cahya')
    
    print("----------- TEST CASE 3 -----------")
    user_3 = User(data)
    user_3.upgrade_plan('ana', 'premium plan')
    
    user_2 = User(data)
    user_2.check_benefit()
    user_2.check_plan('cahya')
    user_2.upgrade_plan('cahya', 'premium plan')
    
    print("----------- Add New Data -----------")
    faizal = NewUser(data)
    faizal.add_user("faizal_icikiwir")
    
    print("------- Print Refferal Code --------")
    print(faizal.get_refferal_code())
    
    print("----------- TEST CASE 4 -----------")
    faizal.pick_plan('faizal_icikiwir', 'basic plan', 'bagus-9f92')
    
    faizal.pick_plan('faizal_icikiwir', 'basic plan', 'indira-9f92')
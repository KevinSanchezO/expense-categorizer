class ExpenseCategorizer:
    def __init__(self):
        self.code_words = {
            "Monthly payments": ("monthly", "bill", "electricity", "internet", "rent"),
            "Food": ("dinner", "breakfast", "lunch", "dinner", "market", "groceries", "cafe", "restaurant"),
            "Transportation": ("uber", "ride", "taxi", "bus", "metro", "gas", "fuel"),
            "Entertainment":    ("movie", "concert", "game", "streaming", "netflix"),
        }

        self.categories_values = {
            "Monthly payments": {"total": 0.0, "highest_amount": 0.0, "highest_name": ""},
            "Food": {"total": 0.0, "highest_amount": 0.0, "highest_name": ""},
            "Transportation": {"total": 0.0, "highest_amount": 0.0, "highest_name": ""},
            "Entertainment": {"total": 0.0, "highest_amount": 0.0, "highest_name": ""},
            "Others" : {"total": 0.0, "highest_amount": 0.0, "highest_name": ""}
        }

        self.categories = []
    
    def categorize_information(self, info_detail: list):
        for expense in info_detail:
            name = expense[0].lower()
            amount = float(expense[1])
            categorized = False

            for category,keywords in self.code_words.items():
                if any(keyword in name for keyword in keywords):
                    self._update_category(category, name, amount)
                    categorized = True
                    break
            if not categorized:
                self._update_category("Others", name, amount)
        
        print(self.categories_values)
        print("\n")
        print(self.categories)
                
    
    def _update_category(self, category:str, name:str, amount:float):
        self.categories_values[category]["total"] += amount

        if amount >= self.categories_values[category]["highest_amount"]:
            self.categories_values[category]["highest_amount"] = amount
            self.categories_values[category]["highest_name"] = name

        self.categories.append([category, name, amount])

# Expense categorizer

# Input: CSV of expenses with descriptions and amounts.
# Categorize automatically using keywords (e.g., “Uber” → Transport).
# Show spending per category.
# Good for: text matching, dict mapping, file parsing.


from file_reader import FileReader
from expense_categorizer import ExpenseCategorizer

file_reader = FileReader("expenses.csv")
file_info = file_reader.open_read_file()

expense_categorizer = ExpenseCategorizer()
expense_categorizer.categorize_information(file_info)


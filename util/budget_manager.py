class BudgetManager:
    def __init__(self):
        self.budget_limit = 0
        self.current_total = 0

    def set_budget(self, budget):
        self.budget_limit = budget

    def add_component_cost(self, cost):
        if not isinstance(cost, (int, float)):
            raise ValueError("Cost must be a number.")
        self.current_total += cost
        return self.check_budget()

    def remove_component_cost(self, cost):
        if not isinstance(cost, (int, float)):
            raise ValueError("Cost must be a number.")
        self.current_total -= cost
        return self.check_budget()

    def check_budget(self):
        if self.current_total > self.budget_limit:
            return {
                'status': 'exceeded',
                'message': BUDGET_EXCEEDED_MSG,
                'over_by': self.current_total - self.budget_limit
            }
        else:
            return {
                'status': 'within_budget',
                'message': '',
                'remaining_budget': self.budget_limit - self.current_total
            }

    def get_current_budget_status(self):
        return {
            'current_total': self.current_total,
            'budget_limit': self.budget_limit,
            'remaining_budget': self.budget_limit - self.current_total
        }

# Shared dependencies
BUDGET_EXCEEDED_MSG = "The current configuration exceeds the set budget limit."
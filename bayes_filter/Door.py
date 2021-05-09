import random

# Simulate a noisy door state detection
# True is open, False (and all others) is closed
class Door:
    # Default is open
    def __init__(self, state=True):
        self.state = state
        # [Open, close]
        self.options = [True, False]

    def observe(self):
        if self.state == True:
            # 60% chance of correctly returning True if state is True
            weights = [0.6, 0.4]
        else:
            weights = [0.2, 0.8]
    
        return random.choices(self.options, weights)[0]

    # Attempt to toggle the door (no idea why it's called push)
    def push(self):
        if self.state == True:
            weights = [1, 0]
        else:
            weights = [0.8, 0.2]

        self.state = random.choices(self.options, weights)[0]

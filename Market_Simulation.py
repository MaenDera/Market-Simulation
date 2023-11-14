import random
import matplotlib.pyplot as plt

# Define the Buyer class
class Buyer:
    def __init__(self):
        # Set a random minimum price between 15 and 25
        self.min_price = round(random.uniform(15, 25))
        # Set a random maximum price between the minimum price and 50
        self.max_price = round(random.uniform(self.min_price, 50))

# Define the Seller class
class Seller:
    def __init__(self):
        # Set a random minimum price between 23 and 40
        self.min_price = round(random.uniform(23, 40))
        # Set a random maximum price between the minimum price and 90
        self.max_price = round(random.uniform(self.min_price, 90))

# Define the market simulation function
def market_simulation(num_buyers, num_sellers):
    # Create a list of Buyer objects with random prices for each buyer
    buyers = [Buyer() for _ in range(num_buyers)]
    # Create a list of Seller objects with random prices for each seller
    sellers = [Seller() for _ in range(num_sellers)]

    # Initialize counters for successful and unsuccessful trades
    successful_trades = 0
    unsuccessful_trades = 0

    # Continue the simulation until there are no more sellers or buyers
    while sellers and buyers: 
        # Randomly select a buyer and a seller
        buyer = random.choice(buyers)
        seller = random.choice(sellers)

        # Check if a trade can be successful based on price criteria
        if buyer.max_price >= seller.min_price or buyer.max_price >= seller.max_price or buyer.min_price >= seller.min_price:
            successful_trades += 1
        else:
            unsuccessful_trades += 1

        # Remove the selected buyer and seller from the lists
        buyers.remove(buyer)
        sellers.remove(seller)

    # Calculate the number of buyers who missed the opportunity to trade
    buyers_missed_opportunity = ((successful_trades + unsuccessful_trades) - num_buyers) * -1

    # Return the counts of successful trades, unsuccessful trades, and missed opportunities
    return successful_trades, unsuccessful_trades, buyers_missed_opportunity

# Define a function to plot the simulation results
def plot_results(successful_trades, unsuccessful_trades, buyers_missed_opportunity):
    # Define labels and values for the bar chart
    labels = ['Successful Trades', 'Unsuccessful Trades', 'Buyers Missed Trades']
    values = [successful_trades, unsuccessful_trades, buyers_missed_opportunity]

    # Plot the bar chart with colored bars
    plt.bar(labels, values, color=['green', 'red', 'gray'])
    # Set the title and labels for the chart
    plt.title('Market Simulation Results')
    plt.xlabel('Trade Outcome')
    plt.ylabel('Number of Trades')
    # Display the chart
    plt.show()

    # Print the counts of successful trades, unsuccessful trades, and missed opportunities
    print(successful_trades)
    print(unsuccessful_trades)
    print(buyers_missed_opportunity)

# Set the number of buyers and sellers for the simulation
num_buyers = 100
num_sellers = 100
# Run the market simulation and get the results
success, failure, missed_opportunity = market_simulation(num_buyers, num_sellers)
# Plot the results using the defined function
plot_results(success, failure, missed_opportunity)

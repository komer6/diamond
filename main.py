import pandas as pd
import enum
import functions

# Enum for menu actions
class Actions(enum.Enum):
    HIGHEST_PRICE = 1
    AVERAGE_PRICE = 2
    COUNT_IDEAL = 3
    COLOR_COUNTER = 4
    MEDIAN_CARAT = 5
    AVERAGE_CARAT_PER_CUT = 6
    AVERAGE_PRICE_PER_COLOR = 7
    EXIT = 9

# Dictionary to map actions to functions
ACTIONS_MAP = {
    Actions.HIGHEST_PRICE: functions.highest_price,
    Actions.AVERAGE_PRICE: functions.average_price,
    Actions.COUNT_IDEAL: functions.count_ideal,
    Actions.COLOR_COUNTER: functions.color_counter,
    Actions.MEDIAN_CARAT: functions.median_carat,
    Actions.AVERAGE_CARAT_PER_CUT: functions.average_carat_per_cut,
    Actions.AVERAGE_PRICE_PER_COLOR: functions.average_price_per_color
}

# Display the menu
def menu(df):
    while True:
        print("\nMenu:")
        for action in Actions:
            print(f"{action.value}. {action.name.replace('_', ' ').title()}")
        try:
            choice = int(input("Enter your choice: "))
            action = Actions(choice)
            if action == Actions.EXIT:
                print("Exiting...")
                break
            # Call the corresponding function from the dictionary
            if action in ACTIONS_MAP:
                ACTIONS_MAP[action](df)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyError:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    path = 'diamond.csv'
    df = pd.read_csv(path)
    menu(df)



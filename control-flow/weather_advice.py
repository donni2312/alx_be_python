# weather_advice.py

def main():
    """
    Asks the user about the current weather and provides clothing recommendations.
    """
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Provide clothing recommendations based on input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry.")

if __name__ == "__main__":
    main()

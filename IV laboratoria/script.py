from dealer import Dealer

if __name__ == "__main__":
    while True:
        try:
            cars_amount_and_prices = {"car": [7, 50000, 300]} #{car: [amount, sell_price, rent_price]}
            Dealer.cars = cars_amount_and_prices
        except KeyboardInterrupt:
            print(Dealer.print_actual_status)
        


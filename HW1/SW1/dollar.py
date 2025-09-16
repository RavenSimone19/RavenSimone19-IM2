def convert_dollar(amount):

    rate_inr = 88.00   
    rate_gbp = 0.74    
    rate_cny = 7.10    

    inr = amount * rate_inr
    gbp = amount * rate_gbp
    cny = amount * rate_cny

    return inr, gbp, cny

def main():
    while True:
        user_input = input("Enter dollar ($) (* to exit): ").strip()
        if user_input == "*":
            print("Bye")
            break

        
        parts = user_input.split('@')
        amounts = []
        for part in parts:
            
            part = part.strip()
            if part == "":
                continue
            try:
                val = float(part)
                amounts.append(val)
            except ValueError:
                print(f"Ignoring invalid dollar amount: {part}")

        if not amounts:
            print("No valid dollar amounts entered.")
            continue

        print("\nDollar ($)\tIndian Rupee (₹)\tBritish Pound (£)\tChinese Yuan (¥)")
        for amt in amounts:
            inr, gbp, cny = convert_dollar(amt)
            print(f"{amt:.2f}\t\t{inr:.2f}\t\t\t{gbp:.2f}\t\t\t{cny:.2f}")
        print()

if __name__ == "__main__":
    main()

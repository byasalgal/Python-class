def find_squares():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        squared_values = [num ** 2 for num in range(start, end + 1)]
        
        odd_squares = [sq for sq in squared_values if sq % 2 != 0]
        even_squares = [sq for sq in squared_values if sq % 2 == 0]

        print("Odd square values:", odd_squares)
        print("Even square values:", even_squares)
    
    except ValueError:
        print("Invalid input! Please enter valid integers.")

find_squares()

def portfolio_cost(filename):
    total = 0.0

    with open(filename, 'r') as f:
        for line in f:
            try:
                data = line.split()
                n_shares = int(data[1])
                price = float(data[2])
                total += n_shares * price
            except ValueError as e:
                print(f"Couldn't parse: {line}\nReason: {e}")
    
    return total

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio3.dat'))
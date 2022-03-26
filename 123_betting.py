import random
import argparse

def simulate_roulette(unit, budget, multiplier):
  progression = list(map(lambda x: x * unit, [1, 2, 3]))
  initial_budget = budget
  profit = 0
  i = 0

  while True:
    i += 1

    if len(progression) >= 2:
      bet = (progression[0] + progression[-1])
    
    else:
      print("You won {}".format(profit))
      return budget

    if budget < bet:
      print("You cannot bet anymore... budget left: {}". format(budget))
      return budget
  
    result = random.randint(0, multiplier - 1)
    result_string = "win" if result == 1 else "lose"

    if result == 1 :
      budget += multiplier * bet
      profit = budget - initial_budget

      progression = progression[(multiplier - 1): -(multiplier - 1)]

    else:
      budget -= bet
      profit = budget - initial_budget
      progression.append(bet)

    print("----------ROUND {}---------".format(i))
    print("Bet:", bet)
    print("Result:", result_string)
    print("Profit:", profit)
    print("Progression", progression)


def do_roulette(unit, budget, multiplier):
  progression = list(map(lambda x: x * unit, [1, 2, 3]))
  initial_budget = budget
  profit = 0
  i = 0

  while True:
    i += 1
    
    if len(progression) >= 2:
      bet = (progression[0] + progression[-1])
      print("bet {} !".format(bet))
    
    else:
      print("You won {}".format(profit))
      return budget

    if budget < bet:
      print("You cannot bet anymore... budget left: {}". format(budget))
      return budget
  
    result_input = str(input("Did you win? (y/n) "))

    while result_input not in ['y', 'n']:
      result_input = str(input("Did you win? (y/n) "))
    
    result = 1 if result_input == 'y' else 0
    result_string = "win" if result == 1 else "lose"

    if result == 1 :
      budget += (multiplier - 1) * bet
      profit = budget - initial_budget

      progression = progression[(multiplier - 1): -(multiplier - 1)]

    else:
      budget -= bet
      profit = budget - initial_budget
      progression.append(bet)

    print("----------ROUND {}---------".format(i))
    print("Bet:", bet)
    print("Result:", result_string)
    print("Profit:", profit)
    print("Progression", progression)
    print("-------------------------------")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=int, default=0, help="0:simulation mode, 1:practical mode (default=0)")
    parser.add_argument("-u", "--unit", type=int, default=1, help="unit of betting (default=1)")
    parser.add_argument("-b", "--budget", type=int, default=100, help="budget (default=100)")
    parser.add_argument("-m", "--multiplier", type=int, default=2, help="choose either 2 or 3 (default=2)")
    args = parser.parse_args()

    print(args.multiplier)

    if args.multiplier not in [2, 3]:
        raise Exception("choose either 2 or 3 as multiplier")

    if args.mode not in [0, 1]:
        raise Exception("choose either 0 or 1 as mode")

    if args.mode == 0:
        simulate_roulette(unit=args.unit, budget=args.budget, multiplier=args.multiplier)
    
    else:
        do_roulette(unit=args.unit, budget=args.budget, multiplier=args.multiplier)


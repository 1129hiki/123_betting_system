# 123 betting system

This is implementation of 123 betting system (I don't know what it is called in English so I named it).
123 betting is betting strategy for casino roulette. The strategy could be used for any betting in which payout are roughly 1/2 or 1/3.

- payout = 1/2: black/red, odd/even...
- payout = 1/3: columns, dozen

![alt text](https://4.bp.blogspot.com/-ZmR3cq7UCp4/UaVVNJaf67I/AAAAAAAAUB8/-m63nOz10zc/s400/roulette.png)



## How it works

1. define list [1,2,3]
2. bet (first_element + last_element)
3. if you win, remove first and last element of list.
4. if you lose, add bet at the end of list (eg. if you bet 4 and lost, list will be [1,2,3,4])
5. repeat 1-4 until length_of_list <= 1 or lose all your budget.

Note, in case of payout = 1/3, first two and last two element of list are removed in 3.

## Usage

You can use 2 mode

1. Simulation mode:

You can simulate this betting system.

```
# simulation mode with betting unit = 1, budget = 100, and payout = 1/2
python3 123_betting.py 0 -u 1 -b 100 -m 2
```



2. Practical mode:

You can calculate how much to bet each rounds.

```
# simulation mode with betting unit = 1, budget = 200, and payout = 1/3
python3 123_betting.py 1 -u 1 -b 200 -m 3
```


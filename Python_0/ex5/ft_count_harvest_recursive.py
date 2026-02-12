def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def harvest_recursive(current_day):
        if current_day > days:
            return
        else:
            print(f"Day {current_day}")
            harvest_recursive(current_day + 1)

    harvest_recursive(1)
    print("Harvest time!")

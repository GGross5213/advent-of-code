


def main():
    nums_lookup = {}
    with open("input.txt") as file:
        for line in file.readlines():
            nums_lookup[int(line)] = 1

    nums_list = list(nums_lookup.keys())

    product = 0

    for idx, num in enumerate(nums_list):
        for num2 in nums_list[idx+1:]:
            num3 = 2020 - (num + num2)
            if num3 > 0 and num3 in nums_lookup:
                product = num * num2 * num3
                break
        
        if product > 0:
            break

    print(product)




if __name__ == "__main__":
    main()
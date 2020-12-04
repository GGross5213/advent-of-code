def problem1():
    valid_passwords_cnt = 0
    with open("input.txt") as file:
        for line in file.readlines():
            rule, letter, password = line.split(" ")
            min_num, max_num = rule.split("-")
            min_num, max_num = int(min_num), int(max_num)

            letter = letter.replace(":" , "")

            cnt = password.count(letter)

            if cnt >= min_num and cnt <= max_num:
                valid_passwords_cnt += 1
    
    print(f"Part 1: {valid_passwords_cnt}")




def problem2():
    def check_password(index, letter, password):
        return index < len(password) and index >= 0 and password[index] == letter
    valid_passwords_cnt = 0
    with open("input.txt") as file:
        for line in file.readlines():
            rule, letter, password = line.split(" ")
            idx1, idx2 = rule.split("-")
            idx1, idx2 = int(idx1), int(idx2)

            letter = letter.replace(":" , "")

            if check_password(idx1 - 1, letter, password) ^ check_password(idx2 - 1, letter, password):
                valid_passwords_cnt += 1
    
    print(f"Part 2: {valid_passwords_cnt}")

            

if __name__ == "__main__":
    problem1()
    problem2()
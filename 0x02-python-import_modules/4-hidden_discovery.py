#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    name_list = dir(hidden_4)
    for j in name_list:
        if j[:2] == "__":
            continue
        else:
            print(j)

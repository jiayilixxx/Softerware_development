import sys

bank = 500
undistributed_exp = 10
distributed = 10
bag = {
    'captain': 0,
    'hero': 0,
    'soldier': 0,
    's2': 0,
    's3': 0,
    's4': 0,
    'w1': 0,
    'w2': 0,
    'w3': 0,
    'i1': 0,
    'i2': 0,
    'i3': 0,
    'resetEx': 0
}
d = {
    'captain': [100, 70, 80, 90, 1],
    'hero': [80, 65, 70, 82, 2],
    'soldier': [30, 23, 33, 49, 3],
    's2': [40, 34, 35, 37, 4],
    's3': [50, 21, 53, 50, 5],
    's4': [60, 38, 50, 60, 6],
    'w1': [10, 6, 2, 0, 7],
    'w2': [20, 0, 17, 3, 8],
    'w3': [15, 2, 10, 0, 9],
    'i1': [10, 3, 0, 7, 10],
    'i2': [20, 5, 5, 10, 11],
    'i3': [15, 4, 1, 7, 12],
    'resetEx': [10, 13]
}


def store():
    global bank
    count = 1
    print("*" * 50)
    for goods in d:
        print(str(count) + '\t', goods + '     ' + '\t', str(d[goods][0]) + '\t')
        count += 1
    print('The credits in your bank are:\t', bank)
    print("*" * 50)
    print('Please input the product number：', end='')
    choice = int(input())
    for i in d.keys():
        if choice == d[i][-1]:
            if bank >= d[i][0]:
                bank -= d[i][0]
                bag[i] += 1
                print('*' * 30)
                print('\n' + i + '\t' + '*1', 'Successful!', 'You have paid:', str(d[list(d.keys())[choice - 1]][0]), 'Account Balance：', bank, '\n')
                print('*' * 30)
                break
            else:
                print('Insufficient balance, please recharge！')
                break



    if int(choice) not in list(range(1, 14)):
        print('Please input the correct number.')
    print('\nDo you want to exit the store? (Y:exit or N:continue shopping)', end='')
    n = input()
    if n.upper() == 'Y':
        menu()
    elif n.upper() == 'N':
        store()
    else:
        print('Input error, return to the menu.')
        menu()


def useGoods():
    if bag == {}:
        print('There are no items available in your roster.')
    else:
        t_dict = {}
        count = 1
        print('*' * 60)
        for i in list(bag.keys())[2:]:
            if bag[i] != 0:
                print(str(count) + '\t' + i)
                t_dict[count] = i
                count += 1
        print('*' * 60)
        n = input('Please input the items NAME you want to use:  ')
        for i in list(d.keys())[6:12]:
            if n.lower() == i:
                n2 = input('Please choose the equipping solider and input the number: \t1.captain\t2.hero ')
                if n2 == '1':
                    if bag['captain'] != 0:
                        print('Equipping the item successfully!')
                        for attr in range(1, 4):
                            d['captain'][attr - 1] += d[i][attr]

                        attribute = d[i][1:4]

                        print('move fight health increased: ' + str(attribute[0]) + '\t' + str(attribute[1]) + '\t' + str(
                            attribute[2]))
                        break
                    else:
                        print('You don not have this solider.')
                elif n2 == '2':
                    if bag['hero'] != 0:
                        print('Equipping the item successfully!')
                        for attr in range(1, 4):
                            d['hero'][attr] += d[i][attr]
                        attribute = d[i][1:4]
                        print('move fight health increased: ' + str(attribute[0]) + '\t' + str(attribute[1]) + '\t' + str(
                            attribute[2]))
                        break
                    else:
                        print('You don not have this solider.')
        input('Input any word to return.')
        menu()


def checkBag():
    print('**************************')
    for goods in bag:
        if bag[goods] != 0:
            print(goods + '\t\t' + "*" + str(bag[goods]))
    print('Current credits:\t' + str(bank))
    print('**************************')
    print('1.Discard item', '\t', '2.Use item ', '\t', '3.Return')
    n = input()
    if n == '1':
        n2 = input('Please input the NAME of item you want to discard: ')
        if n2 in bag:
            if bag[n2] != 0:
                bag[n2] -= 1
                print('Discard%s *1successfully' % n2)
                n3 = input("1.View the roster\t2.Return to the menu")
                if n3 == '1':
                    checkBag()
                elif n3 == '2':
                    menu()
                else:
                    print('Input error, return to the menu.')
                    menu()
        else:

            print('This item does not exist in your roster, Return to the main menu.')
            menu()

    if n == '2':
        useGoods()

    elif n == '3':
        menu()





        # menu()


def checkExp():  # check the experience point
    global undistributed_exp, distributed
    print('Undistributed experience point：', undistributed_exp)
    print('Distributed experience point：', distributed)
    print('You have bought {} reset Experience'.format(str(bag['resetEx'])))
    if bag['resetEx'] > 0:  # if the experience point is not 0,can reset experience
        n = input('1.Use it\t2.Return to the menu ')
        if n == '1':
            undistributed_exp += 1  # Undistributed experience increased 1
            distributed -= 1  # Distributed experience point decreased 1
            bag['resetEx'] -= 1
            print('You have used it, now it becomes:'+ 'Undistributed experience points:'+str(undistributed_exp)+'Distributed experience points:'+str(distributed))
            n = input('Input any word to return.')
            menu()
        elif n == '2':
            menu()
        else:
            print('Input error, return to the menu.')
    else:
        input('Input any word to return.')
        menu()


def checkAttr():
    print('captain\tmove\tfight\thealth')
    print('\t'
          + str(d['captain'][0]) + '\t'
          + str(d['captain'][1]) + '\t'
          + str(d['captain'][2])
          )
    print('hero\tmove\tfight\thealth')
    print('\t'
          + str(d['hero'][0]) + '\t'
          + str(d['hero'][1]) + '\t'
          + str(d['hero'][2])
          )
    input('Input any word to return.')
    menu()


def menu():
    print('*' * 70)
    print('1.View the experience points\t2.Store \t3.View the roster\t4.View the Attribution\t5.Exit')
    print('*' * 70)
    print('Please input your choice:', end='')
    choice = input()
    if choice == '1':
        checkExp()
    elif choice == '2':
        store()
    elif choice == '3':
        checkBag()
    elif choice == '4':
        checkAttr()
    elif choice == '5':
        return


def dropGood():
    pass


def main():
    menu()


if __name__ == '__main__':
    main()


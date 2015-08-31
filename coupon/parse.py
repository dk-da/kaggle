class user:
    def __init__(self, pref):
        self.pref = pref

def parse_user_list():
    result = [];

    f = open('./input/user_list.csv', 'r')
    lines = f.readlines()
    f.close()
    del lines[0]
    for line in lines:
        line = line.strip()
        # reg_date, sex_id, age, withdraw_date, pref_name, user_id_hash = line.split(',')
        params = line.split(',')
        result.append(params)

    return result

def coupon_visit_train_to_copon_purchase_train():
    inputf = open('./input/coupon_visit_train.csv', 'r')
    outputf = open('./input/coupon_purchase_train.csv', 'w')

    lines = inputf.readlines()
    inputf.close()

    firstline = lines[0].strip()
    print >> outputf, firstline
    del lines[0]
    for l in lines:
        l = l.strip()
        cols = l.split(',')
        if cols[0] == '1':
            print >> outputf, l

def coupon_list_test_in_coupon_list_train():
    test = open('./input/coupon_list_test.csv', 'r')
    train = open('./input/coupon_list_train.csv', 'r')
    test_lines = test.readlines()
    train_lines = train.readlines()
    test.close()
    train.close()

    del test_lines[0]
    del train_lines[0]

    for l in test_lines:
        l = l.strip()
        cols_test = l.split(',')
        for l2 in train_lines:
            l2 = l2.strip()
            cols_train = l2.split(',')

            if cols_test[23] == cols_train[23]:
                print "ZZZZ"


if __name__ == '__main__':
    coupon_list_test_in_coupon_list_train()

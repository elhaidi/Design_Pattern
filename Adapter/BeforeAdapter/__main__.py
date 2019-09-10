from mock_customers import MOCKCUSTOMERS as CUSTOMERS
frm mock_vendors import MOCKVENDORS as VENDORS
TYPE = "vendors"
def main():
    if TYPE =='customers'
    for cust in CUSTOMERS:
        print('Name :{}; Adress : {}'.format(cust.name,cust.adddress))
    elif TYPE == 'vendors':
        for vend in VENDORS:
            print("Name: {}, Address :{} ,{}, ".format(vend.name,vend.number,vend.street))
    else:
        raise ValueError('Incorrect type' + tyoe)
if __name__=__main__:
    main()
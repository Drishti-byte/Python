#program to calculate bill by passing keyword arguments 
def generate_invoice(**products):
    if not products:
        print("No items to bill")
    print("============================ INVOICE ============================")
    print("Product Name              Qty                Price                 Subtotal") 
    total = 0 
    for item, (qty, price) in products.items():
        subTotal = qty * price 
        print(f"{item:<25} {qty:<18} {price:<23} {subTotal}") 
        total += subTotal 
    print("------------------------------------------------------------------------------")
    print("Grand Total:", total)
    print("------------------------------------------------------------------------------")
    return total 
generate_invoice(
    Apple = (2, 50), 
    Banana = (4, 60), 
    Cherry = (10, 500), 
    Pineapple = (4, 45), 
    Mango = (10, 40)
)
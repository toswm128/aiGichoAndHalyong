def solution():
    price, saleP = map(int, input().split())

    def get_sale_price(price, saleP):
        return price * (100-saleP)//100

    return get_sale_price(price, saleP)


print(solution())

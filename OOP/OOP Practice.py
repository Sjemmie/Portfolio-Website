import pandas as pd

df = pd.read_csv("articles.csv", dtype={"id": str})


class Product:
    def __init__(self, product_id):
        self.product_id = product_id
        self.product_name = df.loc[df["id"] == self.product_id, "name"].squeeze()
        self.product_stock = df.loc[df["id"] == self.product_id, "in stock"].squeeze()
        self.product_price = df.loc[df["id"] == self.product_id, "price"].squeeze()

    def available(self):
        check = df.loc[df["id"] == self.product_id, "in stock"].squeeze()
        if check > 0:
            return True
        else:
            return False

    def receipt(self):
        content = f"""
        Thanks for shopping with us! 
        You bought: {self.product_name}
        Price: {self.product_price}
        Remaining in stock: {self.product_stock}
        """
        return content

    def sold(self):
        df.loc[df["id"] == self.product_id, "in stock"].squeeze() - 1
        df.to_csv("articles.csv", index=False)


print(df)
order = input("Choose an article to buy: ")
product = Product(order)

if product.available():
    product.sold()
    print(product.receipt())

else:
    print("Product not in stock")

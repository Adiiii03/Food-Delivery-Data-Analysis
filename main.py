import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("food delivery costs.csv")
df = pd.DataFrame(data)
print(df.head())
print(df.info())

#cleaning our data
df["Order Date and Time"] = pd.to_datetime(df["Order Date and Time"])
df["Delivery Date and Time"] = pd.to_datetime(df["Delivery Date and Time"])
print(df.info())


def extract(value):
    a = str(value).split(" ")
    return a[0]


def removeP(value):
    if '%' in value:
        a = value.replace('%', "")
        return float(a)
    else:
        return float(value)


df["Discounts and Offers"] = df["Discounts and Offers"].apply(extract)
print(df.head())
df["Discounts and Offers"] = df["Discounts and Offers"].apply(removeP)

df.loc[(df["Discounts and Offers"] <= 15), "Discounts and Offers"] = (df["Discounts and Offers"]/100) * (df["Order Value"])


df["Discounts and Offers"] = df["Discounts and Offers"].fillna(0)
print(df["Discounts and Offers"])

df["Costs"] = df["Delivery Fee"] + df["Discounts and Offers"] + df["Payment Processing Fee"]
df["Profit"] = df["Commission Fee"] - df["Costs"]

cost_distribution = df[["Delivery Fee", "Payment Processing Fee", "Discounts and Offers"]].sum()
Total_Revenue = df["Commission Fee"].sum()
Total_Profit = df["Profit"].sum()

print(df.head())
print(df["Costs"])
print(df["Profit"])
print(f"Total Distribution: {cost_distribution}")
print(f"Total Revenue: {Total_Revenue}")
print(f"Total profit: {Total_Profit}")

#pie chart of cost distribution
plt.figure(figsize=(3,3))
plt.title("cost distribution")
plt.pie(cost_distribution, labels=cost_distribution.index, autopct="%1.1f%%")
plt.show()

#bar chart of commision fee, sosts and profit
abc = df[["Commission Fee", "Costs", "Profit"]].sum()
plt.figure(figsize=(4,4))
plt.bar(abc.index, abc)
plt.xticks(rotation= 90)
plt.show()

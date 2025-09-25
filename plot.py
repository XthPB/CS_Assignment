import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")
df.columns = df.columns.str.strip()
df["Beer consumption (/100)"] = df["NL Beer consumption [x1000 hectoliter]"] / 100

plt.figure(dpi=300)
plt.plot(df["Year"], df["Beer consumption (/100)"], marker="o", label="Beer consumption")
plt.plot(df["Year"], df["WO [x1000]"], marker="s", label="Higher education enrollment")
plt.xlabel("Year")
plt.ylabel("Values - Beer (x1e5) & Enrollment (x1e3)")
plt.title("Beer Consumption vs Enrollment in Higher Education (2006–2018)")
plt.legend()
plt.grid(True)
plt.savefig("plot.png")
plt.show()

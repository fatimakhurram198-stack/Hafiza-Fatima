
from src.dataset import make_df, make_depts

df = make_df()
depts = make_depts()

# 1. Grouping: average salary by city
print(df.groupby("city")["salary"].mean())

# 2. Grouping with multiple statistics
res = df.groupby("city").agg(
    n=("name", "count"),
    avg=("salary", "mean")
)
print(res)

# 3. Left merge
m = df.merge(depts, on="city", how="left")
print(m[["name", "city", "region"]])

# 4. Inner merge
inner = df.merge(depts, on="city", how="inner")
print(len(inner), "rows in inner join")

# 5. Apply a function to salary
df["tier"] = df["salary"].apply(
    lambda v: "high" if v >= 60 else "low"
)
print(df[["salary", "tier"]].head(3))

# 6. Convert names to uppercase
print(df["name"].str.upper().tolist())

# 7. Calculate the range of age and salary
print(df[["age", "salary"]].apply(
    lambda c: c.max() - c.min()
))

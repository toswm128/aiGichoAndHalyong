# import pandas as pd

# s = pd.Series([80, 95, 70], index=["민수", "지수", "영희"], name="점수")
# print(s)

# print(f"레이블로 선택: {s.loc["지수"]}")

# print(f"위치로 선택: {s.iloc[1]}")
# print(f"shape: {s.shape}")

# s2 = pd.Series([80, 95, 70], name="점수")  # 순번 index

# print(s2)
# print(s2.loc[1])
# print(s2.iloc[1])


import pandas as pd


# name = pd.Series([
#     "Braund, Mr. Owen Harris",
#     "Allen, Mr. William Henry",
#     "Bonnell, Miss. Elizabeth",
# ], name="Name")
# age = pd.Series([22, 35, 58], name="Age")
# gender = pd.Series(["male", "male", "female"], name="Gender")
# df = pd.DataFrame()
# df = pd.concat([df, name], axis=1)
# df = pd.concat([df, age], axis=1)
# df = pd.concat([df, gender], axis=1)
# print(df)
# print(df.values)

# print(df.columns)

# print(df.index)


# df2 = pd.DataFrame({
#     "국어": [80, 90, 100],
#     "영어": [80, 90, 100],
# }, index=["철수", "영희", "민수"])

# sum = pd.Series(df2["국어"] + df2["영어"], name="합계")
# df2 = pd.concat([df2, sum], axis=1)
# print(df2)
# df2_t = df2.T
# print(df2_t)

# print(df2["국어"])
# print(df2[["국어", "합계"]])


# df = pd.read_csv('./crime.csv')
# # print(df)
# df = pd.read_csv('./crime.csv', index_col='범죄중분류')
# print(df)
# df = pd.read_csv('./crime.csv').head(5)
# print(df)
# df = pd.read_csv('./crime.csv').tail(5)
# print(df)


# df = pd.read_csv("students_dirty.csv", dtype={
#                  "student_id": "string"}, na_values=["미응시"])

# print(df[["student_id", "name", "english", "math"]].to_string(index=False))
# print("결측수:")
# print(df.isna().sum().to_string())

# a = df.isna().sum().to_string()

# df = pd.read_excel('crime.xlsx')
# print(df)


df = pd.read_csv("students.csv", dtype={"student_id": "string"})
result = df[["student_id", "name", "math"]]
path = "math_scores.csv"
result.to_csv(path, index=False, encoding="utf-8")

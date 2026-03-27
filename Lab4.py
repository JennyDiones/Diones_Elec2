import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: better looking plots
plt.style.use('seaborn-v0_8')   # or 'default'

# Load the dataset
df = pd.read_csv(r"C:/spark/spark-3.5.8-bin-hadoop3/bin/World-happiness-report-2024.csv")

print(df.head())

# Top 10 for reuse
top10 = df.sort_values(by='Ladder score', ascending=False).head(10)

# =========================
# MATPLOTLIB (5 GRAPHS)
# =========================
plt.figure(figsize=(10,6))
plt.bar(top10['Country name'], top10['Ladder score'])
plt.title("Top 10 Happiest Countries")
plt.xticks(rotation=45, ha='right')
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.savefig("1_top10_happiest.png")   # <-- saved instead of show
plt.show()   # you can keep this if you want to see it immediately

# 2. Histogram
plt.figure(figsize=(8,5))
plt.hist(df['Ladder score'], bins=10)
plt.title("Distribution of Happiness Score")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("2_happiness_histogram.png")
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(8,6))
plt.scatter(df['Log GDP per capita'], df['Ladder score'])
plt.title("GDP vs Happiness")
plt.xlabel("Log GDP per capita")
plt.ylabel("Happiness Score")
plt.savefig("3_gdp_vs_happiness.png")
plt.show()

# 4. Line Plot
plt.figure(figsize=(10,6))
plt.plot(top10['Country name'], top10['Ladder score'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Countries Happiness")
plt.savefig("4_top10_line.png")
plt.show()

# 5. Pie Chart
plt.figure(figsize=(8,8))
plt.pie(top10['Ladder score'], labels=top10['Country name'], autopct='%1.1f%%')
plt.title("Top 10 Happiness Share")
plt.savefig("5_top10_pie.png")
plt.show()

# =========================
# SEABORN (5 GRAPHS)
# =========================
# 1. Barplot
plt.figure(figsize=(10,6))
sns.barplot(x='Ladder score', y='Country name', data=top10)
plt.title("Top 10 Happiest Countries (Seaborn)")
plt.tight_layout()
plt.savefig("6_seaborn_bar.png")
plt.show()

# 2. Histplot
plt.figure(figsize=(8,5))
sns.histplot(df['Ladder score'], kde=True)
plt.title("Happiness Score Distribution")
plt.savefig("7_happiness_histplot.png")
plt.show()

# 3. Scatterplot
plt.figure(figsize=(8,6))
sns.scatterplot(x='Log GDP per capita', y='Ladder score', data=df)
plt.title("GDP vs Happiness (Seaborn)")
plt.savefig("8_gdp_scatter_seaborn.png")
plt.show()

# 4. Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Ladder score'])
plt.title("Boxplot of Happiness Score")
plt.savefig("9_boxplot.png")
plt.show()

# 5. Heatmap
plt.figure(figsize=(10,8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("10_correlation_heatmap.png")
plt.show()


import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Читает CSV с продажами."""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["price"]
    return df


def revenue_by_day(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("date")["revenue"].sum().reset_index()


def revenue_by_product(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("category")["revenue"].sum().reset_index()


def top_products(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return revenue_by_product(df).head(n)


def main():
    df = load_data("data/sales.csv")

    report = {
        "По дням": revenue_by_day(df),
        "По товарам": revenue_by_product(df),
        "По категориям": revenue_by_category(df),
        "Топ-5 товаров": top_products(df, 5),
    }

    with pd.ExcelWriter("output/report.xlsx") as writer:
        for sheet_name, data in report.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Отчёт сохранён в output/report.xlsx")
    print(f"Общая выручка: {df['revenue'].sum():.2f}")


if __name__ == "__main__":
    main()
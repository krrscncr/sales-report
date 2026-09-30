import pandas as pd
from sqlalchemy import create_engine


# --- НАСТРОЙКИ ПОДКЛЮЧЕНИЯ К MYSQL ---
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "sales_db"

CONNECTION_STRING = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def load_data_from_db(query: str) -> pd.DataFrame:
    """Читает данные о продажах из базы MySQL по SQL-запросу."""
    engine = create_engine(CONNECTION_STRING)
    df = pd.read_sql(query, engine)
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
    query = "SELECT date, product, category, quantity, price FROM sales"
    df = load_data_from_db(query)

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
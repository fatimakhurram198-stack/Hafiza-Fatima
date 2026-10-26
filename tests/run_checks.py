"""Auto-checker for Pandas Lab."""
import sys
from src import dataset as d
from src import practice as p
import pandas as pd
import src.dataset as dataset

CHECKS = {
    1: [
        ("1.1 weather_series",
         lambda: p.t1_1_weather_series(d.make_weather()).to_dict(),
         {"Mon": 21, "Tue": 25, "Wed": 23, "Thu": 28,
          "Fri": 30, "Sat": 27, "Sun": 24}),

        ("1.2 hottest_day",
         lambda: p.t1_2_hottest_day(d.make_weather()),
         "Fri"),

        ("1.3 build_frame",
         lambda: p.t1_3_build_frame().to_dict("list"),
         {"item": ["pen", "book", "bag"],
          "price": [10, 120, 800]}),

        ("1.4 series_vs_frame",
         lambda: p.t1_4_series_vs_frame(d.make_weather()),
         ("Series", "DataFrame")),
    ],
    2: [
        ("2.1 series_arithmetic",
         lambda: p.t2_1_series_arithmetic(d.make_weather()).tolist(),
         [69.8, 77.0, 73.4, 82.4, 86.0, 80.6, 75.2]),
        ("2.2 filter_hot_days",
         lambda: p.t2_2_filter_hot_days(d.make_weather())["day"].tolist(),
         ["Thu", "Fri", "Sat"]),
        ("2.3 missing_values",
         lambda: p.t2_3_missing_values(),
         2),
    ],
    
    
    3: [
        ("3.1 math_numeric",
         lambda: pd.to_numeric(
             dataset.make_students()["math"], errors="coerce"
         ).isna().sum(),
         1),
        ("3.2 english_missing",
         lambda: dataset.make_students()["english"].isna().sum(),
         3),
        ("3.3 duplicate_rows",
         lambda: dataset.make_students().duplicated().sum(),
         1),
    ],
    
    6: [
        ("6.1 price_zscore",
         lambda: p.t6_1_price_zscore(d.make_products()),
         [-0.15, -1.06, -1.01, -0.31, -0.97, -0.85]),

        ("6.2 dummy_columns",
         lambda: p.t6_2_dummy_columns(d.make_products()),
         ["cat_Accessories", "cat_Computers", "cat_Furniture"]),

        ("6.3 feature_matrix",
         lambda: list(p.t6_3_feature_matrix(d.make_products()).columns),
         ["stock", "price_z", "cat_Accessories",
          "cat_Computers", "cat_Furniture"]),

        ("6.4 minmax_stock",
         lambda: p.t6_4_minmax_stock(d.make_products()),
         [0.04, 1.00, 0.67, 0.10, 0.00, 0.06]),

        ("6.5 train_test_sizes",
         lambda: p.t6_5_train_test_sizes(d.make_products()),
         (4, 2)),
    ],

    
    7: [
        ("7.1 top_customer",
         lambda: p.t7_1_top_customer(d.make_orders(), d.make_products()),
         "Ali"),

        ("7.2 best_selling_product",
         lambda: p.t7_2_best_selling_product(d.make_orders(), d.make_products()),
         "Mouse"),

        ("7.3 customer_ranking",
         lambda: list(p.t7_3_customer_ranking(d.make_orders(), d.make_products()).index),
         ["Ali", "Hina", "Zoya", "Sara", "Omar"]),

        ("7.4 unmatched_orders",
         lambda: p.t7_4_unmatched_orders(d.make_orders(), d.make_products())["product_id"].tolist(),
         [107]),

        ("7.5 save_report",
         lambda: p.t7_5_save_report(
             d.make_orders(), d.make_products(), "results/test_report.csv"
         ).empty,
         False),
    ],




}


def run(step):
    passed = 0

    for name, fn, expected in CHECKS[step]:
        try:
            got = fn()
            if got == expected:
                print(f"PASS {name}")
                passed += 1
            else:
                print(f"FAIL {name} -> you returned {got!r}")

        except NotImplementedError:
            print(f"TODO {name}")

        except Exception as e:
            print(f"ERROR {name} -> {type(e).__name__}: {e}")

    return passed, len(CHECKS[step])


if __name__ == "__main__":
    steps = [int(sys.argv[1])] if len(sys.argv) > 1 else sorted(CHECKS)
    got = total = 0

    for step in steps:
        print(f"Step {step}")
        a, b = run(step)
        got += a
        total += b

    print(f"\nScore: {got}/{total}")
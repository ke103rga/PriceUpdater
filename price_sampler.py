import re
from xls_file_maker import get_data
from new_price_converter import show_converted_price


def sample_max_year_literature(converted_price):
    year_pattern = r"\(\d{4}\)"

    for cls in converted_price.keys():
        for subject in converted_price[cls].keys():
            converted_price_rows = converted_price[cls][subject].copy()
            ident_rows = {}
            unique_rows = []
            for row in converted_price_rows:
                name = row["Наименование"]
                span = re.search(year_pattern, name)
                if span:
                    span = span.span()
                else:
                    unique_rows.append(name)
                    continue
                year = int(name[span[0]+1: span[1]-1])
                name = name.replace(name[span[0]:span[1]], "")

                if name in ident_rows.keys():
                    ident_rows[name].append(year)
                else:
                    ident_rows[name] = [year]

            for name, years in ident_rows.items():
                unique_rows.append(f"{name}({max(years)})")

            print(f"      {cls}")
            print(f"           {subject}")
            print(unique_rows)

            for row in converted_price_rows:
                name = row["Наименование"]
                if name not in unique_rows:
                    converted_price[cls][subject].remove(row)

    return converted_price


# converted_price = get_data(file_name="C:\\Users\\Анастасия\\Downloads\\knigi-polnyy-prays.xlsx")
# show_converted_price(converted_price)
#
# sampled_price = sample_max_year_literature(converted_price)
# show_converted_price(sampled_price)
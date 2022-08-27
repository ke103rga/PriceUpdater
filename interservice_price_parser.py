import pandas as pd
import re
from templates import new_price_template


def get_price(filename="C:\\Users\\Виктория\\Downloads\\testPrice.xlsx"):
    price = pd.read_excel(filename, header=12)
    return price


def get_study_literature(price, sale=17):
    new_price = new_price_template.copy()
    valid_classes = new_price.keys()

    for row in price.iterrows():
        data = row[1]
        name = data["Наименование"]
        if not pd.isnull(name):
            name = name.split("/")[0].lower()
            cls = contains_cls(name)
            if cls and cls in valid_classes:
                # print(data["ISBN"])
                formalized_data = formalize_data(data.to_dict(), cls, sale)
                new_price[cls].append(formalized_data)

    return new_price


def contains_cls(name):
    cls_pattern = r"\d+?кл"
    period_pattern = r"\d+?-\d+?кл"
    correct_patterns = [r"\d+?доп. кл", r"\d+? доп кл"]
    oge_pattern = r" огэ "
    ege_pattern = r" егэ "

    if re.search(period_pattern, name):
        span = re.search(r"\d+-\d+", name).span()
        return name[span[0]:span[1]].split("-")[-1]
    elif re.search(cls_pattern, name):
        span = re.search(r"\d+", name).span()
        return name[span[0]:span[1]]
    elif "начал" in name and "школ" in name:
        return "4"
    elif "пропис" in name and "горец" in name:
        return "1"
    elif re.search(oge_pattern, name):
        return "огэ"
    elif re.search(ege_pattern, name):
        return "егэ"
    elif any([re.search(pattern, name) for pattern in correct_patterns])\
            or ("интеллект" in name and "наруш" in name):
        return "кор"
    return None


def formalize_data(data, cls, sale):

    def new_cost(cost, sale):
        return cost * (100-sale) / 100

    cols_for_del = ["Переплет", "Код", "Новинка", "В упаковке", "Остаток", "Год издания",
                    "Цена со скидкой", "Сумма", "Сумма со скидкой", "Артикул", "Автор"]
    for column in cols_for_del:
        del data[column]

    data["Класс"] = cls
    data["Цена прайса"] = data.pop("Цена")
    data[f"Цена прайса со скидкой {sale}%"] = new_cost(data["Цена прайса"], sale)

    return data


def parse_price(filename=None, price=None, sale=17):
    if filename:
        price = get_price(filename)

    new_price = get_study_literature(price, sale)

    return new_price


def test(filename="C:\\Users\\Виктория\\Downloads\\knigi-polnyy-prays_3.xlsx"):
    prices = parse_price(filename)
    new_price = []
    for price in prices.values():
        new_price.extend(price)
    df = pd.DataFrame(new_price)
    df.to_excel("test_result.xls", index=False)



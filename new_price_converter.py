from templates import converted_price_template
from subject_selector import selector_params, find_subject_literature


def classify_literature(new_price, converted_price=converted_price_template.copy()):
    for cls in new_price.keys():
        cls_price = new_price.get(cls)
        # if cls in ["10", "11"]:
        #     cls = "10-11"
        subjects = converted_price.get(cls).keys()

        for subject in subjects:
            if subject == "Общее":
                continue
            converted_price[cls][subject], cls_price = find_subject_literature(cls_price, **selector_params[subject])

        converted_price[cls]["Общее"] = cls_price
    return converted_price


def show_converted_price(converted_price):
    for cls in converted_price.keys():
        print(f"                    {cls}")
        for subject in converted_price[cls].keys():
            print(f"                 {subject}")
            print(len(converted_price[cls][subject]))


# converted_price = classify_literature(new_price)
# show_converted_price(converted_price)

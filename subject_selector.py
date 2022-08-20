
def find_subject_literature(cls_price, key_words, exclude_words=None, all_words=False):
    if exclude_words is None:
        exclude_words = []
    result = []
    new_cls_price = cls_price.copy()
    for row in cls_price:
        name = row["Наименование"].lower()
        if all_words:
            if all(word in name for word in key_words) and all(word not in name for word in exclude_words):
                result.append(row)
                new_cls_price.remove(row)
        else:
            if any(word in name for word in key_words) and all(word not in name for word in exclude_words):
                result.append(row)
                new_cls_price.remove(row)

    return (result, new_cls_price)


def find_common(cls_price, converted_cls_price):
    common = []
    for row in cls_price:
        add_row = True
        for subject in converted_cls_price.keys():
            print(list(map(lambda row: row["Наименование"], converted_cls_price[subject])))
            print(row["Наименование"])
            if row["Наименование"] in list(map(lambda row: row["Наименование"], converted_cls_price[subject])):
                add_row = False
                break
        if add_row:
            common.append(row)

    return common


selector_params = {"Иностранные языки": {"key_words": ["англ", "немец", "франц", "итал"], "all_words": False},
                    "Изобразительное искусство": {"key_words": ["изобр", "иск", "изо"], "all_words": True},
                    "Информатика": {"key_words": ["информатик"], "all_words": True},
                    "Литература": {"key_words": ["литерат", "чтен"], "all_words": False},
                    "Математика": {"key_words": ["алгеб", "матем", "геомет", "счет", "цифр"], "all_words": False},
                    "Музыка": {"key_words": ["музык"], "all_words": True},
                    "Окружающий мир": {"key_words": ["окр", "мир", "природ", "естествознан",], "all_words": False},
                    "Русский язык": {"key_words": ["родн", "рус", "яз", "пишем", "чистопис", "писат", "азбук", "грамот", "пропис", "письм", "букварь"], "exclude_words": ["литер", "чтен", "немец","англ", "итал", "цифр"], "all_words": False},
                    "Технология": {"key_words": ["технолог"], "all_words": True},
                    "Физкультура": {"key_words": ["физ", "культ"], "all_words": True},
                    "География": {"key_words": ["географ"], "all_words": True},
                    "Биология": {"key_words": ["биолог", "естественнонауч", "естествознан"], "all_words": False},
                    "История и МХК": {"key_words": ["истор", "мхк"], "all_words": False},
                    "Основы духовно-нравственной культуры народов ": {"key_words": ["этик", "культ", "нравств"], "all_words": False},
                    "Основы религиозных культур и светской этики": {"key_words": ["светс", "этик"], "all_words": True},
                    "Технология и Изобразительное искусство": {"key_words": ["изобр", "иск", "труд", "мастерск", "технолог"], "all_words": False},
                    "ОБЖ и Физкультура": {"key_words": ["здоров", "обж", "физ", "культ"], "all_words": False},
                    "Общественные науки": {"key_words": ["обществ", "культур", "граждан", "финан", "прав"], "all_words": False},
                    "Технология, ИЗО, Черчение": {"key_words": ["изобр", "иск", "труд", "мастерск", "технолог", "черчен"], "all_words": False},
                    "Физика": {"key_words": ["физик", "механик"], "all_words": False},
                    "Химия": {"key_words": ["хими", ], "all_words": False},
                    "Технология и Черчение": {"key_words": ["иск", "труд", "мастерск", "технолог", "черчен"], "all_words": False},
                    "Общественные науки, Экономика": {"key_words": ["обществ", "культур", "граждан", "финан", "прав", "эконом"], "all_words": False},
                    "Физика, астрономия": {"key_words": ["физик", "астроном", "механик"], "all_words": False}}
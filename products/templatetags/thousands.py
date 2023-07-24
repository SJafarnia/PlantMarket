from django import template

register = template.Library()


@register.filter(name='sepp')
def k_separator(num, lang: str) -> str:
    """Gets an English unicode number and separates its translated to Persian/Arabic string by thousands.

    Args:
        num: input number.
        lang (str): target language ('fa' for Persian, 'ar' for Arabic, None for just returning the input number
        separated by thousands).

    Returns:
        str: a string of the input number separated by thousands and translated to target language.

    """

    if lang:
        string_input = str(num)
        reversed_list = [x for x in reversed(list(string_input))]

        loop_n = 0
        for index in range(0, len(string_input)):
            if (index + 1) % 3 == 0:
                reversed_list.insert(index + 1 + loop_n, ",")
                loop_n += 1

        unreversed_list = [x for x in reversed(list(reversed_list))]

        if unreversed_list[0] == ",":
            unreversed_list.pop(0)

        separated_num = "".join(map(str, unreversed_list))

        def transform(number):
            if lang == "fa":
                dic = {
                    "0": '۰',
                    '1': '١',
                    "2": '٢',
                    "3": '۳',
                    '4': '۴',
                    "5": '۵',
                    "6": '۶',
                    "7": '۷',
                    "8": '۸',
                    "9": '۹',
                }
            elif lang == "ar":
                dic = {
                    "0": '٠',
                    '1': '١',
                    "2": '٢',
                    "3": '٣',
                    '4': '٤',
                    "5": '٥',
                    "6": '٦',
                    "7": '٧',
                    "8": '٨',
                    "9": '۹',
                }
            elif lang is None or not lang:
                separated_num = f"{int(num):,}"
                return str(separated_num)

            target = []
            for char in number:
                if char in dic:
                    target.append(dic[char])
                else:
                    target.append(char)

            return "".join(target)

        return str(transform(separated_num))

    separated_num = f"{int(num):,}"
    return str(separated_num)



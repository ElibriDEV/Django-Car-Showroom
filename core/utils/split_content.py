import typing as t


def split_content(data: list[t.Any], per_set: int = 4) -> list[list[t.Any]]:
    page = []
    page_set = []
    for data_index in range(len(data)):
        if data_index % (per_set - 1) == 0 and data_index != 0:
            page_set.append(data[data_index])
            page.append(page_set)
            page_set = []
        else:
            page_set.append(data[data_index])
    else:
        if page_set:
            page.append(page_set)
    return page
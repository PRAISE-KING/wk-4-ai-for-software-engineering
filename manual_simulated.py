def sort_by_key(data, key):
    sorted_list = []
    for item in data:
        inserted = False
        for i in range(len(sorted_list)):
            if item[key] < sorted_list[i][key]:
                sorted_list.insert(i, item)
                inserted = True
                break
        if not inserted:
            sorted_list.append(item)
    return sorted_list

class Element:
    def __init__(self, value: str, timestamp: int):
        self.value = value
        self.timestamp = timestamp


class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [Element(value, timestamp)]
        else:
            self.map[key].append(Element(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        named_list = self.map[key]
        left, right = 0, len(named_list) - 1
        if named_list[left].timestamp > timestamp:
            # if the timestamp we look for is smaller than what we saved
            return ""
        if left == right:
            # only relevant if len(named_list)==1
            return named_list[left].value

        # Now we want to search the list for the timestamp provided
        # OR the largest timestamp that is smaller
        max_small_val = named_list[left].value
        while left <= right:
            middle = (right - left) // 2 + left
            if named_list[middle].timestamp > timestamp:
                right = middle - 1
            elif named_list[middle].timestamp == timestamp:
                return named_list[middle].value
            else:
                max_small_val = named_list[middle].value
                left = middle + 1
        return max_small_val

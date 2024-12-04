def zipmap(key_list, value_list, override=False):
    if not override and len(set(key_list)) != len(key_list):
        return None
    
    length = max(len(key_list), len(value_list))
    extended_keys = key_list + [None] * (length - len(key_list))
    extended_values = value_list + [None] * (length - len(value_list))
    
    result = dict(map(lambda kv: (kv[0], kv[1]), zip(extended_keys, extended_values)))
    return result

# Examples
print(zipmap(['a', 'b', 'c'], [1, 2, 3]))             # {'a': 1, 'b': 2, 'c': 3}
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))      # {1: 4, 2: 7, 3: 6}
print(zipmap([1, 3, 5, 7], [2, 4, 6]))               # {1: 2, 3: 4, 5: 6, 7: None}


from collections import defaultdict

def group_by(f, target_list):
    grouped = defaultdict(list)
    for item in target_list:
        grouped[f(item)].append(item)
    return dict(grouped)

# Examples
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))
# {2: ['hi', 'me'], 3: ['dog', 'bad'], 4: ['good']}


from functools import reduce

def custom_filter(function, iterable):
    return reduce(
        lambda items, value: items + [value] if function(value) else items,
        iterable,
        []
    )

# Examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = lambda x: x % 2 == 0
filtered_numbers = custom_filter(is_even, numbers)
print(filtered_numbers)  # [2, 4, 6, 8, 10]

words = ["hi", "hello", "world", "bye", "python"]
length_criteria = lambda word: len(word) > 3
filtered_words = custom_filter(length_criteria, words)
print(filtered_words)  # ['hello', 'world', 'python']



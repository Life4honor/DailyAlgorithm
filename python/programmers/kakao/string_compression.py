def solution(s):
    length = len(s)
    answer = length
    compressed = {}

    for term in range(1, length):
        char_array = s
        if term not in compressed:
            compressed[term] = {}

        prev = None
        compressed_array = ""
        while char_array != "":
            curr = char_array[:term]
            if prev is not None and prev != curr:
                compressed_array += f"{compressed[term][prev]}" if compressed[term][prev] != 1 else ""
                compressed_array += f"{prev}"
                compressed[term] = {}

            char_array = char_array[term:]
            if curr not in compressed[term]:
                compressed[term][curr] = 0
            compressed[term][curr] += 1

            if char_array == "":
                compressed_array += f"{compressed[term][curr]}" if compressed[term][curr] != 1 else ""
                compressed_array += f"{curr}"
            prev = curr
        answer = min(len(compressed_array), answer)

    return answer

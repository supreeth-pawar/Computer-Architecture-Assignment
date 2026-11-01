
cache = [None] * 8
blocks = [3, 11, 3, 19, 11, 27, 3]
hits = misses = 0

for block in blocks:
    line = block % 8

    if cache[line] == block:
        status = "HIT"
        hits += 1
    else:
        status = "MISS"
        misses += 1
        cache[line] = block

    print(f"Block: {block}, Line: {line}, {status}")
    print("Cache:", cache)

print("\nTotal Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hits / len(blocks))

# # Read input values n, m, and a
# n, m, a = map(int, input().split())

# # Calculate the number of flagstones needed along the length and width
# flagstones_length = (n + a - 1) // a  # ceil(n / a)
# flagstones_width = (m + a - 1) // a    # ceil(m / a)

# # Calculate the total number of flagstones required
# total_flagstones = flagstones_length * flagstones_width

# # Print the result
# print(total_flagstones)



n, m, a = map(int, input().split())
lenght = n // a
width = m // a
if n % a != 0:
    lenght += 1
if m % a != 0:
    width += 1

tiles_need = lenght * width
print(tiles_need)


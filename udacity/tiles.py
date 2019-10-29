# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

 #   How many tiles are needed?
 #   You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?



# Fill this in with an expression that calculates how many tiles are needed.
floor_1 = (9*7)
floor_2 = (5*7)
tiles_required = floor_1+floor_2
print("Tiles required :",tiles_required)

# Fill this in with an expression that calculates how many tiles will be left over.
total_tiles = (17*6)
tiles_left = total_tiles - tiles_required
print("Tiles_left :",(tiles_left))


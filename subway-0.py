# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_corner(mc, xs, ys, zs,xe,ye,ze):
	air = 0;
	mc.setBlocks(xs,ys,zs,xe,ye,ze,air)	

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z,x+h,y+k,z+l,air)	

def clear_with_air_block(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l,air)	

def shaft(mc,xs,ys,zs,wh,l):
	wh = int(wh / 2)
	mc.setBlocks(xs-wh,ys-wh,zs,xs+wh,ys+wh,zs+l,89)
	mc.setBlocks(xs-wh+1,ys-wh+1,zs,xs+wh-1,ys+wh-1,zs+l,0)

def clear_build(mc,x, y, z):
	xs ,ys,zs,xe,ye,ze = -127, -60, -127, 128, 50, 128
	print(xs ,ys,zs,xe,ye,ze )
	#clear_with_air_corner(mc, xs,ys,zs,xe,ye,ze)
	#xs ,ys,zs,xe,ye,ze = -126, -126, -126, 127, -125, 127
	xs ,ys,zs,xe,ye,ze = -127, -70, -127, 128, -55, 128
	mc.setBlocks(xs,ys,zs,xe,ye,ze,79)
	xs ,ys,zs,xe,ye,ze = -10, -70, -10, 10, 50, 10
	#clear_with_air_corner(mc, xs,ys,zs,xe,ye,ze)
	xs ,ys,zs,xe,ye,ze = -127, -70, -127, 128, -60, 128
	mc.setBlocks(xs,ys,zs,xe,ye,ze,13)
	xs ,ys,zs,xe,ye,ze = -1, -63, 0, 0, 50, 0
	#clear_with_air_corner(mc, xs,ys,zs,xe,ye,ze)
	xs,ys,zs = -100, -5, -100
	shaft(mc,xs,ys,zs,10,100)
	mc.player.setPos(xs+1,ys+1,zs+2)
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	print("position ",x,y,z)
	clear_build(mc, x,y,z)
	

main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""

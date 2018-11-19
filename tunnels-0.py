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
	
def stairs(mc,xs,ys,zs,w,steps):
	#steps go up long z
	wd = int(w/2)
	steplength = steps
	for n in range (0,steps):
		mc.setBlocks(xs-wd,ys+n,zs+(n*2),xs+wd,ys+n,zs+(steps*2),42)
		steplength = steplength - 2 


def tunnelc(mc,xs,ys,zy,width,length):
	w = int(width/2); l = length
	mc.setBlocks(xs-w,ys-w,zs,xs+w,ys+w ,zs+l,42 )

def shafts(mc):
	xx,yy,zz,h,k,l = 0,0,0,50,100,50 # comment out when design is good
	clear_with_air_up(mc,xx, yy, zz,h,k,l) # comment out when design is good
	#  +x y -z 
	y = int(30); lgth = int(60)
	#  down shaft
	xs,ys,zs,w,l = -30,y,30,10,20
	mc.setBlocks(xs,ys,zs,xs+w,ys+20 ,zs-w,42 )
	#end down shaft
	#top tunnel
	xs,ys,zs,w,l = -30,y,30,10,lgth # N
	mc.setBlocks(xs,ys,zs,xs+l,ys+w ,zs-w,89)
	# +x +y +z 
	xs,ys,zs,w,l = -30,y,-30,10,lgth # S
	mc.setBlocks(xs,ys,zs,xs+l,ys + w ,zs+w,89)
	#  x +y +z
	xs,ys,zs,w,l = -30,y,30,10,lgth # E
	mc.setBlocks(xs,ys,zs,xs+w,ys + w ,zs-l,89)
	#  x +y +z
	xs,ys,zs,w,l = 30,y,30,10,lgth # W
	mc.setBlocks(xs,ys,zs,xs-w,ys + w ,zs-l,89)
	#air
	xs,ys,zs,w,l = -30+1,y+1,30-1,10-2,lgth-2 #N
	mc.setBlocks(xs,ys,zs,xs+l,ys + w ,zs-w,0)
	# +x +y +z 
	xs,ys,zs,w,l = -30+1,y+1,-30+1,10-2,lgth-2  #S
	mc.setBlocks(xs,ys,zs,xs+l,ys + w ,zs+w,0)
	#  x +y +z
	xs,ys,zs,w,l = -30+1,y+1,30-1,10-2,lgth-2 #E
	mc.setBlocks(xs,ys,zs,xs+w,ys + w ,zs-l,0) 
	#  x +y +z
	xs,ys,zs,w,l = 30-1,y+1,30-1,10-2,lgth-2  #W
	mc.setBlocks(xs,ys,zs,xs-w,ys + w ,zs-l,0)
	#air down shaft
	xs,ys,zs,w,l = -30,y,30,9,20
	mc.setBlocks(xs+1,ys+1,zs+1,xs+w,ys+21 ,zs-w,0)
	#end down shaft
	#stairs
	stairs(mc,xs+5,ys,zs,10,20)
	 
def build_tunnels(mc,x, y, z):
	shafts(mc)
	mc.player.setPos(27,35,-40)
	mc.player.setPos(-26,30+25,25-20)
	#mc.player.setPos(0,50,0)
	
	
def main():
	mc = init()
	x, y, z = mc.player.getPos()
	#print("position ",x,y,z)
	build_tunnels(mc, x,y,z)
	
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

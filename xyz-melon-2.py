# Base project format.
# put this on the desktop : git clone https://github.com/tritechsc/mcpi
from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep
from random import randint

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()		
    return mc

def clear_with_air_up(mc, x, y, z,h,k,l):
	air = 0;
	mc.setBlocks(x-h,y,z-l,x+h,y+k,z+l,air)	

def melon(mc):
	eI=mc.getPlayerEntityIds()
	m = 0
	while m<(len(eI)*50):
		x=randint(-10,10)
		z=randint(-10,10)
		y=mc.getHeight(x,z)
		mc.setBlock(x,y,z,103)
		m = m + 1

def stairs(mc,xs,ys,zs,w,steps):
	#steps go up long z
	wd = int(w/2)
	steplength = steps
	for n in range (0,steps):
		mc.setBlocks(xs-wd,ys+n,zs+(n*2),xs+wd,ys+n,zs+(steps*2),82)
		steplength = steplength - 2 

def FiveBlocks(mc):
	xx,yy,zz,h,k,l = 0,20,0,50,100,50 # comment out when design is good
	clear_with_air_up(mc,xx, yy, zz,h,k,l) # comment out when design is good
	xs,ys,zs = 10,25,10
	mc.setBlocks(xs+5,ys,zs+5,xs-5,ys-5,zs-5,35,14)	 #red
	xs,ys,zs = -10,25,10
	mc.setBlocks(xs+5,ys,zs+5,xs-5,ys-5,zs-5,35,13)	# green
	xs,ys,zs = -10,25,-10
	mc.setBlocks(xs+5,ys,zs+5,xs-5,ys-5,zs-5,35,11)	# blue
	xs,ys,zs = 10,25,-10
	mc.setBlocks(xs+5,ys,zs+5,xs-5,ys-5,zs-5,35,4)	#yellow
	xs,ys,zs = 0,25,0
	mc.setBlocks(xs+5,ys,zs+5,xs-5,ys-5,zs-5,35,0)	#white
	x, y, z = mc.player.getPos()
	#print("position ",x,y,z)
	scnds = 0.25
	mc.player.setPos(13,35	,13)
	sleep(scnds)
	mc.player.setPos(-7,35	,13)
	sleep(scnds)
	mc.player.setPos(-7,35	,-7)
	sleep(scnds)
	mc.player.setPos(13,35	,-7)
	sleep(scnds)
	mc.player.setPos(0,45,0)
	#mc.player.setPos(12,28,10)g 
	stairs(mc,0,25,5,10,10)

def checkHit(mc,score,c):
	eI=mc.getPlayerEntityIds() #eI = entity Ids
	for each in eI:
		if each not in score:
			score.update({each:0})
			mc.setting("world_immutable",True)
			melon(mc)
	bE=mc.events.pollBlockHits() #bE block Event	
	for each in bE:
		x=each.pos.x
		y=each.pos.y
		z=each.pos.z
		if mc.getBlock(x,y,z)==103:
			mc.setBlock(x,y,z,20)
			#meloncount=meloncount-1
			playerId=each.entityId
			score[playerId]=score[playerId]+1
			mc.postToChat("Player {0} has {1} points!".format(playerId,score[playerId]))
def main():
	mc = init()
	mc.setting("world_immutable",True)
	FiveBlocks(mc)
	score = {}
	done = 0
	c = 0
	while (done == 0):
		checkHit(mc,score,c)
		
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

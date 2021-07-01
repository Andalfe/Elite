import sys, math, pygame
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pyglet import *





COBRA_MK_1_VERTEX = ((-18,-1,50),(18,-1,50),(-66,0,7),(66,0,7),(-32,12,-38),(32,12,-38),(-54,-12,-38),(54,-12,-38),(0,12,-6),(0,-1,50),(0,-1,60))
COBRA_MK_1_EDGES  = ((1,0),(0,2),(2,6),(6,7),(7,3),(3,1),(2,4),(4,5),(5,3),(0,8),(8,1),(4,8),(8,5),(4,6),(5,7),(0,6),(1,7),(10,9)) 
COBRA_MK_1_FACES = (())




MISSILE_VERTEX = ((0,0,68),(8,-8,36),(8,8,36),(-8,8,36),(-8,-8,6),(8,8,-44),(8,-8,-44),(-8,-8,-44),(-8,8,-44),(12,12,-44),(12,-12,-44),(-12,-12,-44),(-12,12,-44),(-8,8,-12),(-8,-8,-12),(8,8,-12),(8,-8,-12))
MISSILE_EDGES = ((0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(3,4),(2,3),(2, 5),(1,6),(4,7),(3,8),(7,8),(5,8),(5,6),(6,7),(6,10),(5,9),(8,12),(7,11),(9,15),(10,16),(12,13),(11,14))
MISSILE_FACES = ((-64,0,16),(0,-64,16),(64,0,16),(0,64,16),(32,0,0),(0,-32,0),(-32,0,0),(0,32,0),(0,0,-176))


CORIOLIS_VERTEX = ((160,0,160),(0,160,160),(-160,0,160),(0,-160,160),(160,-160,0),(160,160,0),(-160,160,0),(-160,-160,0),(160,0,-160),(0,160,-160),(-160,0,-160),(0,-160,-160),(10,-30,160),(10,30,160),(-10,30,160),(-10,-30,160))
CORIOLIS_EDGES = ((0,3),(0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(5,1),(1,6),(2,6),(2,7),(3,7),(8,11),(8,9),(9,10),(10,11),(4,11),(4,8),(5,8),(5,9),(6,9),(6,10),(7,10),(7,11),(12,13),(13,14),(14,15),(15,12))
CORIOLIS_FACES = ((0,0,160),(107,-107,107),(107,107,107),(-107,107,107),(-107,-107,107),(0,-160,0),(160,0,0),(-160,0,0),(0,160,0),(-107,-107,-107),(107,-107,-107),(107,107,-107),(-107,107,-107),(0,0,-160))
CORIOLIS_INFO = {'Face list': CORIOLIS_FACES,'Edge list': CORIOLIS_EDGES,'Vertex list': CORIOLIS_VERTEX,'Max. canisters on demise': 0,'Targetable area': 160*160,"Max. edge count": 21,'Gun vertex': 0,'Explosion count': 54,'Number of vertices': 16,'Number of edges': 28,'Bounty': 5,'Number of faces': 14,'Visibility distance': 120,'Max. energy': 240,'Max. speed': 0,'Normals are scaled by': 1,'Laser power': 0,'Missiles': 6}






ESCAPE_POD_VERTEX = ((-7,0,36),(-7,-14,-12),(-7,14,-12),(21,0,0))
ESCAPE_POD_EDGES = ((0,1),(1,2),(2,3),(3,0),(0,2),(3,1))
ESCAPE_POD_FACES = ((26,0,-61),(19,51,15),(19,-51,15),(-56,0,0))
ESCAPE_POD_INFO = {'Face list': ESCAPE_POD_FACES,'Edge list': ESCAPE_POD_EDGES,'Vertex list': ESCAPE_POD_VERTEX,'Max. canisters on demise': 0,'Targetable area': 16*16,"Max. edge count": 6,'Gun vertex': 0,'Explosion count': 22,'Number of vertices': 4,'Number of edges': 6,'Bounty': 5,'Number of faces': 4,'Visibility distance': 8,'Max. energy': 17,'Max. speed': 8,'Normals are scaled by': 8,'Laser power': 0,'Missiles': 0}





PLATE_VERTEX = ((-15,-22,-9),(-15,38,-9),(19,32,11),(10,-46,6))
PLATE_EDGES = ((0,1),(1,2),(2,3),(3,0))


CANISTER_VERTEX = ((24,16,0),(24,5,15),(24,-13,9),(24,-13,-9),(24,5,-15),(-24,16,0),(-24,5,15),(-24,-13,9),(-24,-13,-9),(-24,5,-15))
CANISTER_EDGES = ((0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(1,6),(2,7),(3,8),(4,9),(5,6),(6,7),(7,8),(8,9),(9,5))
CANISTER_FACES = ((96,0,0),(0,41,30),(0,-18,48),(0,-51,0),(0,-18,-48),(0,41,-30),(-96,0,0,))
CANISTER_INFO = {'Face list': CANISTER_FACES,'Edge list': CANISTER_EDGES,'Vertex list': CANISTER_VERTEX,'Max. canisters on demise': 0,'Targetable area': 20*20,"Max. edge count": 12,'Gun vertex': 0,'Explosion count': 18,'Number of vertices': 10,'Number of edges': 15,'Bounty': 5,'Number of faces': 7,'Visibility distance': 12,'Max. energy': 17,'Max. speed': 15,'Normals are scaled by': 4,'Laser power': 0,'Missiles': 0}





BOULDER_VERTEX = ((-18,37,-11),(30,7,12),(28,-7,-12),(2,0,-39),(-28,34,-30),(5,-10,13),(20,17,-30))
BOULDER_EDGES = ((0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(1,5),(2,5),(3,5),(4,5),(0,6),(1,6),(2,6),(3,6),(4,6))




ASTEROID_VERTEX = ((0,80,0),(-80,-10,0),(0,-80,0),(70,-40,0),(60,50,0),(50,0,60),(-40,0,70),(0,30,-75),(0,-50,-60))
ASTEROID_EDGES = ((0,1),(0,4),(3,4),(2,3),(1,2),(1,6),(2,6),(2,5),(5,6),(0,5),(3,5),(0,6),(4,5),(1,8),(1,7),(0,7),(4,7),(3,7),(3,8),(2,8),(7,8))
ASTEROID_FACES = ((9,66,81),(9,-66,81),(-72,64,31),(-64,-73,47),(45,-79,65),(135,15,35),(38,76,70),(-66,59,-39),(-67,-15,-80),(66,-14,-75),(-70,-80,-40),(58,-102,-51),(81,9,-67),(47,94,-63))
ASTEROID_INFO = {'Face list': ASTEROID_FACES,'Edge list': ASTEROID_EDGES,'Vertex list': ASTEROID_VERTEX,'Max. canisters on demise': 0,'Targetable area': 80*80,"Max. edge count": 16,'Gun vertex': 0,'Explosion count': 34,'Number of vertices': 9,'Number of edges': 21,'Bounty': 5,'Number of faces': 14,'Visibility distance': 50,'Max. energy': 60,'Max. speed': 30,'Normals are scaled by': 2,'Laser power': 0,'Missiles': 0}



SPLINTER_VERTEX = ((-24,-25,16),(0,12,-10),(11,-6,2),(12,42,7))
SPLINTER_EDGES = ((0,1),(1,2),(2,3),(3,0),(0,2),(3,1))



SHUTTLE_VERTEX = ((0,-17,23),(-17,0,23),(0,18,23),(18,0,23),(-20,-20,-27),(-20,20,-27),(20,20,-27),(20,-20,-27),(5,0,-27),(0,-2,-27),(-5,0,-27),(0,3,-27),(0,-9,35),(3,-1,31),(4,11,25),(11,4,25),(-3,-1,31),(-3,11,25),(-10,4,25))
SHUTTLE_EDGES = ((0,1),(1,2),(2,3),(0,3),(0,7),(0,4),(1,4),(1,5),(2,5),(2,6),(3,6),(3,7),(4,5),(5,6),(6,7),(4,7),(0,12),(1,12),(2,12),(3,12),(8,9),(9,10),(10,11),(8,11),(13,14),(14,15),(13,15),(16,17),(17,18),(16,18))



#LAST 4 EDGES CANT BE DRAWN. NO IDEA WHY.
TRANSPORTER_VERTEX = ((0,10,-26),(-25,4,-26),(-28,-3,-26),(-25,-8,-26),(26,-8,-26),(29,-3,-26),(26,4,-26),(0,6,12),(-30,-1,12),(-33,-8,12),(33,-8,12),(30,-1,12),(-11,-2,30),(-13,-8,30),(14,-8,30),(11,-2,30),(-5,6,2),(-18,3,2),(-5,7,-7),(-18,4,-7),(-11,6,-14),(-11,5,-7),(5,7,-14),(18,4,-14),(11,5,-7),(5,6,-3),(18,3,-3),(11,4,8),(11,5,-3),(-16,-8,-13),(-16,-8,16),(17,-8,-13),(17,-8,16),(-13,-3-26),(13,-3,-26),(9,3,-26),(-8,3,-26))
TRANSPORTER_EDGES = ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(0,6),(0,7),(1,8),(2,9),(3,9),(4,10),(5,10),(6,11),(7,8),(8,9),(10,11),(7,11),(7,15),(7,12),(8,12),(9,13),(10,14),(11,15),(12,13),(13,14),(14,15),(12,15),(16,17),(18,19),(19,20),(18,20),(20,21),(22,23),(23,24),(24,22),(25,26),(26,27),(25,27),(27,28),(29,30),(31,32),)#(33,34),(34,35),(35,36),(36,33))



COBRA_MK_3_VERTEX = ((32,0,76),(-32,0,76),(0,26,24),(-120,-3,-8),(120,-3,-8),(-88,16,-40),(88,16,-40),(128,-8,-40),(-128,-8,-40),(0,26,-40),(-32,-24,-40),(32,-24,-40),(-36,8,-40),(-8,12,-40),(8,12,-40),(36,8,-40),(36,-12,-40),(8,-16,-40),(-8,-16,-40),(-36,-12,-40),(0,0,76),(0,0,90),(-80,-6,-40),(-80,6,-40),(-88,0,-40),(80,6,-40),(88,0,-40),(80,-6,-40))
COBRA_MK_3_EDGES = ((0,1),(0,4),(1,3),(3,8),(4,7),(6,7),(6,9),(5,9),(5,8),(2,5),(2,6),(3,5),(4,6),(1,2),(0,2),(8,10),(10,11),(7,11),(1,10),(0,11),(1,5),(0,6),(20,21),(12,13),(18,19),(14,15),(16,17),(15,16),(14,17),(13,18),(12,19),(2,9),(22,24),(23,24),(22,23),(25,26),(26,27),(25,27))
COBRA_MK_3_FACES = ((0,62,31),(-18,55,16),(18,55,16),(-16,52,14),(16,52,14),(-14,47,0),(14,47,0),(-61,102,0),(61,102,0),(0,0,-80),(-7,-42,9),(0,-30,6),(7,-42,9))
COBRA_MK_3_INFO = {'Face list': COBRA_MK_3_FACES,'Edge list': COBRA_MK_3_EDGES,'Vertex list': COBRA_MK_3_VERTEX,'Max. canisters on demise': 3,'Targetable area': 95*95,"Max. edge count": 38,'Gun vertex': 0,'Explosion count': 42,'Number of vertices': 28,'Number of edges': 38,'Bounty': 0,'Number of faces': 13,'Visibility distance': 50,'Max. energy': 150,'Max. speed': 28,'Normals are scaled by': 2,'Laser power': 2,'Missiles': 3}




PYTHON_VERTEX = ((0,0,224),(0,48,48),(96,0,-16),(-96,0,-16),(0,48,-32),(0,24,-112),(-48,0,-112),(48,0,-112),(0,-48,48),(0,-48,-32),(0,-24,-112))
PYTHON_EDGES = ((0,8),(0,3),(0,2),(0,1),(2,4),(1,2),(2,8),(1,3),(3,8),(2,9),(3,4),(3,9),(3,5),(3,10),(2,5),(2,10),(2,7),(3,6),(5,6),(5,7),(7,10),(6,10),(4,5),(9,10),(1,4),(8,9))



BOA_VERTEX  = ((0,0,93),(0,40,-87),(38,-25,-99),(-38,-25,-99),(-38,40,-59),(38,40,-59),(62,0,-67),(24,-65,-79),(-24,-65,-79),(-62,0,-67),(0,7,-107),(13,-9,-107),(-13,-9,-107))
BOA_EDGES = ((0,5),(0,7),(0,9),(0,4),(0,6),(0,8),(4,5),(5,6),(6,7),(7,8),(8,9),(4,9),(1,4),(1,5),(3,9),(3,8),(2,6),(2,7),(1,10),(2,11),(3,12),(10,11),(11,12),(12,10))





ANACONDA_VERTEX = ((0,7,-58),(-43,-13,-37),(-26,-47,-3),(26,-47,-3),(43,-13,-37),(0,48,-49),(-69,15,-15),(-43,-39,40),(43,-39,40),(69,15,-15),(-43,53,-23),(-69,-1,32),(0,0,254),(69,-1,32),(43,53,-23))
ANACONDA_EDGES = ((0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(1,6),(2,7),(3,8),(4,9),(5,10),(6,10),(6,11),(7,11),(7,12),(8,12),(8,13),(9,13),(9,14),(5,14),(10,14),(10,12),(11,12),(12,13),(12,14))



ROCK_HERMIT_VERTEX = ((0,80,0),(-80,-10,0),(0,-80,0),(70,-40,0),(60,50,0),(50,0,60),(-40,0,70),(0,30,-75),(0,-50,-60))
ROCK_HERMIT_EDGES = ((0,1),(0,4),(3,4),(2,3),(1,2),(1,6),(2,6),(2,5),(5,6),(0,5),(3,5),(0,6),(4,5),(1,8),(1,7),(0,7),(4,7),(3,7),(3,8),(2,8),(7,8))



VIPER_HERMIT_VERTEX = ((0,0,72),(0,16,24),(0,-16,24),(48,0,-24),(-48,0,-24),(24,-16,-24),(-24,-16,-24),(24,16,-24),(-24,16,-24),(-32,0,-24),(32,0,-24),(8,8,-24),(-8,8,-24),(-8,-8,-24),(8,-8,-24))
VIPER_HERMIT_EDGES = ((0,3),(0,1),(0,2),(0,4),(1,7),(1,8),(2,5),(2,6),(7,8),(5,6),(4,8),(4,6),(3,7),(3,5),(9,12),(9,13),(10,11),(10,14),(11,14),(12,13))
VIPER_HERMIT_FACES = ((0,32,0),(-22,33,11),(22,33,11),(-22,-33,11),(22,-33,11),(0,-32,0),(0,0,-48))



SIDEWINDER_VERTEX = ((-32,0,36),(32,0,36),(64,0,-28),(-64,0,-28),(0,16,-28),(0,-16,-28),(-12,6,-28),(12,6,-28),(12,-6,-28),(-12,-6,-28))
SIDEWINDER_EDGES = ((0,1),(1,2),(1,4),(0,4),(0,3),(3,4),(2,4),(3,5),(2,5),(1,5),(0,5),(6,7),(7,8),(6,9),(8,9))
SIDEWINDER_FACES = ((0,32,8),(-12,47,6),(12,47,6),(0,0,-112),(-12,-47,6),(0,-32,8),(12,-47,6))
SIDEWINDER_INFO = {'Face list': SIDEWINDER_FACES,'Edge list': SIDEWINDER_EDGES,'Vertex list': SIDEWINDER_VERTEX,'Max. canisters on demise': 0,'Targetable area': 65*65,"Max. edge count": 15,'Gun vertex': 0,'Explosion count': 42,'Number of vertices': 10,'Number of edges': 15,'Bounty': 50,'Number of faces': 7,'Visibility distance': 20,'Max. energy': 70,'Max. speed': 37,'Normals are scaled by': 4,'Laser power': 2,'Missiles': 0}


MAMBA_VERTEX = ((0,0,64),(-64,-8,-32),(-32,8,-32),(32,8,-32),(64,-8,-32),(-4,4,16),(4,4,16),(8,3,28),(-8,3,28),(-20,-4,16),(20,-4,16),(-24,-7,-20),(-16,-7,-20),(16,-7,-20),(24,-7,-20),(-8,4,-32),(8,4,-32),(8,-4,-32),(-8,-4,-32),(-32,4,-32),(32,4,-32),(36,-4,-32),(-36,-4,-32),(-38,0,-32),(38,0,-32))
MAMBA_EDGES = ((0,1),(0,4),(1,4),(1,2),(2,3),(3,4),(5,6),(6,7),(7,8),(5,8),(9,11),(9,12),(10,13),(10,14),(13,14),(11,12),(15,16),(17,18),(15,18),(16,17),(20,21),(20,24),(21,24),(19,22),(19,23),(22,23),(0,2),(0,3))
MAMBA_FACES = ((0,-24,2),(0,24,2),(-32,64,16),(32,64,16),(0,0,-127))
MAMBA_INFO = {'Face list': MAMBA_FACES,'Edge list': MAMBA_EDGES,'Vertex list': MAMBA_VERTEX,'Max. canisters on demise': 1,'Targetable area': 70*70,"Max. edge count": 23,'Gun vertex': 0,'Explosion count': 34,'Number of vertices': 25,'Number of edges': 28,'Bounty': 150,'Number of faces': 5,'Visibility distance': 25,'Max. energy': 90,'Max. speed': 30,'Normals are scaled by': 4,'Laser power': 2,'Missiles': 2}




KRAIT_VERTEX = ((0,0,96),(0,18,-48),(0,-18,-48),(90,0,-3),(-90,0,-3),(90,0,87),(-90,0,87),(0,5,53),(0,7,38),(-18,7,19),(18,7,19),(18,11,-39),(18,-11,-39),(36,0,-30),(-18,11,-39),(-18,-11,-39),(-36,0,-30))
KRAIT_EDGES = ((0,1),(0,2),(0,3),(0,4),(1,4),(4,2),(2,3),(3,1),(3,5),(4,6),(1,2),(7,10),(8,10),(7,9),(8,9),(11,13),(13,12),(12,11),(14,15),(15,16),(16,14))




ADDER_VERTEX = ((-18,0,40),(18,0,40),(30,0,-24),(30,0,-40),(18,-7,-40),(-18,-7,-40),(-30,0,-40),(-30,0,-24),(-18,7,-40),(18,7,-40),(-18,7,13),(18,7,13),(-18,-7,13),(18,-7,13),(-11,3,29),(11,3,29),(11,4,24),(-11,4,24))
ADDER_EDGES = ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,0),(3,9),(9,8),(8,6),(0,10),(7,10),(1,11),(2,11),(0,12),(7,12),(1,13),(2,13),(10,11),(12,13),(8,10),(9,11),(5,12),(4,13),(14,15),(15,16),(16,17),(17,14))




GECKO_VERTEX = ((-10,-4,47),(10,-4,47),(-16,8,-23),(16,8,-23),(-66,0,-3),(66,0,-3),(-20,-14,-23),(20,-14,-23),(-8,-6,33),(8,-6,33),(-8,-13,-16),(8,-13,-16))
GECKO_EDGES = ((0,1),(1,5),(5,3),(3,2),(2,4),(4,0),(5,7),(7,6),(6,4),(0,2),(1,3),(0,6),(1,7),(2,6),(3,7),(8,10),(9,11))


WORM_VERTEX = ((10,-10,35),(-10,-10,35),(5,6,15),(-5,6,15),(15,-10,25),(-15,-10,25),(26,-10,-25),(-26,-10,-25),(8,14,-25),(-8,14,-25))
WORM_EDGES = ((0,1),(1,5),(5,7),(7,6),(6,4),(4,0),(0,2),(1,3),(4,2),(5,3),(2,8),(8,6),(3,9),(9,7),(2,3),(8,9))




ASP_MK_2_VERTEX = ((0,-18,0),(0,-9,-45),(43,0,-45),(69,-3,0),(43,-14,28),(-43,0,-45),(-69,-3,0),(-43,-14,28),(26,-7,73),(-26,-7,73),(43,14,28),(-43,14,28),(0,9,-45),(-17,0,-45),(17,0,-45),(0,-4,-45),(0,4,-45),(0,-7,73),(0,-7,83))
ASP_MK_2_EDGES = ((0,1),(0,4),(0,7),(1,2),(2,3),(3,8),(8,9),(6,9),(5,6),(1,5),(3,4),(4,8),(6,7),(7,9),(2,12),(5,12),(10,12),(11,12),(10,11),(6,11),(9,11),(3,10),(8,10),(13,15),(15,14),(14,16),(16,13),(18,17))





PYTHON_P_VERTEX = ((0,0,224),(0,48,48),(96,0,-16),(-96,0,-16),(0,48,-32),(0,24,-112),(-48,0,-112),(48,0,-112),(0,-48,48),(0,-48,-32),(0,-24,-112))
PYTHON_P_EDGES = ((0,8),(0,3),(0,2),(0,1),(2,4),(1,2),(2,8),(1,3),(3,8),(2,9),(3,4),(3,9),(3,5),(3,10),(2,5),(2,10),(2,7),(3,6),(5,6),(5,7),(7,10),(6,10),(4,5),(9,10),(1,4),(8,9))





FER_DE_LANCE_VERTEX = ((0,-14,108),(-40,-14,-4),(-12,-14,-52),(12,-14,-52),(40,-14,-4),(-40,14,-4),(-12,2,-52),(12,2,-52),(40,14,-4),(0,18,-20),(-3,-11,97),(-26,8,18),(-16,14,-4),(3,-11,97),(26,8,18),(16,14,-4),(0,-14,-20),(-14,-14,44),(14,-14,44))
FER_DE_LANCE_EDGES = ((0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(5,6),(6,7),(7,8),(0,8),(5,9),(6,9),(7,9),(8,9),(1,5),(2,6),(3,7),(4,8),(10,11),(11,12),(10,12),(13,14),(14,15),(13,15),(16,17),(16,18),(17,18))





MORAY_VERTEX = ((15,0,65),(-15,0,65),(0,18,-40),(-60,0,0),(60,0,0),(30,-27,-10),(-30,-27,-10),(-9,-4,-25),(9,-4,-25),(0,-18,-16),(13,3,49),(6,0,65),(-13,3,49),(-6,0,65))
MORAY_EDGES = ((0,1),(1,3),(3,6),(5,6),(4,5),(0,4),(1,6),(0,5),(0,2),(1,2),(2,3),(2,4),(2,5),(2,6),(7,8),(7,9),(8,9),(10,11),(12,13))





THARGOID_VERTEX = ((32,-48,48),(32,-68,0),(32,-48,-48),(32,0,-68),(32,48,-48),(32,68,0),(32,48,48),(32,0,68),(-24,-116,116),(-24,-164,0),(-24,-116,-116),(-24,0,-164),(-24,116,-116),(-24,164,0),(-24,116,116),(-24,0,164),(-24,64,80),(-24,64,-80),(-24,-64,-80),(-24,-64,80))
THARGOID_EDGES = ((0,7),(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(0,8),(1,9),(2,10),(3,11),(4,12),(5,13),(6,14),(7,15),(8,15),(8,9),(9,10),(10,11),(11,12),(12,13),(13,14),(14,15),(16,17),(18,19))
THARGOID_FACES = ((103,-60,25),(103,-60,-25),(103,-25,-60),(103,25,-60),(64,0,0),(103,60,-25),(103,60,25),(103,25,60),(103,-25,60),(-48,0,0))





THARGON_VERTEX = ((-9,0,40),(-9,-38,12),(-9,-24,-32),(-9,24,-32),(-9,38,12),(9,0,-8),(9,-10,-15),(9,-6,-26),(9,6,-26),(9,10,-15))
THARGON_EDGES = ((0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(1,6),(2,7),(3,8),(4,9),(5,6),(6,7),(7,8),(8,9),(9,5))





CONSTRICTOR_VERTEX = ((20,-7,80),(-20,-7,80),(-54,-7,40),(-54,-7,-40),(-20,13,-40),(20,13,-40),(54,-7,-40),(54,-7,40),(20,13,5),(-20,13,5),(20,-7,62),(-20,-7,62),(25,-7,-25),(-25,-7,-25),(15,-7,-15),(-15,-7,-15),(0,-7,0))
CONSTRICTOR_EDGES = ((0,1),(1,2),(1,9),(0,8),(0,7),(7,8),(2,9),(2,3),(6,7),(6,8),(5,8),(4,9),(3,9),(3,4),(4,5),(5,6),(3,6),(8,9),(10,12),(12,14),(14,10),(11,15),(13,15),(11,13))




LOGO_VERTEX = ((0,-9,55),(-10,-9,30),(-25,-9,93),(-150,-9,180),(-90,-9,10),(-140,-9,10),(0,-9,-95),(140,-9,10),(90,-9,10),(150,-9,180),(25,-9,93),(10,-9,30),(-85,-9,-30),(85,-9,-30),(-70,11,5),(-70,11,-25),(70,11,-25),(70,11,5),(0,-9,5),(0,-9,5),(0,-9,5),(-28,11,-2),(-49,11,-2),(-49,11,-10),(-49,11,-17),(-28,11,-17),(-28,11,-10),(-24,11,-2),(-24,11,-17),(-3,11,-17),(0,11,-2),(0,11,-17),(4,11,-2),(25,11,-2),(14,11,-2),(14,11,-17),(49,11,-2),(28,11,-2),(28,11,-10),(28,11,-17),(49,11,-17),(49,11,-10))                             
LOGO_EDGE = ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,11),(11,0),(14,15),(15,16),(16,17),(17,14),(4,12),(12,13),(13,8),(8,4),(4,14),(12,15),(13,16),(8,17),(21,22),(22,24),(24,25),(23,26),(27,28),(28,29),(30,31),(32,33),(34,35),(36,37),(37,39),(39,40),(41,38))




COUGAR_VERTEX = ((0,5,67),(-20,0,40),(-40,0,-40),(0,14,-40),(0,-14,-40),(20,0,40),(40,0,-40),(-36,0,56),(-60,0,-20),(36,0,56),(60,0,-20),(0,7,35),(0,8,25),(-12,2,45),(12,2,45),(-10,6,-40),(-10,-6,-40),(10,-6,-40),(10,6,-40))
COUGAR_EDGE = ((0,1),(1,7),(7,8),(8,2),(2,3),(3,6),(2,4),(4,6),(6,10),(10,9),(9,5),(5,0),(0,3),(1,4),(5,4),(1,2),(5,6),(12,13),(13,11),(11,14),(14,12),(15,16),(16,18),(18,17),(17,15))



DODO_VERTEX = ((0,150,196),(143,46,196),(88,-121,196),(-88,-121,196),(-143,46,196),(0,243,46),(231,75,46),(143,-196,46),(-143,-196,46),(-231,75,46),(143,196,-46),(231,-75,-46),(0,-243,-46),(-231,-75,-46),(-143,196,-46),(88,121,-196),(143,-46,-196),(0,-150,-196),(-143,-46,-196),(-88,121,-196),(-16,32,196),(-16,-32,196),(16,32,196),(16,-32,196))
DODO__EDGE = ((0,1),(1,2),(2,3),(3,4),(4,0),(5,10),(10,6),(6,11),(11,7),(7,12),(12,8),(8,13),(13,9),(9,14),(14,5),(15,16),(16,17),(17,18),(18,19),(19,15),(0,5),(1,6),(2,7),(3,8),(4,9),(10,15),(11,16),(12,17),(13,18),(14,19),(20,21),(21,23),(23,22),(22,20))











class Ship:
	# nextBookRef = int(150)
	# bookGroup = []

	def __init__(self, name,vertex_list,edges_list,faces_list,canisters_on_demise,targetable_area,max_edge_count,gun_vertex,explosion_count,number_of_vertices,number_of_edges,bounty,number_of_faces,visibility_distance,max_energy,max_speed,normals_scaled,laser_power,missiles):
		self.name = str(name)
		self.canisters_on_demise = int(canisters_on_demise)
		self.targetable_area = float(targetable_area)
		self.vertex_list = [list(x) for x in list(vertex_list)]
		self.edges_list = [list(x) for x in list(edges_list)]
		self.max_edge_count = int(max_edge_count)
		self.gun_vertex = int(gun_vertex)
		self.explosion_count = int(explosion_count)
		self.number_of_vertices = int(number_of_vertices)
		self.number_of_edges = int(number_of_edges)
		self.bounty = int(bounty)
		self.number_of_faces = int(number_of_faces)
		self.visibility_distance = int(visibility_distance)
		self.max_energy = int(max_energy)
		self.max_speed = int(max_speed)
		self.normals_scaled = int(normals_scaled)
		self.laser_power = int(laser_power)
		self.missiles = int(missiles)
		self.faces_list = [list(x) for x in list(faces_list)]











	def draw_ship(ship_name):
		glEnable(GL_DEPTH_TEST)
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


		glBegin(GL_TRIANGLE_STRIP)

		# glBegin(GL_TRIANGLE_FAN)

		for x in ship_name.edges_list:
			for vertex in x:
				glColor3fv ((0,0,0))
				glVertex3fv(ship_name.vertex_list[vertex])
		glEnd()


		glLineWidth(3)
		glEnable(GL_POLYGON_OFFSET_FILL)
		glPolygonOffset(2,2)


		glBegin(GL_LINES)
		for edge in ship_name.edges_list:
			for cubeVertex in edge:
				glColor3fv ((300,300,300))
				glVertex3fv(ship_name.vertex_list[cubeVertex])
		glEnd()









SIDEWINDER = Ship("SIDEWINDER",SIDEWINDER_INFO['Vertex list'], SIDEWINDER_INFO['Edge list'],SIDEWINDER_INFO['Face list'],SIDEWINDER_INFO['Max. canisters on demise'],SIDEWINDER_INFO['Targetable area'],SIDEWINDER_INFO['Max. edge count'],SIDEWINDER_INFO['Gun vertex'],SIDEWINDER_INFO['Explosion count'],SIDEWINDER_INFO['Number of vertices'],SIDEWINDER_INFO['Number of edges'],SIDEWINDER_INFO['Bounty'],SIDEWINDER_INFO['Number of faces'],SIDEWINDER_INFO['Visibility distance'],SIDEWINDER_INFO['Max. energy'],SIDEWINDER_INFO['Max. speed'],SIDEWINDER_INFO['Normals are scaled by'],SIDEWINDER_INFO['Laser power'],SIDEWINDER_INFO['Missiles'])
ASTEROID = Ship("ASTEROID",ASTEROID_INFO['Vertex list'], ASTEROID_INFO['Edge list'],ASTEROID_INFO['Face list'],ASTEROID_INFO['Max. canisters on demise'],ASTEROID_INFO['Targetable area'],ASTEROID_INFO['Max. edge count'],ASTEROID_INFO['Gun vertex'],ASTEROID_INFO['Explosion count'],ASTEROID_INFO['Number of vertices'],ASTEROID_INFO['Number of edges'],ASTEROID_INFO['Bounty'],ASTEROID_INFO['Number of faces'],ASTEROID_INFO['Visibility distance'],ASTEROID_INFO['Max. energy'],ASTEROID_INFO['Max. speed'],ASTEROID_INFO['Normals are scaled by'],ASTEROID_INFO['Laser power'],ASTEROID_INFO['Missiles'])
CANISTER = Ship("CANISTER",CANISTER_INFO['Vertex list'], CANISTER_INFO['Edge list'],CANISTER_INFO['Face list'],CANISTER_INFO['Max. canisters on demise'],CANISTER_INFO['Targetable area'],CANISTER_INFO['Max. edge count'],CANISTER_INFO['Gun vertex'],CANISTER_INFO['Explosion count'],CANISTER_INFO['Number of vertices'],CANISTER_INFO['Number of edges'],CANISTER_INFO['Bounty'],CANISTER_INFO['Number of faces'],CANISTER_INFO['Visibility distance'],CANISTER_INFO['Max. energy'],CANISTER_INFO['Max. speed'],CANISTER_INFO['Normals are scaled by'],CANISTER_INFO['Laser power'],CANISTER_INFO['Missiles'])
COBRA_MK_3 = Ship("COBRA_MK_3",COBRA_MK_3_INFO['Vertex list'], COBRA_MK_3_INFO['Edge list'],COBRA_MK_3_INFO['Face list'],COBRA_MK_3_INFO['Max. canisters on demise'],COBRA_MK_3_INFO['Targetable area'],COBRA_MK_3_INFO['Max. edge count'],COBRA_MK_3_INFO['Gun vertex'],COBRA_MK_3_INFO['Explosion count'],COBRA_MK_3_INFO['Number of vertices'],COBRA_MK_3_INFO['Number of edges'],COBRA_MK_3_INFO['Bounty'],COBRA_MK_3_INFO['Number of faces'],COBRA_MK_3_INFO['Visibility distance'],COBRA_MK_3_INFO['Max. energy'],COBRA_MK_3_INFO['Max. speed'],COBRA_MK_3_INFO['Normals are scaled by'],COBRA_MK_3_INFO['Laser power'],COBRA_MK_3_INFO['Missiles'])
CORIOLIS = Ship("CORIOLIS",CORIOLIS_INFO['Vertex list'], CORIOLIS_INFO['Edge list'],CORIOLIS_INFO['Face list'],CORIOLIS_INFO['Max. canisters on demise'],CORIOLIS_INFO['Targetable area'],CORIOLIS_INFO['Max. edge count'],CORIOLIS_INFO['Gun vertex'],CORIOLIS_INFO['Explosion count'],CORIOLIS_INFO['Number of vertices'],CORIOLIS_INFO['Number of edges'],CORIOLIS_INFO['Bounty'],CORIOLIS_INFO['Number of faces'],CORIOLIS_INFO['Visibility distance'],CORIOLIS_INFO['Max. energy'],CORIOLIS_INFO['Max. speed'],CORIOLIS_INFO['Normals are scaled by'],CORIOLIS_INFO['Laser power'],CORIOLIS_INFO['Missiles'])
ESCAPE_POD = Ship("ESCAPE_POD",ESCAPE_POD_INFO['Vertex list'], ESCAPE_POD_INFO['Edge list'],ESCAPE_POD_INFO['Face list'],ESCAPE_POD_INFO['Max. canisters on demise'],ESCAPE_POD_INFO['Targetable area'],ESCAPE_POD_INFO['Max. edge count'],ESCAPE_POD_INFO['Gun vertex'],ESCAPE_POD_INFO['Explosion count'],ESCAPE_POD_INFO['Number of vertices'],ESCAPE_POD_INFO['Number of edges'],ESCAPE_POD_INFO['Bounty'],ESCAPE_POD_INFO['Number of faces'],ESCAPE_POD_INFO['Visibility distance'],ESCAPE_POD_INFO['Max. energy'],ESCAPE_POD_INFO['Max. speed'],ESCAPE_POD_INFO['Normals are scaled by'],ESCAPE_POD_INFO['Laser power'],ESCAPE_POD_INFO['Missiles'])
MAMBA = Ship("MAMBA",MAMBA_INFO['Vertex list'], MAMBA_INFO['Edge list'],MAMBA_INFO['Face list'],MAMBA_INFO['Max. canisters on demise'],MAMBA_INFO['Targetable area'],MAMBA_INFO['Max. edge count'],MAMBA_INFO['Gun vertex'],MAMBA_INFO['Explosion count'],ESCAPE_POD_INFO['Number of vertices'],MAMBA_INFO['Number of edges'],MAMBA_INFO['Bounty'],MAMBA_INFO['Number of faces'],MAMBA_INFO['Visibility distance'],MAMBA_INFO['Max. energy'],MAMBA_INFO['Max. speed'],MAMBA_INFO['Normals are scaled by'],MAMBA_INFO['Laser power'],MAMBA_INFO['Missiles'])






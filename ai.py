import random
import time
import multiprocessing
import Queue
class ai_agent():
	mapinfo = []
	maze = []
	def __init__(self):
		self.mapinfo = []
		self.maze = [	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		]
	# rect:					[left, top, width, height]
	# rect_type:			0:empty 1:brick 2:steel 3:water 4:grass 5:froze
	# castle_rect:			[12*16, 24*16, 32, 32]
	# mapinfo[0]: 			bullets [rect, direction, speed]]
	# mapinfo[1]: 			enemies [rect, direction, speed, type]]
	# enemy_type:			0:TYPE_BASIC 1:TYPE_FAST 2:TYPE_POWER 3:TYPE_ARMOR
	# mapinfo[2]: 			tile 	[rect, type] (empty don't be stored to mapinfo[2])
	# mapinfo[3]: 			player 	[rect, direction, speed, Is_shielded]]
	# shoot:				0:none 1:shoot
	# move_dir:				0:Up 1:Right 2:Down 3:Left 4:None
	# keep_action:			0:The tank work only when you Update_Strategy. 	1:the tank keep do previous action until new Update_Strategy.

	# def Get_mapInfo:		fetch the map infomation
	# def Update_Strategy	Update your strategy


			
			
	def operations (self,p_mapinfo,c_control):	
		self.DrawMaze()
		#print self.maze
		#print ((self.mapinfo[3][0][0][0]//16),(self.mapinfo[3][0][0][1]//16))
		# push [WantTo, GoRound]
		GetAwayStack = []
		WantTo = 4
		GoRound = 4
		#preD = 1
		preL = -1
		preT = -1
	
		while True:
		#-----your ai operation,This code is a random strategy,please design your ai !!-----------------------			
			self.Get_mapInfo(p_mapinfo)
			## Initialization ##
			shoot = 0
			shootDist = 100
			shootRange = (2*3)*16
			move_dir = 4
			keep_action = 0
			myL = self.mapinfo[3][0][0][0]
			myT = self.mapinfo[3][0][0][1]
			myW = self.mapinfo[3][0][0][2]
			myH = self.mapinfo[3][0][0][3]
			flagL = (12-1)*16;
			flagT = (24-1)*16;
			flagW = 32+32;
			flagH = 32+32;
			NoTop = False
			NoDown = False
			NoLeft = False
			NoRight = False
			BoundTop = False
			BoundDown = False
			BoundLeft = False
			BoundRight = False
			NoTop_tile = self.mapinfo[2][0]
			NoTop_tile[1] = 6
			NoDown_tile = self.mapinfo[2][0]
			NoDown_tile[1] = 6
			NoLeft_tile = self.mapinfo[2][0]
			NoLeft_tile[1] = 6
			NoRight_tile = self.mapinfo[2][0]
			NoRight_tile[1] = 6
			min_dist = -1
			min_enemy = self.mapinfo[3][0]
			danger_dist = -1
			danger_flag = False
			danger_enemy = self.mapinfo[3][0]
			RunFlag = False
			## Check if path for 4 direction ##
			if (myL < 3) or ((myL in range(flagL+flagW-1, flagL+flagW+3+3)) and (myT in range(flagT-myH, flagT+flagH))):
				NoLeft = True
				#NoLeft_tile[1] = 2
				if (myL < 3):
					BoundLeft = True
			elif ((myL+myW) > (26*16-3)) or (((myL+myW) in range(flagL-3-3, flagL+1)) and (myT in range(flagT-myH, flagT+flagH))):
				NoRight = True
				#NoRight_tile[1] = 2
				if ((myL+myW) > (26*16-3)):
					BoundRight = True
			if (myT < 3):
				NoTop = True
				#NoTop_tile[1] = 2
				BoundTop = True
			elif ((myT+myH) > (26*16-3)) or (((myT+myH) in range(flagT-3-3, flagT+1)) and (myL in range(flagL-myW, flagL+flagW))):
				NoDown = True
				#NoDown_tile[1] = 2
				#print "No Down!!"
				if ((myT+myH) > (26*16-3)):
					BoundDown = True
			# tiles
			for tile in self.mapinfo[2]:
				if ((tile[0][0] in range(myL, myL+myW)) or ((tile[0][0]+tile[0][2]) in range(myL, myL+myW))) and (tile[1] != 4):
					if ((tile[0][1]+tile[0][3]) in range (myT-3-3, myT+1)) and (not NoTop):
						##print "No way to Top"
						NoTop = True
						NoTop_tile = tile
					elif (tile[0][1] in range (myT+myH-1, myT+myH+3+3)) and (not NoDown):
						##print "No way to Down"
						NoDown = True
						NoDown_tile = tile
				if ((tile[0][1] in range(myT, myT+myH)) or ((tile[0][1]+tile[0][3]) in range(myT, myT+myH))) and (tile[1] != 4):
					if ((tile[0][0]+tile[0][2]) in range(myL-3-3, myL+1)) and (not NoLeft):
						##print "No way to Left"
						NoLeft = True
						NoLeft_tile = tile
					elif (tile[0][0] in range(myL+myW-1, myL+myW+3+3)) and (not NoRight):
						##print "No way to Right"
						NoRight = True
						NoRight_tile = tile
			# enemies
			for tile in self.mapinfo[1]:
				dist = (tile[0][0]-myL)*(tile[0][0]-myL) + (tile[0][1]-myT)*(tile[0][1]-myT)
				if (min_dist == -1) or (dist < min_dist):
					min_dist = dist
					min_enemy = tile
				#if (tile[0][1] > (13*16)):
				if (tile[0][1] > myT) or (tile[0][1] > (13*16)):
					if not danger_flag:
						danger_dist = tile[0][1]
						danger_enemy = tile
						danger_flag = True
					elif (tile[0][1] > danger_dist):
						danger_dist = tile[0][1]
						danger_enemy = tile
						
			## Chase nearest/dangerest enemy ##
			if danger_flag:
				enemyL = danger_enemy[0][0]
				enemyT = danger_enemy[0][1]
				enemyW = danger_enemy[0][2]
				enemyH = danger_enemy[0][3]
				enemyD = danger_enemy[1]
			else:
				enemyL = min_enemy[0][0]
				enemyT = min_enemy[0][1]
				enemyW = min_enemy[0][2]
				enemyH = min_enemy[0][3]
				enemyD = min_enemy[1]
			if (enemyT > myT) & (not NoDown) & (not (((myT + flagH) > (enemyT-12)) and (((enemyD == 1) and (enemyL < myL)) or ((enemyD == 3) and (enemyL > myL))))):
				#print "Trace to Down"
				move_dir = 2;
				shoot = 0;
			elif (enemyL < myL) & (not NoLeft) & (not ((myL < (enemyL + enemyW+12)) and (((enemyD == 0) and (enemyT > myT)) or ((enemyD == 2) and (enemyT < myT))))):
				#print "Trace to Left";
				move_dir = 3;
				shoot = 0;
			elif (enemyL > myL) & (not NoRight) & (not (((myL + myW) > (enemyL-12)) and (((enemyD == 0) and (enemyT > myT)) or ((enemyD == 2) and (enemyT < myT))))):
				#print "Trace to Right";
				move_dir = 1;
				shoot = 0;
			elif (enemyT < myT) & (not NoTop) & (not ((myT < (enemyT + enemyH+12)) and (((enemyD == 1) and (enemyL < myL)) or ((enemyD == 3) and (enemyL > myL))))):
				#print "Trace to Top";
				move_dir = 0;
				shoot = 0;
			elif (enemyL < myL) & (NoLeft_tile[1] == 1):
				if ((myT+10+6) < NoLeft_tile[0][1]):
					#print "Shoot Left Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoLeft_tile[0][1]+NoLeft_tile[0][3]) <= (myT+10+1)):
					#print "Shoot Left Wall (U)"
					move_dir = 0
					shoot = 0
				else:
					move_dir = 3;
					#if (myT > (flagT-(flagH/2))) and (flagL < myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = myL-(NoLeft_tile[0][0]+NoLeft_tile[0][2])
					#print "Shoot L wall"
			elif (myL < enemyL) & (NoRight_tile[1] == 1):
				if ((myT+10+6) < NoRight_tile[0][1]):
					#print "Shoot Right Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoRight_tile[0][1]+NoRight_tile[0][3]) <= (myT+10+1)):
					#print "Shoot Right Wall (U)"
					move_dir = 0
					shoot = 0
				else:
					move_dir = 1;
					#if (myT > (flagT-(flagH/2))) and (flagL > myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoRight_tile[0][0]-(myL+myW)
					#print "Shoot R wall"
			elif (enemyT < myT) & (NoTop_tile[1] == 1):
				if ((myL+10+6)< NoTop_tile[0][0]):
					#print "Shoot Top Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoTop_tile[0][0]+NoTop_tile[0][2]) <= (myL+10+1)):
					#print "Shoot Top Wall (L)"
					move_dir = 3
					shoot = 0
				else:
					move_dir = 0;
					shoot = 1;
					shootDist = myT-(NoTop_tile[0][1]+NoTop_tile[0][3])
					#print "Shoot T wall"
					#self.Update_Strategy(c_control,0,move_dir,0);
			elif (myT < enemyT) & (NoDown_tile[1] == 1):
				if ((myL+10+6)< NoDown_tile[0][0]):
					#print "Shoot Down Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoDown_tile[0][0]+NoDown_tile[0][2]) <= (myL+10+1)):
					#print "Shoot Down Wall (L)"
					move_dir = 3
					shoot = 0
				else:
					move_dir = 2;
					#if (myL in range(flagL-myW, flagL+flagW)) and (myT < (22*16)):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoDown_tile[0][1]-(myT+myH)
					#print "Shoot D wall"
			elif (WantTo == 4):
				#if (enemyT < myT) and (enemyL < myL) and NoTop and NoLeft and (not BoundTop) and (not BoundLeft):
				if (enemyT < myT) and (enemyL < myL) and NoTop and NoLeft:
					#if (not NoRight) and (self.mapinfo[3][0][1] != 1):
					#if not NoRight:
					#if not NoRight and (preD == 0):
					nextD = self.PathDecision(3,0)	#return 1 or 2
					if (nextD[0] == 1):
						#print "Stuck at LT (to R)"
						GoRound = 1
						WantTo = 0
						#preD = 1
					else:
						#print "Stuck at LT (to D)"
						GoRound = 2
						WantTo = 3
						#preD = 0
				#elif (enemyT < myT) and (myL < enemyL) and NoTop and NoRight and (not BoundTop) and (not BoundRight):
				elif (enemyT < myT) and (myL < enemyL) and NoTop and NoRight:
					#if (not NoLeft) and (self.mapinfo[3][0][1] != 3):
					#if not NoLeft:
					#if not NoLeft and (preD == 0):
					nextD = self.PathDecision(1,0)	#return 3 or 2
					if (nextD[0] == 3):
						#print "Stuck at RT (to L)"
						GoRound = 3
						WantTo = 0
						#preD = 1
					else:
						#print "Stuck at RT (to D)"
						GoRound = 2
						WantTo = 1
						#preD = 0
				#elif (myT < enemyT) and (enemyL < myL) and NoDown and NoLeft and (not BoundDown) and (not BoundLeft):
				elif (myT < enemyT) and (enemyL < myL) and NoDown and NoLeft:
					#if (not NoRight) and (self.mapinfo[3][0][1] != 1):
					#if not NoRight:
					#if not NoRight and (preD == 0):
					nextD = self.PathDecision(3,2)	#return 1 or 0
					if (nextD[0] == 1):
						#print "Stuck at LD (to R)"
						GoRound = 1
						WantTo = 2
						#preD = 1
					else:
						#print "Stuck at LD (to T)"
						GoRound = 0
						WantTo = 3
						#preD = 0
				#elif (myT < enemyT) and (myL < enemyL) and NoDown and NoRight and (not BoundDown) and (not BoundRight):
				elif (myT < enemyT) and (myL < enemyL) and NoDown and NoRight:
					#if (not NoLeft) and (self.mapinfo[3][0][1] != 3):
					#if not NoLeft:
					#if not NoLeft and (preD == 0):
					nextD = self.PathDecision(1,2)	#return 3 or 0
					if (nextD[0] == 3):
						#print "Stuck at RD (to L)"
						GoRound = 3
						WantTo = 2
						#preD = 1
					else:
						#print "Stuck at RD (to T)"
						GoRound = 0
						WantTo = 1
						#preD = 0
			#	if NoTop:
			#		#print ("Top:",NoTop_tile[1])
			#	if NoRight:
			#		#print ("Right:",NoRight_tile[1])
			#	if NoDown:
			#		#print ("Down:",NoDown_tile[1])
			#	if NoLeft:
			#		#print ("Left:",NoLeft_tile[1])
				
			## Check around ##
			# Enemies #
			for enemy in self.mapinfo[1]:
				enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
				enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
				if (enemy_bulletL in range(myL+10-6+1, myL+10+6-1)):
					if (enemy[0][1] < myT):
					#	#print "Find enemy on the Top"
						move_dir = 0
						shoot = 1
						shootDist = myT-(enemy[0][1]+enemy[0][3])
						if (enemy[3] == 1) or (enemy[1] == 2):
							shootDist = shootDist / 2
					elif (myT < enemy[0][1]):
						#print "Find enemy on the Down"
						move_dir = 2
						shoot = 1
						shootDist = enemy[0][1]-(myT+myH)
						if (enemy[3] == 1) or (enemy[1] == 0):
							shootDist = shootDist / 2
						
				elif (enemy_bulletL in range(myL-6-1, myL+10-6)) and (((enemy[0][1] < myT) and (enemy[1] == 2)) or ((myT < enemy[0][1]) and (enemy[1] == 0))):
					if not NoRight:
						#print "Erun R"
						move_dir = 1
						shoot = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
						#continue
						RunFlag = True
					else:
						#print "Eclose L"
						move_dir = 3
						shoot = 0
				elif (enemy_bulletL in range(myL+10+6, myL+myW+1)) and (((enemy[0][1] < myT) and (enemy[1] == 2)) or ((myT < enemy[0][1]) and (enemy[1] == 0))):
					if not NoLeft:
						#print "Erun L"
						move_dir = 3
						shoot = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
						#continue
						RunFlag = True
					else:
						#print "Eclose R"
						move_dir = 1
						shoot = 0
						
				if (enemy_bulletT in range(myT+10-6+1, myT+10+6-1)):
					if (enemy[0][0] < myL):
						#print "Find enemy on the Left"
						move_dir = 3
						shoot = 1
						shootDist = myL-(enemy[0][0]+enemy[0][2])
						if (enemy[3] == 1) or (enemy[1] == 1):
							shootDist = shootDist / 2
					elif (myL < enemy[0][0]):
						#print "Find enemy on the Right"
						move_dir = 1
						shoot = 1
						shootDist = enemy[0][0]-(myL+myW)
						if (enemy[3] == 1) or (enemy[1] == 3):
							shootDist = shootDist / 2
				elif (enemy_bulletT in range(myT-6-1, myL+10-6)) and (((enemy[0][0] < myL) and (enemy[1] == 1)) or ((myL < enemy[0][0]) and (enemy[1] == 3))):
					if not NoDown:
						#print "Erun D"
						move_dir = 2
						shoot = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
						#continue
						RunFlag = True
					else:
						#print "Eclose T"
						move_dir = 0
						shoot = 0
				elif (enemy_bulletT in range(myT+10+6, myT+myH+1)) and (((enemy[0][0] < myL) and (enemy[1] == 1)) or ((myL < enemy[0][0]) and (enemy[1] == 3))):
					if not NoTop:
						#print "Erun T"
						move_dir = 0
						shoot = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
						#continue
						RunFlag = True
					else:
						#print "Eclose D"
						move_dir = 2
						shoot = 0
						
			# Bullets #
			for bullet in self.mapinfo[0]:
				if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+myW+1)) and (bullet[1] == 0) and ((myT+myH) < (bullet[0][1]+bullet[0][3])):
					#print "Bullet comes Up"
					if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+10-bullet[0][2])):
						#if not NoLeft:
						if (not NoRight) or (NoRight_tile[1] == 1):
							#print "run R"
							move_dir = 1
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close L"
							move_dir = 3
							shoot = 0
					elif (bullet[0][0] in range(myL+10+6, myL+myW+1)):
						#if not NoRight:
						if (not NoLeft) or (NoLeft_tile[1] == 1):
							#print "run L"
							move_dir = 3
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close R"
							move_dir = 1
							shoot = 0
					else:
						move_dir = 2
						shoot = 1
						#shootDist = bullet[0][1]-(myT+myH)
						shootDist = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
				elif (bullet[0][0] in range(myL-bullet[0][2]-1, myL+myW+1)) and (bullet[1] == 2) and (bullet[0][1] < myT):
					#print "Bullet comes Down"
					if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+10-bullet[0][2])):
						#if not NoLeft:
						if (not NoRight) or (NoRight_tile[1] == 1):
							#print "run R"
							move_dir = 1
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close L"
							move_dir = 3
							shoot = 0
					elif (bullet[0][0] in range(myL+10+6, myL+myW+1)):
						#if not NoRight:
						if (not NoLeft) or (NoLeft_tile[1] == 1):
							#print "run L"
							move_dir = 3
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close R"
							move_dir = 1
							shoot = 0
					else:
						move_dir = 0
						shoot = 1
						#shootDist = myL-(bullet[0][0]+bullet[0][2])
						shootDist = 0
				elif (bullet[0][1] in range(myT-bullet[0][3]-1, myT+myH+1)) and (bullet[1] == 3) and ((myL+myW) < (bullet[0][0]+bullet[0][2])):
					#print "Bullet comes Left"
					if (bullet[0][1] in range(myT-bullet[0][3]-1, myT+10-bullet[0][3])):
						if not NoDown:
							#print "run D"
							move_dir = 2
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close T"
							move_dir = 0
							shoot = 0
					elif (bullet[0][1] in range(myT+10+6, myT+myH+1)):
						if not NoTop:
							#print "run T"
							move_dir = 0
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close D"
							move_dir = 2
							shoot = 0
					else:
						move_dir = 1
						shoot = 1
						#shootDist = bullet[0][0]-(myL+myW)
						if (myT in range(flagT-myH, flagT+flagH)) and (myL < flagL) and (flagL < bullet[0][0]):
							shootDist = 100
						else:
							shootDist = 0
				elif (bullet[0][1] in range(myT-bullet[0][3]-1, myT+myH+1)) and (bullet[1] == 1) and (bullet[0][0] < myL):
					#print "Bullet comes Right"
					if (bullet[0][1] in range(myT-bullet[0][3]-1, myT+10-bullet[0][3])):
						if not NoDown:
							#print "run D"
							move_dir = 2
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close T"
							move_dir = 0
							shoot = 0
					elif (bullet[0][1] in range(myT+10+6, myT+myH+1)):
						if not NoTop:
							#print "run T"
							move_dir = 0
							shoot = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
							#continue
							RunFlag = True
						else:
							#print "close D"
							move_dir = 2
							shoot = 0
					else:
						move_dir = 3
						shoot = 1
						#shootDist = bullet[0][0]-(myL+myW)
						if (myT in range(flagT-myH, flagT+flagH)) and (flagL < myL) and (bullet[0][0] < flagL):
							shootDist = 100
						else:
							shootDist = 0
			## Get out of the deadlock ##
			if (WantTo != 4) and (not RunFlag):
				if (WantTo == 0) and ((not NoTop) or (NoTop_tile[1] == 1)):
					#print "Now go Top"
					move_dir = 0
					if (preT == -1):
						preT = myT
					elif (myT < (preT-6)) or (myT <= 3):
						preT = -1
						if len(GetAwayStack) == 0:
							WantTo = 4
							GoRound = 4
						else:
							tmp = GetAwayStack.pop()
							WantTo = tmp[0]
							GoRound = tmp[1]
				elif (WantTo == 1) and ((not NoRight) or (NoRight_tile[1] == 1)):
					#print "Now go Right"
					move_dir = 1
					if (preL == -1):
						preL = myL
					elif ((preL+6) < myL) or ((myL+myW) >= (26*16-3)):
						preL = -1
						if len(GetAwayStack) == 0:
							WantTo = 4
							GoRound = 4
						else:
							tmp = GetAwayStack.pop()
							WantTo = tmp[0]
							GoRound = tmp[1]
				elif (WantTo == 2) and ((not NoDown) or (NoDown_tile[1] == 1)):
					#print "Now go Down"
					move_dir = 2
					if (preT == -1):
						preT = myT
					elif ((preT+6) < myT) or ((myT+myH) >= (26*16-3)):
						preT = -1
						if len(GetAwayStack) == 0:
							WantTo = 4
							GoRound = 4
						else:
							tmp = GetAwayStack.pop()
							WantTo = tmp[0]
							GoRound = tmp[1]
				elif (WantTo == 3) and ((not NoLeft) or (NoLeft_tile[1] == 1)):
					#print "Now go Left"
					move_dir = 3
					if (preL == -1):
						preL = myL
					elif (myL < (preL-6)) or (myL <= 3):
						preL = -1
						if len(GetAwayStack) == 0:
							WantTo = 4
							GoRound = 4
						else:
							tmp = GetAwayStack.pop()
							WantTo = tmp[0]
							GoRound = tmp[1]
				#elif ((GoRound == 0) and NoTop and (not BoundTop) and ((NoTop_tile[1] != 1) and (NoTop_tile[1] != 4))) or ((GoRound == 2) and NoDown and (not BoundDown)) and ((NoDown_tile[1] != 1) and (NoDown_tile[1] != 4)):
				elif ((GoRound == 0) and NoTop and ((NoTop_tile[1] != 1) and (NoTop_tile[1] != 4))) or ((GoRound == 2) and NoDown and ((NoDown_tile[1] != 1) and (NoDown_tile[1] != 4))):
					preL = -1
					preT = -1
					if (WantTo == 1):
						#print "Change Go Left"
						if (not NoLeft):
							GetAwayStack.append([WantTo,GoRound])
							WantTo = GoRound
							GoRound = 3
						elif (GoRound == 0):
							GoRound = 2
							if NoTop and ((NoTop_tile[1] != 1) and (NoTop_tile[1] != 4)):
								WantTo = 2
							else:
								WantTo = 0
						else:
							GoRound = 0
							if NoTop and ((NoTop_tile[1] != 1) and (NoTop_tile[1] != 4)):
								WantTo = 2
							else:
								WantTo = 0
					elif (WantTo == 3):
						#print "Change Go Right"
						if (not NoRight):
							GetAwayStack.append([WantTo,GoRound])
							WantTo = GoRound
							GoRound = 1
						elif (GoRound == 0):
							GoRound = 2
							if NoTop and ((NoTop_tile[1] != 1) and (NoTop_tile[1] != 4)):
								WantTo = 2
							else:
								WantTo = 0
						else:
							GoRound = 0
							if NoTop and ((NoTop_tile[1] != 1) and (NoTop_tile[1] != 4)):
								WantTo = 2
							else:
								WantTo = 0
				#elif ((GoRound == 1) and NoRight and (not BoundRight) and ((NoRight_tile[1] != 1) and (NoRight_tile[1] != 4))) or ((GoRound == 3) and NoLeft and (not BoundLeft) and ((NoLeft_tile[1] != 1) and (NoLeft_tile[1] != 4))):
				elif ((GoRound == 1) and NoRight and ((NoRight_tile[1] != 1) and (NoRight_tile[1] != 4))) or ((GoRound == 3) and NoLeft and ((NoLeft_tile[1] != 1) and (NoLeft_tile[1] != 4))):
					preL = -1
					preT = -1
					if (WantTo == 0):
						#print "Change Go Down"
						if (not NoDown):
							GetAwayStack.append([WantTo,GoRound])
							WantTo = GoRound
							GoRound = 2
							#preD = 0
						elif (GoRound == 1):
							GoRound = 3
							if NoRight and ((NoRight_tile[1] != 1) and (NoRight_tile[1] != 4)):
								WantTo = 3
							else:
								WantTo = 1
						else:
							GoRound = 1
							if NoRight and ((NoRight_tile[1] != 1) and (NoRight_tile[1] != 4)):
								WantTo = 3
							else:
								WantTo = 1
					elif (WantTo == 2):
						#print "Change Go Top"
						if (not NoTop):
							GetAwayStack.append([WantTo,GoRound])
							WantTo = GoRound
							GoRound = 0
						elif (GoRound == 1):
							GoRound = 3
							if NoRight and ((NoRight_tile[1] != 1) and (NoRight_tile[1] != 4)):
								WantTo = 3
							else:
								WantTo = 1
						else:
							GoRound = 1
							if NoRight and ((NoRight_tile[1] != 1) and (NoRight_tile[1] != 4)):
								WantTo = 3
							else:
								WantTo = 1
				elif ((GoRound == 0) and BoundTop) or ((GoRound == 1) and BoundRight) or ((GoRound == 2) and BoundDown) or ((GoRound == 3) and BoundLeft):
					#print "Boundary"
					preL = -1
					preT = -1
					if len(GetAwayStack) != 0:
						tmp = GetAwayStack.pop()
						WantTo = tmp[0]
						GoRound = tmp[1]
					else:
						WantTo = 4
						GoRound = 4
				else:
					move_dir = GoRound
					shoot = 0
			if len(GetAwayStack) > 10:
				while len(GetAwayStack) != 0:
					GetAwayStack.pop()
			## Check block or not ##
			#if (move_dir == 0) and NoTop and (shoot == 0):
			if (move_dir == 0) and NoTop:
				#print ("No way top", NoTop_tile)
				if (NoTop_tile[1] != 1) and (NoTop_tile[1] != 4):
					nextD1 = self.PathDecision(1,0)
					nextD2 = self.PathDecision(3,0)
					WantTo = 0
					if (nextD1[0] == 2) and (nextD2[0] == 2):
						GoRound = 1
						move_dir = 1
						shoot = 0
					elif nextD1[0] == 2:
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
					elif nextD2[0] == 2:
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					elif nextD1[1] < nextD2[1]:
						#print ("Go ", nextD1, nextD2)
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					else:
						#print ("Go ", nextD2, nextD1)
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
				if ((myL+10+6)< NoTop_tile[0][0]) and (NoTop_tile[1] == 1):
					#print "Shoot Top Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoTop_tile[0][0]+NoTop_tile[0][2]) <= (myL+10+1)) and (NoTop_tile[1] == 1):
					#print "Shoot Top Wall (L)"
					move_dir = 3
					shoot = 0
				elif (NoTop_tile[1] == 1):
					move_dir = 0;
					shoot = 1;
					shootDist = myT-(NoTop_tile[0][1]+NoTop_tile[0][3])
					#print "Shoot T wall"
					#self.Update_Strategy(c_control,0,move_dir,0);
				#else:
					#print "Unknown block!?"
			#elif (move_dir == 1) and NoRight and (shoot == 0):
			elif (move_dir == 1) and NoRight:
				#print ("No way right", NoRight_tile)
				if (NoRight_tile[1] != 1) and (NoRight_tile[1] != 4):
					nextD1 = self.PathDecision(1,0)
					nextD2 = self.PathDecision(1,2)
					WantTo = 1
					if (nextD1[0] == 3) and (nextD2[0] == 3):
						GoRound = 0
						move_dir = 0
						shoot = 0
					elif nextD1[0] == 3:
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
					elif nextD2[0] == 3:
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					elif nextD1[1] < nextD2[1]:
						#print ("Go ", nextD1[0])
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					else:
						#print ("Go ", nextD2[0])
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
				if ((myT+10+6) < NoRight_tile[0][1]) and (NoRight_tile[1] == 1):
					#print "Shoot Right Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoRight_tile[0][1]+NoRight_tile[0][3]) <= (myT+10+1)) and (NoRight_tile[1] == 1):
					#print "Shoot Right Wall (U)"
					move_dir = 0
					shoot = 0
				elif (NoRight_tile[1] == 1):
					move_dir = 1;
					#if (myT > (flagT-(flagH/2))) and (flagL > myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoRight_tile[0][0]-(myL+myW)
					#print "Shoot R wall"
				#else:
					#print "Unknown block!?"
			#elif (move_dir == 2) and NoDown and (shoot == 0):
			elif (move_dir == 2) and NoDown:
				#print ("No way down", NoDown_tile)
				if (NoDown_tile[1] != 1) and (NoDown_tile[1] != 4):
					nextD1 = self.PathDecision(1,2)
					nextD2 = self.PathDecision(3,2)
					WantTo = 2
					if (nextD1[0] == 0) and (nextD2[0] == 0):
						GoRound = 1
						move_dir = 1
						shoot = 0
					elif nextD1[0] == 0:
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
					elif nextD2[0] == 0:
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					elif nextD1[1] < nextD2[1]:
						#print ("Go ", nextD1[0])
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					else:
						#print ("Go ", nextD2[0])
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
				if ((myL+10+6)< NoDown_tile[0][0]) and (NoDown_tile[1] == 1):
					#print "Shoot Down Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoDown_tile[0][0]+NoDown_tile[0][2]) <= (myL+10+1)) and (NoDown_tile[1] == 1):
					#print "Shoot Down Wall (L)"
					move_dir = 3
					shoot = 0
				elif (NoDown_tile[1] == 1):
					move_dir = 2;
					#if (myL in range(flagL-myW, flagL+flagW)) and (myT < (22*16)):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoDown_tile[0][1]-(myT+myH)
					#print "Shoot D wall"
				#else:
					#print "Unknown block!?"
			#elif (move_dir == 3) and NoLeft and (shoot == 0):
			elif (move_dir == 3) and NoLeft:
				#print ("No way left", NoLeft_tile)
				if (NoLeft_tile[1] != 1) and (NoLeft_tile[1] != 4):
					nextD1 = self.PathDecision(3,0)
					nextD2 = self.PathDecision(3,2)
					WantTo = 3
					if (nextD1[0] == 1) and (nextD2[0] == 1):
						GoRound = 0
						move_dir = 0
						shoot = 0
					elif nextD1[0] == 3:
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
					elif nextD2[0] == 3:
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					elif nextD1[1] < nextD2[1]:
						#print ("Go ", nextD1[0])
						GoRound = nextD1[0]
						move_dir = nextD1[0]
						shoot = 0
					else:
						#print ("Go ", nextD2[0])
						GoRound = nextD2[0]
						move_dir = nextD2[0]
						shoot = 0
				if ((myT+10+6) < NoLeft_tile[0][1]) and (NoLeft_tile[1] == 1):
					#print "Shoot Left Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoLeft_tile[0][1]+NoLeft_tile[0][3]) <= (myT+10+1)) and (NoLeft_tile[1] == 1):
					#print "Shoot Left Wall (U)"
					move_dir = 0
					shoot = 0
				elif (NoLeft_tile[1] == 1):
					move_dir = 3;
					#if (myT > (flagT-(flagH/2))) and (flagL < myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = myL-(NoLeft_tile[0][0]+NoLeft_tile[0][2])
					#print "Shoot L wall"
				#else:
					#print "Unknown block!?"
			## Final Check: Move_dir ##
			#if (move_dir == 0) and (not RunFlag):
			if move_dir == 0:
				# check if any other enemies/bullets in the front row
				for bullet in self.mapinfo[0]:
					#if (bullet[0][1] in range(myT-2*bullet[0][3], myT-bullet[0][3]-1)) and ((bullet[1]==1) or (bullet[1]==3)):
					if (bullet[0][1] in range(myT-2*bullet[0][3], myT-bullet[0][3])) and ((bullet[1]==1) or (bullet[1]==3)):
						if (bullet[0][0] < myL) and (bullet[1] == 1):
							#print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][0] > myL) and (bullet[1] == 3):
							#print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
					enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
					#if ((enemy[0][1] + enemy[0][3]) in range(myT-6, myT+6)) and ((enemy[1]==1) or (enemy[1]==3)):
					if ((enemy_bulletT + 8) in range(myT-6, myT+6)) and ((enemy[1]==1) or (enemy[1]==3)):
						#if (enemy[0][0] < myL) and (enemy[1] == 1):
						if (enemy_bulletL < myL) and (enemy[1] == 1):
							#print "Take care! enemy!"
							move_dir = 4
						elif (enemy_bulletL > myL) and (enemy[1] == 3):
							#print "Take care! enemy!"
							move_dir = 4
			#elif (move_dir == 2) and (not RunFlag):
			elif move_dir == 2:
				# check if any other enemies/bullets in the front row
				for bullet in self.mapinfo[0]:
					if (bullet[0][1] in range(myT+myH, myT+myH+bullet[0][3])) and ((bullet[1]==1) or (bullet[1]==3)):
						if (bullet[0][0] < myL) and (bullet[1] == 1):
							#print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][0] > myL) and (bullet[1] == 3):
							#print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
					enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
					if (enemy_bulletT in range(myT+myH-6, myT+myH+6)) and ((enemy[1]==1) or (enemy[1]==3)):
						if (enemy_bulletL < myL) and (enemy[1] == 1):
							#print "Take care! enemy!"
							move_dir = 4
						elif (enemy_bulletL > myL) and (enemy[1] == 3):
							#print "Take care! enemy!"
							move_dir = 4
			#elif (move_dir == 1) and (not RunFlag):
			elif move_dir == 1:
				# check if any other enemies/bullets in the front column
				for bullet in self.mapinfo[0]:
					if (bullet[0][0] in range(myL+myW, myL+myW+bullet[0][2])) and ((bullet[1]==0) or (bullet[1]==2)):
						if (bullet[0][1] < myT) and (bullet[1] == 2):
							#print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][1] > myT) and (bullet[1] == 0):
							#print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
					enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
					if (enemy_bulletL in range(myL+myW-6, myL+myW+6)) and ((enemy[1]==0) or (enemy[1]==2)):
						if (enemy_bulletT < myT) and (enemy[1] == 2):
							#print "Take care! enemy!"
							move_dir = 4
						elif (enemy_bulletT > myT) and (enemy[1] == 0):
							#print "Take care! enemy!"
							move_dir = 4
			#elif (move_dir == 3) and (not RunFlag):
			elif move_dir == 3:
				# check if any other enemies/bullets in the front column
				for bullet in self.mapinfo[0]:
					if (bullet[0][0] in range(myL-2*bullet[0][2], myL-bullet[0][2])) and ((bullet[1]==0) or (bullet[1]==2)):
						if (bullet[0][1] < myT) and (bullet[1] == 2):
							#print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][1] > myT) and (bullet[1] == 0):
							#print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
					enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
					if ((enemy_bulletL + 8) in range(myL-6, myL+6)) and ((enemy[1]==0) or (enemy[1]==2)):
						if (enemy_bulletT < myT) and (enemy[1] == 2):
							#print "Take care! enemy!"
							move_dir = 4
						elif (enemy_bulletT > myT) and (enemy[1] == 0):
							#print "Take care! enemy!"
							move_dir = 4
			## Detect enemy around ##
			if (shoot == 0) and (not RunFlag):
				for enemy in self.mapinfo[1]:
					if enemy[0][0] in range(myL+10-enemy[0][2]+1, myL+10+6-1):
						if (enemy[0][1]+enemy[0][3]) in range(myT+1, myT-3):
							move_dir = 0
							shoot = 1
							shootDist = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
						elif enemy[0][1] in range(myT+myH-1, myT+myH+3):
							move_dir = 2
							shoot = 1
							shootDist = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
					elif enemy[0][1] in range(myT+10-enemy[0][3]+1, myT+10+6-1):
						if (enemy[0][0]+enemy[0][2]) in range(myL+1, myL-3):
							move_dir = 3
							shoot = 1
							shootDist = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
						elif enemy[0][0] in range(myL+myW-1, myL+myW+3):
							move_dir = 1
							shoot = 1
							shootDist = 0
							#self.Update_Strategy(c_control,0,move_dir,0)
			## Final Check: Shoot ##
			if (shoot == 1):
				if (shootDist < 1):
					shoot = 1
					self.Update_Strategy(c_control,0,move_dir,0)
				elif (shootDist > shootRange):
					shoot = 0
				elif (myT in range(flagT-myH, flagT+flagH)):
					if (myL < flagL) and ((move_dir == 1) or (self.mapinfo[3][0][1] == 1)):
						shoot = 0
					elif (flagL < myL) and ((move_dir == 3) or (self.mapinfo[3][0][1] == 3)):
						shoot = 0
				elif (myL in range(flagL-myW, flagL+flagW)) and (shootDist > shootRange):
					if (myT < flagT) and ((move_dir == 2) or (self.mapinfo[3][0][1] == 2)):
						shoot = 0
				else:
					self.Update_Strategy(c_control,0,move_dir,0)
			#-----------
			##print (move_dir, shoot)
			self.Update_Strategy(c_control,shoot,move_dir,keep_action)
		#------------------------------------------------------------------------------------------------------

	def Get_mapInfo(self,p_mapinfo):
		if p_mapinfo.empty()!=True:
			try:
				self.mapinfo = p_mapinfo.get(False)
			except Queue.Empty:
				skip_this=True

	def Update_Strategy(self,c_control,shoot,move_dir,keep_action):
		if c_control.empty() ==True:
			c_control.put([shoot,move_dir,keep_action])
			return True
		else:
			return False

	def DrawMaze(self):
		for tile in self.mapinfo[2]:
			if (tile[1] != 1) and (tile[1] != 4) and (tile[1] != 0):
				T = tile[0][1]/16
				L = tile[0][0]/16
				self.maze[T][L] = 1
		self.maze[23][11] = 1
		self.maze[23][12] = 1
		self.maze[23][13] = 1
		self.maze[23][14] = 1
		self.maze[24][11] = 1
		self.maze[24][12] = 1
		self.maze[24][13] = 1
		self.maze[24][14] = 1
		self.maze[25][11] = 1
		self.maze[25][12] = 1
		self.maze[25][13] = 1
		self.maze[25][14] = 1
		
	def PathDecision(self,RL,TD):
		my16T = self.mapinfo[3][0][0][1]//16
		my16L = self.mapinfo[3][0][0][0]//16
		if TD == 0:
			tmpT = my16T -1
		else:
			tmpT = my16T +2
		ptr = my16L
		blkcounter = 0
		RLcounter = 0
		while (blkcounter < 2) and (ptr < 26) and (ptr > -1) and (tmpT < 26) and (tmpT > -1):
			if (self.maze[tmpT][ptr] == 1):
				if (self.maze[my16T][ptr] == 0):
					RLcounter+=1
				else:
					#RLcounter = 26
					RLcounter += 10
					break
			elif (self.maze[tmpT][ptr] == 0):
				if (self.maze[my16T][ptr] == 0):
					blkcounter+=1
				else:
					RLcounter = 26
					break
			if RL == 1:
				ptr-=1
			else:
				ptr+=1
		if ((ptr > 25) or (ptr < 0)) and (blkcounter < 2):
			#print "RL No road"
			RLcounter = 26
		if (tmpT > 25) or (tmpT < 0):
			#print "RL out"
			RLcounter = 26
		if (RLcounter == 0):
			RLcounter = 100
		if RL == 1:
			tmpL = my16L +2
		else:
			tmpL = my16L -1
		ptr = my16T
		blkcounter = 0
		TDcounter = 0
		while (blkcounter < 2) and (ptr < 26) and (ptr > -1) and (tmpL < 26) and (tmpL > -1):
			if (self.maze[ptr][tmpL] == 1):
				if (self.maze[ptr][my16L] == 0):
					TDcounter+=1
				else:
					#TDcounter = 26
					TDcounter += 10
					break
			elif (self.maze[ptr][tmpL] == 0):
				if (self.maze[ptr][my16L] == 0):
					blkcounter+=1
				else:
					TDcounter = 26
					break
			if TD == 2:
				ptr-=1
			else:
				ptr+=1
		if ((ptr > 25) or (ptr < 0)) and (blkcounter < 2):
			#print "No road"
			TDcounter = 26
		if (tmpL > 25) or (tmpL < 0):
			#print "out"
			TDcounter = 26
		if (TDcounter == 0):
			TDcounter = 100
		
		#print (RLcounter, TDcounter)
		if (TDcounter < RLcounter):
			if TD == 0:
				return [2,TDcounter]
			else:
				return [0,TDcounter]
		else:
			if RL == 1:
				return [3,RLcounter]
			else:
				return [1,RLcounter]
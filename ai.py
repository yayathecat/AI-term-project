import random
import time
import multiprocessing
import Queue
class ai_agent():
	mapinfo = []
	def __init__(self):
		self.mapinfo = []

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

		WantTo = 4
		GoRound = 4
	
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
			## Check if path for 4 direction ##
			if (myL <= 2) or ((myL in range(flagL+flagW-1, flagL+flagW+3+3)) and (myT in range(flagT-myH, flagT+flagH))):
				NoLeft = True;
			elif ((myL+myW) >= (26*16-2)) or (((myL+myW) in range(flagL-3-3, flagL+1)) and (myT in range(flagT-myH, flagT+flagH))):
				NoRight = True;
			if (myT <= 2):
				NoTop = True;
			elif ((myT+myH) >= (26*16-2)) or (((myT+myH) in range(flagT-3-3, flagT+1)) and (myL in range(flagL-myW, flagL+flagW))):
				NoDown = True;
			# tiles
			for tile in self.mapinfo[2]:
				if ((tile[0][0] in range(myL, myL+myW)) or ((tile[0][0]+tile[0][2]) in range(myL, myL+myW))) and (tile[1] != 4):
					if ((tile[0][1]+tile[0][3]) in range (myT-3-3, myT+1)) and (not NoTop):
						#print "No way to Top"
						NoTop = True
						NoTop_tile = tile
						#if (tile[0][1] in (flagT-1, flagT+flagH)):
						#	NoTop_tile[1] = 6
					elif (tile[0][1] in range (myT+myH-1, myT+myH+3+3)) and (not NoDown):
						#print "No way to Down"
						NoDown = True
						NoDown_tile = tile
						#if (tile[0][1] in (flagT-1, flagT+flagH)) and (tile[0][0] in range(flagL-1, flagL+flagW)):
						#	NoDown_tile[1] = 6
				if ((tile[0][1] in range(myT, myT+myH)) or ((tile[0][1]+tile[0][3]) in range(myT, myT+myH))) and (tile[1] != 4):
					if ((tile[0][0]+tile[0][2]) in range(myL-3-3, myL+1)) and (not NoLeft):
						#print "No way to Left"
						NoLeft = True
						NoLeft_tile = tile
						#if tile[0][0] in range(flagL-1, flagL+flagW):
						#if (tile[0][1] in (flagT-1, flagT+flagH)) and (tile[0][0] in range(flagL-1, flagL+flagW)):
						#	NoLeft_tile[1] = 6
					elif (tile[0][0] in range(myL+myW-1, myL+myW+3+3)) and (not NoRight):
						#print "No way to Right"
						NoRight = True
						NoRight_tile = tile
						#if tile[0][0] in range(flagL-1, flagL+flagW):
						#if (tile[0][1] in (flagT-1, flagT+flagH)) and (tile[0][0] in range(flagL-1, flagL+flagW)):
						#	NoRight_tile[1] = 6
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
			#	if ((tile[0][0] in range(myL, myL+myW)) or ((tile[0][0]+tile[0][2]) in range(myL, myL+myW))) and (tile[1] != 4):
			#		if (tile[0][1]+tile[0][3]) in range (myT-2, myT-1):
			#			#print "#No way to Top"
			#			NoTop = True
			#			#NoTop_tile = tile
			#		elif tile[0][1] in range (myT+myH+1, myT+myH+2):
			#			#print "#No way to Down"
			#			NoDown = True
			#			#NoDown_tile = tile
			#	if ((tile[0][1] in range(myT, myT+myH)) or ((tile[0][1]+tile[0][3]) in range(myT, myT+myH))) and (tile[1] != 4):
			#		if (tile[0][0]+tile[0][2]) in range(myL-2, myL-1):
			#			#print "#No way to Left"
			#			NoLeft = True
			#			#NoLeft_tile = tile
			#		elif tile[0][0] in range(myL+myW+1, myL+myW+2):
			#			#print "#No way to Right"
			#			NoRight = True
			#			#NoRight_tile = tile
						
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
				print "Trace to Down"
				move_dir = 2;
				shoot = 0;
			elif (enemyL < myL) & (not NoLeft) & (not ((myL < (enemyL + enemyW+12)) and (((enemyD == 0) and (enemyT > myT)) or ((enemyD == 2) and (enemyT < myT))))):
				print "Trace to Left";
				move_dir = 3;
				shoot = 0;
			elif (enemyL > myL) & (not NoRight) & (not (((myL + myW) > (enemyL-12)) and (((enemyD == 0) and (enemyT > myT)) or ((enemyD == 2) and (enemyT < myT))))):
				print "Trace to Right";
				move_dir = 1;
				shoot = 0;
			elif (enemyT < myT) & (not NoTop) & (not ((myT < (enemyT + enemyH+12)) and (((enemyD == 1) and (enemyL < myL)) or ((enemyD == 3) and (enemyL > myL))))):
				print "Trace to Top";
				move_dir = 0;
				shoot = 0;
			elif (myT < enemyT) & (NoDown_tile[1] == 1):
				if ((myL+10+6)< NoDown_tile[0][0]):
					print "Shoot Down Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoDown_tile[0][0]+NoDown_tile[0][2]) <= (myL+10+1)):
					print "Shoot Down Wall (L)"
					move_dir = 3
					shoot = 0
				else:
					move_dir = 2;
					#if (myL in range(flagL-myW, flagL+flagW)) and (myT < (22*16)):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoDown_tile[0][1]-(myT+myH)
					print "Shoot D wall"
			elif (enemyL < myL) & (NoLeft_tile[1] == 1):
				if ((myT+10+6) < NoLeft_tile[0][1]):
					print "Shoot Left Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoLeft_tile[0][1]+NoLeft_tile[0][3]) <= (myT+10+1)):
					print "Shoot Left Wall (U)"
					move_dir = 0
					shoot = 0
				else:
					move_dir = 3;
					#if (myT > (flagT-(flagH/2))) and (flagL < myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = myL-(NoLeft_tile[0][0]+NoLeft_tile[0][2])
					print "Shoot L wall"
			elif (myL < enemyL) & (NoRight_tile[1] == 1):
				if ((myT+10+6) < NoRight_tile[0][1]):
					print "Shoot Right Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoRight_tile[0][1]+NoRight_tile[0][3]) <= (myT+10+1)):
					print "Shoot Right Wall (U)"
					move_dir = 0
					shoot = 0
				else:
					move_dir = 1;
					#if (myT > (flagT-(flagH/2))) and (flagL > myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoRight_tile[0][0]-(myL+myW)
					print "Shoot R wall"
			elif (enemyT < myT) & (NoTop_tile[1] == 1):
				if ((myL+10+6)< NoTop_tile[0][0]):
					print "Shoot Top Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoTop_tile[0][0]+NoTop_tile[0][2]) <= (myL+10+1)):
					print "Shoot Top Wall (L)"
					move_dir = 3
					shoot = 0
				else:
					move_dir = 0;
					shoot = 1;
					shootDist = myT-(NoTop_tile[0][1]+NoTop_tile[0][3])
					print "Shoot T wall"
					#self.Update_Strategy(c_control,0,move_dir,0);
			else:
				if NoTop:
					print ("Top:",NoTop_tile[1])
				if NoRight:
					print ("Right:",NoRight_tile[1])
				if NoDown:
					print ("Down:",NoDown_tile[1])
				if NoLeft:
					print ("Left:",NoLeft_tile[1])
				
			## Check around ##
			# Enemies #
			for enemy in self.mapinfo[1]:
				enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
				enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
				#if (enemy_bulletL in range(myL+9-6+1, myL+9+6-1)):
				if (enemy_bulletL in range(myL+10-6+1, myL+10+6-1)):
					if (enemy[0][1] < myT):
						print "Find enemy on the Top"
						move_dir = 0
						shoot = 1
						shootDist = myT-(enemy[0][1]+enemy[0][3])
						if (enemy[3] == 1) or (enemy[1] == 2):
							shootDist = shootDist / 2
						#self.Update_Strategy(c_control,0,move_dir,0)
						
						if NoTop & (NoTop_tile[1] == 1):
							if ((myL+10+6)< NoTop_tile[0][0]):
								print "Shoot Top Wall (R)"
								move_dir = 1
								shoot = 0
							#elif ((NoTop_tile[0][0]+NoTop_tile[0][2]) < (myL+9+1)):
							elif ((NoTop_tile[0][0]+NoTop_tile[0][2]) <= (myL+10+1)):
								print "Shoot Top Wall (L)"
								move_dir = 3
								shoot = 0
							else:
								move_dir = 0;
								shoot = 1;
								#shootDist = myT-(NoTop_tile[0][1]+NoTop_tile[0][3])
								shootDist = 0
								print "Shoot T wall"
								#self.Update_Strategy(c_control,0,move_dir,0);
						
					elif (myT < enemy[0][1]):
						print "Find enemy on the Down"
						move_dir = 2
						shoot = 1
						shootDist = enemy[0][1]-(myT+myH)
						if (enemy[3] == 1) or (enemy[1] == 0):
							shootDist = shootDist / 2
						#self.Update_Strategy(c_control,0,move_dir,0)
						
						if NoDown & (NoDown_tile[1] == 1):
							if ((myL+10+6)< NoDown_tile[0][0]):
								print "Shoot Down Wall (R)"
								move_dir = 1
								shoot = 0
							elif ((NoDown_tile[0][0]+NoDown_tile[0][2]) <= (myL+10+1)):
								print "Shoot Down Wall (L)"
								move_dir = 3
								shoot = 0
							else:
								move_dir = 2;
								#if (myL in range(flagL-myW, flagL+flagW)) and (myT < (22*16)):
								#	shoot = 0;
								#else:
								shoot = 1;
								#shootDist = NoDown_tile[0][1]-(myT+myH)
								shootDist = 0
						
				elif (enemy_bulletL in range(myL-6-1, myL+10-6)) and (((enemy[0][1] < myT) and (enemy[1] == 2)) or ((myT < enemy[0][1]) and (enemy[1] == 0))):
					if not NoRight:
						print "Erun R"
						move_dir = 1
						shoot = 0
					else:
						print "Eclose L"
						move_dir = 3
						shoot = 0
				elif (enemy_bulletL in range(myL+10+6, myL+myW+1)) and (((enemy[0][1] < myT) and (enemy[1] == 2)) or ((myT < enemy[0][1]) and (enemy[1] == 0))):
					if not NoLeft:
						print "Erun L"
						move_dir = 3
						shoot = 0
					else:
						print "Eclose R"
						move_dir = 1
						shoot = 0
						
				#elif (enemy_bulletT in range(myT+9-6+1, myT+9+6-1)):
				if (enemy_bulletT in range(myT+10-6+1, myT+10+6-1)):
					if (enemy[0][0] < myL):
						print "Find enemy on the Left"
						move_dir = 3
						shoot = 1
						shootDist = myL-(enemy[0][0]+enemy[0][2])
						if (enemy[3] == 1) or (enemy[1] == 1):
							shootDist = shootDist / 2
						#self.Update_Strategy(c_control,0,move_dir,0)
						
						if NoLeft & (NoLeft_tile[1] == 1):
							if ((myT+10+6) < NoLeft_tile[0][1]):
								print "Shoot Left Wall (D)"
								move_dir = 2
								shoot = 0
							elif ((NoLeft_tile[0][1]+NoLeft_tile[0][3]) <= (myT+10+1)):
								print "Shoot Left Wall (U)"
								move_dir = 0
								shoot = 0
							else:
								move_dir = 3;
								#if (myT in range(flagT-flagH, flagT+flagheight)) and (flagL < myL):
								#if (myT > (flagT-(flagH/2))) and (flagL < myL):
								#	shoot = 0;
								#else:
								shoot = 1;
								#shootDist = myL-(NoLeft_tile[0][0]+NoLeft_tile[0][2])
								shootDist = 0
								print "Shoot L wall"
								#self.Update_Strategy(c_control,0,move_dir,0);
								#self.Update_Strategy(c_control,shoot,move_dir,0);
						
					elif (myL < enemy[0][0]):
						print "Find enemy on the Right"
						move_dir = 1
						shoot = 1
						shootDist = enemy[0][0]-(myL+myW)
						if (enemy[3] == 1) or (enemy[1] == 3):
							shootDist = shootDist / 2
						#self.Update_Strategy(c_control,0,move_dir,0)
						
						if NoRight & (NoRight_tile[1] == 1):
							if ((myT+10+6) < NoRight_tile[0][1]):
								print "Shoot Right Wall (D)"
								move_dir = 2
								shoot = 0
							elif ((NoRight_tile[0][1]+NoRight_tile[0][3]) <= (myT+10+1)):
								print "Shoot Right Wall (U)"
								move_dir = 0
								shoot = 0
							else:
								move_dir = 1;
								#if (myT in range(flagT-flagH, flagT+flagheight)) and (flagL > myL):
								#if (myT > (flagT-(flagH/2))) and (flagL > myL):
								#	shoot = 0;
								#else:
								shoot = 1;
								#shootDist = NoRight_tile[0][0]-(myL+myW)
								shootDist = 0
								print "Shoot R wall"
								#self.Update_Strategy(c_control,0,move_dir,0);
								#self.Update_Strategy(c_control,shoot,move_dir,0);
						
				elif (enemy_bulletT in range(myT-6-1, myL+10-6)) and (((enemy[0][0] < myL) and (enemy[1] == 1)) or ((myL < enemy[0][0]) and (enemy[1] == 3))):
					if not NoDown:
						print "Erun D"
						move_dir = 2
						shoot = 0
					else:
						print "Eclose T"
						move_dir = 0
						shoot = 0
				elif (enemy_bulletT in range(myT+10+6, myT+myH+1)) and (((enemy[0][0] < myL) and (enemy[1] == 1)) or ((myL < enemy[0][0]) and (enemy[1] == 3))):
					if not NoTop:
						print "Erun T"
						move_dir = 0
						shoot = 0
					else:
						print "Eclose D"
						move_dir = 2
						shoot = 0
						
			# Bullets #
			for bullet in self.mapinfo[0]:
				if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+myW+1)) and (bullet[1] == 0) and ((myT+myH) < (bullet[0][1]+bullet[0][3])):
					print "Bullet comes Up"
					#if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+9-bullet[0][2])):
					if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+10-bullet[0][2])):
						#if not NoLeft:
						if not NoRight:
							print "run R"
							move_dir = 1
							shoot = 0
						else:
							print "close L"
							move_dir = 3
							shoot = 0
					#elif (bullet[0][0] in range(myL+9+6, myL+myW+1)):
					elif (bullet[0][0] in range(myL+10+6, myL+myW+1)):
						#if not NoRight:
						if not NoLeft:
							print "run L"
							move_dir = 3
							shoot = 0
						else:
							print "close R"
							move_dir = 1
							shoot = 0
					else:
						move_dir = 2
						shoot = 1
						#shootDist = bullet[0][1]-(myT+myH)
						shootDist = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
				elif (bullet[0][0] in range(myL-bullet[0][2]-1, myL+myW+1)) and (bullet[1] == 2) and (bullet[0][1] < myT):
					print "Bullet comes Down"
					#if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+9-bullet[0][2])):
					if (bullet[0][0] in range(myL-bullet[0][2]-1, myL+10-bullet[0][2])):
						#if not NoLeft:
						if not NoRight:
							print "run R"
							move_dir = 1
							shoot = 0
						else:
							print "close L"
							move_dir = 3
							shoot = 0
					#elif (bullet[0][0] in range(myL+9+6, myL+myW+1)):
					elif (bullet[0][0] in range(myL+10+6, myL+myW+1)):
						#if not NoRight:
						if not NoLeft:
							print "run L"
							move_dir = 3
							shoot = 0
						else:
							print "close R"
							move_dir = 1
							shoot = 0
					else:
						move_dir = 0
						shoot = 1
						#shootDist = myL-(bullet[0][0]+bullet[0][2])
						shootDist = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
				elif (bullet[0][1] in range(myT-bullet[0][3]-1, myT+myH+1)) and (bullet[1] == 3) and ((myL+myW) < (bullet[0][0]+bullet[0][2])):
					print "Bullet comes Left"
					#if (bullet[0][1] in range(myT-bullet[0][3]-1, myT+9-bullet[0][3])):
					if (bullet[0][1] in range(myT-bullet[0][3]-1, myT+10-bullet[0][3])):
						#if not NoDown:
						if not NoTop:
							print "run T"
							move_dir = 0
							shoot = 0
						else:
							print "close D"
							move_dir = 2
							shoot = 0
					#elif (bullet[0][1] in range(myT+9+6, myT+myH+1)):
					elif (bullet[0][1] in range(myT+10+6, myT+myH+1)):
						#if not NoTop:
						if not NoDown:
							print "run D"
							move_dir = 2
							shoot = 0
						else:
							print "close T"
							move_dir = 0
							shoot = 0
					else:
						move_dir = 1
						shoot = 1
						#shootDist = bullet[0][0]-(myL+myW)
						if (myT in range(flagT-myH, flagT+flagH)) and (myL < flagL) and (flagL < bullet[0][0]):
							shootDist = 100
						else:
							shootDist = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
				elif (bullet[0][1] in range(myT-bullet[0][3]-1, myT+myH+1)) and (bullet[1] == 1) and (bullet[0][0] < myL):
					print "Bullet comes Right"
					#if (bullet[0][1] in range(myT-bullet[0][3]-1, myT+9-bullet[0][3])):
					if (bullet[0][1] in range(myT-bullet[0][3]-1, myT+10-bullet[0][3])):
						#if not NoDown:
						if not NoTop:
							print "run T"
							move_dir = 0
							shoot = 0
						else:
							print "close D"
							move_dir = 2
							shoot = 0
					#elif (bullet[0][1] in range(myT+9+6, myT+myH+1)):
					elif (bullet[0][1] in range(myT+10+6, myT+myH+1)):
						#if not NoTop:
						if not NoDown:
							print "run D"
							move_dir = 2
							shoot = 0
						else:
							print "close T"
							move_dir = 0
							shoot = 0
					else:
						move_dir = 3
						shoot = 1
						#shootDist = bullet[0][0]-(myL+myW)
						if (myT in range(flagT-myH, flagT+flagH)) and (flagL < myL) and (bullet[0][0] < flagL):
							shootDist = 100
						else:
							shootDist = 0
						#self.Update_Strategy(c_control,0,move_dir,0)
			## Go around ##
			## Check block or not ##
			if (move_dir == 0) and NoTop and (shoot == 0):
				print ("No way top", NoTop_tile)
				if ((myL+10+6)< NoTop_tile[0][0]) and (NoTop_tile[1] == 1):
					print "Shoot Top Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoTop_tile[0][0]+NoTop_tile[0][2]) <= (myL+10+1)) and (NoTop_tile[1] == 1):
					print "Shoot Top Wall (L)"
					move_dir = 3
					shoot = 0
				elif (NoTop_tile[1] == 1):
					move_dir = 0;
					shoot = 1;
					shootDist = myT-(NoTop_tile[0][1]+NoTop_tile[0][3])
					print "Shoot T wall"
					#self.Update_Strategy(c_control,0,move_dir,0);
				else:
					print "Unknown block!?"
			elif (move_dir == 1) and NoRight and (shoot == 0):
				print ("No way right", NoRight_tile)
				if ((myT+10+6) < NoRight_tile[0][1]) and (NoRight_tile[1] == 1):
					print "Shoot Right Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoRight_tile[0][1]+NoRight_tile[0][3]) <= (myT+10+1)) and (NoRight_tile[1] == 1):
					print "Shoot Right Wall (U)"
					move_dir = 0
					shoot = 0
				elif (NoRight_tile[1] == 1):
					move_dir = 1;
					#if (myT > (flagT-(flagH/2))) and (flagL > myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoRight_tile[0][0]-(myL+myW)
					print "Shoot R wall"
				else:
					print "Unknown block!?"
			elif (move_dir == 2) and NoDown and (shoot == 0):
				print ("No way down", NoDown_tile)
				if ((myL+10+6)< NoDown_tile[0][0]) and (NoDown_tile[1] == 1):
					print "Shoot Down Wall (R)"
					move_dir = 1
					shoot = 0
				elif ((NoDown_tile[0][0]+NoDown_tile[0][2]) <= (myL+10+1)) and (NoDown_tile[1] == 1):
					print "Shoot Down Wall (L)"
					move_dir = 3
					shoot = 0
				elif (NoDown_tile[1] == 1):
					move_dir = 2;
					#if (myL in range(flagL-myW, flagL+flagW)) and (myT < (22*16)):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = NoDown_tile[0][1]-(myT+myH)
					print "Shoot D wall"
				else:
					print "Unknown block!?"
			elif (move_dir == 3) & NoLeft & (shoot == 0):
				print ("No way left", NoLeft_tile)
				if ((myT+10+6) < NoLeft_tile[0][1]) and (NoLeft_tile[1] == 1):
					print "Shoot Left Wall (D)"
					move_dir = 2
					shoot = 0
				elif ((NoLeft_tile[0][1]+NoLeft_tile[0][3]) <= (myT+10+1)) and (NoLeft_tile[1] == 1):
					print "Shoot Left Wall (U)"
					move_dir = 0
					shoot = 0
				elif (NoLeft_tile[1] == 1):
					move_dir = 3;
					#if (myT > (flagT-(flagH/2))) and (flagL < myL):
					#	shoot = 0;
					#else:
					shoot = 1;
					shootDist = myL-(NoLeft_tile[0][0]+NoLeft_tile[0][2])
					print "Shoot L wall"
				else:
					print "Unknown block!?"
			## Final Check: Move_dir ##
			if move_dir == 0:
				# check if any other enemies/bullets in the front row
				for bullet in self.mapinfo[0]:
					if (bullet[0][1] in range(myT-2*bullet[0][3], myT-bullet[0][3]-1)) and ((bullet[1]==1) or (bullet[1]==3)):
						if (bullet[0][0] < myL) and (bullet[1] == 1):
							print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][0] > myL) and (bullet[1] == 3):
							print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					if ((enemy[0][1] + enemy[0][3]) in range(myT-6, myT+6)) and ((enemy[1]==1) or (enemy[1]==3)):
						if (enemy[0][0] < myL) and (enemy[1] == 1):
							print "Take care! enemy!"
							move_dir = 4
						elif (enemy[0][0] > myL) and (enemy[1] == 3):
							print "Take care! enemy!"
							move_dir = 4
			elif move_dir == 2:
				# check if any other enemies/bullets in the front row
				for bullet in self.mapinfo[0]:
					if (bullet[0][1] in range(myT+myH+1, myT+myH+bullet[0][3])) and ((bullet[1]==1) or (bullet[1]==3)):
						if (bullet[0][0] < myL) and (bullet[1] == 1):
							print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][0] > myL) and (bullet[1] == 3):
							print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					if (enemy[0][1] in range(myT+myH-6, myT+myH+6)) and ((enemy[1]==1) or (enemy[1]==3)):
						if (enemy[0][0] < myL) and (enemy[1] == 1):
							print "Take care! enemy!"
							move_dir = 4
						elif (enemy[0][0] > myL) and (enemy[1] == 3):
							print "Take care! enemy!"
							move_dir = 4
			elif move_dir == 1:
				# check if any other enemies/bullets in the front column
				for bullet in self.mapinfo[0]:
					if (bullet[0][0] in range(myL+myW+1, myL+myW+bullet[0][2])) and ((bullet[1]==0) or (bullet[1]==2)):
						if (bullet[0][1] < myT) and (bullet[1] == 2):
							print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][1] > myT) and (bullet[1] == 0):
							print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					if (enemy[0][0] in range(myL+myW-6, myL+myW+6)) and ((enemy[1]==0) or (enemy[1]==2)):
						if (enemy[0][1] < myT) and (enemy[1] == 2):
							print "Take care! enemy!"
							move_dir = 4
						elif (enemy[0][1] > myT) and (enemy[1] == 0):
							print "Take care! enemy!"
							move_dir = 4
			elif move_dir == 3:
				# check if any other enemies/bullets in the front column
				for bullet in self.mapinfo[0]:
					if (bullet[0][0] in range(myL-2*bullet[0][2], myL-bullet[0][2]-1)) and ((bullet[1]==0) or (bullet[1]==2)):
						if (bullet[0][1] < myT) and (bullet[1] == 2):
							print "Take care! bullet!"
							move_dir = 4
						elif (bullet[0][1] > myT) and (bullet[1] == 0):
							print "Take care! bullet!"
							move_dir = 4
				for enemy in self.mapinfo[1]:
					if ((enemy[0][0] + enemy[0][2]) in range(myL-6, myL+6)) and ((enemy[1]==0) or (enemy[1]==2)):
						if (enemy[0][1] < myT) and (enemy[1] == 2):
							print "Take care! enemy!"
							move_dir = 4
						elif (enemy[0][1] > myT) and (enemy[1] == 0):
							print "Take care! enemy!"
							move_dir = 4
						#shoot = 0;
				#		careful = True;
			## Detect enemy around ##
			if shoot == 0:
				for enemy in self.mapinfo[1]:
					#if enemy[0][0] in range(myL+9-enemy[0][2]+1, myL+9+6-1):
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
					#elif enemy[0][1] in range(myT+9-enemy[0][3]+1, myT+9+6-1):
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
			#print (move_dir, shoot)
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


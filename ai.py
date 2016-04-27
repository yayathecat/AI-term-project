import random
import time
import multiprocessing
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

		while True:
		#-----your ai operation,This code is a random strategy,please design your ai !!-----------------------			
			self.Get_mapInfo(p_mapinfo)
			#time.sleep(0.1)	
			#q=0
			#for i in range(10000000):
			#	q+=1
			move_dir = 4
			shoot = 0
			keep_action = 1
			myleft = self.mapinfo[3][0][0][0]
			mytop = self.mapinfo[3][0][0][1]
			myweight = self.mapinfo[3][0][0][2]
			myheight = self.mapinfo[3][0][0][3]
			flagleft = 12*16;
			flagtop = 24*16;
			flagwidth = 32;
			flagheight = 32;
			Noleft = False;
			Noright = False;
			Notop = False;
			Nodown = False;
			## Check if path for 4 direction ##
			# tiles
			for i in range(0, len(self.mapinfo[2]), 1):
				tile = self.mapinfo[2][i];
				if ((tile[0][0] in range(myleft-1, myleft+myweight)) or ((tile[0][0]+tile[0][2]) in range(myleft, myleft+myweight))) and (tile[1] != 4):
					#if (tile[0][1]+tile[0][3]) in range(mytop-2, mytop-1):
					if (tile[0][1]+tile[0][3]) == (mytop-1):
					#	print "No way to Top";
						Notop = True;
					#elif tile[0][1] in range(mytop+myheight+1, mytop+myheight+2):
					elif tile[0][1] == (mytop+myheight+1):
					#	print "No way to Down";
						Nodown = True;
				if ((tile[0][1] in range(mytop-1, mytop+myheight)) or ((tile[0][1]+tile[0][3]) in range(mytop, mytop+myheight))) and (tile[1] != 4):
					#if (tile[0][0]+tile[0][2]) in range(myleft-2, myleft-1):
					if (tile[0][0]+tile[0][2]) == (myleft-1):
					#	print "No way to Left";
						Noleft = True;
					#elif tile[0][0] in range(myleft+myweight+1, myleft+myweight+2):
					elif tile[0][0] == (myleft+myweight+1):
					#	print "No way to Right";
						Noright = True;
			# enemies
			for i in range(0, len(self.mapinfo[1]), 1):
				tile = self.mapinfo[1][i];
				if ((tile[0][0] in range(myleft-1, myleft+myweight)) or ((tile[0][0]+tile[0][2]) in range(myleft, myleft+myweight+1))) and (tile[1] != 4):
					if (tile[0][1]+tile[0][3]) in range (mytop-2, mytop-1):
					#	print "#No way to Top";
						Notop = True;
					elif tile[0][1] in range (mytop+myheight+1, mytop+myheight+2):
					#	print "#No way to Down";
						Nodown = True;
				if ((tile[0][1] in range(mytop-1, mytop+myheight)) or ((tile[0][1]+tile[0][3]) in range(mytop, mytop+myheight+1))) and (tile[1] != 4):
					if (tile[0][0]+tile[0][2]) in range(myleft-2, myleft-1):
					#	print "#No way to Left";
						Noleft = True;
					elif tile[0][0] in range(myleft+myweight+1, myleft+myweight+2):
					#	print "#No way to Right";
						Noright = True;
			## Pay attention to bullets ##
			#for bullet in self.mapinfo[0]:
			for i in range(0, len(self.mapinfo[0]), 1):
				bullet = self.mapinfo[0][i]
				#if(self.mapinfo[0][i][0][0] == self.mapinfo[3][0][0][0]):
				#if((bullet[0][0] >= myleft-myweight) and (bullet[0][0] <= myleft+myweight)) | ((bullet[0][1] >= mytop-myheight) and (bullet[0][1] <= mytop+myheight)):
				if(bullet[0][0] in range(myleft-bullet[0][2], myleft+myweight)) and (bullet[1] == 0):
				#if(bullet[0][0] in range(myleft-myweight, myleft+2*myweight)) and (bullet[1] == 0) and (bullet[0][1] < mytop):
					print "Bullet goes Up"
					#break_cnt = 0;
					#while (bullet[0][0] in range(myleft-bullet[0][2], myleft+myweight/4)):
					#while (bullet[0][0] in range(myleft-bullet[0][2], myleft+9)):
					for j in range(0, myleft+9-bullet[0][0]-bullet[0][2]):
						move_dir = 3;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#break_cnt = 0;
					#while (bullet[0][0] in range(myleft+myweight*3/4, myleft+myweight)):
					#while (bullet[0][0] in range(myleft+15, myleft+myweight)):
					for j in range(0, bullet[0][0]-myleft-15):
						move_dir = 1;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#if (bullet[0][1] < mytop):
					#	move_dir = 0;
					#	self.Update_Strategy(c_control,0,move_dir,keep_action);
					#	shoot = 1;
					#	self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#else:
					if (bullet[0][1] > mytop):
						move_dir = 2;
						self.Update_Strategy(c_control,0,move_dir,keep_action);
						if (myleft in range(flagleft-myweight, flagleft+flagwidth)):
							shoot = 0;
						else:
							shoot = 1;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#return;
				elif(bullet[0][0] in range(myleft-bullet[0][2], myleft+myweight)) and (bullet[1] == 2):
				#if(bullet[0][0] in range(myleft-myweight, myleft+2*myweight)) and (bullet[1] == 0) and (bullet[0][1] < mytop):
					print "Bullet goes Down"
					#break_cnt = 0;
					#while (bullet[0][0] in range(myleft-bullet[0][2], myleft+myweight/4)):
					#while (bullet[0][0] in range(myleft-bullet[0][2], myleft+9)):
					for j in range(0, myleft+9-bullet[0][0]-bullet[0][2]):
						move_dir = 3;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#break_cnt = 0;
					#while (bullet[0][0] in range(myleft+myweight*3/4, myleft+myweight)):
					#while (bullet[0][0] in range(myleft+15, myleft+myweight)):
					for j in range(0, bullet[0][0]-myleft-15):
						move_dir = 1;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#if (bullet[0][1] > mytop):
					#	move_dir = 2;
					#	self.Update_Strategy(c_control,0,move_dir,keep_action);
						#if (myleft in range(flagleft-myweight, flagleft+flagwidth)):
						#	shoot = 0;
						#else:
					#	shoot = 1;
					#	self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#else:
					if (bullet[0][1] < mytop):
						move_dir = 0;
						self.Update_Strategy(c_control,0,move_dir,keep_action);
						shoot = 1;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
				elif(bullet[0][1] in range(mytop-bullet[0][3], mytop+myheight)) and (bullet[1] == 1):
					print "Bullet goes Right"
					#break_cnt = 0;
					#while (bullet[0][1] in range(mytop-bullet[0][3], mytop+myheight/4)):
					#while (bullet[0][1] in range(mytop-bullet[0][3], mytop+9)):
					for j in range(0, mytop+9-bullet[0][1]-bullet[0][3]):
						move_dir = 0;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#break_cnt = 0;
					#while (bullet[0][1] in range(mytop+myheight*3/4, mytop+myheight)):
					#while (bullet[0][1] in range(mytop+15, mytop+myheight)):
					for j in range(0, bullet[0][1]-mytop-15):
						move_dir = 2;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#if (bullet[0][0] > myleft):
					#	move_dir = 1;
					#	self.Update_Strategy(c_control,0,move_dir,keep_action);
					#	if (mytop in range(flagtop-myheight, flagtop+flagheight)) and (flagleft > myleft):
					#		shoot = 0;
					#	else:
					#		shoot = 1;
					#	self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#else:
					if (bullet[0][0] < myleft):
						move_dir = 3;
						self.Update_Strategy(c_control,0,move_dir,keep_action);
						if (mytop in range(flagtop-myheight, flagtop+flagheight)) and (flagleft < myleft):
							shoot = 0;
						else:
							shoot = 1;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#return;
				elif(bullet[0][1] in range(mytop-bullet[0][3], mytop+myheight)) and (bullet[1] == 3):
				#elif(bullet[0][1] in range(mytop-myheight, mytop+2*myheight)) and (bullet[1] == 1) and (bullet[0][0] < myleft):
					print "Bullet goes Left"
					#break_cnt = 0;
					#while (bullet[0][1] in range(mytop-bullet[0][3], mytop+myheight/4)):
					#while (bullet[0][1] in range(mytop-bullet[0][3], mytop+9)):
					for j in range(0, mytop+9-bullet[0][1]-bullet[0][3]):
						move_dir = 0;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#break_cnt = 0;
					#while (bullet[0][1] in range(mytop+myheight*3/4, mytop+myheight)):
					#while (bullet[0][1] in range(mytop+15, mytop+myheight)):
					for j in range(0, bullet[0][1]-mytop-15):
						move_dir = 2;
						shoot = 0;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#	break_cnt+=1;
					#	if (break_cnt > 100):
					#		break;
					#if (bullet[0][0] < myleft):
					#	move_dir = 3;
					#	self.Update_Strategy(c_control,0,move_dir,keep_action);
					#	if (mytop in range(flagtop-myheight, flagtop+flagheight)) and (flagleft < myleft):
					#		shoot = 0;
					#	else:
					#		shoot = 1;
					#	self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#else:
					if (bullet[0][0] > myleft):
						move_dir = 1;
						self.Update_Strategy(c_control,0,move_dir,keep_action);
						if (mytop in range(flagtop-myheight, flagtop+flagheight)) and (flagleft > myleft):
							shoot = 0;
						else:
							shoot = 1;
						self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#return;
				#else:
			min_dist = -1;
			min_enemy = self.mapinfo[3][0];
			danger_flage = False;
			danger_enemy = self.mapinfo[3][0];
			for j in range(0, len(self.mapinfo[1]), 1):
				enemy = self.mapinfo[1][j];
				dist = (enemy[0][0]-myleft)*(enemy[0][0]-myleft) + (enemy[0][1]-mytop)*(enemy[0][1]-mytop);
				if (min_dist == -1) or (dist < min_dist):
					min_dist = dist;
					min_enemy = enemy;
				if (enemy[0][1] > (13*16)):
					danger_enemy = enemy;
					danger_flage = True;
				enemy_bulletL = enemy[0][0] + (enemy[0][2] - 6)/2;
				enemy_bulletT = enemy[0][1] + (enemy[0][3] - 6)/2;
				#if (enemy[0][0] in range(myleft-myweight/2, myleft+myweight)) and (enemy[0][1] < mytop):
				#if (enemy[0][0] in range(myleft-myweight/2, myleft+15)) and (enemy[0][1] < mytop):
				if (enemy_bulletL in range(myleft+3+1, myleft+myweight-9-1)) and (enemy[0][1] < mytop):
					print "Find enemy on the Up"
					move_dir = 0;
					self.Update_Strategy(c_control,0,move_dir,keep_action);
					shoot = 1;
					self.Update_Strategy(c_control,shoot,move_dir,keep_action)
					#break;
				#elif (enemy[0][0] in range(myleft-myweight/2, myleft+myweight)) and (enemy[0][1] > mytop):
				#elif (enemy[0][0] in range(myleft-myweight/2, myleft+15)) and (enemy[0][1] > mytop):
				elif (enemy_bulletL in range(myleft+3+1, myleft+myweight-9-1)) and (enemy[0][1] > mytop):
					print "Find enemy on the Down"
					move_dir = 2;
					self.Update_Strategy(c_control,0,move_dir,keep_action);
					if (myleft in range(flagleft-myweight, flagleft+flagwidth)):
						shoot = 0;
					else:
						shoot = 1;
					self.Update_Strategy(c_control,shoot,move_dir,keep_action)
					#break;
				#elif (enemy[0][1] in range(mytop-myheight/2, mytop+myheight)) and (enemy[0][0] > myleft):
				#elif (enemy[0][1] in range(mytop-myheight/2, mytop+15)) and (enemy[0][0] > myleft):
				elif (enemy_bulletT in range(mytop+3+1, mytop+myheight-9-1)) and (enemy[0][0] > myleft):
					print "Find enemy on the Right"
					move_dir = 1;
					self.Update_Strategy(c_control,0,move_dir,keep_action);
					if (mytop in range(flagtop-myheight, flagtop+flagheight)) and (flagleft > myleft):
						shoot = 0;
					else:
						shoot = 1;
					self.Update_Strategy(c_control,shoot,move_dir,keep_action)
					#break;
				#elif (enemy[0][1] in range(mytop-myheight/2, mytop+myheight)) and (enemy[0][0] < myleft):
				#elif (enemy[0][1] in range(mytop-myheight/2, mytop+15)) and (enemy[0][0] < myleft):
				elif (enemy_bulletT in range(mytop+3+1, mytop+myheight-9-1)) and (enemy[0][0] < myleft):
					print "Find enemy on the Left"
					move_dir = 3;
					self.Update_Strategy(c_control,0,move_dir,keep_action);
					if (mytop in range(flagtop-myheight, flagtop+flagheight)) and (flagleft < myleft):
						shoot = 0;
					else:
						shoot = 1;
					self.Update_Strategy(c_control,shoot,move_dir,keep_action);
					#break;
				#move_dir = random.randint(0,4);
				#move_dir = self.mapinfo[3][1];
				#move_dir = 4;
				#shoot = random.randint(0,1)
				#shoot = 0;
			if (move_dir == 4):
			#	print ("Min Dist:", min_dist, ", Min Enemy:", min_enemy[0]);
				# try to move to the closest enemy
				if danger_flage:
					print "Danger!"
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
				break_cnt = 0;
				#if (enemyL < myleft) & (not Noleft) & ((min_enemy[1] == 1) or (min_enemy[1] == 3)):
				#if (enemyL < myleft) & (not Noleft):
				if (enemyL < myleft) & (not Noleft) & (not ((myleft < (enemyL + enemyW+12)) and (((enemyD == 0) and (enemyT > mytop)) or ((enemyD == 2) and (enemyT < mytop))))):
					#if (myleft == (enemyL + enemyW+1)) and (((enemyD == 0) and (enemyT > mytop)) or ((enemyD == 2) and (enemyT < mytop))):
					#if (myleft < (enemyL + enemyW+12)) and (((enemyD == 0) and (enemyT > mytop)) or ((enemyD == 2) and (enemyT < mytop))):
					#	print "Wait(Left)"
					#	move_dir = 4;
					#else:
					print "Trace to Left";
					move_dir = 3;
					shoot = 0;
					self.Update_Strategy(c_control,shoot,move_dir,1);
				#	break_cnt+=1;
				#	if (break_cnt > 16):
				#		break;
				#break_cnt = 0;
				#elif (enemyL > myleft) & (not Noright) & ((min_enemy[1] == 1) or (min_enemy[1] == 3)):
				#elif (enemyL > myleft) & (not Noright):
				elif (enemyL > myleft) & (not Noright) & (not (((myleft + myweight) > (enemyL-12)) and (((enemyD == 0) and (enemyT > mytop)) or ((enemyD == 2) and (enemyT < mytop))))):
					#if ((myleft + myweight-1) == enemyL) and (((enemyD == 0) and (enemyT > mytop)) or ((enemyD == 2) and (enemyT < mytop))):
					#if ((myleft + myweight) > (enemyL-12)) and (((enemyD == 0) and (enemyT > mytop)) or ((enemyD == 2) and (enemyT < mytop))):
					#	print "Wait(Right)"
					#	move_dir = 4;
					#else:
					print "Trace to Right";
					move_dir = 1;
					shoot = 0;
					self.Update_Strategy(c_control,shoot,move_dir,1);
				#	break_cnt+=1;
				#	if (break_cnt > 16):
				#		break;
				#break_cnt = 0;
				#elif (enemyT < mytop) & (not Notop) & ((min_enemy[1] == 0) or (min_enemy[1] == 2)):
				#elif (enemyT < mytop) & (not Notop):
				elif (enemyT < mytop) & (not Notop) & (not ((mytop < (enemyT + enemyH+12)) and (((enemyD == 1) and (enemyL < myleft)) or ((enemyD == 3) and (enemyL > myleft))))):
					#if (mytop == (enemyT + enemyH+1)) and (((enemyD == 1) and (enemyL < myleft)) or ((enemyD == 3) and (enemyL > myleft))):
					#if (mytop < (enemyT + enemyH+12)) and (((enemyD == 1) and (enemyL < myleft)) or ((enemyD == 3) and (enemyL > myleft))):
					#	print "Wait(Top)"
					#	move_dir = 4;
					#else:
					print "Trace to Top";
					move_dir = 0;
					shoot = 0;
					self.Update_Strategy(c_control,shoot,move_dir,1);
				#	break_cnt+=1;
				#	if (break_cnt > 16):
				#		break;
				#break_cnt = 0;
				#elif (enemyT > mytop) & (not Nodown) & ((min_enemy[1] == 0) or (min_enemy[1] == 2)):
				#elif (enemyT > mytop) & (not Nodown):
				elif (enemyT > mytop) & (not Nodown) & (not (((mytop + myheight) > (enemyT-12)) and (((enemyD == 1) and (enemyL < myleft)) or ((enemyD == 3) and (enemyL > myleft))))):
					#if (mytop == (enemyT + enemyH+1)) and (((enemyD == 1) and (enemyL < myleft)) or ((enemyD == 3) and (enemyL > myleft))):
					#if ((mytop + myheight) > (enemyT-12)) and (((enemyD == 1) and (enemyL < myleft)) or ((enemyD == 3) and (enemyL > myleft))):
					#	print "Wait(Down)"
					#	move_dir = 4;
					#else:
					print "Trace to Down"
					move_dir = 2;
					shoot = 0;
					self.Update_Strategy(c_control,shoot,move_dir,1);
				#	break_cnt+=1;
				#	if (break_cnt > 16):
				#		break;
			
			#shoot = random.randint(0,1)
			#move_dir = random.randint(0,4)
			#keep_action = 0
			#keep_action = 1
			#-----------
			self.Update_Strategy(c_control,shoot,move_dir,keep_action);
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


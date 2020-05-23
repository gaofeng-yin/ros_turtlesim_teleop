#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
import math
import sys, select, termios, tty

def getKey():
 	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin,termios.TCSADRAIN,settings)
	return key

def moveRobot():
 	rospy.init_node('MoverTartaruga', anonymous=True) 					# Cria o nome do no. Anonimo para distinguir este no de outros nós
   	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 	# cria o publisher, que ira publicar no topico /turtle1/cmd_vel
  	vel_msg = Twist() 													# cria uma variavel do Tipo twis, que contem a estrutura para controlar a velocidade dos robos
   	rate = rospy.Rate(10) 												# frequencia de atualização do nó. 10 hz
	# inicializacao da variavel de movimentação e velocidade
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	linearSpeed = 1
	angularSpeed = 1
   	print("\nInstruções:")
	print("W: para mover para frente\nX: mover para tras\nA: movimento anti-horario\nD: movimento horario\nS: parar\n")
	print("1: incrementar velocidade linear\n2: decrementar velocidade linear\n3: incrementar velocidade angular\n4: decrementar velocidade angular\n")
	print("P: shutdown")

	while not rospy.is_shutdown():
		key=getKey()
		if key == 'w' :
			vel_msg.linear.x = linearSpeed
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = 0
			pub.publish(vel_msg)
			
		if key == 'x' :
			vel_msg.linear.x = - linearSpeed
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = 0
			pub.publish(vel_msg)
			
		if key == 'a' :
			vel_msg.linear.x = 0
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = angularSpeed * (math.pi/2)
			pub.publish(vel_msg)
			
		if key == 'd' :
			vel_msg.linear.x = 0
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = -angularSpeed * (math.pi/2)
			pub.publish(vel_msg)
			
		if key == 's':
			vel_msg.linear.x = 0
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = 0	
			pub.publish(vel_msg)
		if key == 'p' :
			rospy.signal_shutdown("OFF")
			
		if key == '1' :
			linearSpeed += 1
			print "aumentou velocidade linear para",linearSpeed			
		if key == '2' :
			if linearSpeed > 0:
				linearSpeed -= 1
				print "diminuiu velocidade linear para",linearSpeed
			else :
				print "velocidade linear já está no 0!"
		if key == '3' :
			angularSpeed +=  1
			print "aumentou velocidade linear para",angularSpeed
		if key == '4' :
			if angularSpeed > 0 :
				angularSpeed -= 1
				print "diminuiu velocidade angular para",angularSpeed
			else :
				print "velocidade angular já está no 0"
		
if __name__ == '__main__':						
	try:
		settings = termios.tcgetattr(sys.stdin)
		moveRobot()

	except rospy.ROSInterruptException: pass
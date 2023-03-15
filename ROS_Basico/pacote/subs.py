#!/usr/bin/python3

import numpy as np
import rospy
from geometry_msgs.msg import Accel, Point

class Node2(object):
    def __init__(self):
        #define publicação e subscrição
        self.pub = rospy.Publisher('/topic2', Point, queue_size=10)
        self.sub = rospy.Subscriber('/topic1', Accel, self.callback)

    def callback(self, accel_msg):
        #processa mengagem recebida no topico 1, e tranforma posições dos vetores em seus modulos
        point_msg = Point()
        point_msg.x = np.linalg.norm(accel_msg.linear.x)
        point_msg.y = np.linalg.norm(accel_msg.angular.y)


        #publica modulos em topico 2
        self.pub.publish(point_msg)

    
if __name__ == '__main__':
    #inicia node 2, e mantem nó rodando
    rospy.init_node('node2')
    node = Node2()
    rospy.spin()
#!/usr/bin/python3

import random
import rospy
from geometry_msgs.msg import Accel, Point

class Node1():
    def __init__(self):
        #define publicação e subscrição
        self.pub = rospy.Publisher('/topic1', Accel, queue_size=10)
        self.sub = rospy.Subscriber('/topic2', Point, self.callback)

    def callback(self, point_msg):
        #publica módulos recebidos no topico2
        rospy.loginfo(' Modulo do vetor linear:%d\n Modulo do vetor angular:%d',point_msg.x, point_msg.y)
    
    def run(self):
        #gera randomicamente posições dos vetores entre -20 e 20
        accel_msg = Accel()

        accel_msg.linear.x = random.uniform(-20,20)
        accel_msg.linear.y = random.uniform(-20,20)
        accel_msg.linear.z = random.uniform(-20,20)

        accel_msg.angular.x = random.uniform(-20,20)
        accel_msg.angular.y = random.uniform(-20,20)
        accel_msg.angular.z = random.uniform(-20,20)
        #publica as posições geradas no topico 1
        self.pub.publish(accel_msg)
    
if __name__ == '__main__':
    #inicia node 1, e mantem nó rodando
    rospy.init_node('node1')
    node = Node1()
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        node.run()
        rate.sleep()
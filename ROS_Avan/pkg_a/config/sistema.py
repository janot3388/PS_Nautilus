#!/usr/bin/python3

# importa bibliotecas
import rospy
import tf2_ros
import math
import geometry_msgs.msg

# classe que instancia planetas, com seus próprios broadcasters, e calcula a posição dos mesmos
class Planet:
    def __init__(self, name, radius, orbit_dist, period, parent):

        self.name = name
        self.radius = radius
        self.orbit_dist = orbit_dist
        self.parent = parent
        self.angle = 0
        self.period = period
        self.transform_broadcaster = tf2_ros.TransformBroadcaster()

        # método calculados de posição 
        # (formula trigonométrica em função de angulo e raio de órbita)
        # obs: devido ao marcador usado no rviz, a variável de raio do planeta caiu em desuso
    def get_position(self):
        x = math.cos(self.angle) * self.orbit_dist
        y = math.sin(self.angle) * self.orbit_dist
        z = 0
        return (x, y, z) #retorna posição
        
        # método que devolve a posição nova ao broadcaster
        # junto a outras especificações do tipo da mensagem
    def update_position(self):
            
            # chama o método calculador e retem posição transformada na variavel tupla
            position = self.get_position() 
        
            # variavel que retem template da mensagem
            transform = geometry_msgs.msg.TransformStamped()

            # attribui informações de frame (stamp, pai e filho)
            transform.header.stamp = rospy.Time.now()
            transform.header.frame_id = self.parent
            transform.child_frame_id = self.name

            # atribui posição transformada
            transform.transform.translation.x = position[0]
            transform.transform.translation.y = position[1]
            transform.transform.translation.z = position[2]
            transform.transform.rotation.w = 1.0

            # publica a mensagem no tópico /tf
            self.transform_broadcaster.sendTransform(transform)
        


if __name__ == '__main__':

    # inicia nó do sistema
    rospy.init_node('sis')

    rate=rospy.Rate(60)

    # obtem respectivamente raio, distancia de orbita e variação de velocidade
    # de cada planeta, a partir do arquivo param.yaml
    sun_radius = rospy.get_param("/sun/rd")
    earth_radius = rospy.get_param("/earth/rd")
    mars_radius = rospy.get_param("/mars/rd")
    moon_radius = rospy.get_param("/moon/rd")

    nau_radius = rospy.get_param("/nau/rd")
    ti_radius = rospy.get_param("/ti/rd")
    lu_radius = rospy.get_param("/lu/rd")

    sun_orbit_radius = rospy.get_param("/sun/od")
    earth_orbit_radius = rospy.get_param("/earth/od")
    mars_orbit_radius = rospy.get_param("/mars/od")
    moon_orbit_radius = rospy.get_param("/moon/od")

    nau_orbit_radius = rospy.get_param("/nau/od")
    ti_orbit_radius = rospy.get_param("/ti/od")
    lu_orbit_radius = rospy.get_param("/lu/od")

    sun_period = rospy.get_param("/sun/p")
    earth_period = rospy.get_param("/earth/p")
    mars_period = rospy.get_param("/mars/p")
    moon_period = rospy.get_param("/moon/p")

    nau_period = rospy.get_param("/nau/p")
    ti_period = rospy.get_param("/ti/p")
    lu_period = rospy.get_param("/lu/p")

    # lista que instancia cada planeta em um objeto, com suas caracteristicas
    planets = [
        Planet('sun', sun_radius, sun_orbit_radius, sun_period, 'world'),
        Planet('earth', earth_radius, earth_orbit_radius, earth_period, 'sun'),
        Planet('moon', moon_radius, moon_orbit_radius ,moon_period, 'earth'),
        Planet('mars', mars_radius, mars_orbit_radius, mars_period , 'sun'),
        Planet('nau', nau_radius, nau_orbit_radius, nau_period , 'sun'),
        Planet('ti', ti_radius, ti_orbit_radius, ti_period , 'nau'),
        Planet('lu', lu_radius, lu_orbit_radius, lu_period , 'ti')        
    ]

    # loop de execução
    while not rospy.is_shutdown():

        # para cada planeta da lista, calcula e envia posição transformada ao tópico /tf
        # e incrimenta valor a variavel angulo de cada um, que varia de acordo
        # com suas variaveis de variação de velocidade
        for p in planets:
            p.update_position()
            p.angle += 0.01 * (p.period)
            rate.sleep()

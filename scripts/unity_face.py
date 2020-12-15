#!/usr/bin/python


from roboy_control_msgs.msg import Emotion
from roboy_control_msgs.srv import ShowEmotion
from std_msgs.msg import String

import os
import sys

import rospy

topic_root = "/roboy/brain"

def face_callback(req):
	pub = rospy.Publisher(topic_root + '/cognition/face/emotion', Emotion, queue_size=1)
	msg = Emotion()
	msg.emotion = req.emotion;
	pub.publish(msg)
	return {'success':True}

def topic_face_callback(data):	
	pub = rospy.Publisher(topic_root + '/cognition/face/emotion', Emotion, queue_size=1)
	msg = Emotion()
	msg.emotion = data.data;
	pub.publish(msg)
	return {'success':True}


if __name__ == '__main__':
	rospy.init_node('roboy_face')
	s_sys = rospy.Service(topic_root + '/cognition/face/emotion', ShowEmotion, face_callback)
	rospy.Subscriber(topic_root + "/cognition/face/show_emotion", String, topic_face_callback)
	print topic_root + "/cognition/face/emotion is ready"

	rospy.spin()

#!/usr/bin/python


from roboy_communication_control.msg import Emotion
from roboy_communication_control.srv import ShowEmotion
from std_msgs.msg import String

import os
import sys

import rospy

def face_callback(req):
	pub = rospy.Publisher('/roboy/cognition/face/emotion', Emotion, queue_size=10)
	msg = Emotion()
	msg.emotion = req.emotion;
	pub.publish(msg)
	return {'success':True}

def topic_face_callback(data):	
	pub = rospy.Publisher('/roboy/cognition/face/emotion', Emotion, queue_size=10)
	msg = Emotion()
	msg.emotion = data.data;
	pub.publish(msg)
	return {'success':True}


if __name__ == '__main__':
	rospy.init_node('roboy_face')
	s_sys = rospy.Service('/roboy/cognition/face/emotion', ShowEmotion, face_callback)
	rospy.Subscriber("/roboy/cognition/face/show_emotion", String, topic_face_callback)
	print "/roboy/cognition/face/emotion is ready"

	rospy.spin()
#!/usr/bin/python


from roboy_communication_control.msg import Emotion
from roboy_communication_control.srv import ShowEmotion

import os
import sys

import rospy

def face_callback(req):
	pub = rospy.Publisher('/roboy_face/emotion', Emotion, queue_size=10)
	msg = EmotionMsg()
	msg.emotion = req.emotion;
	pub.publish(msg)
	return {'success':True}

if __name__ == '__main__':
	rospy.init_node('roboy_face')
	s_sys = rospy.Service('/roboy_face/show_emotion', ShowEmotion, face_callback)
	print "/roboy_face/emotion is ready"

	rospy.spin()
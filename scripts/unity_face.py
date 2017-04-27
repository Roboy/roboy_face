#!/usr/bin/python


from roboy_unity_face.msg import EmotionMsg
from roboy_unity_face.srv import ShowEmotion

import os
import sys

import rospy

def face_callback(req):
	pub = rospy.Publisher('/roboy_unity_face/emotion', EmotionMsg, queue_size=10)
	msg = EmotionMsg()
	msg.emotion = req.emotion;
	pub.publish(msg)
	return {'success':True}

if __name__ == '__main__':
	rospy.init_node('roboy_unity_face')
	s_sys = rospy.Service('/roboy_unity_face/show_emotion', ShowEmotion, face_callback)
	print "/roboy_unity_face/emotion is ready"

	rospy.spin()
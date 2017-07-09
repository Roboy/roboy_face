#!/usr/bin/python


from roboy_communication_control.msg import Emotion
from roboy_communication_control.srv import ShowEmotion

import os
import sys

import rospy

def face_callback(req):
	pub = rospy.Publisher('/roboy/control/face/emotion', Emotion, queue_size=10)
	msg = Emotion()
	msg.emotion = req.emotion;
	pub.publish(msg)
	return {'success':True}

if __name__ == '__main__':
	rospy.init_node('roboy_face')
	s_sys = rospy.Service('/roboy/control/face/emotion', ShowEmotion, face_callback)
	print "/roboy/control/face/emotionis ready"

	rospy.spin()
#!/usr/bin/python
# -*- coding: utf-8 -*-

import tensorflow as tf

import scratch

tf.set_random_seed(seed=20)

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)  # also tf.float32 implicitly

print(node1, node2)

sess = tf.Session()

print(sess.run([node1, node2]))

print scratch.trust
print scratch.honesty
print scratch.discretion
print scratch.humor

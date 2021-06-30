import tensorflow as tf
import numpy as np

q = np.array([[1, 0, 1, 1], [0, 1, 1, 1], [1, 0, 0, 1]]).astype(np.float32)
k = np.array([[1, 1, 0, 1], [1, 0, 1, 1 ], [0, 1, 1, 0], [0, 0, 0, 1]]).astype(np.float32)
v = np.array([[0, 0], [1, 0], [1, 0], [1, 1]]).astype(np.float32)

matmul_qk = tf.matmul(q, k)

# scale matmul_qk
dk = float(k.shape[1])
scaled_attention_logits = matmul_qk / tf.sqrt(dk)

# softmax is normalized on the last axis (seq_len_k) so that the scores
# add up to 1.
attention_weights = tf.nn.softmax(scaled_attention_logits, axis=)  # (..., seq_len_q, seq_len_k)
# attention_weights * V
output = tf.matmul(attention_weights, v)  # (..., seq_len_q, depth_v)





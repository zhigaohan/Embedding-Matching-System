

import tensorflow as tf
import tensorflow_hub as hub
import logging

MODULE_URL = 'https://tfhub.dev/google/universal-sentence-encoder/2'


class EmbedUtil:

  def __init__(self):

    logging.info('Initialising embedding utility...')
    embed_module = hub.Module(MODULE_URL)
    placeholder = tf.placeholder(dtype=tf.string)
    embed = embed_module(placeholder)
    session = tf.Session()
    session.run([tf.global_variables_initializer(), tf.tables_initializer()])
    logging.info('tf.Hub module is loaded.')

    def _embeddings_fn(sentences):
      computed_embeddings = session.run(
        embed, feed_dict={placeholder: sentences})
      return computed_embeddings

    self.embedding_fn = _embeddings_fn
    logging.info('Embedding utility initialised.')

  def extract_embeddings(self, query):
    return self.embedding_fn([query])[0]





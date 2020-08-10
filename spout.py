from heronpy.api.spout.spout import Spout
from heronpy.api.stream import Stream 
from time import sleep
from random import choice

class TestWordSpout(Spout): 
  words = ('nathan', 'mike', 'jackson', 'golda', 'bertels')
  outputs = ( 
    Stream(fields=('field1',), name='stream1'),
    Stream(fields=('field2', 'field3'), name='stream2')
  )

  def next_tuple(self): 
    sleep(5) 
    word1 = choice(self.words) 
    word2 = choice(self.words)
    word3 = choice(self.words)
    self.log('next_tuple stream1 ' + word1) 
    self.emit(tup=(word1,), stream="stream1")
    self.log('next_tuple stream2 ' + word2 + ' ' + word3)
    self.emit(tup=(word2, word3), stream="stream2")
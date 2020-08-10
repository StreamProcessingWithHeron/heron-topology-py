from heronpy.api.bolt.bolt import Bolt 

class ExclamationBolt(Bolt): 
  outputs = ['word'] 
  def process(self, tup): 
    if tup.stream == 'stream2':
      word = tup.values[0]+'&'+tup.values[1]+'!!!' 
      self.emit((word,)) 
    else:
      word = tup.values[0] + '!!!'
      self.emit((word,))
    self.log('process ' + word)
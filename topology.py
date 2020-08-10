from heronpy.api.stream import Grouping
from heronpy.api.topology import TopologyBuilder 

from spout import TestWordSpout
from bolt import ExclamationBolt

if __name__ == '__main__':
  builder = TopologyBuilder('my-python-topology') 
  word = builder.add_spout('word', TestWordSpout, par=2) 
  exclaim1 = builder.add_bolt('exclaim1', \
    ExclamationBolt, par=2, \
    inputs={word['stream1']: Grouping.SHUFFLE, \
            word['stream2']: Grouping.SHUFFLE}) 
  exclaim2 = builder.add_bolt('exclaim2', \
    ExclamationBolt, par=2, \
    inputs={exclaim1: Grouping.SHUFFLE})
  builder.build_and_submit() 
import random
from datetime import datetime

'''
Algorithm to approximately count 
Space Complexity O(log log n)

https://en.wikipedia.org/wiki/Approximate_counting_algorithm
https://www.inf.ed.ac.uk/teaching/courses/exc/reading/morris.pdf (Original Paper)
http://algo.inria.fr/flajolet/Publications/Flajolet85c.pdf (Follow Up with Proof)

Proof -
http://gregorygundersen.com/blog/2019/11/11/morris-algorithm/ (Blog) 
http://people.seas.harvard.edu/~minilek/cs229r/fall15/lec/lec1.pdf (Harvard Course)
https://www.youtube.com/watch?v=s9xSfIw83tk&index=1&list=PL2SOU6wwxB0v1kQTpqpuu5kEJo2i-iUyf (Harvard Course)
'''


class MorrisAlgorithm:

    def __init__(self, seed: float = datetime.now().timestamp()) -> None:
        self.counter = 0
        self.random = random.Random(seed)

    def increment(self) -> None:
        p = pow(2 ** self.counter, -1)
        r = self.random.uniform(0, 1)
        if p > r:
            self.counter += 1

    def approx_count(self) -> int:
        return 2 ** self.counter - 1

"""
Flight Leg:
NEP -> QAT -> USA
2 segments (NEP -> QAT, QAT -> USA)

@propery make the method to attribute of class. 

"""

from typing import List



class Segment:
    def __init__(self,departure,destination):
        self.departure = departure
        self.destination = destination

class Flight:
    def __init__(self,segments:List[Segment]):
        self.segments = segments


    

    def __repr__(self):
        stops = [self.segments[0].departure,self.segments[0].destination]


        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return ' -> '.join(stops)

        
    @property
    def departure_point(self) -> str:
        return self.segments[0].departure

    @departure_point.setter                         # to change the departure point
    def departure_point(self,val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val,destination=dest)





flight = Flight(Segment('NEP','QAT'))
print(flight.departure_point)

#to change 
flight.departure_point = 'IND'
print(flight.departure_point)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # make two stacks, for each type with the idx of when they show up, if it wins move to end with + size of the original string

        if senate == "D":
            return "Dire"
        elif senate == "R":
            return "Radiant"

        og_len = len(senate)
        
        radiant_spots = []
        dire_spots = []

        for idx, person in enumerate(senate):
            if person == 'R':
                radiant_spots.append(idx)
            else:
                dire_spots.append(idx)

        while (True):
            if len(radiant_spots) == 0 or len(dire_spots) == 0:
                break
            elif radiant_spots[0] < dire_spots[0]:
                radiant_spots.append(radiant_spots[0]+og_len)
                radiant_spots.pop(0)
                dire_spots.pop(0)
            else:
                dire_spots.append(dire_spots[0]+og_len)
                dire_spots.pop(0)
                radiant_spots.pop(0)     
        
        if len(radiant_spots) != 0:
            return "Radiant"
        else:
            return "Dire"
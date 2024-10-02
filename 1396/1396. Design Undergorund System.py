class UndergroundSystem:

    def __init__(self):
        self.travel_times = {}
        self.checked_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checked_in[id][0]
        startTime = self.checked_in[id][1]
        travel = (startStation, stationName)
        travel_time = t - startTime

        del self.checked_in[id]

        if travel in self.travel_times:
            time_travelled =  self.travel_times[travel][0] + travel_time
            trips = self.travel_times[travel][1] + 1
            self.travel_times[travel] = [time_travelled, trips]
        else:
            self.travel_times[travel] = [travel_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_travelled = self.travel_times[(startStation, endStation)][0]
        trips = self.travel_times[(startStation, endStation)][1]
        return time_travelled / trips

def main():
    underground = None

    while True:
        user_input = input("What would you like to do: \"initialize\", \"check-in\", \"check-out\", \"get average time\" or \"quit\"? ").strip()

        if user_input == "quit":
            break

        if user_input == "initialize":
            underground = UndergroundSystem()
            print("Initialized the underground system!")

        elif user_input == "check-in":
            id = int(input("Traveller ID? "))
            station = input("Boarding Station Name: ")
            time = int(input("Current time? "))

            underground.checkIn(id, station, time)
            print(f"You are person {id} who boarded from station {station} at {time}")

        elif user_input == "check-out":
            id = int(input("Traveller ID? "))
            station = input("Departing Station Name: ")
            time = int(input("Current time? "))

            underground.checkOut(id, station, time)
            print(f"You are person {id} who departed from station {station} at {time}")

        elif user_input == "get average time":
            start = input("Boarding Station Name: ")
            end = input("Departing Station Name: ")

            avg = underground.getAverageTime(start, end)
            print(f"The averge time it takes to get from {start} to {end} is: {avg}")
        
        else:
            print("Invalid command or robot not initialized. Please try again.")

if __name__ == "__main__":
    main()
class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def upade_valid_time(self) -> None:
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

    def next_second(self) -> str:
        self.seconds += 1

        self.upade_valid_time()

        return self.get_time()


"""
Author: Olivia Bakke
Starting Date: Feb, 24, 2026

Contraption definitions for Cats vs Homework
"""

from src.managers import GameManager, Actor, Tile
from src.cats import Cat


class Contraption(Actor):
    """
    Base class that represents all contraptions
    """

    _cost: int
    """
    Cost (in batteries) to place this contraption
    """

    def __init__(self, image_name: str, cost: int):
        """
        Initializes this contraption with a positive cost
        """
        super().__init__(image_name)
        assert isinstance(cost, int) and cost >= 0
        self._cost = cost

    def cost(self) -> int:
        """
        Returns the cost in batteries for this contraption
        """
        return self._cost

    def place(self, tile: 'Tile'):
        """
        Places this contraption on the board
        """
        assert isinstance(tile, Tile)

        GameManager.manager().add_contraption(self)
        self.teleport(tile)

    def end_round(self):
        """
        Takes some action as a contraption
        By default, a contraption does nothing at the end of the round
        """
        pass

    def interact(self):
        """
        A cat interacts with this contraption
        Any interaction immediately knocks the base contraption over
          and removes it from the board
        """
        self.tile().clear_actor()
        self._tile = None
        GameManager.manager().remove_contraption(self)


class LaserPointer(Contraption):
    """
    Each round, points a laser to attempt to distract the first cat in its lane
    """

    def __init__(self):
        """
        The constructor for a LaserPointer
        Laser pointers have an image name 'laser' and cost 7 batteries
        """
        super().__init__('laser', 7)

    def end_round(self):
        """
        A laser pointer distracts the first cat in its lane
        """
        next = self._tile.entrance()
        while next is not None:
            if isinstance(next.actor(), Cat):
                next.actor().distract(1)
                return  # we can simply return when we find a cat
            next = next.entrance()

# Part 1: "Basic Contraptions"


class SnackDispenser(Contraption):
    """
    A Snack dispenser does nothing by itself, but can be interacted with
      a total of 5 times before being knocked over
    """

    _uses: int

    def __init__(self):
        """
        The constructor for a SnackDispenser
        Snack dispensers have an image name of 'snacks' and cost 4 batteries
        """
        # TODO: Implement me!
        super().__init__('snacks', 4)
        self._uses = 5

    # TODO: potentially override more methods of Contraption

    def interact(self):
        self._uses -= 1
        if self._uses == 0:
            self.tile().clear_actor()
            self._tile = None
            GameManager.manager().remove_contraption(self)
            self._uses = 5


class BatteryCharger(Contraption):
    """
    Every other round, charges a new battery
    Does not charge a battery the round it is placed
    """
    _ready: bool

    def __init__(self):
        """
        The constructor for a BatteryCharger
        Battery chargers have an image name 'charger' and cost 3 batteries
        """
        # TODO: Implement me!
        super().__init__('charger', 3)
        self._ready = False

    # TODO: potentially override more methods of Contraption
    def end_round(self):
        if self._ready == True:
            GameManager.manager()._batteries += 1
        self._ready = not self._ready

class BallThrower(Contraption):
    """
    Each round, throws a ball to distract the nearest Cat within 3 spaces
    If there is no such Cat, this contraption does nothing
    """

    def __init__(self):
        """
        The constructor for a BallThrower
        Ball throwers have an image name 'thrower' and cost 3 batteries
        """
        # TODO: Implement me!
        super().__init__('thrower', 3)

    # TODO: potentially override more methods of Contraption
    def end_round(self):
        next = self._tile.entrance()
        count = 3
        while count > 0 and next is not None:
            if isinstance(next.actor(), Cat):
                next.actor().distract(1)
                return  # we can simply return when we find a cat
            next = next.entrance()
            count -= 1

# Part 3: "Advanced Contraptions"
# We recommend adding more Cats before implementing these contraptions


class TripleLaserPointer(Contraption):
    """
    Each round, points a laser to attempt to distract the first cat in its lane
      _and_ a cat in both the lane above and below this contraption
    """

    def __init__(self):
        """
        The constructor for a TripleLaserPointer
        Triple laser pointers have an image name 'triple_laser' and cost 12 batteries
        """
        # TODO: Implement me!
        super().__init__('triple_laser', 12)

    # TODO: potentially override more methods of Contraption
    def end_round(self):
        """
        A laser pointer distracts the first cat in its lane
        """
        next = self._tile.entrance()
        while next is not None:
            if isinstance(next.actor(), Cat):
                next.actor().distract(1)
                break  # we can simply return when we find a cat
            next = next.entrance()

        if self.tile().above() is not None:
            above = self._tile.above().entrance()
            while above is not None:
                if isinstance(above.actor(), Cat):
                    above.actor().distract(1)
                    break  # we can simply return when we find a cat
                above = above.entrance()

        if self.tile().below() is not None:
            below = self._tile.below().entrance()
            while below is not None:
                if isinstance(below.actor(), Cat):
                    below.actor().distract(1)
                    break  # we can simply return when we find a cat
                below = below.entrance()


class ColorfulBallThrower(Contraption):
    """
    Each round, throws a ball to distract the nearest Cat within 3 spaces
    If there is no such Cat, adds a colorful ball to the furthest empty space
      within the 3-space range of this colorful ball thrower
    """

    def __init__(self):
        """
        The constructor for a ColorfulBallThrower
        Colorful ball throwers have an image name 'colorful_thrower' and cost 5 batteries
        """
        # TODO: Implement me!
        super().__init__('colorful_thrower', 5)

    # TODO: potentially override more methods of Contraption and/or update Cat
    # Note that you are permitted to change this to be a child class of BallThrower
    #   though this may or may not be easier than just keeping this directly inheriting from Contraption

    # Hint: consider creating a new Actor class to represent the colorful ball that gets placed
    # Note that a colorful ball has the image name colorful_ball
    # Specifically note the set_actor and clear_actor methods in Tile

    def end_round(self):
        next = self._tile.entrance()
        count = 3
        while count > 0 and next is not None:
            current = next
            if isinstance(next.actor(), Cat):
                next.actor().distract(1)
                return  # we can simply return when we find a cat
            next = next.entrance()
            count -= 1

        second = current.exit()
        third = current.exit()

        if current.is_empty():
            current.set_actor(Ball())
        elif second.is_empty():
            second.set_actor(Ball())
        elif third.is_empty():
            third.set_actor(Ball())

class Ball(Actor):
    def __init__(self):
        super().__init__('colorful_ball')

    def interact(self):
        if self._tile is not None:
            self._tile.remove_from_board()


class SpaceHeater(Contraption):
    """
    This Contraption, by itself, does nothing
    However, any cat that ends a move within a range of two of this Contraption
      is distracted for exactly one point
    """

    def __init__(self):
        """
        The constructor for a SpaceHeater
        Space heaters have an image name 'heater' and cost 4 batteries
        """
        # TODO: Implement me!
        super().__init__('heater', 4)

    # TODO: potentially update Cat to work with the space heater
    # Note that the space heater does not distract the cat during its action...

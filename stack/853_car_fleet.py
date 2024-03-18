class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        """
        There are n cars going to the same destination along a one-lane road. The destination is target miles away.
        You are given two integer array position and speed, both of length n,
        where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

        A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
        The faster car will slow down to match the slower car's speed.
        The distance between these two cars is ignored (i.e., they are assumed to have the same position).

        A car fleet is some non-empty set of cars driving at the same position and same speed.
        Note that a single car is also a car fleet.
        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
        Return the number of car fleets that will arrive at the destination.
        :param target:
        :param position:
        :param speed:
        :return:
        """
        n = len(speed)
        if n == 1:
            return 1
        damn_it = sorted(zip(position, speed), key=lambda x: x[0])
        stack = []
        while len(damn_it) != 0:
            current_pos, current_speed = damn_it.pop()
            curr_time_to_target = (target - current_pos) / current_speed
            if len(stack) == 0:
                stack.append((current_pos, current_speed))
                print(f"1) stack = {stack}")
                continue

            stack_pos, stack_speed = stack[-1]
            stack_time_to_target = (target - stack_pos) / stack_speed
            if curr_time_to_target > stack_time_to_target:
                stack.append((current_pos, current_speed))
        return len(stack)


def some_test():
    a = Solution()
    target = 16
    speed = [2, 2, 6, 7]
    position = [11, 14, 13, 6]

    print(f"original = {list(zip(position, speed))}")
    print(f"original_sorted = {sorted(zip(position, speed), key=lambda x: x[0])}")
    print(f"target = {target}")
    print(
        a.carFleet(target, position, speed)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    some_test()

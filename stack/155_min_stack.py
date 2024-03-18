class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    You must implement a solution with O(1) time complexity for each function

    To Implement this, my Idea is to create a dict of {index :stack}
    where at each stack the minimum is the first item that was pushed to that stack.
    If we push a new value that is less than the minimum, we create a new stack where it is the minimum.
    This will cause the following:

                  12,
    dict =        11,     10,
                  10,      9,     8

    min_val =     10,      9,      8

    this way the minimum is always at the buttom of the latest stack
    """

    def __init__(self):
        """
        MinStack() initializes the stack object.
        """
        self.min_val = 0
        self.bucket_num = 0
        self.bucket_stack = {self.bucket_num: []}
        self.bucket_min_val = {self.bucket_num: self.min_val}

    def __str__(self):
        return (f"[* min_val = {self.min_val} "
                f"| bucket_num = {self.bucket_num} | "
                f"bucket_stack ={self.bucket_stack} | "
                f" bucket_min_val = {self.bucket_min_val}*]")

    def push(self, val: int):
        """
        void push(int val) pushes the element val onto the stack.
        :param val:
        :return:
        """
        if len(self.bucket_stack) == 0:
            self.bucket_stack[0] = []
        if len(self.bucket_stack[0]) == 0:
            # if the stack bucket is empty -> fill the first stack with the value
            # update the list that keeps track of minimal value in each stack with the minimum
            self.bucket_min_val[0] = val
            self.min_val = val
            self.bucket_stack[0] = [val]
            return

        if self.bucket_min_val[self.bucket_num] <= val:
            # If the stack bucket is not empty BUT the new value is larger than the latest buckets minimum,
            # push the value in to the latest bucket
            self.bucket_stack[self.bucket_num].append(val)
        else:
            # However, if the new value is smaller than the minimum in the latest bucket:
            # open a new bucket with this value ( make it the latest)
            # update the minimal value in this bucket as the value
            self.bucket_num += 1
            self.bucket_stack[self.bucket_num] = [val]
            self.bucket_min_val[self.bucket_num] = val

    def pop(self):
        """
        removes the element on the top of the stack.
        :return:
        """
        self.bucket_stack[self.bucket_num].pop()
        if len(self.bucket_stack[self.bucket_num]) == 0:
            self.bucket_stack.pop(self.bucket_num)
            self.bucket_min_val.pop(self.bucket_num)
            self.bucket_num = max(0, self.bucket_num - 1)

    def top(self) -> int:
        """
        gets the top element of the stack.
        :return:
        """
        return self.bucket_stack[self.bucket_num][-1]

    def getMin(self) -> int:
        """
        retrieves the minimum element in the stack.
        :return:
        """
        # this is kind of cheating because at worse case this will be O(n)
        return self.bucket_stack[self.bucket_num][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def some_test():
    input_funcs = ["push","push","push","getMin","pop","top","getMin"]
    input_values = [[-2],[0],[-3],[],[],[],[]]
    results = []
    stack = MinStack()
    for i in range(len(input_funcs)):
        results.append(func_wrapper(stack, input_funcs[i], input_values[i]))
        print(f"{i}) after {input_funcs[i]} with input {input_values[i]}")
        print(f"{i}) stack is {stack}")
    print(results)


def func_wrapper(stack: MinStack, func_name, value):
    match func_name:
        case "MinStack":
            return MinStack()
        case "push":
            return stack.push(value[0])
        case "top":
            return stack.top()
        case "pop":
            return stack.pop()
        case "getMin":
            return stack.getMin()

        # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    some_test()

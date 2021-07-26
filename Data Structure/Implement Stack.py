# First in last out
# Last in first out

class Stack:
      def __init__(self):
            self.items = []

      def is_Empty(self):
            return self.items == []

      def push(self, element):
            self.items.append(element)
      
      def pop(self):
            self.items.pop()
      
      def peek(self):
            return self.items[-1]

if __name__ == "__main__":
      stack1 = Stack()
      print(stack1.is_Empty())

      stack1.push(1)
      stack1.push(2)
      stack1.push(5)
      stack1.pop()
      stack1.push(3)
      print(stack1.peek())
      print(stack1.items)
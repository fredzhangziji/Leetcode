class Queue:
      def __init__(self):
            self.items = []
      
      def is_Empty(self):
            return self.items == []

      def push(self, element):
            self.items.append(element)

      def pop(self):
            self.items.pop(0)

      def peek(self):
            return self.items[-1]

if __name__ == "__main__":
      queue1 = Queue()
      print(queue1.is_Empty())
      queue1.push(5)
      queue1.push(3)
      queue1.push(1)
      queue1.pop()
      queue1.push(0)
      print(queue1.peek())
      print(queue1.items) 
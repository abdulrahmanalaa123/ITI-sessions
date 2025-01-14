class QueueOutOfRangeException(Exception):
    pass

class queue:
    def __init__(self):
        self.__list = []
    #def __init__(self,elements):
    #    # creating a new list to elminiate referencing to the original list
    #    self.__list = [*elements]

    def insert(self,element):
        self.__list.append(element)

    def __str__(self):
        return f"{self.__list}"

    def __len__(self):
        return len(self.__list)


    def create_from_string(inputStr):
        strList = inputStr.strip('[]') 
        retQueue = queue()
        for elem in strList:
            if elem.isdigit():
                retQueue.insert(int(elem))
            else:
                retQueue.insert(elem)
        return retQueue

    def pop(self):
        if self.is_empty(): 
            print("no elements to pop :D")
            return None

        popped = self.__list[0]
        self.__list = self.__list[1:]
        return popped

    def is_empty(self):
        if len(self):
            return False
        else:
            return True

class queueMaster(queue):
    __queueList = []

    def __init__(self,name,size):
        super().__init__()
        self.name = name
        self.size = size
        queueMaster.__queueList.append(self)

    

    def insert(self, element):
        if(len(self) < self.size):
            super().insert(element)
        else:
            raise QueueOutOfRangeException("queue is full sorry")

        
    def get_queue(name):
        for queue in queueMaster.__queueList:
                if name in queue.name:
                    return queue
        return None
    
    def save():
       with open('queues.txt','w') as file:
            file.write(f"{list(map(lambda x: str(x),queueMaster.__queueList))}")
    def load():
        with open('queues.txt','r') as file:
            stringList = file.read()
            queueMaster.__queueList = map()

if __name__ == "__main__":
    myqueue = queue()
    myqueue.insert(3)
    myqueue.insert(4)
    myqueue.insert(5)
    myqueue.insert(6)
    myqueue.insert(7)
    print(myqueue.pop())
    print(myqueue.pop())
    print(myqueue.pop())
    print(myqueue.pop())
    print(myqueue)

    queue1 = queueMaster("Mine",3)
    queue2 = queueMaster("Nice",2)
    queue3 = queueMaster("Nice",2)
    queue4 = queueMaster("Mohamed",2)
    #print(queueMaster)
    queue1.insert(1)
    queue1.insert(2)
    queue1.insert(3)
    queue4.insert(2)
    queue4.insert(3)
    try:
        queue1.insert(1)
    except Exception as e:
        print(e)
    print("queue2",queueMaster.get_queue("Mohamed"))
    print(queue1)
    queueMaster.save()
    #queueMaster.load()
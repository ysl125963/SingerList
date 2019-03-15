class Element:
    def __init__(self, item):
        # 定义元素特征, 有数据和指标
        self.head = item
        self.next = None


class SingleList(object):
    """
    生成一个单向链表, 具有类似list的方法
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, item):
        # 在链表开头添加元素
        node = Element(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        # 在链表末尾添加元素
        node = Element(item)
        if self.is_empty():
            self.add_first(item)
        else:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            cursor.next = node

    def insert(self, index, item):
        # 按给定索引插入元素
        node = Element(item)
        count = 0
        cursor = self.head
        while cursor is not None:
            count += 1
            if count == index:
                node.next = cursor.next
                cursor.next = node
                break
            cursor = cursor.next

    def pop(self):
        # 弹出最后一个元素
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        else:
            return cursor

    def travel(self):
        # 遍历链表, 返回生成器
        cursor = self.head
        while cursor is not None:
            yield cursor.head
            cursor = cursor.next

    def len(self):
        cursor = self.head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    def remove(self, item):
        chain = [i for i in self.travel()]
        if item in chain:   # 判断item是否在单向链中
            cursor = self.head
            if cursor.head == item:
                self.head = cursor.next
            else:
                while cursor.next.head != item:
                    cursor = cursor.next
                else:
                    cursor.next = cursor.next.next
        else:
            print('单向链中不存在{}'.format(item))


if __name__ == '__main__':
    test = SingleList()
    


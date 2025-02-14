#链表初始化
class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

#移除链表元素，删除链表中等于给定值 val 的所有节点。
#使用虚拟头节点，遍历链表，删除等于val的节点
def removeElements(head:ListNode,val:int) -> ListNode:
    dummy_head=ListNode(val=0,next=head)#虚拟头节点

    #遍历链表
    cur=dummy_head
    while cur.next:
        if cur.next.val==val:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return dummy_head.next

#给我一个例子
def example():
    head=ListNode(1)#通常这点可以用dummy_head代替
    '''
    dummy_hea=ListNode(0)
    '''
    values=[2,6,3,4,5,6]
    for value in values:
        head.next = ListNode(value)
        head = head.next
    val=6
    res=removeElements(head,val)
    while res:
        print(res.val)
        res=res.next

example()


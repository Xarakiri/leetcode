class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = Node(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        next_page = Node(url)

        self.head.next = next_page
        next_page.prev = self.head

        self.head = self.head.next

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.head.prev:
            steps -= 1
            self.head = self.head.prev
        return self.head.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.head.next:
            steps -= 1
            self.head = self.head.next
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
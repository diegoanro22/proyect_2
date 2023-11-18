class Tips():
    def __init__(self, tip):
        """
         Initialize the object with a tip. This is called by __init__ and should not be called directly
         
         @param tip - The tip to use
        """
        self.tips= tip

    def getTip(self):
        """
         Returns the tip of the object. This is used to determine where the object is in the tree when displaying the tree.
         
         
         @return a string or None if there is no tip to display ( for example if the object is a tree
        """
        return self.tip
    
    def setTip(self, tip):
        """
         Set the tip of the widget. This is used to display the tooltip when the widget is clicked.
         
         @param tip - The tip to display in the widget ( string
        """
        self.tip = tip
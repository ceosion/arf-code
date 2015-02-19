'''
Created on Feb 19, 2015

@author: arf1855
'''

import Tkinter as tk

class DialogPrompt(tk.Frame):
    '''
    classdocs
    '''

    def __init__(self, master=None):
        '''
        Constructor
        '''
        self.root = tk.Tk()
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.label = tk.Label(self, text='Enter encryption password:')
        self.label.grid()
        self.passwordField = tk.Entry(self, show='*')
        self.passwordField.grid()
        self.passwordField.bind(sequence='<Return>', func=self.fin)
        self.enterButton = tk.Button(self, text='Enter', command=self.fin)
        self.enterButton.grid()
        
    def fin(self, event=tk.Event):
        #print 'User entered the following: ' + self.getValue()
        self.passwordValue = self.passwordField.get()
        self.root.destroy()
        self.root.quit()
        
    def getValue(self):
        return self.passwordValue

'''
Sample code for how to use this Class. If ran directly from this module,
it will produce the most common configuration of this dialog prompt.
'''
#app = DialogPrompt()
#app.master.title('Sample App')
#app.mainloop()
        
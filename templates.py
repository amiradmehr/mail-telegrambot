from helper import progressBar


class Templates:


        def __init__(self,num):
            self.num = num
            

        def get(self, prof=' ', topic=' ', paper=' ', arb1=' ', arb2=' ', arb3=' '):
                self.temp1 = f'''

hello {prof}
this is {topic}
this is {paper}
'''
                self.temp2 = f'''

Hello {prof}
                
                '''

                temps = [self.temp1, self.temp2]

                if self.num > len(temps) or self.num ==0 or self.num == None:
                    return ' '
                else:
                    return temps[self.num-1]


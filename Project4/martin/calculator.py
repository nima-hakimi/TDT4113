import numbers
import numpy
import re
from container import Stack, Queue
from Function import Function, Operator

class Calculator:
    def __init__(self):
        self.functions = {"EXP": Function(numpy.exp),
                          "LOG": Function(numpy.log),
                          "SIN": Function(numpy.sin),
                          "COS": Function(numpy.cos),
                          "SQRT": Function(numpy.sqrt)}
        self.operators = {"PLUSS": Operator(numpy.add, 0),
                          "GANGE": Operator(numpy.multiply, 1),
                          "DELE": Operator(numpy.divide, 1),
                          "MINUS": Operator(numpy.subtract, 0)}
        self.output_queue = Queue() # kø for RPN, trenger en stack for mellomlagring

    def calculate(self):
        tempStack = Stack() # midlertidig stack for mellomlagring
        for i in range(self.output_queue.size()):
            element = self.output_queue.pop()
            if isinstance(element, numbers.Number):
                tempStack.push(element)
            elif isinstance(element, Function):
                tempNumber = element.execute(tempStack.pop())
                tempStack.push(tempNumber)  # Bruker funksjonen på øverse element i stacken
            elif isinstance(element, Operator):  # husk å utføre i "feil rekkefølge"
                n1 = tempStack.pop()
                n2 = tempStack.pop()
                tempNumber = element.execute(n2, n1)
                tempStack.push(tempNumber)
            else:
                print("something is very wrong with your RPN-queue")
                break
        if not (tempStack.size() == 1 and self.output_queue.size() == 0):  #DEBUG
            print("Her bør du sjekke litt mer, stack skal ha ett element, kø skal ha 0") # print len(..) hvis..
        return tempStack.pop()

    def outputQueueMaker(self, elements):  # shunting-yard algorithm
        operatorStack = Stack()
        outputQueue = Queue() # bruk self.output_queue?
        for element in elements:  # Emm GÅR DETTE????????????????????????????????? Gjøre om til pop? -> Gitt kø
            # element = elements.pop() # for i in range(elements.size()):
            if isinstance(element, numbers.Number):
                outputQueue.push(element)
            elif isinstance(element, Function):
                operatorStack.push(element)
            elif element == "(":
                operatorStack.push(element)
            elif element == ")":
                while(operatorStack.peek() != "(" and operatorStack.size() != 0):
                    operator = operatorStack.pop()
                    outputQueue.push(operator)
                    #print("THIS is it")
                operatorStack.pop()  # Vi kaster "(", og gjør ingenting med ")"
            elif isinstance(element, Operator):  # Det er muligens denne som feiler?
                while(operatorStack.size() != 0):
                    if isinstance(operatorStack.peek(), Operator):
                        if operatorStack.peek().strength < element.strength:
                            break  # Stopp hvis styrken er mindre
                    if operatorStack.peek() == "(" or operatorStack.peek() == ")":
                        break
                    temp = operatorStack.pop()
                    outputQueue.push(temp)
                operatorStack.push(element)
            else:
                print("something is very wrong with your RPN-queue")
                break
        for i in range(operatorStack.size()):
            temp = operatorStack.pop()
            outputQueue.push(temp)

        self.output_queue = outputQueue

    def text_parser(self, text):
        returnList = []
        text = text.replace(" ", "").upper()
        functions = "|".join(["^" + func for func in self.functions.keys()])
        operators = "|".join(["^" + func for func in self.operators.keys()])
        parenthesis = "^[()]"
        nums = "^[-1234567890]+"

        """check = re.search(nums, text)
        print("funksjonsjekk:", check != None)
        print(type(check.__getitem__(0)))
        print(len(check.__getitem__(0)))"""

        while text != "":
            check = re.search(nums, text) # Sjekker om det er nummer
            if check != None:
                #print("item:", check.__getitem__(0), ", type:", type(check.__getitem__(0)))
                returnList.append(float(check.__getitem__(0))) # Gjør om tall til float
                text = text[len(check.__getitem__(0))::]
                continue

            check = re.search(parenthesis, text)  # Sjekker om det er parantes
            if check != None:
                returnList.append(check.__getitem__(0))  # Lar parantes forbli str
                text = text[1::]
                continue

            check = re.search(operators, text)  # Sjekker om det er operator
            if check != None:
                returnList.append(self.operators[check.__getitem__(0)])  # eks: append(self.operators["GANGE"])
                text = text[len(check.__getitem__(0))::]
                continue

            check = re.search(functions, text)  # Sjekker om det er function
            if check != None:
                returnList.append(self.functions[check.__getitem__(0)])  # eks: append(self.function["EXP"])
                text = text[len(check.__getitem__(0))::]
                continue


        return returnList

            #check = re.search(functions, text)
            #print("funksjonsjekk:", check != None)
            #print(check.__getitem__(0))
            #check = re.search(operators, text)
            #print("operatorsjekk:", check != None)
            #check = re.search(parenthesis, text)
            #print(check)
            #print(check.__getitem__(0))
            #print("parantessjekk:", check != None)"""



    def tester(self):
        for i in range(self.output_queue.size()):
            if isinstance(self.output_queue.peek(), Function):
                print(self.output_queue.pop().execute(2), "-> funksjon")
            elif isinstance(self.output_queue.peek(), Operator):
                print(self.output_queue.pop().execute(5, 5), "-> Operator")
            else:
                print(self.output_queue.pop())







"""calc = Calculator()
a = calc.text_parser("exp(-432 GANGE (3 PLUSS 1))")
for i in a:
    print(i)
#calc.text_parser("EXP(1)")
#calc.text_parser("(3-2)*2")"""


#DET FUNKER! NÅ BARE VÆR OBS PÅ for element in elements
"""calc = Calculator()
t1 = calc.functions["EXP"]
t2 = calc.operators["PLUSS"]
t3 = calc.operators["GANGE"]
#testliste = [t1, "(", 1, t2, 2, t3, 3, ")"]
testliste = [2, calc.operators["GANGE"], 3, calc.operators["PLUSS"], 1]
calc.outputQueueMaker(testliste)
print("")
calc.tester()"""




#print(calc.functions["EXP"].execute(calc.operators["PLUSS"].execute(1, calc.operators["GANGE"].execute(2, 3))))
"""calc = Calculator()
calc.output_queue.push(1)
calc.output_queue.push(2)
calc.output_queue.push(3)
calc.output_queue.push(calc.operators["GANGE"])
calc.output_queue.push(calc.operators["PLUSS"])
calc.output_queue.push(calc.functions["EXP"])
print(calc.calculate())"""







#Dette er for å teste importering:
'''test = Stack()
test.push(1)
test.push(2)
print(test.pop())
print(test.size())'''

"""add_op = Operator(numpy.add, 0)
multiply_op = Operator(numpy.multiply, 1)
print(add_op.execute(1, multiply_op.execute(2, 3)))"""



"""
Prosedyre:
- Ta inn streng
- gjøre strengen til en liste med .split()
- oversette til rpn

- iterere gjennom lista:
    - legge tall, altså type(i)==int, til i en stack (objekt)
    - hvis det er en funksjon (exp)
"""
from math import sqrt

class Location:
    def __init__(self,x,y,theta):
        self.x = x
        self.y = y
        self.theta = theta

    def copy(self):
        return Location(self.x,self.y,self.theta)     
        
    def __eq__(self,other):
        return all([self.x == other.x, self.y == other.y, self.theta == other.theta])
        
    def compareMagnitude(self,reference,tolerance):
        mag = sqrt((self.x - reference.x)**2 + (self.y - reference.y)**2)
        print mag, tolerance
        return mag < tolerance
        
    def compareAngle(self,reference,tolerance):
        if tolerance < 0:
            return (self.theta - reference.theta) < tolerance
        elif tolerance > 0:
            return (self.theta - reference.theta) > tolerance
            
        

class Task:
    def __init__(self,name,priority,location,action):
        self.name = name
        self.priority = priority
        self.isActive = False
        self.location = location
        self.action = action

    def copy(self):
        task = Task(self.name,self.priority,self.location.copy(),self.action)
        if self.isActive:
            task.activate()
        return task
        
    def getKey(self):
        return self.priority * self.isActive
        
    def activate(self):
        self.isActive = True

    def deactivate(self):
        self.isActive = False
        
    def getLocation(self):
        return self.location
        
    def getAction(self):
        return self.action
        
    def getPriority(self):
        return self.priority

    def __cmp__(self,other):
        if hasattr(other,'getKey'):
            return self.getKey().__cmp__(other.getKey())
            
    def __eq__(self,other):
        return all([self.name == other.name, self.priority == other.priority, self.isActive == other.isActive, self.location == other.location, self.action == other.action])
        
class TaskFactory:
    def __init__(self, taskList):
        self.tasks = taskList
        self.currentTask = None    

    def addTask(self,newTask):
        self.tasks.append(newTask)
        
    def activateTask(self,name):
        for task in self.tasks:
            if task.name == name:
                task.activate()
                return
        print 'task with name \'' + name + '\' not found'
        print [task.name for task in self.tasks]
            

    def deactivateTask(self,name):
        for task in self.tasks:
            if task.name == name:
                task.deactivate()    
    
    def getNextTask(self):
        tasks = sorted([task for task in self.tasks if task.getKey() != 0])
        if len(tasks) != 0:
            self.currentTask = tasks[0]
            return self.currentTask
        else: 
            print 'No tasks found!'
            return None
            
    def getActiveTasks(self):
        return [task for task in self.tasks if task.getKey() != 0]
    
    def getAllTasks(self):
        return self.tasks        
        
    def getCurrentTask(self):
        return self.currentTask
        

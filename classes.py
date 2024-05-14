import json
import psycopg2
from abc import ABC, abstractmethod
from config import user, password, host, port, database

connection = psycopg2.connect(user=user,
                              password=password,  # пароль, который указали при установке PostgreSQL
                              host=host,
                              port=port,
                              database=database)

cursor = connection.cursor()


class Computer:
    """Класс выходного объекта компьютера"""
    def __init__(self, components: list) -> None:
        self.__components = components

    def checkCompatibility() -> bool:  # функция проверки компонент на совместимость
        pass
    
    def getInfo() -> json:  # функция вывода информации о компоненте
        pass

class ComputerBuilder(ABC):
    """Класс интерфейс строителя ПК"""

    @property
    @abstractmethod
    def buildOS(self, OS) -> None:
        pass

    @abstractmethod
    def buildPowerSupply(self, PowerSupply) -> None:
        pass

    @abstractmethod
    def buildSSD(self, SSD) -> None:
        pass
 
    @abstractmethod
    def buildCPUCooler(self, CPUCooler) -> None:
        pass

    @abstractmethod
    def buildCase(self, Case) -> None:
        pass

    @abstractmethod
    def buildCPU(self, CPU) -> None:
        pass

    @abstractmethod
    def buildGPU(self, GPU) -> None:
        pass
    
    @abstractmethod
    def buildMotherBoard(self, MotherBoard) -> None:
        pass

    @abstractmethod
    def buildRAM(self, RAM) -> None:
        pass

    @abstractmethod
    def getResult() -> Computer:
        pass

class ComputerAssembler:
    """Класс фабрики строителей(директор)"""
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def computerAssembler(builder) -> Computer:
        pass

    def changeBuiler(builder) -> Computer:
        pass
    
class Client:
    """Класс клиент"""
    def __init__(self, build, assembler: ComputerAssembler):
        self.build = build
        self.assembler = assembler

class ConcreteComputerBuilder2(ComputerBuilder):
    """Класс конкретный строитель ПК с реализацией шагов"""
    def __init__(self, computer: Computer):
        self.__computer = computer

    def buildOS(self, OS) -> None:
        pass

    def buildPowerSupply(self, PowerSupply) -> None:
        pass

    def buildSSD(self, SSD) -> None:
        pass

    def buildCPUCooler(self, CPUCooler) -> None:
        pass

    def buildCase(self, Case) -> None:
        pass

    def buildCPU(self, CPU) -> None:
        pass

    def buildGPU(self, GPU) -> None:
        pass

    def buildMotherBoard(self, MotherBoard) -> None:
        pass

    def buildRAM(self, RAM) -> None:
        pass

    def getResult() -> Computer:
        pass

class Component:
    """Класс компоненты компьютера"""
    def __init__(self, cost, name, uuid):
        self._cost = cost
        self._name = name
        self._uuid = uuid

    def getInfo() -> json:
        pass

class OS(Component):
    """Класс операционной системы"""
    def __init__(self, cost, name, uuid, mode, maxSupportedMemory):
        super().__init__(cost, name, uuid)
        self.__mode = mode
        self.__maxSupportedMemory = maxSupportedMemory

class SSD(Component):
    """Класс SSD"""
    def __init__(self, cost, name, uuid, capacity, formFactor, cache):
        super().__init__(cost, name, uuid)
        self.__capacity = capacity
        self.__formFactor = formFactor
        self.__cache = cache

class CPUCooler(Component):
    """Класс охлаждения процессора"""
    def __init__(self, cost, name, uuid, fanRPM, color, noiseLevel):
        super().__init__(cost, name, uuid)
        self.__fanRPM = fanRPM
        self.__color = color
        self.__noiseLevel = noiseLevel

class Case(Component):
    """Класс системного блока"""
    def __init__(self, cost, name, uuid, type, color, sidePanel, external525):
        super().__init__(cost, name, uuid)
        self.__type = type
        self.__color = color
        self.__sidePanel = sidePanel
        self.__external525 = external525

class CPU(Component):
    """Класс центрального процесса"""
    def __init__(self, cost, name, uuid, coreCount, boostClock, integratedGraphics, coreClock, TDP):
        super().__init__(cost, name, uuid)
        self.__coreCount = coreCount
        self.__boostClock = boostClock
        self.__integratedGraphics = integratedGraphics
        self.__coreClock = coreClock
        self.__TDP = TDP

class GPU(Component):
    """Класс графического процессора"""
    def __init__(self, cost, name, uuid, chipSet, coreClock, color, memory, boostClock, length):
        super().__init__(cost, name, uuid)
        self.__chipSet = chipSet
        self.__coreClock = coreClock
        self.__color = color
        self.__memory = memory
        self.__boostClock = boostClock
        self.__length = length

class MotherBoard(Component):
    """Класс материнской платы"""
    def __init__(self, cost, name, uuid, socket, memoryMax, formFactor, memorySlots):
        super().__init__(cost, name, uuid)
        self.__socket = socket
        self.__memoryMax = memoryMax
        self.__formFactor = formFactor
        self.__memorySlots = memorySlots

class RAM(Component):
    """Класс оперативной памяти ПК"""
    def __init__(self, cost, name, uuid, modules, CASLatency):
        super().__init__(cost, name, uuid)
        self.__modules = modules
        self.__CASLatency = CASLatency

class PowerSupply(Component):
    """Класс блока питания"""
    def __init__(self, cost, name, uuid, type, wattage, efficiencyRating, Modular):
        super().__init__(cost, name, uuid)
        self.__type = type
        self.__wattage = wattage
        self.__efficiencyRating = efficiencyRating
        self.__Modular = Modular

class ComponentStorage:
    def __init__(self, listOS: list, listSSD: list, listCPUCooler: list, listCase: list, listCPU: list, listGPU: list, 
                 listMotherBoard: list, listRAM: list, listPowerSupply: list):
        self.__listOS = listOS
        self.__listSSD = listSSD
        self.__listCPUCooler = listCPUCooler
        self.__listCase = listCase
        self.__listCPU = listCPU
        self.__listGPU = listGPU
        self.__listMotherBoard = listMotherBoard
        self.__listRAM = listRAM
        self.__listPowerSupply = listPowerSupply
    
    def addOS(os: OS) -> bool:
        return True

    def addSSD(ssd: SSD) -> bool:
        pass

    def addCPUCooler(cpucooler: CPUCooler) -> bool:
        pass

    def addCase(case: Case) -> bool:
        pass

    def addCPU(cpu: CPU) -> bool:
        pass

    def addGPU(gpu: GPU) -> bool:
        pass

    def addMotherBoard(motherboard: MotherBoard) -> bool:
        pass

    def addRAM(ram: RAM) -> bool:
        pass

    def addPowerSupply(powersupply: PowerSupply) -> bool:
        pass

    def removeOS(os: OS) -> bool:
        pass

    def removeSSD(ssd: SSD) -> bool:
        pass

    def removeCPUCooler(cpucooler: CPUCooler) -> bool:
        pass

    def removeCase(case: Case) -> bool:
        pass

    def removeCPU(cpu: CPU) -> bool:
        pass

    def removeGPU(gpu: GPU) -> bool:
        pass

    def removeMotherBoard(motherboard: MotherBoard) -> bool:
        pass

    def removeRAM(ram: RAM) -> bool:
        pass

    def removePowerSupply(powersupply: PowerSupply) -> bool:
        pass

    def showListOS() -> list:
        query = """"""

    def showListSSD() -> list:
        query = """"""

    def showListCPUCooler() -> list:
        query = """"""

    def showListCase() -> list:
        query = """"""

    def showListCPU() -> list:
        query = """"""

    def showListGPU() -> list:
        query = """"""

    def showListMotherBoard() -> list:
        query = """"""

    def showListRAM() -> list:
        query = """"""

    def showListPowerSupply() -> list:
        query = """"""     

class Admin:
    """Класс Admin"""

    def addComponent(self, component: Component) -> bool:
        choice = int(input("""Что хотим добавить в базу данных?
        1 - ОС
        2 - SSD
        3 - Охлаждение
        4 - Системный блок
        5 - Центральный процессор
        6 - Графический процессор
        7 - Материнская плата
        8 - Оперативная память
        9 - Блок питания
        """))
        
        component._cost = int(input("Введите стоимость: "))
        component._name = str(input("Введите назваание: "))

        while True:
            component._uuid = int(input("Введите id: "))
            """if component._uuid in database: # если этот id есть в бд
                   continue
               else:  # этого id нет в бд
                   break"""
            break

        match choice:
            case 1:   # ОС
                mode = int(input("Введите mode: "))
                sMemory = int(input("Введите maxSupportedMemory: "))
                objectOS = OS(component._cost,component._name,component._uuid,mode=mode,maxSupportedMemory=sMemory)  
                if ComponentStorage.addOS(objectOS) == True:
                    print(f"ОС {objectOS} добавлена")
                    return True
                
            case 2:  # SSD
                capacity = str(input("Введите capacity: "))
                formFactor = str(input("Введите formFactor: "))
                cache = str(input("Введите cache: "))
                objectSSD = SSD(component._cost,component._name,component._uuid,capacity=capacity, formFactor=formFactor,cache=cache)
                if ComponentStorage.addSSD(objectSSD) == True:
                    print(f"SSD {objectSSD} добавлен")
                    return True
                
            case 3:  # Охлаждение
                fanRPM = str(input("Введите fanRPM: "))
                color = str(input("Введите color: "))
                noiseLevel = float(input("Введите noiseLevel: "))
                objectCPUCooler = CPUCooler(component._cost,component._name,component._uuid,fanRPM=fanRPM,color=color,noiseLevel=noiseLevel)
                if ComponentStorage.addCPUCooler(objectCPUCooler) == True:
                    print(f"CPUCooler {objectCPUCooler} добавлен")
                    return True
                
            case 4:  # Системный блок
                type = str(input("Введите type: "))
                color = str(input("Введите color: "))
                sidePanel = str(input("Введите sidePanel: "))
                external525 = int(input("Введите external525: "))
                objectCase = Case(component._cost,component._name,component._uuid,type=type,color=color,sidePanel=sidePanel,external525=external525)
                if ComponentStorage.addCase(objectCase) == True:
                    print(f"Case {objectCase} добавлен")
                    return True
                
            case 5:  # Центральный процессор
                coreCount = int(input("Введите coreCount: "))
                boostClock = float(input("Введите boostClock: "))
                integratedGraphics = str(input("Введите integratedGraphics: "))
                coreClock = float(input("Введите coreClock: "))
                TDP = int(input("Введите TDP: "))
                objectCPU = CPU(component._cost,component._name,component._uuid,coreCount=coreCount,boostClock=boostClock,integratedGraphics=integratedGraphics,coreClock=coreClock,TDP=TDP)
                if ComponentStorage.addCPU(objectCPU) == True:
                    print(f"CPU {objectCPU} добавлен")
                    return True
                
            case 6:  # Графический процессор
                chipSet = str(input("Введите chipSet: "))
                boostClock = float(input("Введите boostClock: "))
                color = str(input("Введите color: "))
                coreClock = float(input("Введите coreClock: "))
                memory = str(input("Введите memory: "))
                length = int(input("Введите length: "))
                objectGPU = GPU(component._cost,component._name,component._uuid,chipSet=chipSet,coreClock=coreClock,color=color,memory=memory,boostClock=boostClock,length=length)
                if ComponentStorage.addGPU(objectGPU) == True:
                    print(f"GPU {objectGPU} добавлен")
                    return True
                
            case 7:  # Материнская плата
                socket = str(input("Введите socket: "))
                memoryMax = int(input("Введите memoryMax: "))
                formFactor = str(input("Введите formFactor: "))
                memorySlots = int(input("Введите memorySlots: "))
                objectMotherBoard = MotherBoard(component._cost,component._name,component._uuid,socket=socket,memoryMax=memoryMax,formFactor=formFactor,memorySlots=memorySlots)
                if ComponentStorage.addMotherBoard(objectMotherBoard) == True:
                    print(f"MotherBoard {objectMotherBoard} добавлен")
                    return True
                
            case 8:  # Оперативная память
                modules = str(input("Введите modules: "))
                CASLatency = int(input("Введите CASLatency: "))
                objectRAM = RAM(component._cost,component._name,component._uuid,modules=modules,CASLatency=CASLatency)  
                if ComponentStorage.addRAM(objectRAM) == True:
                    print(f"RAM {objectRAM} добавлена")
                    return True
             
            case 9:  # Блок питания
                type = str(input("Введите type: "))
                wattage = int(input("Введите wattage: "))
                efficiencyRating = str(input("Введите efficiencyRating: "))
                Modular = str(input("Введите Modular: "))
                objectPowerSupply = PowerSupply(component._cost,component._name,component._uuid,type=type,wattage=wattage,efficiencyRating=efficiencyRating,Modular=Modular)
                if ComponentStorage.addPowerSupply(objectPowerSupply) == True:
                    print(f"PowerSupply {objectPowerSupply} добавлен")
                    return True
                
            case _:  # Некорректная цифра
                print("Некорректная цифра")  

    def removeComponent(self, component: Component) -> bool:
        choice = int(input("""Что хотим удалить из базы данных?
        1 - ОС
        2 - SSD
        3 - Охлаждение
        4 - Системный блок
        5 - Центральный процессор
        6 - Графический процессор
        7 - Материнская плата
        8 - Оперативная память
        9 - Блок питания
        """))
        
        match choice:
            case 1:  # ОС
                ComponentStorage.removeOS()  
            case 2:  # SSD
                ComponentStorage.removeSSD()  
            case 3:  # Охлаждение
                ComponentStorage.removeCPUCooler()  
            case 4:  # Системный блок
                ComponentStorage.removeCase()  
            case 5:  # Центральный процессор
                ComponentStorage.removeCPU()  
            case 6:  # Графический процессор
                ComponentStorage.removeGPU()  
            case 7:  # Материнская плата
                ComponentStorage.removeMotherBoard()  
            case 8:  # Оперативная память
                ComponentStorage.removeRAM()  
            case 9:  # Блок питания
                ComponentStorage.removePowerSupply()  
            case _:  # Некорректная цифра
                print("Некорректная цифра")  

    def showComponents(self) -> list:
        choice = int(input("""Список каких компонентов показать?
        1 - ОС
        2 - SSD
        3 - Охлаждение
        4 - Системный блок
        5 - Центральный процессор
        6 - Графический процессор
        7 - Материнская плата
        8 - Оперативная память
        9 - Блок питания
        """))
        
        match choice:
            case 1:  # ОС
                ComponentStorage.showListOS()  
            case 2:  # SSD
                ComponentStorage.showListSSD()  
            case 3:  # Охлаждение
                ComponentStorage.showListCPUCooler()  
            case 4:  # Системный блок
                ComponentStorage.showListCase()  
            case 5:  # Центральный процессор
                ComponentStorage.showListCPU()  
            case 6:  # Графический процессор
                ComponentStorage.showListGPU()  
            case 7:  # Материнская плата
                ComponentStorage.showListMotherBoard()  
            case 8:  # Оперативная память
                ComponentStorage.showListRAM()  
            case 9:  # Блок питания
                ComponentStorage.showListPowerSupply()  
            case _:  # Некорректная цифра
                print("Некорректная цифра")  

cursor.close()
connection.close()

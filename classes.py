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
cursor.close()
connection.close()

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
    def __init__(self, cost, name, uuid, computer: Computer):
        self._computer = computer
        self._cost = cost
        self._name = name
        self._uuid = uuid

    def getInfo() -> json:
        pass

class OS(Component):
    """Класс операционной системы"""
    def __init__(self, cost, name, uuid, mode, maxSupportedMemory):
        super().init(cost, name, uuid)
        self.__mode = mode
        self.__maxSupportedMemory = maxSupportedMemory

class SSD(Component):
    """Класс SSD"""
    def __init__(self, cost, name, uuid, capacity, formFactor, cache):
        super().init(cost, name, uuid)
        self.__capacity = capacity
        self.__formFactor = formFactor
        self.__cache = cache

class CPUCooler(Component):
    """Класс охлаждения процессора"""
    def __init__(self, cost, name, uuid, fanRPM, color, noiseLevel):
        super().init(cost, name, uuid)
        self.__fanRPM = fanRPM
        self.__color = color
        self.__noiseLevel = noiseLevel

class Case(Component):
    """Класс системного блока"""
    def __init__(self, cost, name, uuid, type, color, sidePanel, external525):
        super().init(cost, name, uuid)
        self.__type = type
        self.__color = color
        self.__sidePanel = sidePanel
        self.__external525 = external525

class CPU(Component):
    """Класс центрального процесса"""
    def __init__(self, cost, name, uuid, coreCount, boostClock, integratedGraphics, coreClock, TDP):
        super().init(cost, name, uuid)
        self.__coreCount = coreCount
        self.__boostClock = boostClock
        self.__integratedGraphics = integratedGraphics
        self.__coreClock = coreClock
        self.__TDP = TDP

class GPU(Component):
    """Класс графического процессора"""
    def __init__(self, cost, name, uuid, chipSet, coreClock, color, memory, boostClock, length):
        super().init(cost, name, uuid)
        self.__chipSet = chipSet
        self.__coreClock = coreClock
        self.__color = color
        self.__memory = memory
        self.__boostClock = boostClock
        self.__length = length

class MotherBoard(Component):
    """Класс материнской платы"""
    def __init__(self, cost, name, uuid, socket, memoryMax, formFactor, memorySlots):
        super().init(cost, name, uuid)
        self.__socket = socket
        self.__memoryMax = memoryMax
        self.__formFactor = formFactor
        self.__memorySlots = memorySlots

class RAM(Component):
    """Класс оперативной памяти ПК"""
    def __init__(self, cost, name, uuid, modules, CASLatency):
        super().init(cost, name, uuid)
        self.__modules = modules
        self.__CASLatency = CASLatency

class PowerSupply(Component):
    """Класс блока питания"""
    def __init__(self, cost, name, uuid, type, wattage, efficiencyRating, Modular):
        super().init(cost, name, uuid)
        self.__type = type
        self.__wattage = wattage
        self.__efficiencyRating = efficiencyRating
        self.__Modular = Modular

class Admin:
    """Класс Admin"""

    def addComponent(self, component: Component) -> bool:
        print("""Что хотим добавить в базу данных?
              1 - ОС
              2 - SSD
              3 - Охлаждение
              4 - Системный блок
              5 - Центральный процессор
              6 - Графический процессор
              7 - Материнская плата
              8 - Оперативная память
              9 - Блок питания
              """)
        
    def removeComponent(self, component: Component) -> bool:
        print("""Что хотим удалить из базы данных?
              1 - ОС
              2 - SSD
              3 - Охлаждение
              4 - Системный блок
              5 - Центральный процессор
              6 - Графический процессор
              7 - Материнская плата
              8 - Оперативная память
              9 - Блок питания
              """)

    def showComponents(self) -> list:
        print("""Список каких компонентов показать?
              1 - ОС
              2 - SSD
              3 - Охлаждение
              4 - Системный блок
              5 - Центральный процессор
              6 - Графический процессор
              7 - Материнская плата
              8 - Оперативная память
              9 - Блок питания
              """)

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
    
    def addOS(self, os: OS) -> bool:
        pass

    def addSSD(self, ssd: SSD) -> bool:
        pass

    def addCPUCooler(self, cpucooler: CPUCooler) -> bool:
        pass

    def addCase(self, case: Case) -> bool:
        pass

    def addCPU(self, cpu: CPU) -> bool:
        pass

    def addGPU(self, gpu: GPU) -> bool:
        pass

    def addMotherBoard(self, motherboard: MotherBoard) -> bool:
        pass

    def addRAM(self, ram: RAM) -> bool:
        pass

    def addPowerSupply(self, powersupply: PowerSupply) -> bool:
        pass

    def removeOS(self, os: OS) -> bool:
        pass

    def removeSSD(self, ssd: SSD) -> bool:
        pass

    def removeCPUCooler(self, cpucooler: CPUCooler) -> bool:
        pass

    def removeCase(self, case: Case) -> bool:
        pass

    def removeCPU(self, cpu: CPU) -> bool:
        pass

    def removeGPU(self, gpu: GPU) -> bool:
        pass

    def removeMotherBoard(self, motherboard: MotherBoard) -> bool:
        pass

    def removeRAM(self, ram: RAM) -> bool:
        pass

    def removePowerSupply(self, powersupply: PowerSupply) -> bool:
        pass

    def showListOS(self) -> list:
        pass

    def showListSSD(self) -> list:
        pass

    def showListCPUCooler(self) -> list:
        pass

    def showListCase(self) -> list:
        pass

    def showListCPU(self) -> list:
        pass

    def showListGPU(self) -> list:
        pass

    def showListMotherBoard(self) -> list:
        pass

    def showListRAM(self) -> list:
        pass

    def showListPowerSupply(self) -> list:
        pass

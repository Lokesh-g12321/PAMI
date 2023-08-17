# imagery2Databases is used to  create a transactional Database.
#
#
#
# **Importing this algorithm into a python program**
# --------------------------------------------------------
#
#     from PAMI.extras.imageProcessing import imagery2Databases as db
#
#     obj = db.imagery2Databases(detected_objects, 16)
#
#     obj.save()
#
#
__copyright__ = """
 Copyright (C)  2021 Rage Uday Kiran

     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.

     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pandas as pd
# creating transactional database by applying threshold
class imagery2Databases():
    """

             :Description:
                        utilityToFuzzy is a code used to convert the transactional database into Fuzzy transactional database.

             :param  detected_objects: str :

             :param  threshold: int:
                                 Takes the input value int

             **Importing this algorithm into a python program**
             --------------------------------------------------------
             .. code-block:: python

             from PAMI.extras.imageProcessing import imagery2Databases as db

             obj = db.imagery2Databases(detected_objects, 16)

             obj.save(oFile)


    """

class createDatabase:
    # pass the list of detected objects and specify the minimum probability score an object must maintain.
    def __init__(self, detected_objects: list, threshold: float):
        # initialize data frame to store objects
        self.dataframe = pd.DataFrame(columns=['objects'])
        self.threshold = threshold
        self.itemList = []
        self.probabilityValuesList = []
        self.detected_objects = detected_objects
        self.itemSupport = []
        self.itemSupportSum = []  # pruning the objects having scores less than threshold value
        for objectList in self.detected_objects:
            supportSum = 0
            dataDic = {}
            self.items = []
            self.values = []
            self.supports = []
            for item in objectList:
                supportSum = supportSum + 1
                if item[1] >= self.threshold:
                    if item[0] not in dataDic.keys():
                        dataDic[item[0]] = [item[1]]
                    else:
                        dataDic[item[0]].append(item[1])
            # storing objects,their probabilities and count
            self.items = [item for item in dataDic.keys()]
            self.values = [max(value) for value in dataDic.values()]
            self.supports = [len(value) for value in dataDic.values()]

            self.itemSupportSum.append(supportSum)
            self.itemList.append(self.items)
            self.probabilityValuesList.append(self.values)
            self.itemSupport.append(self.supports)
            self.dataframe.loc[self.dataframe.shape[0], 'objects'] = dataDic.keys()

    def getDataFrame(self) -> pd.DataFrame:
        return self.dataframe

    # This function will save the list of objects found in each image as a transactional database.

    # creating transactional database
    def saveAsTransactionalDB(self, outputFile: str, sep: str) -> None:
        writeFile = open(outputFile, 'w')
        for i in range(len(self.itemList)):
            if self.itemList[i]:
                writeLine = sep.join(map(str, self.itemList[i]))
                writeFile.write(writeLine + '\n')
        writeFile.close()

    # creating temporal database
    def saveAsTemporalDB(self, outputFile: str, sep: str):
        writeFile = open(outputFile, 'w')

        for i in range(len(self.itemList)):
            if self.itemList[i]:
                writeLine = sep.join(map(str, self.itemList[i]))
                writeFile.write(str(i) + sep + writeLine + '\n')

        writeFile.close()

    # creating utility transactional database

    def saveAsUtilityTransactionalDB(self, outputFile: str, sep: str) -> None:
        writeFile = open(outputFile, 'w')
        for i in range(len(self.itemList)):
            if self.itemList[i]:
                writeLine = sep.join(map(str, self.itemList[i]))
                writeLine2 = sep.join(map(str, self.itemSupport[i]))
                writeFile.write(writeLine + ':' + str(self.itemSupportSum[i]) + ':' + writeLine2 + '\n')
        writeFile.close()

    # creating utility temporal database

    def saveAsUtilityTemporalDB(self, outputFile: str, sep: str) -> None:
        writeFile = open(outputFile, 'w')
        for i in range(len(self.itemList)):
            if self.itemList[i]:
                writeLine = sep.join(map(str, self.itemList[i]))
                writeLine2 = sep.join(map(str, self.itemSupport[i]))
                writeFile.write(
                    str(i) + str(sep) + writeLine + ':' + str(self.itemSupportSum[i]) + ':' + writeLine2 + '\n')
        writeFile.close()

    # creating uncertain transactional database

    def saveAsUncertainTransactionalDB(self, outputFile: str, sep: str) -> None:
        writeFile = open(outputFile, 'w')
        for i in range(len(self.itemList)):
            if self.itemList[i]:
                writeLine = sep.join(map(str, self.itemList[i]))
                writeLine2 = sep.join(map(str, self.probabilityValuesList[i]))
                writeFile.write(writeLine + ":1:" + writeLine2 + '\n')
        writeFile.close()

    # creating uncertain Temporal database

    def saveAsUncertainTemporalDB(self, outputFile: str, sep: str) -> None:
        writeFile = open(outputFile, 'w')
        for i in range(len(self.itemList)):
            if self.itemList[i]:
                writeLine = sep.join(map(str, self.itemList[i]))
                writeLine2 = sep.join(map(str, self.probabilityValuesList[i]))
                writeFile.write(str(i) + str(sep) + writeLine + ":1:" + writeLine2 + '\n')
        writeFile.close()

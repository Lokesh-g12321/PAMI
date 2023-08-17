# generateTransactionalDatabase this code is used to generates a transactional Database.
#
# **Importing this algorithm into a python program**
# --------------------------------------------------------
#
#     from PAMI.extras.generateDatabase import generateTransactionalDatabase as db
#
#     obj = db.generateTransactionalDatabase(numOfTransactions, maxNumOfDistinctItems, numOfItemsPerTransaction, oFile, "\t" )
#
#     obj.save()
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

import random


class generateTransactionalDatabase:
    """
       Description:
       -------------
          generateTransactionalDatabase generates a transactional database


        :param numOfTransactions: int
            number of transactions
        :param maxNumOfDistinctItems: int
            maximum number of distinct items
        :param numOfItemsPerTransaction: int
            number of items per transaction
        :param outFileName: str
            output file name
        :param sep: str
            seperator in file, default is tab space

        Methods:
        --------
        getFileName()
            get output filename

        **Importing this algorithm into a python program**
        --------------------------------------------------------
        .. code-block:: python

        from PAMI.extras.generateDatabase import generateTransactionalDatabase as db

        obj = db.generateTransactionalDatabase(numOfTransactions, maxNumOfDistinctItems, numOfItemsPerTransaction, oFile, "\t" )

        obj.save(oFile)

    """
    def __init__(self, numOfTransactions, maxNumOfDistinctItems, numOfItemsPerTransaction, outFileName, sep='\t'):
        """

        :param numOfTransactions: number of transactions
        :type numOfTransactions: int
        :param maxNumOfDistinctItems: distinct items per transactions
        :type maxNumOfDistinctItems: int 
        :param numOfItemsPerTransaction: items per transaction
        :type numOfItemsPerTransaction: int
        :param outFileName: output filename
        :type outFileName: str
        :param sep: seperator
        :type sep: str
        """
        self.numOfTransactions = numOfTransactions
        self.maxNumOfDistinctItems = maxNumOfDistinctItems
        self.numOfItemsPerTransaction = numOfItemsPerTransaction
        self.outFileName = outFileName
        self.sep = sep

        # make outFile
        with open(self.outFileName, "w+") as outFile:
            # For the number of transactions to be generated
            for i in range(self.numOfTransactions):
                # This hashset will be used to remember which items have
                # already been added to this item set.
                alreadyAdded = set()
                # create an arraylist to store items from the item set that will be generated
                itemSet = list()
                # We randomly decide how many items will appear in this transaction
                randNumOfItems = random.randrange(self.maxNumOfDistinctItems) + 1
                # for the number of items that was decided above
                for j in range(randNumOfItems):
                    # we generate the item randomly and write it to disk
                    item = random.randrange(self.maxNumOfDistinctItems) + 1
                    # if we already added this item to this item set
                    # we choose another one
                    while item in alreadyAdded:
                        item = random.randrange(self.maxNumOfDistinctItems) + 1
                    alreadyAdded.add(item)
                    itemSet.append(item)
                # sort the item set
                itemSet.sort()
                # write the item set
                for j in itemSet:
                    outFile.write(str(j) + self.sep)
                outFile.write('\n')
        # close outFile
        outFile.close()

    def getFileName(self) -> str:
        """
        return output file name
        :return: output file name
        """
        return self.outFileName

if __name__ == '__main__':
    numOfTransactions = 500
    maxNumOfDistinctItems = 1000
    numOfItemsPerTransaction = 20
    outFileName = '/Users/Likhitha/Downloads/out.txt'

    tDG = generateTransactionalDatabase(numOfTransactions, maxNumOfDistinctItems, numOfItemsPerTransaction, outFileName)

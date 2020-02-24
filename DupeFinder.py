import os

# format colours for CMD
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# this returns bytes into a readable file size
def dataSize( bytesSize ):
    kb = 1024
    mb = kb * 1024
    gb = mb * 1024
    # str( round((sizeTotal / mb), 2 ) )

    if bytesSize > 1000000000:
        endNum = round((bytesSize / gb), 2)
        numFormat = str(endNum) + " GB"
    elif bytesSize > 1000000:
        endNum = round((bytesSize / mb), 2)
        numFormat = str(endNum) + " MB"
    else:
        endNum = round((bytesSize / kb), 2)
        numFormat = str(endNum) + " KB"

    return numFormat


def dupeFinder( dirName ):

    fileCount = 0
    dupeFileCount = 0
    sizeTotal = 0

    completeSet = set()

    for root, dirs, files in os.walk( dirName ):
        for x in files:

            # Get file size
            fileSize = os.path.getsize( os.path.join( root, x ) )

            # Simple search add name and size together?
            # ***** May need better Logic later *****

            finalNameCompare = x + "_" + str(fileSize)

            if finalNameCompare in completeSet:
                print( color.BOLD + color.RED + "Dupe found: " + x + color.END )
                dupeFileCount += 1
                sizeTotal += fileSize
                os.remove( os.path.join( root, x ) )

            else:    
                completeSet.add( finalNameCompare )
                fileCount += 1

    print( color.BOLD + color.GREEN + "total files found: " + str( fileCount ) + color.END )
    print( color.GREEN + "total size: " + dataSize( sizeTotal ) + color.END )


#
dirName = "f://test"
dupeFinder( dirName )
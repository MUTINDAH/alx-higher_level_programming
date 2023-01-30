try:
    myFile = open(f"my data.txt", encoding="utf-8")

except FileNotFoundError as ex:
    #print("that file was not found")
    print(ex.args)

else:
    print("File: ", myFile)
    myFile.close()

finally:
    print("Finished working on this file")

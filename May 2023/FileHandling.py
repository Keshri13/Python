
writeMessage1 = "\nI am writing myself in a File 1\n\n\nwith open(\"fileEg1.txt\",\"w\") as f:\n\tf.write(writeMessage1)\n\nAnd I am Indian"
writeMessage2 = "\nI am writing myself in a File 2\n\n\nfp = open(\"fileEg2\",\"w\")\nfp.write(writeMessage2)\nfp.close()\n\nAnd I am Rossi"

#Writing way1
# with open("fileEg1.txt","w") as f:
#     f.write(writeMessage1)

#Writing way2
# fpw = open("fileEg2","w")
# fpw.write(writeMessage2)
# fpw.close()

#Reading way1
# with open("fileEg1.txt","r") as f:
#     message1=f.read()
#     print(message1)

#Readin way2
# fpr = open("fileEg2","r")
# message2=fpr.read()
# print(message2)
# fpr.close()
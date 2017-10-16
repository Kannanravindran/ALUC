from subprocess import call

outputFile = open("program_output.txt", "w")

n = raw_input("Enter the value of n: ")
k = raw_input("Enter the value of k: ")

call(["clingo", "schur", "-c", "n=%s" % n, "-c", "k=%s" % k, "--verbose=0"], stdout=outputFile)

outputFile.close()
readFile = open("program_output.txt", "r")

answer = readFile.readline().strip().split(" ")
print "\n".join(answer)

readFile.close()

from subprocess import call,Popen,PIPE
from config import *
from ast import literal_eval

def exec_schur(_n=30,_k=10):
    outputFile = open("program_output.txt", "w")
    call([PROJECT_PATH+"core/clingo/clingo", PROJECT_PATH+"core/schur", "-c", "n=%s" % _n, "-c", "k=%s" % _k, "--verbose=0"], stdout=outputFile)
    outputFile.close()
    readFile = open("program_output.txt", "r")

    groups = readFile.readline().strip().split(" ")
    # print groups
    readFile.close()
    output = {}
    for group in groups:
        try:
            g_key,g_value = literal_eval(group[1:])
        except Exception as e:
            return {"error":"Unsatisfiable"}
        if g_key in output.keys():
            output[g_key].append(g_value)
        else:
            output[g_key] = [g_value]

    return output

def exec_similar(_n=30,_k=10):
    outputFile = open(PROJECT_PATH+"program_output.txt", "w")
    call([PROJECT_PATH+"core/clingo/clingo", PROJECT_PATH+"core/similar_groupify", PROJECT_PATH+"core/sample_data", "--verbose=0"], stdout=outputFile)
    outputFile.close()
    readFile = open(PROJECT_PATH+"program_output.txt", "r")

    groups = readFile.readline().strip().split(" ")
    # print groups
    readFile.close()
    output = {}
    for group in groups:
        try:
            g_key,g_id,g_value = literal_eval(group[1:])
        except Exception as e:
            return {"error":"Unsatisfiable"}
        if g_key in output.keys():
            output[g_key].append((g_id,g_value))
        else:
            output[g_key] = [(g_id,g_value)]

    return output

def exec_dissimilar(_n=30,_k=10):
    outputFile = open(PROJECT_PATH+"program_output.txt", "w")
    call([PROJECT_PATH+"core/clingo/clingo", PROJECT_PATH+"core/dissimilar_groupify", PROJECT_PATH+"core/sample_data", "--verbose=0"], stdout=outputFile)
    outputFile.close()
    readFile = open(PROJECT_PATH+"program_output.txt", "r")

    groups = readFile.readline().strip().split(" ")
    # print groups
    readFile.close()
    output = {}
    print groups
    for group in groups:
        try:
            g_key,g_id,g_value = literal_eval(group[1:])
        except Exception as e:
            return {"error":"Unsatisfiable"}
        if g_key in output.keys():
            output[g_key].append((g_id,g_value))
        else:
            output[g_key] = [(g_id,g_value)]
    return output

if __name__ == '__main__':
    print exec_similar()
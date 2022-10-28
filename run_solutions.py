import argparse
import json
import os
import re

PYTHON_COMMAND = "python3"

def rememberDirectoryDecorator(func):
	def wrapper(*args, **kwargs):
		originalDir = os.getcwd()
		returnVal = func(*args, **kwargs)
		os.chdir(originalDir)
		return returnVal
	return wrapper

class ChallengeRun:
	def __init__(self, path):
		self.path = path

	def run(self):
		raise TypeError("Base class cannot be run")

class PythonChallenge(ChallengeRun):
	def __init__(self, path):
		super().__init__(path)

	@rememberDirectoryDecorator
	def run(self) -> bool:
		os.chdir(self.path)
		if os.path.exists("part1.py"):
			result = os.system("part1.py") == 0

			if os.path.exists("part2.py"):
				result = result or os.system(str(f"{PYTHON_COMMAND} part2.py"))

			return result == 0

class CPPChallenge(ChallengeRun):
	@rememberDirectoryDecorator
	def buildCPP(self):
		os.chdir(self.path)
		print(os.getcwd())
		if os.path.exists("makefile"):
			os.system("make -j")
		elif os.path.exists("solution.cpp"):
			os.system("g++ solution.cpp")
		else:
			raise RuntimeError(
				f"Could not build cpp solution at {self.path}. Try adding compilation instructions")
	
	@rememberDirectoryDecorator
	def run(self)-> bool:
		# Compile code
		self.buildCPP()

		os.chdir(self.path)
		if os.path.exists("a.out"):
			return os.system("a.out") == 0

challengeTypes = {"python":PythonChallenge, "cpp":CPPChallenge}

@rememberDirectoryDecorator
def runCPP(executablePath: str):
	os.chdir(os.path.dirname(executablePath))
	if os.path.exists(os.path.basename(executablePath)):
		os.system(os.path.basename(executablePath))
	else:
		raise RuntimeError(f"Could not locate executable {executablePath}")


@rememberDirectoryDecorator
def runPython(executablePath: str):
	os.chdir(os.path.dirname(executablePath))
	os.system(str(f"{PYTHON_COMMAND} {os.path.basename(executablePath)}"))

@rememberDirectoryDecorator
def getAllChallenges(baseDir:str) -> list:
	challenges = list()
	
	yearDirectories = next(os.walk(baseDir))[1]
	for year in yearDirectories:
		if re.match("\d+", year) != None:
			dayDirectories = next(os.walk(os.path.join(baseDir, year)))[1]
			for day in dayDirectories:
				if re.match("\d+", day) != None:
					challenges.append(str(f"{year}:{day}"))

	return challenges

@rememberDirectoryDecorator
def getChallengeType(configFile:str, challengeYear:str, challengeDay:str, guessType:bool = False, baseChallengeDir:str = ".") -> str:
	with open(configFile, "r") as inFile:
		configJson = json.loads(inFile.read())
	
	try:
		return configJson["challenges"][challengeYear][challengeDay]["type"]
	except IndexError as e:
		if guessType:
			files = next(os.walk(os.path.join(baseChallengeDir, challengeYear, challengeDay)))[2]
			for file in files:
				if re.search(".py", file):
					return "python"
				elif re.search(".cpp", file):
					return "cpp"
			raise RuntimeError(f"Could not determine type of challenge{challengeYear}:{challengeDay}")
		else:
			raise e

def runChallengeNumber(challengeNumber:str, challengeBaseDir:str, configFileName:str) -> bool:
	challengeType = getChallengeType(configFileName, challengeNumber.split(":")[0], challengeNumber.split(":")[1])

	challenge = challengeTypes[challengeType](challengeBaseDir)



	return challenge.run()

def main():
	parser = argparse.ArgumentParser(
		prog="Run challenge solutions", usage="", description="")
	parser.add_argument("-c", "--config", required=False, default="config.json")
	parser.add_argument("challenges", nargs="*")
	parsedArgs = parser.parse_args()
	print(parsedArgs)

	if len(parsedArgs.challenges) == 0:
		runList = getAllChallenges(".")
		print(f"No challenges specified, running all {runList}")
	else:
		runList = parsedArgs.challenges


	for challenge in runList:
		success = runChallengeNumber(challenge, os.path.join(challenge.split(":")[0], challenge.split(":")[1]), parsedArgs.config)
		if success: print(f"\x1b[32mComplete: {challenge}\x1b[0m")
		else: print(f"\x1b[31mFailed: {challenge}\x1b[0m")

if __name__ == "__main__":
	main()

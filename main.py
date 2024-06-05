from TarjanAlgorithm import TarjanAlgorithm

from TestCases import Case0, Case1, Case2, Case3, Case4, Case5

tarjanAlgorithm = TarjanAlgorithm(Case0["Edges"])
assert Case0["Ans"] == tarjanAlgorithm.getSCCs()

tarjanAlgorithm = TarjanAlgorithm(Case1["Edges"])
assert Case1["Ans"] == tarjanAlgorithm.getSCCs()

tarjanAlgorithm = TarjanAlgorithm(Case2["Edges"])
assert Case2["Ans"] == tarjanAlgorithm.getSCCs()

tarjanAlgorithm = TarjanAlgorithm(Case3["Edges"])
assert Case3["Ans"] == tarjanAlgorithm.getSCCs()

tarjanAlgorithm = TarjanAlgorithm(Case4["Edges"])
assert Case4["Ans"] == tarjanAlgorithm.getSCCs()

tarjanAlgorithm = TarjanAlgorithm(Case5["Edges"])
assert Case5["Ans"] == tarjanAlgorithm.getSCCs()

print("All testcase passes :)")

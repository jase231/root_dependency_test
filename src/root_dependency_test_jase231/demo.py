import ROOT

# disable canvas/web view
ROOT.gROOT.SetBatch(True)

# create a RDataFrame and define a branch with random values
df = ROOT.RDataFrame(10000)
ROOT.gRandom.SetSeed(1)
df_rand = df.Define("rng", "gRandom->Gaus()")

# book histogram and write it to png
hist = df_rand.Histo1D("rng")
c = ROOT.TCanvas("rng_hist", "rng_hist", 800, 400)
hist.Draw()
c.SaveAs("rng_normal_hist.png")
print("Wrote demo histogram to rng_normal_hist.png")

# write the RDF to root file
df_rand.Snapshot("rng_Tree", "rng.root", [ "rng" ])
print("Wrote demo root file to rng.root")

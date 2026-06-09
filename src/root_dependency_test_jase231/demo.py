import ROOT

# disable canvas/web view
ROOT.gROOT.SetBatch(True)

# custom C++ function for obtaining random values
ROOT.gInterpreter.Declare("""
#include <random>
                        
class gauss_rng {
public:
    gauss_rng(double mean = 0, double dev = 5) : generator(std::random_device{}()), normalizer(mean, dev) {}
    double operator()() { return normalizer(generator); }

private:
    std::mt19937 generator;
    std::normal_distribution<double> normalizer;
};

gauss_rng normal_dist_gen{};""")


# create a RDataFrame and define a branch with random values
df = ROOT.RDataFrame(10000)
ROOT.gRandom.SetSeed(1)
df_rand = df.Define("rng", "normal_dist_gen();")

# book histogram and write it to png
hist = df_rand.Histo1D("rng")
c = ROOT.TCanvas("rng_hist", "rng_hist", 800, 400)
hist.Draw()
c.SaveAs("rng_normal_hist.png")
print("Wrote demo histogram to rng_normal_hist.png")

# write the RDF to root file
df_rand.Snapshot("rng_Tree", "rng.root", [ "rng" ])
print("Wrote demo root file to rng.root")

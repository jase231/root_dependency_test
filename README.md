# root_dependency_test
This repository serves to test the ROOT PyPI distribution to function as a dependency in other projects

`src/root_dependency_test_jase231/demo.py` runs a basic battery of common ROOT tasks, including RDataFrame branch and I/O operations, histogram plotting, and writing TCanvas to an image file.

# Setup instructions
- Create and source a virtual environment: `python3 -m venv venv && source venv/bin/activate`
- From project root, install the package with `pip install .`
- To test the demo functionality, run `python3 -m root_dependency_test_jase231.demo`, which should write a rendered histogram image and .root file to disk.

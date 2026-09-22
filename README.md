## Irish Film Institute's Command Line Interface

This is the second generation of the IFI's [suite of digital preservation scripts](https://github.com/Irish-Film-Institute/IFIscripts/), and is under active development. Goals of this refactor include:

1. Reducing repetition in the codebase
2. Improving O(n) cost of various actions (e.g. directory traversal)
3. Changing error handling, argument parsing, and other actions to be more consistent
4. Modularizing the code to permit tighter iterations on code changes, that is, allowing developers to receive quick feedback on code changes without waiting several hours for sipcreator.py to complete
5. Standardizing how the scripts output results (some info is sent to stdout, and some is written to a logfile)
6. Organizing functions such that they can be unit tested


### Installation and usage

This tool is currently a stub for specific steps in the Irish Film Institute digital preservation workflow, with functionality added in stages. The first package type to be supported will be Digital Cinema Packages (DCP), which is the format that films are distributed to cinemas for screening. 

To install this package, 

1. Clone the repository 
2. `$ cd` into the directory where you cloned the code
3. Create a python environment, e.g. `$ virtualenv venv`
4. Activate environment, e.g. `$ source ./venv/bin/activate`
5. Run `$ pip install -r requirements.txt`
6. Install the software. Because this software is under active development, the instructions are to install the tool *for local editing only*: `$  python -m pip install -e ./`

To invoke the tool, the root cli command is `$ ifidp` (for Irish Film Institute Digital Preservation). The two main arguments are:

`makesip`
`makeaip`

Any invocation of the packaging tool requires an `--input-directory` and an `--output-directory`, with short options of `-i` and `-o`, respectively. 

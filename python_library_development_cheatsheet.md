
## Here are some common steps for starting your own Python library

0. Create a fresh conda environment with the name of your library

1. Create a directory with name of our project / library

2. Create `setup.py` file which include version, description, etc.
  - A good idea would be copying / modifying an existing setup.py

3. Create package directory with the same name as our library (`aci`)

4. Add a `README.md` file 
  - I used a markdown file (`.md`) but this could be any text file
  - include `Description`, `Installation`, and `Usage` instructions

5. Add an `aci/__init__.py` which tells Python the `aci` directory is a Python package

6. Add `aci/core.py` file which will contain the meat of our code

7. Add imports to your `__init__.py` so users can easily access functions
   - `from aci.core import create_vrf`

8. Install library into environment
   - `python setup.py develop`




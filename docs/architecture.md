# Architecture Overview

- **common/**: shared logic  
  - `pin_checker.py`: common‑PIN lookup  
  - `demographics.py`: date‑based checks  
- **data/**: static resources (common PIN list)  
- **src/**: PartA–PartE scripts, each imports from `common/`  
- **.github/workflows/ci.yml**: CI pipeline that runs PartE tests  
- **run_all.sh**: convenience script orchestrating all scripts  

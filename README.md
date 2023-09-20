# research-base

This python library is a framework for programs that should include all the basics of a research project, including logging, correct environment and arguments loading, result keeping and more.

## Commands

`nix develop`: start the nix dev environment. 

`pytest src/tests/`: run all tests. Add flag `-s` for displaying captured logs.

`nix build .#devShells.x86_64-linux`: build ?

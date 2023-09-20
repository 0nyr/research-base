{
  description = "A python package for easy python programming for research projects.";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # import packages
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python311Packages;
      in
      {
        # Dev environment
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [
            # the environment.
            pythonPackages.python

            # python packages
            pythonPackages.python-dotenv
            pythonPackages.psutil

            # python dev packages
            pythonPackages.pytest
            pythonPackages.setuptools
          ];

          buildInputs = with pkgs; [ ];
        };

        # Python package definition
        packages.${system}.research-base = pkgs.pythonPackages.buildPythonPackage rec {
          pname = "research-base";
          version = "0.1.0";

          src = ./.;

          propagatedBuildInputs = with pkgs.pythonPackages; [
            # Add your dependencies here
            python-dotenv
          ];

          meta = with pkgs.lib; {
            description = "research-base python framework";
            license = licenses.mit;
          };
        };

        # Add this line to specify a default package
        defaultPackage.${system} = self.packages.${system}.research-base;
      }
    );
}

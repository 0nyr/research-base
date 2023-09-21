{
  description = "A python package for easy python programming for research projects.";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
  };

  outputs = { self, nixpkgs, ... }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    pythonPackages = pkgs.python311Packages;
  in {
    defaultPackage.${system} = pythonPackages.buildPythonPackage rec {
      pname = "research-base";
      version = "0.0.1";
      src = ./.;

      nativeBuildInputs = with pkgs; [
        pythonPackages.pip
        pythonPackages.setuptools
        pythonPackages.pytest
      ];

      propagatedBuildInputs = with pythonPackages; [
        python-dotenv
      ];

      meta = with pkgs.lib; {
        description = "research-base python framework";
        license = licenses.mit;
      };
    };

    devShells.${system} = pkgs.mkShell {
      nativeBuildInputs = with pythonPackages; [
        python
        pytest
      ];
    };
  };
}

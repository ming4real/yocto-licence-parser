#!/usr/bin/env python3

import argparse
import os.path
import sys

class Package:
    def __init__(self):
        self.package_name = None
        self.package_version = None
        self.recipe_name = None
        self.licenses = []

class Licenses:
    def __init__(self):
        self.licenses = {}
        self.packages = []

    def parseManifest(self, manifest):
        # Initialise a package object
        package = Package()
        with open(manifest) as file:
            for line in file:
                if line == "\n":
                    # New package
                    self.packages.append(package)
                    for license in package.licenses:
                        if not self.licenses.get(license):
                            self.licenses[license] = [package]
                        else:
                            self.licenses[license].append(package)
                    package = Package()

                else:
                    tmp = line.split(': ')
                    if tmp[0] == "PACKAGE NAME":
                        package.package_name = tmp[1].strip()
                    elif tmp[0] == "PACKAGE VERSION":
                        package.package_version = tmp[1].strip()
                    elif tmp[0] == "RECIPE NAME":
                        package.recipe_name = tmp[1].strip()
                    elif tmp[0] == "LICENSE":
                        package.licenses = tmp[1].strip().split(' & ')

    def printLicenses(self):
        for license, packages in self.licenses.items():
            print("{}:".format(license))
            for package in packages:
                print(package.package_name)

            print(" ")

    def printPackages(self, csv=False):
        join_string = " "
        if csv:
            join_string = ","
            print("Package Name,Version,Recipe,Licenses")
        for package in self.packages:
            print("{1}{0}{2}{0}{3}{0}{4}".format(join_string, package.package_name, package.package_version, package.recipe_name, " & ".join(package.licenses)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", help="Path to the licence.manifest file")
    parser.add_argument("-l", "--licenses", help="Show each licence type and which packgages use it", action="store_true")
    parser.add_argument("-p", "--packages", help="Show each package, version and license type", action="store_true")
    parser.add_argument("-c", "--csv", help="Display the output as CSV", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.manifest):
        print("{} does not exist".format(args.manifest))
        sys.exit()

    licenses = Licenses()
    licenses.parseManifest(args.manifest)

    if args.licenses:
        licenses.printLicenses()
    elif args.packages:
        licenses.printPackages(args.csv)

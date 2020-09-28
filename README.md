# Yocto License Manifest Parser

A Python script to parse the license.manifest file from a Yocto build and display the data in a more usage format.

## Usage
```bash
usage: yocto_licenses.py [-h] [-l] [-p] [-c] manifest

positional arguments:
  manifest        Path to the licence.manifest file

optional arguments:
  -h, --help      show this help message and exit
  -l, --licenses  Show each licence type and which packgages use it
  -p, --packages  Show each package, version and license type
  -c, --csv       Display the output as CSV
```

## Licenses

The Licenses option will display each license type followed by a list of packages that use that licence.

e.g.:

```bash
GPLv3+:
bash
findutils
parted
readline
 
GPLv2+:
bluez5
desktop-file-utils
ethtool
i2c-tools
...
```

## Packages

The Packages option will reformat the file so that each package is display on a single line with the version, recipe and license type.

The CSV option just uses CSV format to make it easier to import into a spreadsheet (which is why I wrote the code in the first place!)

e.g.:

```bash
Package Name,Version,Recipe,Licenses
base-files,3.0.14,base-files,GPLv2
base-passwd,3.5.29,base-passwd,GPLv2
bash,5.0,bash,GPLv3+
bluez5,5.54,bluez5,GPLv2+ & LGPLv2.1+
busybox,1.31.1,busybox,GPLv2 & bzip2-1.0.6
busybox-syslog,1.31.1,busybox,GPLv2 & bzip2-1.0.6
```

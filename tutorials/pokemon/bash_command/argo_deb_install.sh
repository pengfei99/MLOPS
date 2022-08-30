#!/bin/bash

# To run this script, you need to have sudo right
# Example 1: Without argument, it will install the default version(latest)
# sudo sh argo_deb_install.sh
#
# Example 2: With a version as argument, you can install a specific version
# sudo sh argo_deb_install.sh 3.1.3

default=3.3.5
if [ $# -eq 0 ]
  then
    current=$default
    echo "No arguments supplied, we will install the default(latest) version ${current} "
  else
    current=$1
    echo "We will install the given version ${current}"
fi
# Download the binary
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v${current}/argo-linux-amd64.gz

# Unzip
gunzip argo-linux-amd64.gz

# Make binary executable
chmod +x argo-linux-amd64

# Move binary to path
mv ./argo-linux-amd64 /usr/local/bin/argo

# Test installation
argo version
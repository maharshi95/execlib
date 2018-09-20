# Create a dir for binaries
rm -r bin
mkdir bin

# Create symbolic links
ln -sf $PWD/gpp.py bin/gpp
ln -sf $PWD/py.py bin/py

# Grant permission to execute
chmod +x bin/gpp
chmod +x bin/py

# Include in Environment PATH
echo "export PATH=$PATH:$PWD/bin" >> ~/.bashrc

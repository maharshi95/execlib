# Create a dir for binaries
rm -r bin
mkdir bin

chmod +x contest.sh

# Create symbolic links
ln -sf $PWD/gpp.py bin/gpp
ln -sf $PWD/py.py bin/py
ln -sf $PWD/contest.sh bin/contest

# Grant permission to execute
chmod +x bin/gpp
chmod +x bin/py

# Include in Environment PATH
echo "export PATH=$PATH:$PWD/bin" >> ~/.bashrc
echo "export PATH=$PATH:$PWD/bin" >> ~/.zshrc

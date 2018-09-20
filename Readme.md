execlib
--

#### A library for executing python projects and single program files for competetive programming questions.

### Installation:
```
    cd ~
    git clone https://github.com/maharshi95/execlib.git
    cd execlib && chmod +x setup.sh
    ./setup.sh
```

Add the following line to .bashrc or .zshrc file:
```
export PATH=$PATH:/path/to/execlib/bin
```

### Usage:
```
# Build and Executing a file and take inputs from console.
gpp <cpp-filename>.cpp        

# Build and Executing a file and take inputs from default input file path.
gpp <cpp-filename>.cpp -i     

# Build and Executing a file and take inputs from the given input file path.
gpp <cpp-filename>.cpp -i <path-to-input-file>
```
#### Executing C++ code:

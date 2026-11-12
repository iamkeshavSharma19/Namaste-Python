# ? First we need a Python Interpretor (Software)

# ? Byte Code is Mostly Hidden.But in some cases it is visible when you import methods from one file to another file i.e __pycache__

# & Along with Python there is one more thing which gets installed i.e Python VM.This is basically the Virtual Machine which actually runs your Byte Code.Byte Code is being fetched inside the Python Virtual Machine and inside this VM whole byte code is run.

# ? 1. Python code is being compiled to the Byte Code.Byte code is Low Level And Platform Independent.

# ? 2. Byte Code Runs faster because most of the parsing and checks have already been completed.


# ? 3. .pyc === Compiled Python [Byte Code].It is called frozen Binaries.

# ? 4. __pycache__ === 1.) The __pycache__ folder is an organizational directory created by Python to store compiled bytecode files (with a .pyc extension).

# ? 2.) Automated Management: Python automatically manages these files. If you modify your source code, Python uses diffing algorithms to detect changes and will recreate the necessary bytecode files. Source Change And Python Version === hello_chai.cpython-312.pyc

# ? cpython === There are diff. versions of python are there.Basically our standard python is cpython.

# ? Works only for imported files. Not for top level files.

# ?The Python Virtual Machine (PVM) is the runtime engine that executes Python code (12:12). Think of it as the 'engine' of your Python programs; just as a car requires an engine to run, Python requires this runtime environment to function (13:21).

# ? Key characteristics of the PVM include:

# ? Execution Loop: At its core, the PVM runs a continuous loop that fetches and executes code (12:24). When you feed it a script or bytecode, it processes those instructions from start to finish (12:35).
# ? Flexibility: The PVM is highly versatile because it can accept both high-level Python source code files and pre-compiled bytecode (12:47).
# ? Standardized Implementation: In the context of standard Python (often referred to as CPython), the PVM is the default engine that comes with your Python installation (13:54). It is the same underlying engine used by various environments like notebooks or command-line interfaces (14:02).
# ? Runtime Engine: Because it manages the execution of your code, it is formally known as a runtime engine or simply the Python interpreter (14:11).

# * The distinction between bytecode and machine code is fundamental to how Python executes instructions (14:46):

# * Bytecode: This is a low-level, platform-independent intermediate code (5:55). It is not a direct instruction set for your computer's hardware. Instead, it is designed to be interpreted or executed by a specific virtual machine, like the Python Virtual Machine (PVM) (15:18).

# * Machine Code: This is a low-level language that consists of direct instructions for the hardware (CPU). Unlike bytecode, machine code is specific to the architecture of the processor and hardware it runs on (14:58).

# * Essentially, bytecode acts as an abstraction layer. While machine code speaks directly to the silicon of your computer, bytecode requires an environment (the PVM) to translate those intermediate steps into actions the hardware can perform (15:24).


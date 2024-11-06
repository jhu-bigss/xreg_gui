Installation
============

System Requirements
-------------------

Before installing the BIGSS xreg GUI, ensure that your system meets the following requirements:

- **Operating System**: Linux, Windows, or macOS.
- **Python Version**: Python 3.6 or higher.
- **Dependencies**:
  - PyQt5
  - xreg library and its dependencies
  - PyInstaller (if building from source)
  - Other Python modules as specified in `requirements.txt` (if provided)

Installation Steps
-------------------

### Option 1: Using the Executable

The easiest way to use the BIGSS xreg GUI is by downloading the pre-built executable.

1. **Download the Executable**

   Obtain the executable file for your operating system from the official source or repository.

2. **Run the Executable**

   Double-click the executable file to launch the GUI.

### Option 2: Building from Source

If you prefer to build the GUI from source, follow these steps:

1. **Clone the Repository**

   .. code-block:: bash

      git clone https://github.com/yourusername/bigss_xreg_gui.git

2. **Install Dependencies**

   Navigate to the project directory and create a new conda environment (xreg_gui):

   .. code-block:: bash

      conda create -n xreg_gui python=3.8
      conda activate xreg_gui
      conda install pip

   Then, install the dependencies:

   .. code-block:: bash

      cd bigss_xreg_gui/gui
      pip install -r requirements.txt

3. **Run the GUI**

   Execute the following command to start the GUI:

   .. code-block:: bash

      python main.py


Downloading the pre-built Executable
------------------------------------


# TO BE ADDED
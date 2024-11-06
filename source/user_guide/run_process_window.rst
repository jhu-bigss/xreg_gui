Run Process Window
==================

The **Run Process Window** is where you execute the selected process using the provided configuration.

Overview
--------

.. figure:: images/run_process_window.png
   :align: center
   :width: 80%

   The Run Process Window for registration processes.


.. figure:: images/run_process_window_DRR.png
   :align: center
   :width: 80%

   The Run Process Window for DRR processes.

Components
----------

1. **XREG_BUILD_DIR Selection**

   - Displays the path to the XReg build directory.

2. **Executable Path Display**

   - Shows the path to the process executable based on the XReg build directory.

3. **Configuration File Selection**

   - The path to the configuration file. The default path is set to the exact same file that was generated in the **Configuration Window**. The current GUI version only supports the JSON format for configuration files.

4. **Verbose Checkbox**

   - Option to enable verbose output during process execution.

5. **Output Display (DRR generation only)**

   - A text area displaying real-time output from the process.


Notes
-----

- The **Run Process** button is enabled only when all required fields are valid. The process will check if the folder paths and the file formats are correct before execution.
- Output logs are saved automatically for future reference.


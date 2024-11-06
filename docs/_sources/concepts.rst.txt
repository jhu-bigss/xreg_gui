Key Concepts
============

This section introduces essential concepts related to medical image processing, DRR generation, and image registration to help new users understand the underlying processes.

Digital Reconstructed Radiograph (DRR)
--------------------------------------

A **Digital Reconstructed Radiograph (DRR)** is a simulated X-ray image generated from 3D volumetric data, such as CT scans. DRRs are used for:

- Preoperative planning.
- Image-guided surgery.
- Comparing with actual X-ray images for registration.

**How DRRs are Generated**

- A virtual X-ray source and detector are positioned relative to the 3D volume.
- Rays are cast through the volume, simulating attenuation based on the material properties.
- The resulting 2D projection is the DRR.


Image Registration
------------------

**Image Registration** is the process of aligning two or more images of the same scene taken at different times, from different viewpoints, or by different sensors.

**2D/3D Registration** involves aligning a 2D image (e.g., X-ray) with a 3D volume (e.g., CT scan), which is essential for image-guided interventions where preoperative 3D data is registered with intraoperative 2D images in order to achive tasks like (1) tracking the position of surgical tools in human body and assist with tool navigation, (2) accessing the surgery results, (3) visualizing the 3D volume in the same coordinate system as the 2D images (e.g. overlaying tools/lesions in 2D images), (4) AR applications.

**Types of Registration in the GUI**

- **Single-target Singleview Registration**

  Aligns a single target structure using one projection view.

- **Single-target Multiview Registration**

  Uses multiple views to improve alignment accuracy. In our current setup with the GUI we are using 3 views for multi-view registration.

Literature Review
------------------

TO BE ADDED

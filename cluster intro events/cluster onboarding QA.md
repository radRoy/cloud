creation date: 2023.02.20
Discussion (Thomas, Daniel W) about the sciencecloud portation & the central IT onboarding on this Wednesday.
The following questions stuck out as noteworthy.

meeting date (with Philip Shemella (philip.shemella@uzh.ch)): 2023.02.22, 1000 - 1100

Questions:
- are drivers preinstalled - nvidia/cuda for 2D unet via Fiji
  => Yes, the drivers are. Inside an instance you can install other CUDA versions, but the drivers are fixed (at least on the science cluster, I (DW) don't remember the specifics regarding the science cloud).
    => One can install new stuff within conda (or outside of conda), and then include the working/compatible installed version of CUDA in your conda (or mamba?) .yaml file.
    => (Can also create snapshots / image snapshots of your whole cloud instance, so .yaml s are not even always needed for sharing environments)
- Can T4s be parallelized:
  => No, just for testing purposes (the T4 nodes are not connected to each other with Infiniband, or some other equivalent data BUS system for connecting compute &/ data of multiple computer systems (nodes)).
cloud:
- single virtual machine (cloud instance)
- limit is 32 cores 256 gb ram (per instance, I suppose)
=> cluster has more resources

cluster...

beyond cluster: cscs: eiger:
>= 128 cores for sure, then it makes sense to discuss using eiger (/ cscs stuff)

- - -
Cluster vs. Cloud:
- difference is [mainly] in accessing them.
- Cloud: your isolated instance running on-demand permanently
- Cluster: shared, but more resources
  - slurm
- cluster: fyi, cores & gpus are not overbooked

cluster:
- multi gpu / node: will require specific code which you can/should/will come to us for help with hardware specifics
- slurm cscs & cluster: is the same slurm.

work with cluster:
- text editor, type your commands in a file first, to check them, then copy them into the cluster
- CLI for the cluster comm.

- do **not** run code on **login node**.
  - first go through the sbatch system ~ (TBD: potentially correct after the meeting)

`~$ quota`
Filesystems usage for user dwalth ( uid 891903425 ):
----------------------------------------------------------------------------
Directory                  Used/Limit        %                 files/(Limit)
----------------------------------------------------------------------------
/home/dwalth              154KB/15GB     (  0%)                   13/100000
/data/dwalth                 0B/200GB    (  0%)                    0
/scratch/dwalth              0B/20TB     (  0%)                    0

/shares/lienkamp.anatomy.uzh    0B                                      0
----------------------------------------------------------------------------
- home ...
- data:
  - store data
  - store virtual 'singularity' environments (container stuff)
  - nothing will be automatically / regularly wiped there
=> these 2 cost nothing
=> these 2 are on ssd and are fast
- scratch: temp. storage
  - where you store everything *while* working.
    - *after work* / at milestone, store data etc. on your */data drive*

- (? out of context snippet) ...share, lienkamp lab...: scalable file system (even bigger shit...)

- - -
QU: questions:

- word 'node' is always used for hardware, right?
  => Yes.
- I first copied training.tar straight into <shortname>@cluster.s3it.uzh.ch - but I can not find it... where is it, how to delete?
  => things that you are not supposed to (be able to) do: you can not do. so no need to delete, because it probably didn't get (/ shouldn't have gotten) copied, anyways
- diff. between squeue and sinfo? (and srun)
  => srun is "slurmrun"
    => btw: ...train #5 s3it.ch... dehte halt (?wat, was isch halt dehte zfinde? nvm)
  => squeue: shows every JOB individually.
  => sinfo: shows you all of the NODES.
- Can you scp only in one direction?
  => No, you can do it in both directions. But, for scp to work, you must be able to access the origin and destination location from where you run the command.
- ###() Here are the SBATCH parameters that you should always consider:
  - #SBATCH --time=0-00:05:00   ## days-hours:minutes:seconds  ## the time I request QU: max. for this job?
  - #SBATCH --mem 3000M         ## 3GB ram (hardware ratio is < 4GB/core)  ## how much you want QU: total memory allocated = max. for this job?
  => Yes, ~think of these requested quantities/resources as the upper limit of what you / your job have/has available.
- what is checkpointing?
  => got it. (relevant for when you are running really big jobs)
- conda vs. pip, etc.
  => **always first use conda install**, **`source activate <env>`** your env, **THEN use pip inside** it to install new modules.
  => https://stackoverflow.com/questions/65210378/im-learing-about-conda-environment-yml-and-im-not-sure-how-to-get-conda-to-fin

- self: 'full thorus'?
  => nvm, probably some way of interconnecting all the compute and data components within a node...
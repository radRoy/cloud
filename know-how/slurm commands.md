# slurm commands

Maybe also some other commands useful surrounding using slurm commands.

author: Daniel Walther  
creation date: 2023.04.02

If a session already exists & want to connect to that one:
```bash
srun --jobid=<jobid, some number>
sattach <jobid>.<step no.>  # also works, prefer this one
```

`squeue` gives info about the slurm jobs
`squeue -s -u <username>` returns current jobs of the given user (-u), and displays all job steps, too (-s).
`sinfo` gives info about the nodes of a computing center
`sbatch` makes it possible to run scripted job requests connected with bash scripts, instead of using `srun` with interactive sessions.
`<commands> &` puts the output into the background (i.e., does not show it, maybe some finished running message or fail message or so, idk)
`screen` is useful for running multiple shell sessions in parallel and navigating between them. can also leave something running on a server, leave the screen session, leave this computer's terminal and open it all on another computer. also very useful to prevent network connection problems interrupting a running program.
`screen -S <name>` creates a new shell session
`<ctrl + A + D>` detaches from the currently active session
`tmux` does similar things like `screen` does.
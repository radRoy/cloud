```bash
screen -S test-srun-insertYourSesionName
	# inside that screen shell session
	top  # shows and updates every second the resources of the system (node or whole cluster, idk)
		# can press <CTRL + Z> to put any running foreground process to the background
		# bg  # then shows the backgrounded processes
		# fg  # puts (some?) bg process into the foreground
	# press <CTRL + A + D> to detach from this session. whether something is running or not.
screen -ls
screen -x test-srun
```
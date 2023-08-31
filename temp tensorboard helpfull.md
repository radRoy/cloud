# title temp


(3dunet) dwalth@u20-login-1:~$ tensorboard --helpfull
TensorFlow installation not found - running with reduced feature set.
usage: tensorboard [-h] [--helpfull] [--logdir PATH] [--logdir_spec PATH_SPEC] [--host ADDR] [--bind_all] [--port PORT] [--reuse_port BOOL]
                   [--load_fast {false,auto,true}] [--extra_data_server_flags EXTRA_DATA_SERVER_FLAGS] [--grpc_creds_type {local,ssl,ssl_dev}]
                   [--grpc_data_provider PORT] [--purge_orphaned_data BOOL] [--db URI] [--db_import] [--inspect] [--version_tb] [--tag TAG]
                   [--event_file PATH] [--path_prefix PATH] [--window_title TEXT] [--max_reload_threads COUNT] [--reload_interval SECONDS]
                   [--reload_task TYPE] [--reload_multifile BOOL] [--reload_multifile_inactive_secs SECONDS] [--generic_data TYPE]
                   [--samples_per_plugin SAMPLES_PER_PLUGIN] [--detect_file_replacement BOOL]
                   {serve,dev} ...

TensorBoard is a suite of web applications for inspecting and understanding your TensorFlow runs and graphs. https://github.com/tensorflow/tensorboard

positional arguments:
  {serve,dev}           TensorBoard subcommand (defaults to 'serve')
    serve               start local TensorBoard server (default subcommand)
    dev                 upload data to TensorBoard.dev

options:
  -h, --help            show this help message and exit
  --helpfull            show full help message and exit
  --logdir PATH         Directory where TensorBoard will look to find TensorFlow event files that it can display. TensorBoard will recursively walk the
                        directory structure rooted at logdir, looking for .*tfevents.* files. A leading tilde will be expanded with the semantics of
                        Python's os.expanduser function.
  --logdir_spec PATH_SPEC
                        Like `--logdir`, but with special interpretation for commas and colons: commas separate multiple runs, where a colon specifies a
                        new name for a run. For example: `tensorboard --logdir_spec=name1:/path/to/logs/1,name2:/path/to/logs/2`. This flag is discouraged
                        and can usually be avoided. TensorBoard walks log directories recursively; for finer-grained control, prefer using a symlink tree.
                        Some features may not work when using `--logdir_spec` instead of `--logdir`.
  --host ADDR           What host to listen to (default: localhost). To serve to the entire local network on both IPv4 and IPv6, see `--bind_all`, with
                        which this option is mutually exclusive.
  --bind_all            Serve on all public interfaces. This will expose your TensorBoard instance to the network on both IPv4 and IPv6 (where available).
                        Mutually exclusive with `--host`.
  --port PORT           Port to serve TensorBoard on. Pass 0 to request an unused port selected by the operating system, or pass "default" to try to bind
                        to the default port (6006) but search for a nearby free port if the default port is unavailable. (default: "default").
  --reuse_port BOOL     Enables the SO_REUSEPORT option on the socket opened by TensorBoard's HTTP server, for platforms that support it. This is useful
                        in cases when a parent process has obtained the port already and wants to delegate access to the port to TensorBoard as a
                        subprocess.(default: False).
  --load_fast {false,auto,true}
                        Use alternate mechanism to load data. Typically 100x faster or more, but only available on some platforms and invocations.
                        Defaults to "auto" to use this new mode only if available, otherwise falling back to the legacy loading path. Set to "true" to
                        suppress the advisory note and hard-fail if the fast codepath is not available. Set to "false" to always fall back.
                        Feedback/issues: https://github.com/tensorflow/tensorboard/issues/4784 (default: auto)
  --extra_data_server_flags EXTRA_DATA_SERVER_FLAGS
                        Experimental. With `--load_fast`, pass these additional command-line flags to the data server. Subject to POSIX word splitting per
                        `shlex.split`. Meant for debugging; not officially supported.
  --grpc_creds_type {local,ssl,ssl_dev}
                        Experimental. The type of credentials to use to connect to the data server. (default: local)
  --grpc_data_provider PORT
                        Experimental. Address of a gRPC server exposing a data provider. Set to empty string to disable. (default: )
  --purge_orphaned_data BOOL
                        Whether to purge data that may have been orphaned due to TensorBoard restarts. Setting --purge_orphaned_data=False can be used to
                        debug data disappearance. (default: True)
  --db URI              [experimental] sets SQL database URI and enables DB backend mode, which is read-only unless --db_import is also passed.
  --db_import           [experimental] enables DB read-and-import mode, which in combination with --logdir imports event files into a DB backend on the
                        fly. The backing DB is temporary unless --db is also passed to specify a DB path to use.
  --inspect             Prints digests of event files to command line. This is useful when no data is shown on TensorBoard, or the data shown looks weird.
                        Must specify one of `logdir` or `event_file` flag. Example usage: `tensorboard --inspect --logdir mylogdir --tag loss` See
                        tensorboard/backend/event_processing/event_file_inspector.py for more info.
  --version_tb          Prints the version of Tensorboard
  --tag TAG             tag to query for; used with --inspect
  --event_file PATH     The particular event file to query for. Only used if --inspect is present and --logdir is not specified.
  --path_prefix PATH    An optional, relative prefix to the path, e.g. "/path/to/tensorboard". resulting in the new base url being located at
                        localhost:6006/path/to/tensorboard under default settings. A leading slash is required when specifying the path_prefix. A trailing
                        slash is optional and has no effect. The path_prefix can be leveraged for path based routing of an ELB when the website base_url
                        is not available e.g. "example.site.com/path/to/tensorboard/".
  --window_title TEXT   changes title of browser window
  --max_reload_threads COUNT
                        The max number of threads that TensorBoard can use to reload runs. Not relevant for db read-only mode. Each thread reloads one run
                        at a time. (default: 1)
  --reload_interval SECONDS
                        How often the backend should load more data, in seconds. Set to 0 to load just once at startup. Must be non-negative. (default:
                        5.0)
  --reload_task TYPE    [experimental] The mechanism to use for the background data reload task. The default "auto" option will conditionally use threads
                        for legacy reloading and a child process for DB import reloading. The "process" option is only useful with DB import mode. The
                        "blocking" option will block startup until reload finishes, and requires --load_interval=0. (default: auto)
  --reload_multifile BOOL
                        [experimental] If true, this enables experimental support for continuously polling multiple event files in each run directory for
                        newly appended data (rather than only polling the last event file). Event files will only be polled as long as their most recently
                        read data is newer than the threshold defined by --reload_multifile_inactive_secs, to limit resource usage. Beware of running out
                        of memory if the logdir contains many active event files. (default: false)
  --reload_multifile_inactive_secs SECONDS
                        [experimental] Configures the age threshold in seconds at which an event file that has no event wall time more recent than that
                        will be considered an inactive file and no longer polled (to limit resource usage). If set to -1, no maximum age will be enforced,
                        but beware of running out of memory and heavier filesystem read traffic. If set to 0, this reverts to the older last-file-only
                        polling strategy (akin to --reload_multifile=false). (default: 86400 - intended to ensure an event file remains active if it
                        receives new data at least once per 24 hour period)
  --generic_data TYPE   [experimental] Hints whether plugins should read from generic data provider infrastructure. For plugins that support only the
                        legacy multiplexer APIs or only the generic data APIs, this option has no effect. The "auto" option enables this only for plugins
                        that are considered to have stable support for generic data providers. (default: auto)
  --samples_per_plugin SAMPLES_PER_PLUGIN
                        An optional comma separated list of plugin_name=num_samples pairs to explicitly specify how many samples to keep per tag for that
                        plugin. For unspecified plugins, TensorBoard randomly downsamples logged summaries to reasonable values to prevent out-of-memory
                        errors for long running jobs. This flag allows fine control over that downsampling. Note that if a plugin is not specified in this
                        list, a plugin-specific default number of samples will be enforced. (for example, 10 for images, 500 for histograms, and 1000 for
                        scalars). Most users should not need to set this flag.
  --detect_file_replacement BOOL
                        [experimental] If true, this enables experimental support for detecting when event files are replaced with new versions that
                        contain additional data. This is not needed in the normal case where new data is either appended to an existing file or written to
                        a brand new file, but it arises, for example, when using rsync without the --inplace option, in which new versions of the original
                        file are first written to a temporary file, then swapped into the final location. This option is currently incompatible with
                        --load_fast=true, and if passed will disable fast-loading mode. (default: false)

absl.app:
  -?,--[no]help: show this help
    (default: 'false')
  --[no]helpfull: show full help
    (default: 'false')
  --[no]helpshort: show this help
    (default: 'false')
  --[no]helpxml: like --helpfull, but generates XML output
    (default: 'false')
  --[no]only_check_args: Set to true to validate args and exit.
    (default: 'false')
  --[no]pdb: Alias for --pdb_post_mortem.
    (default: 'false')
  --[no]pdb_post_mortem: Set to true to handle uncaught exceptions with PDB post mortem.
    (default: 'false')
  --profile_file: Dump profile information to a file (for python -m pstats). Implies --run_with_profiling.
  --[no]run_with_pdb: Set to true for PDB debug mode
    (default: 'false')
  --[no]run_with_profiling: Set to true for profiling the script. Execution will be slower, and the output format might change over time.
    (default: 'false')
  --[no]use_cprofile_for_profiling: Use cProfile instead of the profile module for profiling. This has no effect unless --run_with_profiling is set.
    (default: 'true')

absl.logging:
  --[no]alsologtostderr: also log to stderr?
    (default: 'false')
  --log_dir: directory to write logfiles into
    (default: '')
  --logger_levels: Specify log level of loggers. The format is a CSV list of `name:level`. Where `name` is the logger name used with `logging.getLogger()`,
    and `level` is a level name  (INFO, DEBUG, etc). e.g. `myapp.foo:INFO,other.logger:DEBUG`
    (default: '')
  --[no]logtostderr: Should only log to stderr?
    (default: 'false')
  --[no]showprefixforinfo: If False, do not prepend prefix to info messages when it's logged to stderr, --verbosity is set to INFO level, and python logging
    is used.
    (default: 'true')
  --stderrthreshold: log messages at this level, or more severe, to stderr in addition to the logfile.  Possible values are 'debug', 'info', 'warning',
    'error', and 'fatal'.  Obsoletes --alsologtostderr. Using --alsologtostderr cancels the effect of this flag. Please also note that this flag is subject
    to --verbosity and requires logfile not be stderr.
    (default: 'fatal')
  -v,--verbosity: Logging verbosity level. Messages logged at this level or lower will be included. Set to 1 for debug logging. If the flag was not set or
    supplied, the value will be changed from the default of -1 (warning) to 0 (info) after flags are parsed.
    (default: '-1')
    (an integer)

absl.flags:
  --flagfile: Insert flag definitions from the given file into the command line.
    (default: '')
  --undefok: comma-separated list of flag names that it is okay to specify on the command line even if the program does not define a flag with that name.
    IMPORTANT: flags in this list that have arguments MUST use the --flag=value format.
    (default: '')

#!/usr/bin/env bash
#
# Copyright (C) 2016 Francesco Lumachi <francesco.lumachi@gmail.com>

# If no args provided, show usage
if [[ $# -eq 0 ]]
then
    echo 'Usage: bkgjob <command plus args to instantiate>'
    exit 0
fi

cmd="$@"        # Command to launch in background with args

# If "sudo" is used for 1st time, need to call a dummy sudo (if not, sudo runned
# in background can't prompt for pwd). Moreover, background process will be
# killed only calling "sudo kill <pid>"
isSudo=""         # False
if [[ $1 == "sudo" ]]
then
  sudo echo "" >/dev/null
  isSudo="sudo "  # True
fi

# Python need "-u" (unbuffered) to output while computing
if [[ $1 == "python" ]]
then
  cmd=${cmd/python/python -u}
fi

# Execute in background, redirect output(1) and error(2) to <cmd>.log file
nohup $cmd 1>${cmd// /_}.log 2>&1 &
echo Job \"$cmd\" started.
echo - Use \"less ${cmd// /_}.log\" to inspect output/error.
echo - Use \"${isSudo}kill $!\" to terminate if required.

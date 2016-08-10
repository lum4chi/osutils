#!/usr/bin/env bash
#
# Copyright (C) 2016 Francesco Lumachi <francesco.lumachi@gmail.com>

rsync -aAXv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/data/*" "/backup/*", "/lost+found"} / /backup

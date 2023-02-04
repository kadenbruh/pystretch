#!/usr/bin/env bash
source config.sh

xrandr --output $monitor --primary --mode $monitor_maxres --scale-from $stretched_res --rate $refresh_rate

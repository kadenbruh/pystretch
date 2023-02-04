#!/usr/bin/env bash
source config.sh

xrandr --output $monitor --primary --mode $monitor_maxres --transform none --rate $refresh_rate

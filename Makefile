# Makefile for source rpm: device-mapper-multipath
# $Id$
NAME := device-mapper-multipath
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common

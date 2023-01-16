#!/bin/bash
# Checksum function in bash

calc_checksum () {
    return_value=$( cksum $1 )
    echo $return_value
}

checksum=$( calc_checksum $1 )

echo $checksum
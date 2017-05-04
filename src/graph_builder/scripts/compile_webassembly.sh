#!/bin/bash

set -e # exit on error

TOTAL_MEMORY=${2:-16777216}

emcc "$1" -O3 -s "EXPORTED_FUNCTIONS=['_run','_init','_get_weight_buffer','_get_data_buffer']" -s "WASM=1" -s TOTAL_MEMORY=$TOTAL_MEMORY --pre-js `dirname "$0"`/webassembly_header.js -o "${1%.*}.js"
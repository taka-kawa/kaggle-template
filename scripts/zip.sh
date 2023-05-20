#!/bin/bash

while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --target)
            target="$2"
            shift
            shift
            ;;
        *)
            echo "Unknown option: $key"
            exit 1
            ;;
    esac
done

if [ -z "$target" ]; then
    echo "Please specify a target directory with --target option"
    exit 1
fi

if [ "$target" == "src" ]; then
    rm -f src.zip
    zip -r src.zip src run.py config
    echo "src.zip created successfully"
elif [ "$target" == "model" ]; then
    rm -f model.zip
    zip -r model.zip model data/feature
    echo "model.zip created successfully"
elif [ "$target" == "lib" ]; then
    rm -f lib.zip
    zip -r lib.zip lib
    echo "lib.zip created successfully"
else
    echo "Unknown target directory: $target"
    exit 1
fi

#!/bin/bash

# Load env KAGGLE_USERNAME, KAGGLE_KEY
if [ -f .env ]; then
    source .env
else
    echo "No .env file found"
    exit 1
fi

# Set env
export KAGGLE_USERNAME=$KAGGLE_USERNAME
export KAGGLE_KEY=$KAGGLE_KEY


COMPETETION='psp-test'
FIRST=false


# Create zip file
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --target)
            TARGET="$2"
            shift
            shift
            ;;
        --first)
            FIRST=true
            shift
            ;;
        *)
            echo "Unknown option: $key"
            exit 1
            ;;
    esac
done

bash ./scripts/zip.sh --target $TARGET

# Make a dataset directory
DATASET_DIR=${TARGET}-upload
mkdir $DATASET_DIR

# zip ファイルの移動
mv ${TARGET}.zip $DATASET_DIR

# Make a metadata file
echo '{
  "licenses": [
    {
      "name": "CC0-1.0"
    }
  ],
  "title": "'${COMPETETION}'-'${TARGET}'",
  "id": "ta6ka4shi/'${COMPETETION}'-'${TARGET}'",
  "subtitle":"'${TARGET}' Dataset for Kaggle",
  "description": "This is a description of '${TARGET}' dataset."
}' > $DATASET_DIR/dataset-metadata.json

# Kaggle へのアップデート
if $FIRST ; then
  kaggle datasets create -p $DATASET_DIR
else
  kaggle datasets version -p $DATASET_DIR -m "Updated $TARGET"
fi

# Dataset ディレクトリの削除
rm -r $DATASET_DIR


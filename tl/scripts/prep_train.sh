#! /bin/bash
# AUM SHREEGANESHAAYA NAMAH||

XML_DIR=/home/ishanhmisra/Downloads/659_data/train_rgb/rgb/train/traffic_light_xmls
IMG_DIR=/home/ishanhmisra/Downloads/659_data/train_rgb/rgb/train/traffic_light_images

TEST_PERC=0.2 # percentage of files that may be used for testing in the future

ls -d "$XML_DIR"/* > ../xml_list.txt

declare -a Train
declare -a Test

for file in ./*
do
  Train=(${Train[*]} $(realpath "$file"))
done

testLeft=$(bc <<<  "(${#Train[@]} * $TEST_PERC)/1")

while [ $testLeft -ge 1 ]
do
	index=$(shuf -i 1-${#Train[@]} -n 1)
	tomove=${Train[$(bc -l <<< "$index - 1")]}
	Train=(${Train[@]/$tomove})
	Test=(${Test[*]} $tomove)
	testLeft=$(bc -l <<< "$testLeft - 1")
done

for item in "${Train[@]}"
do
  echo "$item" >> data_train.txt
done

for item in "${Test[@]}"
do
  echo "$item" >> data_test.txt
done

# after this script, run data_get.py manually

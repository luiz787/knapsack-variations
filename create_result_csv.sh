#!/bin/bash
for file in dataset/low-dimensional/*; do
    backtracking_output=$(python3 src/main.py $file backtracking)
    branch_and_bound_output=$(python3 src/main.py $file branch_and_bound)

    line_backtracking="$file;Luiz Augusto Dias Berto;$backtracking_output;backtracking"
    echo $line_backtracking >> output.csv
    line_branch_and_bound="$file;Luiz Augusto Dias Berto;$branch_and_bound_output;branch_and_bound"
    echo $line_branch_and_bound >> output.csv
done

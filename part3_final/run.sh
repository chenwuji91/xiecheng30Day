python ensemble.py part1result.csv part2result.csv part3_base.csv
mkdir result
mv part3_base.csv result
cd ../part2_final/code
python fit_spring.py
python wave.py

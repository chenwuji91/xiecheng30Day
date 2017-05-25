rm featuremap
#python scripts/feature1.py datapoint/datapoint.all tmp/feature1
#python scripts/feature2.py data/newhotelstaticinfo.csv datapoint/datapoint.all tmp/feature2
#python scripts/feature3.py data/hotelminprice_comp.csv datapoint/datapoint.all tmp/feature3
#python scripts/feature4.py datapoint/firstappear_notzero datapoint/datapoint.all tmp/feature4
#python scripts/feature5.py datapoint/firstappear_notzero data/inHtl_cii_compfz.csv datapoint/datapoint.all tmp/feature5
#if false;then
python scripts/getnewhtlinfo.py data/htlinfo.csv data/newhtlinfo.csv
python scripts/findfirstappear.py data/hotelminprice_comp.csv datapoint/firstappear
python scripts/gettrainpoint.py data/htlcii.csv data/htlpredlist.csv datapoint/firstappear datapoint/datapoint.train
python scripts/getvalidpoint.py data/htlcii.csv data/htlpredlist.csv datapoint/firstappear datapoint/datapoint.valid
python scripts/gettestpoint.py data/htlcii.csv data/htlpredlist.csv datapoint/datapoint.test
python scripts/getallpoint.py datapoint/datapoint.train datapoint/datapoint.valid datapoint/datapoint.test datapoint/datapoint.all
python scripts/yunhaitrick.py data/htlcii.csv datapoint/firstappear data/htlpredlist.csv tmpresults/baseresult.csv

python scripts/feature1.py data/htlcii.csv tmp/feature1
python scripts/feature2.py data/newhtlinfo.csv datapoint/datapoint.all tmp/feature2
python scripts/feature3.py data/htlprice.csv datapoint/datapoint.all tmp/feature3
python scripts/feature5.py data/htlcii.csv datapoint/datapoint.all tmp/feature5
python scripts/feature6.py data/htlcii.csv datapoint/datapoint.all tmp/feature6
echo "join"
for i in train valid test
do
	python scripts/join.py datapoint/datapoint.$i tmp/feature1 tmp/join_1.$i
	python scripts/join.py tmp/join_1.$i tmp/feature2 tmp/join_2.$i
	python scripts/join.py tmp/join_2.$i tmp/feature3 tmp/join_3.$i
	python scripts/join.py tmp/join_3.$i tmp/feature5 tmp/join_4.$i
	python scripts/join.py tmp/join_4.$i tmp/feature6 tmp/join.$i
	python scripts/feature_map.py tmp/join.$i $i/$i featuremap
done
#fi
#if false;then
echo "train"
num=0
for md in 4 5 6
do
for lr in 0.05 0.07 0.03
do
for nest in 100 150 200 
do
echo $md,$lr,$nest
python scripts/train.py train/train valid/valid valid/valid_pred test/test test/test_pred $md $lr $nest
paste -d ',' test/test_sampleid test/test_pred > tmpresults/tmpresult.csv
python scripts/makeresult.py tmpresults/tmpresult.csv tmpresults/result_$num.csv
num=$[num+1]
done
done
done
python scripts/ensemble_step1.py tmpresults/result 27 tmpresults/ensembresult.csv
python scripts/makepart1res.py tmpresults/baseresult.csv tmpresults/ensembresult.csv part1result.csv
rm tmp/join*
#fi

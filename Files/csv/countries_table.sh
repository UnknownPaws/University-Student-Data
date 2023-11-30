# First line function call
echo "INSERT INTO countries(" > countriestable.txt
cut -f1,9 -d, education_expenditure.csv | egrep "2011"  >> countriestable.txt
sed -Ei.bak "s/2011/gdp_percent/" countriestable.txt
echo ") VALUES\n" >> countriestable.txt
tr "\r" "\n" < countriestable.txt > temp.txt
mv temp.txt countriestable.txt
tr -d "\n" < countriestable.txt > temp.txt
mv temp.txt countriestable.txt
echo "" >> countriestable.txt

# Data input
egrep -v "2011" education_expenditure.csv | cut -f1,9 -d, > temp.txt
sed -Ei.bak "s/^(.+),/('\1',/g" temp.txt
sed -Ei.bak "s/$/),/g" temp.txt
tr "\r" "\n" < temp.txt > temp2.txt
mv temp2.txt temp.txt
tr -d "\n" < temp.txt > temp2.txt
mv temp2.txt temp.txt
sed -Ei.bak "s/,$/;/" temp.txt
sed -Ei.bak "s/),/),\n/g" temp.txt
sed -Ei.bak "s/',)/',NULL)/g" temp.txt
egrep "\(" temp.txt >> countriestable.txt
rm temp.txt
rm temp.txt.bak
rm countriestable.txt.bak

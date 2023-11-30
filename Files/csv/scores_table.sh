# First line function call
echo "INSERT INTO scores(" > scorestable.txt
cut -f1,8,9 -d, student_scores.csv | egrep "^\D"  >> scorestable.txt
echo ") VALUES\n" >> scorestable.txt
tr -d "\n" < scorestable.txt > temp.txt
mv temp.txt scorestable.txt
echo "" >> scorestable.txt

# Data input
egrep "^\d" student_scores.csv | cut -f1,8,9 -d, > temp.txt
sed -Ei.bak "s/^/(/g" temp.txt
sed -Ei.bak "s/$/),/g" temp.txt
tr -d "\n" < temp.txt > temp2.txt
mv temp2.txt temp.txt
sed -Ei.bak "s/,$/;/" temp.txt
sed -Ei.bak "s/),/),\n/g" temp.txt
egrep "\(" temp.txt >> scorestable.txt
rm temp.txt
rm temp.txt.bak

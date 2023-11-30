# First line function call
echo "INSERT INTO students(" > studenttable.txt
cut -f1-6 -d, student_scores.csv | egrep "^\D"  >> studenttable.txt
echo ") VALUES\n" >> studenttable.txt
tr -d "\n" < studenttable.txt > temp.txt
mv temp.txt studenttable.txt
echo "" >> studenttable.txt

# Data input
egrep "^\d" student_scores.csv | cut -f1-6 -d, > temp.txt
sed -Ei.bak "s/,/','/g" temp.txt
sed -Ei.bak "s/([0-9])',/\1,/g" temp.txt
sed -Ei.bak "s/^/(/g" temp.txt
sed -Ei.bak "s/$/'),/g" temp.txt
tr -d "\n" < temp.txt > temp2.txt
mv temp2.txt temp.txt
sed -Ei.bak "s/,$/;/" temp.txt
sed -Ei.bak "s/),/),\n/g" temp.txt
egrep "\(" temp.txt >> studenttable.txt
rm temp.txt
rm temp.txt.bak

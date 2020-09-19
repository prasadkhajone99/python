for x in {10..1}
do
echo $x
x=`expr $x - 2`
echo $x
echo "In loop"
done

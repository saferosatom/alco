comm=(date +%Y%m%d%H%M%S)
#$comm="\""+$comm+"\"
#echo {$comm}
git add .
git commit -m "{$comm}"

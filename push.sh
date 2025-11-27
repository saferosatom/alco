#if [ -z %1 ]; then
    comm=$(date +%Y%m%d%H%M%S)
#else
#    comm=$1
#fi

git add .
git commit -m "$comm"
git push -u origin main

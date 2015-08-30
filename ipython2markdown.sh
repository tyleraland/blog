#!/bin/bash

CONTENT=$1
NOTEBOOKS=$2

cd $NOTEBOOKS
for NOTEBOOK in *.ipynb; do
    NAME=$(basename $NOTEBOOK .ipynb)
    ipython nbconvert ${NOTEBOOK} --to markdown
    if [[ -d ../content/images/${NAME}_files ]]; then
        rm -R ../content/images/${NAME}_files
    fi
    mv -f ${NAME}_files ../content/images/
    echo "title: ${NAME}" > ../content/${NAME}.md
    echo "date: `date '+%Y-%m-%d'`" >> ../content/${NAME}.md
    echo "category: tech" >> ../content/${NAME}.md
    sed "s/${NAME}_files/{attach}\/images\/${NAME}_files/g" ${NAME}.md >> ../content/${NAME}.md
    rm ${NAME}.md
done

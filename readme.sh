#!/bin/bash

markdown readme.md > readme/readme.html
cp readme/readme.html readme/readme.anki
sed -i 's/h1/b/g' readme/readme.anki
sed -i 's/h2/b/g' readme/readme.anki
sed -i 's/h3/b/g' readme/readme.anki
sed -i 's/strong/b/g' readme/readme.anki
sed -i 's/<p>//g' readme/readme.anki
sed -i 's/<\/p>//g' readme/readme.anki
sed -i 's/<br>//g' readme/readme.anki
sed -i 's/<\/br>//g' readme/readme.anki
fold -w 80 -s readme.md > readme/readme.txt

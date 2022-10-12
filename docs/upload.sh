gitbook build ./ docs
sleep 1
git add . 
git commit -m "update"
git push -u origin master
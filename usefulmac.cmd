du -k -I Library ~/* | awk '$1 > 500000' | sort -nr  #find folders larger than 500000

import pdfkit




def golaw(list_no):
    base_url = 'https://zh.wikipedia.org'
    flist = open('{}.txt'.format(list_no) , 'r')
    target = flist.readlines()
    for count, i in enumerate(target):
        tgt=base_url + str(i)
        pdfkit.from_url(tgt, 'out.pdf')
        counts = count+1
        print ('No. {} Cases; id {}'.format(counts, i)) 

    print ('Get {} Cases from this round'.format(counts))
#    with open('test3.csv', 'a') as f:
#        writer = csv.writer(f)
#        writer.writerow(['Title', 'Content'])
#        writer.writerow(['Webpage',tgt])
#        for row in articles:
#            writer.writerow(row)


#list_file=['list105_11']

list_file=['wiki_link_1']


for count1, listno in enumerate(list_file):
    counts1=count1+1
    print ('--- Starting No. {} round... ---'.format(counts1))
    golaw(listno)
    print ('--- No. {} round END... ---'.format(counts1))
    print("--- %s seconds ---" % (time.time() - start_time))


print("--- %s seconds ---" % (time.time() - start_time))






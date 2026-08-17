---
title: Python에서 PDF 파일을 개별 페이지로 분할
linktitle: Python에서 PDF 파일을 개별 페이지로 분할
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
description: Aspose.PDF를 사용하여 Python에서 PDF를 개별 페이지로 분할하여 페이지를 쉽게 추출하고 관리하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 개별 페이지로 분할하려면 **SplitAllPages** 클래스를 호출하기만 하면 됩니다.


```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **Split Pages(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)

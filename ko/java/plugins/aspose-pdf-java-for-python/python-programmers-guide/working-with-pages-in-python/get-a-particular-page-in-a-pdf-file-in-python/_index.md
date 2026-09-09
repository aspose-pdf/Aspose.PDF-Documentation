---
title: Python에서 PDF 파일의 특정 페이지 가져오기
linktitle: Python에서 PDF 파일의 특정 페이지 가져오기
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
description: 자세한 문서 처리를 위해 Aspose.PDF를 사용하여 Python의 PDF 파일에서 특정 페이지를 추출하는 방법을 살펴보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 특정 페이지를 가져오려면 **GetPage** 클래스를 호출하기만 하면 됩니다.


```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 
**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 **Get Page(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)

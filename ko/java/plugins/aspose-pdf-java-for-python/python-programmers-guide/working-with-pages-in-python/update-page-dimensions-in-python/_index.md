---
title: Python에서 페이지 차원 업데이트
linktitle: Python에서 페이지 차원 업데이트
type: docs
weight: 90
url: /java/update-page-dimensions-in-python/
description: 더 나은 문서 레이아웃 제어를 위해 Aspose.PDF를 사용하여 Python에서 PDF 문서 내의 페이지 크기를 업데이트하는 방법을 이해합니다.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 페이지 차원을 업데이트하려면 **UpdatePageDimensions** 클래스를 호출하기만 하면 됩니다.


```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```


**실행 코드 다운로드**



아래 언급된 소셜 코딩 사이트에서 В **업데이트 페이지 크기(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)

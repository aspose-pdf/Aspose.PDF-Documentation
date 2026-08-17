---
title: Python의 PDF 파일에서 특정 페이지 삭제
linktitle: Python의 PDF 파일에서 특정 페이지 삭제
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: 효율적인 문서 편집을 제공하는 Aspose.PDF를 사용하여 Python의 PDF 문서에서 특정 페이지를 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서에서 특정 페이지를 삭제하려면 **DeletePage** 클래스를 호출하면 됩니다.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **페이지 삭제(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)

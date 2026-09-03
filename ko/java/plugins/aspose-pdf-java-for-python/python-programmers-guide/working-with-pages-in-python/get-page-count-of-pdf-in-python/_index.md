---
title: Python에서 PDF의 페이지 수 가져오기
linktitle: Python에서 PDF의 페이지 수 가져오기
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-python/
description: 정확한 문서 분석을 위해 Aspose.PDF를 사용하여 Python에서 PDF 문서의 총 페이지 수를 검색하는 방법을 이해합니다.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 페이지 수를 얻으려면 **GetNumberOfPages** 클래스를 호출하기만 하면 됩니다.


```Python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "Page Count:" . page_count

```


**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드**페이지 수 가져오기(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)

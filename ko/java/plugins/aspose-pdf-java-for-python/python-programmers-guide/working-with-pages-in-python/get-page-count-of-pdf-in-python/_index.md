---
title: 파이썬에서 PDF의 페이지 수 얻기
type: docs
weight: 40
url: /ko/java/get-page-count-of-pdf-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 페이지 수를 얻으려면, **GetNumberOfPages** 클래스를 호출하세요.

```Python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "페이지 수:" . page_count

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get Page Count (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)
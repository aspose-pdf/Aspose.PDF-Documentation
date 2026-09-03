---
title: Python에서 PDF 파일 정보 얻기
linktitle: Python에서 PDF 파일 정보 얻기
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: 문서 관리를 위해 Aspose.PDF를 사용하여 Python에서 메타데이터 및 속성과 같은 자세한 PDF 파일 정보를 검색하는 방법을 살펴보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 파일 정보를 얻으려면 **GetPdfFileInfo** 클래스를 호출하면 됩니다.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```


**실행 코드 다운로드**

다운로드В **PDF 파일 정보(Aspose.PDF)**В를 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)

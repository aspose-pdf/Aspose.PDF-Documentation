---
title: 파이썬에서 PDF 파일 정보 얻기
type: docs
weight: 40
url: ko/java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 Pdf 문서의 파일 정보를 얻으려면, **GetPdfFileInfo** 클래스를 호출하십시오.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 문서 정보 가져오기
doc_info = doc.getInfo();

# 문서 정보 표시
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get PDF File Information (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
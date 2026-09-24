---
title: Python의 PDF 파일에서 XMP 메타데이터 가져오기
linktitle: Python의 PDF 파일에서 XMP 메타데이터 가져오기
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
description: Aspose.PDF를 사용하여 Python의 PDF 파일에서 XMP 메타데이터를 검색하여 자세한 콘텐츠 분석을 가능하게 하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서에서 XMP 메타데이터를 가져오려면 **GetXMPMetadata** 클래스를 호출하기만 하면 됩니다.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```


**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드****XMP 메타데이터(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)

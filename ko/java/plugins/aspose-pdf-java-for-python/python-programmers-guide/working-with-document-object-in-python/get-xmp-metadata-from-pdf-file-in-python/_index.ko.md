---
title: Python에서 PDF 파일에서 XMP 메타데이터 얻기
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서에서 XMP 메타데이터를 얻으려면, **GetXMPMetadata** 클래스를 호출하세요.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 속성 가져오기
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get XMP Metadata (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
---
title: Python의 PDF에서 메타데이터 제거
linktitle: Python의 PDF에서 메타데이터 제거
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
description: Aspose.PDF를 사용하여 Python의 PDF 문서에서 메타데이터를 제거하여 개인 정보 보호 및 데이터 보안을 보장하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서에서 메타데이터를 제거하려면 **RemoveMetadata** 클래스를 호출하기만 하면 됩니다.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```


**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트에서 В **메타데이터 제거(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

---
title: Python에서 PDF 파일 연결
linktitle: Python에서 PDF 파일 연결
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
description: Aspose.PDF를 사용하여 Python에서 여러 PDF 파일을 단일 PDF 문서로 연결하여 문서 관리를 단순화하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 파일을 연결하려면 **ConcatenatePdfFiles** 클래스를 호출하기만 하면 됩니다.


```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```


**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **PDF 파일 연결(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)

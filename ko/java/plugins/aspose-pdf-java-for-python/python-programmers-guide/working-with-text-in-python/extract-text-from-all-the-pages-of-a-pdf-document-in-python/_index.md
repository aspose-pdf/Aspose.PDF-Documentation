---
title: Python에서 PDF 문서의 모든 페이지에서 텍스트 추출
linktitle: Python에서 PDF 문서의 모든 페이지에서 텍스트 추출
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: PDF 파일 형식 API를 사용하여 Python에서 PDF 페이지에서 텍스트를 추출하는 방법을 설명합니다.
---
## 
Python을 사용하여 PDF에서 텍스트 추출



**Aspose.PDF Java for Python**을 사용하여 TextrFrom All the Pages Pdf 문서를 추출하려면 **ExtractTextFromAllPages** 모듈을 호출하기만 하면 됩니다.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **모든 페이지에서 텍스트 추출(Aspose.PDF)**을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)

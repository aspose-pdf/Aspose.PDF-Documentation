---
title: Python에서 PDF를 SVG 형식으로 변환
linktitle: Python에서 PDF를 SVG 형식으로 변환
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
description: 확장 가능한 벡터 출력을 위해 Aspose.PDF를 사용하여 Python에서 PDF 문서를 SVG 형식으로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF를 SVG 형식으로 변환하려면 **PdfToSvg** 모듈을 호출하기만 하면 됩니다.


```python

# Open the target document
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instantiate an object of SvgSaveOptions
save_options = self.SvgSaveOptions()

# do not compress SVG image to Zip archive
save_options.CompressOutputToZipArchive = False;

# Save the output to XLS format
doc.save(self.dataDir + "Output1.svg", save_options)

print "Document has been converted successfully"
```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 SVG 형식으로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)

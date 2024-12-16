---
title: Python에서 SVG 파일을 PDF 형식으로 변환
type: docs
weight: 40
url: /ko/java/convert-svg-file-to-pdf-format-in-python/
lastmod: "2021-06-05"
---

## Python에서 SVG 파일을 PDF 형식으로 변환하는 방법

**Aspose.PDF Java for Python**을 사용하여 SVG 파일을 PDF 형식으로 변환하려면, **SvgToPdf** 모듈을 호출하십시오.

Python 코드:

```python
options = self.SvgLoadOptions();
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'
출력을 XLS 형식으로 저장
doc.save(self.dataDir + "SVG1.pdf");
print "문서가 성공적으로 변환되었습니다"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert SVG to PDF (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/SvgToPdf/SvgToPdf.py)
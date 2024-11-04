---
title: Python에서 PDF를 SVG 형식으로 변환
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF를 SVG 형식으로 변환하려면 **PdfToSvg** 모듈을 호출하세요.

```python

# 대상 문서 열기
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# SvgSaveOptions 객체 인스턴스화
save_options = self.SvgSaveOptions()

# SVG 이미지를 Zip 아카이브로 압축하지 않음
save_options.CompressOutputToZipArchive = False;

# 출력물을 XLS 형식으로 저장
doc.save(self.dataDir + "Output1.svg", save_options)

print "문서가 성공적으로 변환되었습니다"
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to SVG Format (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
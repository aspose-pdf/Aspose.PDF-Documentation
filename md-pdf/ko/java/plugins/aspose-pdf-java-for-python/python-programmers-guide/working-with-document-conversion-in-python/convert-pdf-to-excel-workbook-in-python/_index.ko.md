---
title: Python에서 PDF를 Excel 워크북으로 변환
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서를 Excel 워크북으로 변환하려면 **PdfToExcel** 모듈을 호출하십시오.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# ExcelSave 옵션 객체 인스턴스화
excelsave=self.ExcelSaveOptions();

# 출력 파일을 XLS 형식으로 저장
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "문서가 성공적으로 변환되었습니다"
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to Excel Workbook (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
---
title: Python에서 PDF를 Excel 통합 문서로 변환
linktitle: Python에서 PDF를 Excel 통합 문서로 변환
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: 구조화된 데이터 추출을 위해 Aspose.PDF를 사용하여 Python에서 PDF 문서를 Excel 통합 문서로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서를 Excel 통합 문서로 변환하려면 **PdfToExcel** 모듈을 호출하기만 하면 됩니다.


```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instantiate ExcelSave Option object
excelsave=self.ExcelSaveOptions();

# Save the output to XLS format
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Document has been converted successfully"
```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 Excel 통합 문서(Aspose.PDF)로 변환**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)

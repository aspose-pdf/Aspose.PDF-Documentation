---
title: PHP에서 PDF를 Excel 통합 문서로 변환
linktitle: PHP에서 PDF를 Excel 통합 문서로 변환
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-php/
description: Aspose.PDF를 사용하여 PHP에서 PDF 파일을 Excel 통합 문서로 변환하여 원활한 데이터 추출 및 조작을 가능하게 하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF를 Excel 통합 문서로 변환



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 Excel 통합 문서로 변환하려면 **PdfToExcel** 모듈을 호출하기만 하면 됩니다.

PHP 코드


```php
# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Instantiate ExcelSave Option object
$excelsave = new ExcelSaveOptions();

# Save the output to XLS format
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "Document has been converted successfully" . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 Excel 통합 문서(Aspose.PDF)로 변환**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)

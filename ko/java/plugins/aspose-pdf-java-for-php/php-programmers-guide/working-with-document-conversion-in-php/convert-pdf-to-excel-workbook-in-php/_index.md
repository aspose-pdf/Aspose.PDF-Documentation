---
title: PHP에서 PDF를 Excel 워크북으로 변환
type: docs
weight: 20
url: ko/java/convert-pdf-to-excel-workbook-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF를 Excel 워크북으로 변환

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 Excel 워크북으로 변환하려면, **PdfToExcel** 모듈을 호출하세요.

PHP 코드

```php
# 대상 문서 열기
$pdf = new Document($dataDir . 'input1.pdf');

# Excel 저장 옵션 객체 인스턴스화
$excelsave = new ExcelSaveOptions();

# XLS 형식으로 출력 저장
$pdf->save($dataDir . "Converted_Excel.xls", $excelsave);

print "문서가 성공적으로 변환되었습니다" . PHP_EOL;

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to Excel Workbook (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToExcel.php)
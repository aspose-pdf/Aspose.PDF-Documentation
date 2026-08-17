---
title: PHP에서 SVG 파일을 PDF 형식으로 변환
linktitle: PHP에서 SVG 파일을 PDF 형식으로 변환
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: 효과적인 문서 관리를 위해 Aspose.PDF를 사용하여 PHP에서 SVG 파일을 PDF 형식으로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - SVG를 PDF로 변환



**Aspose.PDF Java for PHP**를 사용하여 SVG 파일을 PDF 형식으로 변환하려면 **SvgToPdf** 모듈을 호출하기만 하면 됩니다.



PHP 코드


```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **SVG를 PDF로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)

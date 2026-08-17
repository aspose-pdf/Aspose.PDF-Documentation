---
title: PHP에서 PDF를 SVG 형식으로 변환
linktitle: PHP에서 PDF를 SVG 형식으로 변환
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: 고품질 벡터 그래픽 변환을 위해 Aspose.PDF를 사용하여 PDF 문서를 PHP에서 SVG 형식으로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF를 SVG로 변환



PHP용 **Aspose.PDF Java**를 사용하여 PDF를 SVG 형식으로 변환하려면 **PdfToSvg** 모듈을 호출하기만 하면 됩니다.



PHP 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 SVG 형식으로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)

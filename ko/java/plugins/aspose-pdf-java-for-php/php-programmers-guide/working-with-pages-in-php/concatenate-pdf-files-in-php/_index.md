---
title: PHP에서 PDF 파일 연결
linktitle: PHP에서 PDF 파일 연결
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
description: 더 쉬운 문서 관리를 위해 Aspose.PDF를 사용하여 PHP에서 여러 PDF 파일을 단일 문서로 연결하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 연결



**Aspose.PDF Java for PHP**를 사용하여 PDF 파일을 연결하려면 **ConcatenatePdfFiles** 클래스를 호출하기만 하면 됩니다.



PHP 코드


```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF 파일 연결(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)

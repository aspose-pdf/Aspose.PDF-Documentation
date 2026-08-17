---
title: PHP에서 PDF를 DOC 또는 DOCX 형식으로 변환
linktitle: PHP에서 PDF를 DOC 또는 DOCX 형식으로 변환
type: docs
weight: 10
url: /java/convert-pdf-to-doc-or-docx-format-in-php/
description: 더 쉬운 문서 편집을 위해 Aspose.PDF를 사용하여 PHP에서 PDF 문서를 DOC 또는 DOCX 형식으로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF를 DOC 또는 DOCX로 변환



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 DOC 또는 DOCX 형식으로 변환하려면 **PdfToDoc** 모듈을 호출하기만 하면 됩니다.



PHP 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.doc");

print "Document has been converted successfully";

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 DOC 또는 DOCX로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)

---
title: PHP에서 PDF의 메타데이터 제거
linktitle: PHP에서 PDF의 메타데이터 제거
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-php/
description: 향상된 개인 정보 보호 및 문서 보안을 위해 Aspose.PDF를 사용하여 PHP의 PDF 문서에서 메타데이터를 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 메타데이터 제거



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서에서 메타데이터를 제거하려면 **RemoveMetadata** 클래스를 호출하기만 하면 됩니다.

PHP 코드


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# save update document with new information
$doc->save($dataDir . "Remove_Metadata.pdf");

print "Removed metadata successfully, please check output file." . PHP_EOL;

```


**실행 코드 다운로드**



아래 언급된 소셜 코딩 사이트에서 В **메타데이터 제거(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)

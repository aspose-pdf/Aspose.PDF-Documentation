---
title: PHP의 PDF 파일에서 XMP 메타데이터 가져오기
linktitle: PHP의 PDF 파일에서 XMP 메타데이터 가져오기
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-php/
description: 고급 콘텐츠 분석을 위해 Aspose.PDF를 사용하여 PHP의 PDF 문서에서 XMP 메타데이터를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - XMP 메타데이터 가져오기



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서에서 XMP 메타데이터를 가져오려면 **GetXMPMetadata** 클래스를 호출하기만 하면 됩니다.

PHP 코드


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get properties
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드****XMP 메타데이터(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)

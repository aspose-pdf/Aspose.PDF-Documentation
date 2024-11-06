---
title: PHP에서 PDF 파일에서 XMP 메타데이터 가져오기
type: docs
weight: 50
url: ko/java/get-xmp-metadata-from-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - XMP 메타데이터 가져오기

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에서 XMP 메타데이터를 가져오려면, **GetXMPMetadata** 클래스를 단순히 호출하면 됩니다.

PHP 코드

```php

# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

# 속성 가져오기
print "xmp:CreateDate: " + $doc->getMetadata()->get_Item("xmp:CreateDate") . PHP_EOL;
print "xmp:Nickname: " + $doc->getMetadata()->get_Item("xmp:Nickname") . PHP_EOL;
print "xmp:CustomProperty: " + $doc->getMetadata()->get_Item("xmp:CustomProperty") . PHP_EOL;

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get XMP Metadata (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetXMPMetadata.php)
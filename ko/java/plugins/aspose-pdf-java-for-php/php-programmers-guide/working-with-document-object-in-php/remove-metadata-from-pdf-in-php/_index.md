---
title: PHP에서 PDF의 메타데이터 제거
type: docs
weight: 70
url: ko/java/remove-metadata-from-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 메타데이터 제거

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에서 메타데이터를 제거하려면, 간단히 **RemoveMetadata** 클래스를 호출하십시오.

PHP 코드

```php

# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

if (preg_match('/pdfaid:part/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("pdfaid:part");

}

if (preg_match('/dc:format/',$doc->getMetadata())) {
    $doc->getMetadata()->removeItem("dc:format");

}

# 새 정보로 업데이트된 문서 저장
$doc->save($dataDir . "Remove_Metadata.pdf");

print "메타데이터가 성공적으로 제거되었습니다. 출력 파일을 확인하세요." . PHP_EOL;

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Remove Metadata (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/RemoveMetadata.php)
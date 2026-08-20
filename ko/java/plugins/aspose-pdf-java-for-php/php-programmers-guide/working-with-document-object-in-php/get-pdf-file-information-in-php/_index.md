---
title: PHP에서 PDF 파일 정보 얻기
linktitle: PHP에서 PDF 파일 정보 얻기
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
description: Aspose.PDF를 사용하여 PHP에서 메타데이터 및 속성을 포함하여 PDF 파일에 대한 자세한 정보를 검색하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 정보 얻기



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서의 파일 정보를 얻으려면 **GetPdfFileInfo** 클래스를 호출하면 됩니다.

PHP 코드


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

# Show document information
print "Author:-" . $doc_info->getAuthor();
print "Creation Date:-" . $doc_info->getCreationDate();
print "Keywords:-" . $doc_info->getKeywords();
print "Modify Date:-" . $doc_info->getModDate();
print "Subject:-" . $doc_info->getSubject();
print "Title:-" . $doc_info->getTitle();

```


**실행 코드 다운로드**



다운로드В **PDF 파일 정보(Aspose.PDF)**В를 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)

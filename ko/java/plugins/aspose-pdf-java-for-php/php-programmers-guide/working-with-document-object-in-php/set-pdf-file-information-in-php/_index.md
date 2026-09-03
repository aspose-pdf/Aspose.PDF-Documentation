---
title: PHP에서 PDF 파일 정보 설정
linktitle: PHP에서 PDF 파일 정보 설정
type: docs
weight: 90
url: /java/set-pdf-file-information-in-php/
description: Aspose.PDF를 사용하여 PHP에서 PDF 문서의 메타데이터와 같은 다양한 파일 속성을 설정하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 정보 설정



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서 정보를 업데이트하려면 **SetPdfFileInfo** 클래스를 호출하면 됩니다.

PHP 코드


```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get document information
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF Information");
$doc_info->setTitle("Setting PDF Document Information");

# save update document with new information
$doc->save($dataDir . "Updated_Information.pdf");

print "Update document information, please check output file.";

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF 파일 정보 설정(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)

---
title: PHP에서 PDF 파일 정보 설정
type: docs
weight: 90
url: /ko/java/set-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 정보 설정

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서 정보를 업데이트하려면, **SetPdfFileInfo** 클래스를 단순히 호출하십시오.

PHP 코드

```php

# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

# 문서 정보 가져오기
$doc_info = $doc->getInfo();

$doc_info->setAuthor("Aspose.PDF for java");
$doc_info->setCreationDate(new Date());
$doc_info->setKeywords("Aspose.PDF, DOM, API");
$doc_info->setModDate(new Date());
$doc_info->setSubject("PDF 정보");
$doc_info->setTitle("PDF 문서 정보 설정");

# 새 정보로 문서 업데이트 저장
$doc->save($dataDir . "Updated_Information.pdf");

print "문서 정보를 업데이트했습니다. 출력 파일을 확인하십시오.";

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Set PDF File Information (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetPdfFileInfo.php)
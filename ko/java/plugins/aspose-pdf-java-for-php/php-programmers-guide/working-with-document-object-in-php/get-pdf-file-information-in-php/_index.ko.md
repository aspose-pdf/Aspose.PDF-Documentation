---
title: PHP에서 PDF 파일 정보 가져오기
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 정보 가져오기

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서의 파일 정보를 가져오려면, **GetPdfFileInfo** 클래스를 호출하십시오.

PHP 코드

```php

# pdf 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

# 문서 정보 가져오기
$doc_info = $doc->getInfo();

# 문서 정보 표시
print "저자:-" . $doc_info->getAuthor();
print "생성 날짜:-" . $doc_info->getCreationDate();
print "키워드:-" . $doc_info->getKeywords();
print "수정 날짜:-" . $doc_info->getModDate();
print "주제:-" . $doc_info->getSubject();
print "제목:-" . $doc_info->getTitle();

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get PDF File Information (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)
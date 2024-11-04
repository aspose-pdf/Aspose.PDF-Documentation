---
title: PHP에서 DOM을 사용하여 HTML 문자열 추가
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - HTML 추가

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에 HTML 문자열을 추가하려면, **AddHtml** 모듈을 호출하세요.

PHP 코드

```php
# Document 객체를 인스턴스화합니다
$doc = new Document();

# PDF 파일의 페이지 컬렉션에 페이지를 추가합니다
$page = $doc->getPages()->add();

# HTML 내용을 가진 HtmlFragment를 인스턴스화합니다
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# 여백 세부 정보를 위해 MarginInfo를 설정합니다
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# 여백 정보를 설정합니다
$title->setMargin($margin);

# 페이지의 단락 컬렉션에 HTML 프래그먼트를 추가합니다
$page->getParagraphs()->add($title);

# PDF 파일을 저장합니다
$doc->save($dataDir . "html.output.pdf");

print "HTML이 성공적으로 추가되었습니다" . PHP_EOL;

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Add HTML (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
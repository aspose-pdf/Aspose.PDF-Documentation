---
title: PHP에서 DOM을 사용하여 HTML 문자열 추가
linktitle: PHP에서 DOM을 사용하여 HTML 문자열 추가
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: 풍부한 문서 생성을 위해 Aspose.PDF와 함께 PHP의 DOM을 사용하여 PDF 문서에 HTML 콘텐츠를 추가하는 방법을 살펴보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - HTML 추가



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서에 HTML 문자열을 추가하려면 **AddHtml** 모듈을 호출하기만 하면 됩니다.



PHP 코드


```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 HTML(Aspose.PDF) 추가**를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)

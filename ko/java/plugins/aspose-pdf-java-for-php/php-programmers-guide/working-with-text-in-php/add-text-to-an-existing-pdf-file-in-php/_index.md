---
title: PHP에서 기존 PDF 파일에 텍스트 추가
linktitle: PHP에서 기존 PDF 파일에 텍스트 추가
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
description: 콘텐츠 향상을 위해 Aspose.PDF를 사용하여 PHP의 기존 PDF 문서에 새 텍스트를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 텍스트 추가



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서에 텍스트 문자열을 추가하려면 **AddText** 모듈을 호출하기만 하면 됩니다.

PHP 코드


```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트에서 В **텍스트 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)

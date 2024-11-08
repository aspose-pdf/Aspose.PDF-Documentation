---
title: PHP에서 기존 PDF 파일에 텍스트 추가
type: docs
weight: 20
url: /ko/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 텍스트 추가

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서에 텍스트 문자열을 추가하려면, **AddText** 모듈을 호출하십시오.

PHP 코드

```php

# Document 객체 인스턴스화
$doc = new Document($dataDir . 'input1.pdf');

# 특정 페이지 가져오기
$pdf_page = $doc->getPages()->get_Item(1);

# 텍스트 프래그먼트 생성
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# 텍스트 속성 설정
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# TextBuilder 객체 생성
$text_builder = new TextBuilder($pdf_page);

# PDF 페이지에 텍스트 프래그먼트 추가
$text_builder->appendText($text_fragment);

# PDF 파일 저장
$doc->save($dataDir . "Text_Added.pdf");

print "텍스트가 성공적으로 추가되었습니다" . PHP_EOL;

```


**코드 실행 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **텍스트 추가 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
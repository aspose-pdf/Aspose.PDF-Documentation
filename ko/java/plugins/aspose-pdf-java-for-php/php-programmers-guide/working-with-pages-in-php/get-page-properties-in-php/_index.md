---
title: PHP에서 페이지 속성 가져오기
type: docs
weight: 50
url: /ko/java/get-page-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 속성 가져오기

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서의 페이지 속성을 가져오려면, **GetPageProperties** 클래스를 호출하세요.

PHP 코드

```php

# PDF 문서 생성
$pdf_document = new Document($dataDir . 'input1.pdf');

# 페이지 컬렉션 가져오기
$page_collection = $pdf_document->getPages();

# 특정 페이지 가져오기
$pdf_page = $page_collection->get_Item(1);

# 페이지 속성 가져오기
print "ArtBox : 높이 = " . $pdf_page->getArtBox()->getHeight() . ", 너비 = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : 높이 = " . $pdf_page->getBleedBox()->getHeight() . ", 너비 = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : 높이 = " . $pdf_page->getCropBox()->getHeight() . ", 너비 = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : 높이 = " . $pdf_page->getMediaBox()->getHeight() . ", 너비 = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : 높이 = " . $pdf_page->getTrimBox()->getHeight() . ", 너비 = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : 높이 = " . $pdf_page->getRect()->getHeight() . ", 너비 = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "페이지 번호 :- " . $pdf_page->getNumber() . PHP_EOL ;
print "회전 :-" . $pdf_page->getRotate() . PHP_EOL ;

```


**실행 코드 다운로드**

**Get Page Properties (Aspose.PDF)**를 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)
---
title: 获取 PHP 中的页面属性
type: docs
weight: 50
url: /zh/java/get-page-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取页面属性

要使用 **Aspose.PDF Java for PHP** 获取 PDF 文档的页面属性，只需调用 **GetPageProperties** 类。

PHP 代码

```php

# 创建 PDF 文档
$pdf_document = new Document($dataDir . 'input1.pdf');

# 获取页面集合
$page_collection = $pdf_document->getPages();

# 获取特定页面
$pdf_page = $page_collection->get_Item(1);

# 获取页面属性
print "ArtBox : 高度 = " . $pdf_page->getArtBox()->getHeight() . ", 宽度 = " . $pdf_page->getArtBox()->getWidth() . ", LLX = " . $pdf_page->getArtBox()->getLLX() . ", LLY = " . $pdf_page->getArtBox()->getLLY() . ", URX = " . $pdf_page->getArtBox()->getURX() . ", URY = " . $pdf_page->getArtBox()->getURY() . PHP_EOL ;

print "BleedBox : 高度 = " . $pdf_page->getBleedBox()->getHeight() . ", 宽度 = " . $pdf_page->getBleedBox()->getWidth() . ", LLX = " . $pdf_page->getBleedBox()->getLLX() . ", LLY = " . $pdf_page->getBleedBox()->getLLY() . ", URX = " . $pdf_page->getBleedBox()->getURX() . ", URY = " . $pdf_page->getBleedBox()->getURY() . PHP_EOL ;

print "CropBox : 高度 = " . $pdf_page->getCropBox()->getHeight() . ", 宽度 = " . $pdf_page->getCropBox()->getWidth() . ", LLX = " . $pdf_page->getCropBox()->getLLX() . ", LLY = " . $pdf_page->getCropBox()->getLLY() . ", URX = " . $pdf_page->getCropBox()->getURX() . ", URY = " . $pdf_page->getCropBox()->getURY() . PHP_EOL ;

print "MediaBox : 高度 = " . $pdf_page->getMediaBox()->getHeight() . ", 宽度 = " . $pdf_page->getMediaBox()->getWidth() . ", LLX = " . $pdf_page->getMediaBox()->getLLX() . ", LLY = " . $pdf_page->getMediaBox()->getLLY() . ", URX = " . $pdf_page->getMediaBox()->getURX() . ", URY = " . $pdf_page->getMediaBox()->getURY() . PHP_EOL ;

print "TrimBox : 高度 = " . $pdf_page->getTrimBox()->getHeight() . ", 宽度 = " . $pdf_page->getTrimBox()->getWidth() . ", LLX = " . $pdf_page->getTrimBox()->getLLX() . ", LLY = " . $pdf_page->getTrimBox()->getLLY() . ", URX = " . $pdf_page->getTrimBox()->getURX() . ", URY = " . $pdf_page->getTrimBox()->getURY() . PHP_EOL ;

print "Rect : 高度 = " . $pdf_page->getRect()->getHeight() . ", 宽度 = " . $pdf_page->getRect()->getWidth() . ", LLX = " . $pdf_page->getRect()->getLLX() . ", LLY = " . $pdf_page->getRect()->getLLY() . ", URX = " . $pdf_page->getRect()->getURX() . ", URY = " . $pdf_page->getRect()->getURY() . PHP_EOL ;
print "页码 :- " . $pdf_page->getNumber() . PHP_EOL ;
print "旋转 :-" . $pdf_page->getRotate() . PHP_EOL ;

```


**下载运行代码**

从以下任一社交编码网站下载 **获取页面属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPageProperties.php)
---
title: 在PHP中向现有PDF文件添加文本
type: docs
weight: 20
url: /zh/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加文本

要使用**Aspose.PDF Java for PHP**在Pdf文档中添加文本字符串，只需调用**AddText**模块。

PHP代码

```php

# 实例化Document对象
$doc = new Document($dataDir . 'input1.pdf');

# 获取特定页面
$pdf_page = $doc->getPages()->get_Item(1);

# 创建文本片段
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# 设置文本属性
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# 创建TextBuilder对象
$text_builder = new TextBuilder($pdf_page);

# 将文本片段附加到PDF页面
$text_builder->appendText($text_fragment);

# 保存PDF文件
$doc->save($dataDir . "Text_Added.pdf");

print "文本添加成功" . PHP_EOL;

```


**下载可运行代码**

从以下任一社交编码网站下载 **添加文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
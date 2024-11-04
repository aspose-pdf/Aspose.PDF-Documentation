---
title: 获取 PHP 中的文档窗口和页面显示属性
type: docs
weight: 30
url: /java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取文档窗口和页面显示属性

要使用 **Aspose.PDF Java for PHP** 获取 PDF 文档的窗口和页面显示属性，只需调用 **GetDocumentWindow** 类。

PHP 代码

```php

# 打开一个 PDF 文档。
$doc = new Document($dataDir . "input1.pdf");

# 获取不同的文档属性
# 文档窗口的位置 - 默认值: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# 主要的阅读顺序；决定页面的位置
# 当并排显示时 - 默认值: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# 窗口的标题栏是否应显示文档标题。
# 如果为 false，标题栏显示 PDF 文件名 - 默认值: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# 是否调整文档窗口的大小以适合
# 第一个显示页面的大小 - 默认值: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# 是否隐藏查看器应用程序的菜单栏 - 默认值: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# 是否隐藏查看器应用程序的工具栏 - 默认值: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# 是否隐藏 UI 元素如滚动条
# 并只显示页面内容 - 默认值: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# 文档的页面模式。退出全屏模式时如何显示文档。
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# 页面布局，即单页、一列
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# 打开文档时应如何显示。
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**下载运行代码**

从以下任一社交编码网站下载**获取文档窗口和页面显示属性 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)
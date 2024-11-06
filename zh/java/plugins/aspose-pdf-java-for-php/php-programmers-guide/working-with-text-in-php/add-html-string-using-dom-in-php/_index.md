---
title: 使用 DOM 在 PHP 中添加 HTML 字符串
type: docs
weight: 10
url: zh/java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加 HTML

要在 Pdf 文档中添加 HTML 字符串，使用 **Aspose.PDF Java for PHP**，只需调用 **AddHtml** 模块。

PHP 代码

```php
# 实例化 Document 对象
$doc = new Document();

# 向 PDF 文件的页面集合中添加一个页面
$page = $doc->getPages()->add();

# 使用 HTML 内容实例化 HtmlFragment
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# 设置 MarginInfo 以获取边距详细信息
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# 设置边距信息
$title->setMargin($margin);

# 将 HTML 片段添加到页面的段落集合中
$page->getParagraphs()->add($title);

# 保存 PDF 文件
$doc->save($dataDir . "html.output.pdf");

print "HTML 添加成功" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载 **添加 HTML (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
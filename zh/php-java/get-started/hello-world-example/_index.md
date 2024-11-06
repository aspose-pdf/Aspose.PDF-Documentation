---

title: Hello World PHP via Java 示例
linktitle: Hello World 示例
type: docs
weight: 40
url: zh/php-java/hello-world-example/
description: 本页面展示如何使用简单编程创建一个包含文本 - Hello World 的PDF文档，使用Aspose.PDF for PHP via Java。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World 示例

“Hello World” 示例通常用于通过一个简单的用例来展示编程语言或软件的基本功能。

Aspose.PDF for PHP via Java API 使开发者能够在他们的 Java 应用程序中创建、读取、编辑和操作 PDF 文件。它支持读取和转换各种文件类型到 PDF 格式以及从 PDF 格式转换。本文的 Hello World 示例展示了如何使用 Aspose.PDF for PHP via Java API 创建一个 PDF 文件。在你的环境中[安装 Aspose.PDF for PHP via Java](/pdf/php-java/installation/)之后，你可以执行下面的代码示例来查看 Aspose.PDF API 的工作原理。

下面的代码片段遵循这些步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 对象
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page)
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 对象
1. 将 TextFragment 添加到页面的 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 集合中
1. 保存生成的 PDF 文档

以下代码片段是一个 Hello World 程序，用于展示通过 Java API 使用 Aspose.PDF for PHP 的工作原理。

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```
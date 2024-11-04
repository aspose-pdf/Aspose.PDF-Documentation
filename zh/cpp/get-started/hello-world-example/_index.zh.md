---
title: Aspose.PDF C++ 示例
linktitle: Hello World 示例
type: docs
weight: 40
url: /cpp/hello-world-example/
description: 本页面展示如何使用简单的编程来创建包含文本 - Hello World 的 PDF 文档。
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

"Hello World" 示例传统上用于通过简单的用例介绍编程语言或软件的功能。

Aspose.PDF for C++ 是一个功能丰富的 PDF API，允许开发人员在其 C++ 应用程序中嵌入 PDF 文档创建、操作和转换功能。它支持处理许多流行的文件格式，包括 PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX 和图像文件格式。在本文中，我们将创建一个包含文本 "Hello World!" 的 PDF 文档。在您的环境中安装 Aspose.PDF for C++ 后，您可以执行以下代码示例以查看 Aspose.PDF API 的工作原理。

以下代码片段遵循这些步骤：

1.
``` 创建一个[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)用于路径名和文件名。
1. 实例化一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。在这一步我们将创建一个带有一些元数据但没有页面的空PDF文档。
1. 向文档对象添加一个[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。所以，现在我们的文档将有一页。
1. [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa)结果PDF文档

以下代码片段是一个Hello World程序，用于展示Aspose.PDF for C++ API的工作原理。

```cpp
void ExampleSimple()
{
    // 用于存储组合路径的缓冲区。
    String outputFileName;

    // 路径名的字符串。
    String _dataDir("C:\\Samples\\");

    // 文件名的字符串。
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 向新页面添加文本
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 保存更新后的PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```
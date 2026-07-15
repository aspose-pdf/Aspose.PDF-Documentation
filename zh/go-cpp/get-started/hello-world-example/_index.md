---
title: 使用 Go 语言的 Hello World 示例
linktitle: Hello World 示例
type: docs
weight: 40
url: /zh/go-cpp/hello-world-example/
description: 此示例演示了如何使用 Aspose.PDF for Go 创建包含文本 Hello World 的简单 PDF 文档。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Aspose.PDF for Go 的 Hello World
Abstract: 通过 C++ 的 Aspose.PDF for Go 入门指南提供了库使用的介绍，涵盖了创建和操作 PDF 文档的基本步骤。它包含一个 'Hello World' 示例，演示如何生成包含文本内容的简单 PDF 文件，帮助开发者快速了解 API 的核心功能。
SoftwareApplication: go-cpp
---

传统上，\"Hello World\" 示例用于通过一个简单的用例来介绍编程语言或软件的特性。

**Aspose.PDF for Go** 是功能丰富的 PDF API，允许开发者使用 Go 嵌入 PDF 文档的创建、操作和转换功能。它支持多种流行的文件格式，包括 PDF、TXT、XPS、EPUB、TEX、DOC、DOCX、PPTX、图像格式等。在本文中，我们将创建一个包含文本 “Hello World!” 的 PDF 文档。安装 Aspose.PDF for Go 后，您可以运行代码示例，查看 Aspose.PDF API 的工作方式。
下面的代码片段遵循以下步骤：

1. 创建一个新的 PDF 文档实例。
1. 使用以下方式向 PDF 文档添加新页面 [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) 函数。
1. 使用以下方式设置页面大小 [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. 使用以下方式向第一页添加 “Hello World!” 文本 [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. 使用以下方式保存修复后的 PDF 文档 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 方法。
1. 关闭 PDF 文档并释放任何已分配的资源。

以下代码片段是一个 Hello World 程序，用于展示 Aspose.PDF for Go API 的工作原理。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```

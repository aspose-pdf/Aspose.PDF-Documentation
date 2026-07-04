---
title: 使用 Go 提取 PDF 文本
linktitle: 提取 PDF 文本
type: docs
weight: 30
url: /zh/go-cpp/extract-text-from-pdf/
description: 本文介绍了使用 Aspose.PDF for Go 从 PDF 文档中提取文本的多种方法。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 提取文本
Abstract: 通过 C++ 的 Aspose.PDF for Go 提供了一种强大且高效的方式来从 PDF 文档中提取文本。该库支持多种提取技术，允许用户从整个文档、特定页面或 PDF 中的预定义区域检索文本。
SoftwareApplication: go-cpp
---

## 从 PDF 文档中提取文本

从 PDF 文档中提取文本是一项非常常见且有用的任务。PDF 往往包含需要为各种目的访问、分析或处理的关键信息。提取文本可以更容易地在数据库、报告或其他文档中重复使用。

提取文本使 PDF 内容可搜索，允许用户快速定位特定信息，而无需手动查看整个文档。

如果您想从 PDF 文档中提取文本，可以使用 [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) 函数。
请查看以下代码片段，以使用 Go 从 PDF 文件中提取文本。

1. 使用给定的文件名打开 PDF 文档。
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) 从 PDF 文档中提取文本内容。
1. 将提取的文本打印到控制台。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
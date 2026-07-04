---
title: 使用 Go 向 PDF 添加文本
linktitle: 向 PDF 添加文本
type: docs
weight: 10
url: /zh/go-cpp/add-text-to-pdf-file/
description: 了解如何在 Go 中使用 Aspose.PDF 向 PDF 文档添加文本，以实现内容增强和文档编辑。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: 使用 Aspose.PDF for Go 向 PDF 添加文本
Abstract: Aspose.PDF for C++ 和 Go 文档中的 “Add Text to PDF File” 部分提供了逐步说明，帮助以编程方式向 PDF 文档插入文本。它涵盖了多种添加文本的方法，包括定位、字体自定义、颜色调整以及文本对齐选项。该指南演示了如何在 PDF 的特定页面和位置添加文本，以确保内容精确放置。通过详细的代码示例和说明，开发人员可以轻松将文本插入功能集成到其应用程序中，从而提升 PDF 文档管理。
SoftwareApplication: go-cpp
---

向现有 PDF 文件添加文本：

1. 打开 PDF 文件。
1. 使用将文本添加到 PDF 文档中 [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) 函数。
1. 将修改保存到同一文件。

## 添加文本

以下代码片段向您展示如何在现有 PDF 文件中添加文本。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

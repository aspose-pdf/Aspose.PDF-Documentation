---
title: 在 Go 中将 PDF 转换为 PPTX
linktitle: 将 PDF 转换为 PowerPoint
type: docs
weight: 30
url: /zh/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF 允许您使用 Go 将 PDF 转换为 PPTX 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 用于将 PDF 转换为 PowerPoint 的 Golang 工具
Abstract: Aspose.PDF for Go via C++ 提供了一种可靠的解决方案，可将 PDF 文档转换为 PowerPoint（PPTX）格式，同时保留原始的布局、格式和内容结构。此功能使开发者能够无缝地将静态 PDF 文件转化为动态、可编辑的演示文稿。该库提供了自定义选项以控制转换过程，确保输出高质量，适用于商业和专业使用。文档提供了逐步指南和代码示例，帮助开发者高效地将 PDF-to-PowerPoint 转换集成到其应用程序中。
SoftwareApplication: go-cpp
---

## 将 PDF 转换为 PPTX

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 PPTX：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 PPTX [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for Go 为您提供在线免费应用 [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 您可以尝试了解其功能和工作质量。

[![Aspose.PDF 免费应用将 PDF 转换为 PPTX](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

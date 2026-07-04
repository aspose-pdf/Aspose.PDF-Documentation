---
title: 使用 Go 为 PDF 设置背景颜色
linktitle: 设置背景颜色
type: docs
weight: 80
url: /zh/go-cpp/set-background-color/
description: 使用 Go 为您的 PDF 文件设置背景颜色。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 为 PDF 设置背景颜色
Abstract: Aspose.PDF for Go 通过 C++ 提供设置 PDF 页面背景颜色的功能，允许开发人员自定义文档的外观。此功能可将纯色应用于整个页面背景，提升文档的视觉呈现。开发人员可以使用 RGB 或 CMYK 等标准颜色模型轻松指定颜色值。文档提供了详细的说明和代码示例，帮助开发人员在其 C++ 应用程序中有效实现背景颜色自定义。
SoftwareApplication: go-cpp
---

1. 提供的代码片段演示了如何使用 Go 中的 Aspose.PDF 库为 PDF 文件设置背景颜色。
1. 该 [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) Open 方法将指定的 PDF 文件加载到内存中，允许进一步的操作，例如修改其外观或内容。
1. 该 [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) 该方法为 PDF 文档应用新的背景颜色。RGB 值允许用户自定义文档的视觉样式。
1. 该 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 该方法将更新后的 PDF 保存为新名称。

此代码非常适合需要自动化 PDF 定制的应用程序，例如创建品牌报告、添加水印或提升多个文档之间的视觉一致性。

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
---
title: 使用 Go 旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 50
url: /zh/go-cpp/rotate-pages/
description: 本主题描述如何使用 Go 通过 C++ 以编程方式旋转现有 PDF 文件的页面方向。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 旋转 PDF 页面
Abstract: Aspose.PDF for Go via C++ 提供强大的功能来旋转 PDF 文档中的页面，允许开发人员根据需要修改页面方向。该库支持将页面旋转 90、180 或 270 度，从而快速高效地调整文档布局。此功能有助于纠正方向错误的页面或改变文档的展示方式。文档包括逐步说明和代码示例，帮助开发人员将页面旋转功能无缝集成到其应用程序中。
SoftwareApplication: go-cpp
---

本节描述如何使用 Go 在现有 PDF 文件中将页面方向从横向更改为竖向，或反之。

旋转页面可确保在专业环境中打印或显示 PDF 时的正确对齐

1. 打开 PDF 文档。
1. 旋转 PDF 页面。该 [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) 函数对给定页面应用特定的旋转（在本例中为 180 度）。
1. 将更改保存为新文件。该 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 函数创建一个新的 PDF 文件，以在保留原始文件的同时存储更新后的版本。

在本例中，您旋转 PDF 文档中的特定页面：

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

您还可以选择旋转文档中的所有 PDF 页面：

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```
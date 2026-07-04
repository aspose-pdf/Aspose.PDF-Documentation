---
title: 使用 Aspose.PDF for Go via C++ 优化 PDF
linktitle: 优化 PDF 文件
type: docs
weight: 10
url: /zh/go-cpp/optimize-pdf/
description: 使用 Go 工具优化和压缩 PDF 文件。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 优化和压缩 PDF 文件
Abstract: Aspose.PDF for Go via C++ 提供强大的优化功能，以减小 PDF 文档的体积并提升性能。该库提供多种优化选项，包括压缩图像、删除未使用的对象、减少字体大小以及优化内容流。这些功能有助于提升文档存储效率，并确保更快的处理和加载时间。文档提供了分步指南和代码示例，帮助开发者在其应用程序中有效实现 PDF 优化。
SoftwareApplication: go-cpp
---

## 优化 PDF 文档

使用 Aspose.PDF for Go via C\u002B\u002B 的工具包可让您优化 PDF 文档。

此代码片段对那些减少 PDF 文件大小或提升效率至关重要的应用程序非常有用，例如网页上传、归档或在带宽受限的情况下共享。

1. 该 [打开](https://reference.aspose.com/pdf/go-cpp/core/open/) 方法将指定的 PDF 文件（sample.pdf）加载到内存中。
1. 该 [Optimize 方法](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) 通过执行诸如删除未使用的对象、压缩图像、扁平化注释、取消嵌入字体以及启用内容复用等优化来减小文件大小。这些步骤有助于降低存储需求并提升 PDF 文档的处理速度。
1. 该 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 此方法将优化后的 PDF 保存到新文件中。

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
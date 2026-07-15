---
title: 使用 Go 优化 PDF 资源
linktitle: 优化 PDF 资源
type: docs
weight: 15
url: /zh/go-cpp/optimize-pdf-resources/
description: 使用 Go 工具优化 PDF 文件的资源。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 优化 PDF 资源
Abstract: Aspose.PDF for Go 通过 C++ 提供了优化 PDF 资源的高级功能，提升文档效率并减少文件大小。该库允许开发者通过删除冗余数据和压缩资源来优化字体、图像和元数据，同时不影响文档质量。这些优化技术改善文档性能，使 PDF 更适合共享和存储。文档提供了详细的指南和代码示例，帮助开发者在应用程序中有效实现资源优化。
SoftwareApplication: go-cpp
---

## 优化 PDF 资源

优化文档中的资源：

  1. 未在文档页面上使用的资源将被删除。
  1. 相同的资源将合并为单个对象。
  1. 未使用的对象将被删除。

优化可能包括压缩图像、删除未使用的对象以及优化字体，以减小文件大小并提升性能。此操作期间的任何错误都会被记录并终止程序。  
 
1. 该 [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method 将指定的 PDF 文件 (sample.pdf) 加载到内存中。
1. 使用优化 PDF 中的资源以提高效率 [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) method.
1. 该 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method 将优化后的 PDF 保存到新文件中。

下面的代码片段展示了如何优化 PDF 文档。

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
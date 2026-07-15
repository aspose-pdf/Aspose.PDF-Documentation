---
title: 使用 Go 删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 30
url: /zh/go-cpp/delete-pages/
description: 您可以使用 Aspose.PDF for Go via C++ 删除 PDF 文件中的页面。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 删除 PDF 页面
Abstract: Aspose.PDF for Go via C++ 提供高效的功能，可从 PDF 文档中删除页面，使开发者能够轻松删除不需要或多余的页面。该库通过指定页码或范围，支持删除单页或多页，确保文档修改的精确性。此功能通过消除冗余内容并优化文档结构，帮助简化 PDF 文件。文档提供了逐步指南和代码示例，帮助开发者在应用程序中有效实现页面删除功能。
SoftwareApplication: go-cpp
---

您可以使用 **Aspose.PDF for Go via C++** 删除 PDF 文件中的页面。下面的代码片段演示了如何通过删除特定页面来操作 PDF 文档。此方法对于 PDF 文档的操作任务非常高效，尤其是删除页面、保存修改后的文档以及确保正确的资源管理。

1. 打开 PDF 文件。
1. 使用 删除特定页面 [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) 函数。
1. 使用 保存文档 [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) 方法。

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
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

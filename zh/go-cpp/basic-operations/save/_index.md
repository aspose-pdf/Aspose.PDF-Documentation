---
title: 以编程方式保存 PDF 文档
linktitle: 保存 PDF
type: docs
weight: 30
url: /zh/go-cpp/save-pdf-document/
description: 了解如何使用 Aspose.PDF for Go 通过 C++ 保存 PDF 文件。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 通过 C++ 保存 PDF 文档
Abstract: Aspose.PDF for Go 通过 C++ 提供了全面的功能，可高效灵活地将 PDF 文档保存为各种格式和位置。该库允许开发者将 PDF 保存到文件系统、内存流，或输出为其他格式，如 DOCX、XLSX 和图像。它提供了自定义保存参数、优化文件大小以及确保数据完整性的选项。文档中包含详细的说明和代码示例，帮助开发者在其应用程序中高效实现 PDF 保存功能。
SoftwareApplication: go-cpp
---

## 将 PDF 文档保存到文件系统

该示例展示了 [New](https://reference.aspose.com/pdf/go-cpp/core/new/) 用于创建新 PDF 文档的方法，这是动态生成文档（如报告或发票）的基本功能。

代码简洁，可作为添加文本、图像或注释等更高级功能的模板。

此示例演示了 Aspose.PDF Go 库的直接使用，展示了其在创建、修改和保存文档方面的潜力。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

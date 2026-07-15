---
title: 在 Go 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /zh/go-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-04"
description: Aspose.PDF for Go 允许您将 PDF 转换为 XLSX 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 用于将 PDF 转换为 Excel 文档的 Golang 工具
Abstract: Aspose.PDF for Go 通过 C++ 库提供了一个强大的解决方案，可将 PDF 文档高精度、高效率地转换为 XLSX 格式。此功能使开发人员能够从 PDF 中提取表格数据，同时保留 Excel 电子表格的原始布局、结构和格式。文档提供了关于实现转换过程的详细指导，包括示例代码和分步说明，以促进该功能无缝集成到 Go 应用程序中。
SoftwareApplication: go-cpp
---

**Aspose.PDF for Go** 支持将 PDF 文件转换为 Excel 格式的功能。

## 将 PDF 转换为 XLSX

Excel 提供了用于排序、过滤和分析数据的高级工具，使得执行趋势分析或财务建模等任务更加容易，这些在静态 PDF 文件中很难实现。手动将数据从 PDF 复制到 Excel 耗时且易出错。转换可自动化此过程，为大数据集节省大量时间。

Aspose.PDF for Go 使用 [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/) 将下载的 PDF 文件转换为 Excel 电子表格并保存。

1. 导入所需的包。
1. 打开 PDF 文件。
1. 使用将 PDF 转换为 XLSX [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/).
1. 关闭 PDF 文档。

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
    // SaveXlsX(filename string) saves previously opened PDF-document as XlsX-document with filename
    err = pdf.SaveXlsX("sample.xlsx")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 Excel**

Aspose.PDF for Go 为您呈现在线免费应用 ["PDF 转 XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)， 您可以尝试探究其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 Excel 的免费应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

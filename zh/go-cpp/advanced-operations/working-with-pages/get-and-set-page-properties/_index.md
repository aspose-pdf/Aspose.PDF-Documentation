---
title: 获取和设置页面属性
linktitle: 获取和设置页面属性
type: docs
url: /zh/go-cpp/get-and-set-page-properties/
description: 了解如何使用 Aspose.PDF for Go 获取和设置 PDF 文档的页面属性，以实现自定义文档格式化。
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 获取和设置页面属性
Abstract: Aspose.PDF for Go via C++ 提供了全面的功能，用于在 PDF 文档中获取和设置页面属性，允许开发者访问和修改诸如尺寸、旋转、边距和元数据等多种页面属性。这些能力使得能够对文档布局和外观进行精确控制，以满足特定的应用需求。该库确保对 PDF 页面进行无缝的自定义和优化。文档提供了详细的指导和代码示例，帮助开发者在其应用程序中高效地检索和更新页面属性。
SoftwareApplication: go-cpp
---


Aspose.PDF for Go 允许您读取和设置 PDF 文件中页面的属性。本节展示了如何获取 PDF 文件的页数、获取 PDF 页面属性（如颜色）信息以及设置页面属性。

## 获取 PDF 文件的页数

在处理文档时，您通常想要了解它们包含多少页。使用 Aspose.PDF，这只需要不到两行代码。

**Aspose.PDF for Go via C++** 允许您使用 [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) 函数。

下面的代码片段旨在打开 PDF 文档，获取其页数，然后打印结果。

该 [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) 此方法用于获取 PDF 文档的总页数。当需要了解文档长度的任务（例如提取特定页或对所有页执行操作）时，它非常有用。该方法是查询文档结构的直接方式。

获取 PDF 文件的页数：

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
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## 设置页面尺寸

在此示例中，方法 pdf.PageSetSize() 更改 PDF 文档首页的尺寸。PageSizeA1 常量确保首页被设为 A1 纸张尺寸。这在将文档转换为标准化格式或确保特定内容在页面上正确适配时非常有用。

1. 使用以下方式打开 PDF 文档 [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) 方法。
1. 使用以下方式设置页面尺寸 [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) 函数。
1. 使用以下方式保存文档 [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) 方法。

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
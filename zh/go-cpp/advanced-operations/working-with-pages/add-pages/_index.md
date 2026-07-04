---
title: 向 PDF 文档添加页面
linktitle: 添加页面
type: docs
weight: 10
url: /zh/go-cpp/add-pages/
description: 了解如何使用 Aspose.PDF 在 Go 中向现有 PDF 添加页面，以增强和扩展您的文档。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 添加 PDF 页面
Abstract: Aspose.PDF for Go 通过 C++ 提供强大的功能，可向 PDF 文档添加页面，允许开发者动态创建新页面并根据特定需求进行定制。该库支持插入空白页或从现有文档复制页面，同时提供定义页面尺寸、方向和内容的选项。这些功能实现了无缝的文档扩展和定制。文档中包含详细的说明和代码示例，帮助开发者在其应用中高效实现页面添加功能。
SoftwareApplication: go-cpp
---

## 在 PDF 文件中添加页面

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库在 PDF 末尾执行添加页面操作。 

1. 该 [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) function 允许程序加载现有的 PDF 文件（sample.pdf）以进行操作。这对于任何 PDF 相关的操作都是必不可少的，例如编辑、添加内容或读取数据。
1. 该 [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) method 用于向现有 PDF 文档插入一个新的空白页。这对于扩展文档或为追加内容做准备很有用。
1. 该 [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) 方法确保对 PDF 的修改写回文件。此步骤对于持久化更改至关重要，例如新增页面的添加。
1. 该 [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) 方法通过 defer 调用，以释放在 PDF 操作期间分配的任何资源。这对于防止内存泄漏并确保高效的资源使用非常重要。

此代码段是一个简明高效的示例，展示如何使用 Aspose.PDF Go 库执行基本的 PDF 操作任务。

Aspose.PDF for Go 允许您在文件的任意位置向 PDF 文档插入页面，也可以在 PDF 文件末尾添加页面。

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## 在 PDF 文件中插入页面

该 [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) 该方法在指定位置插入一个新页面。当您需要向现有文档中插入额外页面时，此功能非常有用，例如向报告或演示文稿添加新章节或内容。

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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
---
title: 在 Go 中将 PDF 转换为 EPUB、TeX、文本、XPS
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: 本主题演示如何使用 Go 将 PDF 文件转换为其他文件格式，如 EPUB、LaTeX、Text、XPS 等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Golang 工具用于将 PDF 转换为 EPUB、TeX、Text 和 XPS。
Abstract: Aspose.PDF for Go via C++ 提供强大的功能，可将 PDF 文档转换为多种文件格式，包括 DOCX、PPTX、HTML、EPUB、SVG 等。此功能使开发人员能够无缝提取和重新利用 PDF 内容，同时在不同输出格式之间保持格式、结构和质量。该库提供灵活的选项，可根据特定需求定制转换过程。文档包含全面的指南和代码示例，帮助开发人员在其应用程序中高效实现 PDF 到文件的转换。
SoftwareApplication: go-cpp
---

## 将 PDF 转换为 EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** 是一种由国际数字出版论坛（IDPF）推出的免费且开放的电子书标准。文件的扩展名为 .epub。
EPUB 旨在可重排内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。EPUB 还支持固定布局内容。该格式旨在作为一种单一格式，供出版商和转换机构内部使用，以及用于分发和销售。它取代了 Open eBook 标准。

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 EPUB：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 EPUB [保存Epub]() 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 转 EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), 您可以尝试调查它的功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 EPUB 的免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## 将 PDF 转换为 TeX

**Aspose.PDF for Go** 支持将 PDF 转换为 TeX。
LaTeX 文件格式是一种带有特殊标记的文本文件格式，用于基于 TeX 的文档排版系统，以实现高质量的排版。

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 TeX：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 TeX [保存 TeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 转 LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), 您可以尝试调查它的功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 LaTeX/TeX 的免费应用](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为 TXT

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 TXT：

1. 打开 PDF 文档。
1. 使用将 PDF 文件转换为 TXT [SaveTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试将 PDF 转换为文本在线**

Aspose.PDF for Go 为您提供在线免费应用程序 [PDF 转文本](https://products.aspose.app/pdf/conversion/pdf-to-txt), 您可以尝试调查它的功能和工作质量。

[![Aspose.PDF 将 PDF 转换为文本的免费应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

XPS 文件类型主要与微软公司（Microsoft Corporation）的 XML 纸张规范（XML Paper Specification）相关联。XML 纸张规范（XPS），此前代号为 Metro，并包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的倡议。

**Aspose.PDF for Go** 提供将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式。让我们尝试使用所示的代码片段将 PDF 文件转换为 XPS 格式，使用 Go。

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 XPS：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 XPS [保存Xps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 转 XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), 您可以尝试调查它的功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 XPS 的免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## 将 PDF 转换为灰度 PDF

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为灰度 PDF：

1. 打开 PDF 文档。
1. 使用 将 PDF 页面转换为灰度 PDF [页面灰度](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

此示例将您的 PDF 的特定页面转换为灰度：

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

此示例将把整个 PDF 文档转换为灰度：

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
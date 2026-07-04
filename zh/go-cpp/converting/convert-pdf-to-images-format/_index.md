---
title: 在 Go 中将 PDF 转换为图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: /zh/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: 本主题向您展示如何使用 Aspose.PDF for Go 将 PDF 转换为多种图像格式，例如 TIFF、BMP、JPEG、PNG、SVG，只需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 将 PDF 转换为图像格式的工具
Abstract: Aspose.PDF for Go via C++ 可实现 PDF 文档无缝转换为多种图像格式，包括 JPEG、PNG、BMP 和 TIFF。此功能允许开发者在渲染高质量图像的同时保留原始文档的内容、布局和分辨率。该库提供灵活的输出设置选项，如分辨率、图像质量和色深。文档提供了逐步说明和代码示例，帮助开发者高效地将 PDF 转图像转换集成到其应用程序中。
SoftwareApplication: go-cpp
---

## Go 将 PDF 转换为图像

在本文中，我们将向您展示将 PDF 转换为图像格式的选项。

之前扫描的文档通常以 PDF 文件格式保存。然而，您是否需要在图形编辑器中编辑它或进一步以图像格式发送？我们为您提供了一款通用工具，可使用 **Aspose.PDF for Go via C++** 将 PDF 转换为图像。
最常见的任务是当您需要将整个 PDF 文档或文档的某些特定页面保存为一组图像时。**Aspose.PDF for Go via C++** 允许您将 PDF 转换为 JPG 和 PNG 格式，以简化从特定 PDF 文件获取图像所需的步骤。

**Aspose.PDF for Go via C++** 支持各种 PDF 到图像格式的转换。请检查该部分 [Aspose.PDF 支持的文件格式](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## 将 PDF 转换为 JPEG

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 JPEG 图像：

1. 打开 PDF 文档。
1. 使用 将页面转换为 JPEG [PageToJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 JPEG**

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 转 JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 JPEG 的免费应用](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## 将 PDF 转换为 TIFF

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为 TIFF 图像：

1. 打开 PDF 文档。
1. 使用 将页面转换为 TIFF [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 转 TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 TIFF 的免费应用](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## 将 PDF 转换为 PNG

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为 PNG 图像：

1. 打开 PDF 文档。
1. 使用 将页面转换为 PNG [PageToPng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序工作方式的示例，请查看下一个功能。

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 到 PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试调查其功能和工作质量。

[![如何使用免费应用将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**可伸缩矢量图形（SVG）** 是一组基于 XML 的文件格式规范，用于二维矢量图形，包括静态和动态（交互式或动画）图形。SVG 规范是一项开放标准，自 1999 年起由万维网联盟（W3C）进行开发。

## 将 PDF 转换为 SVG

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 SVG 图像：

1. 打开 PDF 文档。
1. 使用将页面转换为 SVG [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for Go 为您提供在线免费应用程序 ["PDF 转 SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 SVG 的免费应用](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## 将 PDF 转换为 DICOM

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为 DICOM 图像：

1. 打开 PDF 文档。
1. 使用将页面转换为 DICOM [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## 将 PDF 转换为 BMP

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 BMP 图像：

1. 打开 PDF 文档。
1. 使用 将页面转换为 BMP [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) 函数。
1. 关闭 PDF 文档并释放所有已分配的资源。

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
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
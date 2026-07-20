---
title: 在 Rust 中将 PDF 转换为图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: /zh/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: 本主题向您展示如何使用 Aspose.PDF for Rust 将 PDF 转换为多种图像格式，例如 TIFF、BMP、JPEG、PNG、SVG，只需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 将 PDF 转换为图像格式的工具
Abstract: Aspose.PDF for Rust via C++ 可实现 PDF 文档到各种图像格式的无缝转换，包括 JPEG、PNG、BMP 和 TIFF。此功能允许开发者在渲染高质量图像的同时，保留原始文档的内容、布局和分辨率。该库提供灵活的输出设置选项，如分辨率、图像质量和色彩深度。文档提供了逐步指南和代码示例，帮助开发者高效地将 PDF 到图像的转换集成到其应用程序中。
SoftwareApplication: rust-cpp
---

## 将 PDF 转换为图像

在本文中，我们将向您展示将 PDF 转换为图像格式的选项。

以前扫描的文档通常会保存为 PDF 文件格式。但是，您是否需要在图形编辑器中编辑它，或进一步以图像格式发送？我们为您提供了一个通用工具，使用 **Aspose.PDF for Rust via C++** 将 PDF 转换为图像。
最常见的任务是当您需要将整个 PDF 文档或文档的某些特定页面保存为一组图像时。**Aspose.PDF for Rust via C++** 允许您将 PDF 转换为 JPG 和 PNG 格式，以简化从特定 PDF 文件获取图像所需的步骤。

**Aspose.PDF for Rust via C++** 支持将 PDF 转换为各种图像格式。请检查该部分。 [Aspose.PDF 支持的文件格式](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### 将 PDF 转换为 JPEG

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 JPEG 图像：

1. 打开 PDF 文档。
1. 使用将页面转换为 JPEG [page_to_jpg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 JPEG**

Aspose.PDF for Rust 为您呈现在线免费应用 [PDF 转 JPEG](https://products.aspose.app/pdf/conversion/pdf-to-jpg), 您可以尝试调查其功能和质量是否正常。

[![Aspose.PDF 将 PDF 转换为 JPEG 的免费应用](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### 将 PDF 转换为 TIFF

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 TIFF 图像：

1. 打开 PDF 文档。
1. 使用将 Page 转换为 TIFF [page_to_tiff](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF 转 TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), 您可以尝试调查其功能和质量是否正常。

[![Aspose.PDF 将 PDF 转换为 TIFF 的免费应用](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### 将 PDF 转换为 PNG

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 PNG 图像：

1. 打开 PDF 文档。
1. 使用将页面转换为 PNG [页面转PNG](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序工作方式的示例，请检查下一个功能。

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF 转 PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), 您可以尝试调查其功能和质量是否正常。

[![如何使用免费应用将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**可伸缩矢量图形 (SVG)** 是一系列基于 XML 的文件格式规范，用于二维矢量图形，既包括静态也包括动态（交互式或动画）。SVG 规范是一项开放标准，自 1999 年起由万维网联盟 (W3C) 开发。

### 将 PDF 转换为 SVG

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为 SVG 图像：

1. 打开 PDF 文档。
1. 使用将页面转换为 SVG [页面转SVG](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for Rust 为您呈现在线免费应用 [PDF 转 SVG](https://products.aspose.app/pdf/conversion/pdf-to-svg), 您可以尝试调查其功能和质量是否正常。

[![Aspose.PDF 将 PDF 转换为 SVG 的免费应用](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### 将 PDF 转换为 SVG ZIP 压缩包

下面的示例将 PDF 文档转换为 SVG 存档，其中每页被保存为 ZIP 容器内的单独 SVG 文件。

1. 打开源 PDF 文档。
1. 将文档保存为包含 SVG 文件的 ZIP 存档。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### 将 PDF 转换为 DICOM

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的第一页转换为 DICOM 图像：

1. 打开 PDF 文档。
1. 使用将 Page 转换为 DICOM [页面_to_DICOM](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### 将 PDF 转换为 BMP

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为 BMP 图像：

1. 打开 PDF 文档。
1. 使用将页面转换为 BMP [页面转BMP](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```
---
title: 在 Rust 中将 PDF 转换为 EPUB、TeX、Text、XPS
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/rust-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-20"
description: 本主题向您展示如何使用 Rust 将 PDF 文件转换为其他文件格式，如 EPUB、LaTeX、文本、XPS 等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 用于将 PDF 转换为 EPUB、TeX、文本和 XPS 的 Rust 工具
Abstract: Aspose.PDF for Rust via C++ 提供强大的功能，将 PDF 文档转换为多种文件格式，包括 DOCX、PPTX、HTML、EPUB、SVG 等。此功能允许开发者无缝提取和重新利用 PDF 内容，同时在不同输出格式之间保持格式、结构和质量。该库提供灵活的选项，可根据具体需求自定义转换过程。文档包括完整的指南和代码示例，帮助开发者在应用程序中高效实现 PDF 到文件的转换。
SoftwareApplication: rust-cpp
---

## 将 PDF 转换为 EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** 是一种来自国际数字出版论坛（IDPF）的免费且开放的电子书标准。文件的扩展名为 .epub。
EPUB 旨在用于可重排内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。EPUB 也支持固定布局内容。该格式旨在作为出版商和转换机构可内部使用的单一格式，以及用于分发和销售。它取代了 Open eBook 标准。

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 EPUB：

1. 打开 PDF 文档。
1. 使用将 PDF 文件转换为 EPUB [保存_epub](https://reference.aspose.com/pdf/rust-cpp/convert/save_epub/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Epub-document
      pdf.save_epub("sample.epub")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF 转 EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以尝试调查其功能及工作质量。

[![Aspose.PDF 将 PDF 转换为 EPUB 的免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## 将 PDF 转换为 TeX

**Aspose.PDF for Rust** 支持将 PDF 转换为 TeX。
LaTeX 文件格式是一种带有特殊标记的文本文件格式，用于基于 TeX 的文档排版系统，以实现高质量的排版。

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 TeX：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 TeX [保存_tex](https://reference.aspose.com/pdf/rust-cpp/convert/save_tex/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as TeX-document
      pdf.save_tex("sample.tex")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Rust 为您呈现在线免费应用 [PDF 转 LaTeX](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以尝试调查其功能及工作质量。

[![Aspose.PDF 将 PDF 转换为 LaTeX/TeX 的免费应用](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为 TXT

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 TXT：

1. 打开 PDF 文档。
1. 使用将 PDF 文件转换为 TXT [保存_txt](https://reference.aspose.com/pdf/rust-cpp/convert/save_txt/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Txt-document
      pdf.save_txt("sample.txt")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为文本**

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF转文本"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以尝试调查其功能及工作质量。

[![Aspose.PDF 免费应用将 PDF 转换为文本](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 XPS

XPS 文件类型主要与微软公司的 XML Paper Specification（XML 纸张规范）相关联。XML Paper Specification（XPS），其前代代号为 Metro，并整合了 Next Generation Print Path（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的倡议。

**Aspose.PDF for Rust** 提供了一种将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式。让我们尝试使用提供的代码片段将 PDF 文件转换为 XPS 格式，使用 Rust。

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 XPS。

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 XPS [save_xps](https://reference.aspose.com/pdf/rust-cpp/convert/save_xps/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Xps-document
      pdf.save_xps("sample.xps")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF 转 XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以尝试调查其功能及工作质量。

[![Aspose.PDF 将 PDF 转换为 XPS 的免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## 将 PDF 转换为灰度 PDF

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档的首页转换为灰度 PDF：

1. 打开 PDF 文档。
1. 使用 将 PDF 页面转换为灰度 PDF [页面灰度](https://reference.aspose.com/pdf/rust-cpp/organize/page_grayscale/) 函数。

此示例将 PDF 的特定页面转换为灰度：

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Convert page to black and white
      pdf.page_grayscale(1)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_page1_grayscale.pdf")?;

      Ok(())
  }
```

## 将 PDF 转换为 Markdawn

提供的 Rust 代码片段演示了如何使用 Aspose.PDF for Rust 将 PDF 文档转换为 Markdown（.md）文件。

1. 打开源 PDF 文件。
1. 将 PDF 转换为 Markdown。
1. 将打开的 PDF 文档另存为 Markdown 文件。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Markdown-document
      pdf.save_markdown("sample.md")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 MD**

Aspose.PDF for Rust 为您呈现在线免费应用 [PDF 转 MD](https://products.aspose.app/pdf/conversion/md)，您可以尝试调查其功能及工作质量。

[![Aspose.PDF 转换 PDF 为 MD 的免费应用](pdf_to_md.png)](https://products.aspose.app/pdf/conversion/md)
{{% /alert %}}

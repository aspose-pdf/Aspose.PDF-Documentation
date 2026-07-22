---
title: 在 Rust 中将 PDF 转换为 PPTX
linktitle: 将 PDF 转换为 PowerPoint
type: docs
weight: 30
url: /zh/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF 允许您使用 Rust 将 PDF 转换为 PPTX 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 用于将 PDF 转换为 PowerPoint 的 Rust 工具
Abstract: Aspose.PDF for Rust 提供了一种可靠的解决方案，可将 PDF 文档转换为 PowerPoint (PPTX) 格式，同时保留原始布局、格式和内容结构。此功能使开发人员能够无缝地将静态 PDF 文件转换为动态、可编辑的演示文稿。该库提供自定义选项来控制转换过程，确保输出高质量，满足商业和专业用途。文档提供分步说明和代码示例，帮助开发人员高效地将 PDF 到 PowerPoint 的转换功能集成到他们的应用程序中。
SoftwareApplication: rust-cpp
---

## 将 PDF 转换为 PPTX

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 PPTX：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 PPTX [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) 函数。

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for Rust 为您呈现在线免费应用程序 ["PDF 转 PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，在这里您可以尝试探索其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 PPTX 的免费应用](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
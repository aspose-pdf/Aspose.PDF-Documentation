---
title: 在 Rust 中将 PDF 转换为 Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/rust-cpp/convert-pdf-to-doc/
lastmod: "2026-07-20"
description: 学习如何编写 Rust 代码将 PDF 转换为 DOC（DOCX）。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 将 PDF 转换为 Word 的工具
Abstract: Aspose.PDF for Rust via C++ 实现了 PDF 文档到 DOC 格式的无缝转换，同时保留原始文本、图像、表格和整体文档结构。此功能允许开发者将静态 PDF 转换为可编辑的 Word 文件，以便进一步修改和处理。该库提供了多种自定义选项来控制转换输出，确保高保真度和准确性。文档包含详细的说明和示例代码，帮助开发者在其应用程序中高效实现 PDF 到 DOC 的转换。
SoftwareApplication: rust-cpp
---

在 Microsoft Word 或其他支持 DOC 和 DOCX 格式的文字处理器中编辑 PDF 文件的内容。PDF 文件是可编辑的，但 DOC 和 DOCX 文件更灵活且可自定义。

## 将 PDF 转换为 DOC

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 DOC：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 DOC [save_doc](https://reference.aspose.com/pdf/rust-cpp/convert/save_doc/) 函数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Doc-document
      pdf.save_doc("sample.doc")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF 转 DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), 您可以尝试调查它的功能和工作质量。

[![将 PDF 转换为 DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Rust API 允许您读取并将 PDF 文档转换为 DOCX。DOCX 是 Microsoft Word 文档的常用格式，其结构已从纯二进制更改为 XML 与二进制文件的组合。Docx 文件可在 Word 2007 及其后续版本中打开，但无法在仅支持 DOC 文件扩展名的早期 MS Word 版本中打开。

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 DOCX：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 DOCX [save_docx](https://reference.aspose.com/pdf/rust-cpp/convert/save_docx/) 函数。

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document
      pdf.save_docx("sample.docx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Rust 为您呈现在线免费应用 ["PDF 转 Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), 您可以尝试调查它的功能和工作质量。

[![Aspose.PDF 转换 PDF 到 Word 免费应用](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 使用增强识别模式将 PDF 转换为 DOCX

使用 Aspose.PDF for Rust 的增强识别模式将 PDF 文档转换为 Microsoft Word（DOCX）文件。

增强识别模式生成可完全编辑的 DOCX，保留：

 - 段落结构
 - 将表格保留为原生 Word 表格
 - 逻辑文本流和格式

1. 打开源 PDF 文件。
1. 将 PDF 保存为启用了增强布局识别的 DOCX 文件。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document with Enhanced Recognition Mode (fully editable tables and paragraphs)
      pdf.save_docx_enhanced("sample_enhanced.docx")?;

      Ok(())
  }
```

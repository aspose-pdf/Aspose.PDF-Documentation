---
title: 使用 Rust 从 AcroForm 提取数据
linktitle: 从 AcroForm 提取数据
type: docs
weight: 50
url: /zh/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF 使从 PDF 文件中提取表单字段数据变得轻松。了解如何从 AcroForm 提取数据并将其保存为 XML、FDF 或 XFDF 格式。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过 Rust 从 AcroForm 提取数据
Abstract: 这篇文章解释了如何使用 Aspose.PDF for Rust via C++ 从 PDF 文件中提取 AcroForm 数据，并将其导出为广泛使用的数据交换格式——XML、FDD 和 XFDF。它演示了如何打开包含交互式表单字段的 PDF 文档，并以编程方式导出表单字段的名称和值，以便在原始 PDF 之外重新使用。通过为每种导出格式提供实用的 Rust 示例，文章突出了常见工作流，包括数据处理、表单提交、系统集成和长期数据存储，帮助开发者在应用程序中高效管理和重用 PDF 表单数据。
---

## 将 PDF 文件中的数据导出为 XML

此代码片段展示了如何使用 Aspose.PDF for Rust 将 PDF 文档中的 AcroForm 数据导出为 XML 文件。
该过程包括打开一个带有表单字段的现有 PDF 文件，然后将这些字段及其值导出到 XML 文档，以便进一步处理、存储或数据交换。

1. 打开 PDF 文档。
1. 调用 'export_xml' 方法提取表单字段数据并将其保存为 XML 文件。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## 从 PDF 文件导出数据到 FDF

Aspose.PDF for Rust via C++ 允许您将 PDF 文档中的 AcroForm 数据导出到 FDF 文件。表单数据格式（FDF）文件将表单字段名称和值与 PDF 分离存储，使其在数据交换、表单提交工作流以及在不将表单数据嵌入原始文档的情况下归档表单数据时非常有用。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## 从 PDF 文件导出数据到 XFDF

XFDF（XML Forms Data Format）是一种基于 XML 的格式，它将表单字段数据与 PDF 文件分开表示，使其非常适合数据交换、表单提交以及与基于 Web 的工作流集成。
Aspose.PDF for Rust via C++ 可帮助将 PDF 文档中的 AcroForm 数据导出为 XFDF 文件。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```

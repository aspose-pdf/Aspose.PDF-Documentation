---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
weight: 20
url: /zh/rust-cpp/open-pdf-document/
description: 了解如何使用 Aspose.PDF for Rust via C++ 打开 PDF 文件。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust via C++ 打开 PDF 文档
Abstract: Aspose.PDF for Rust via C++ 提供强大的功能，以编程方式打开和加载 PDF 文档，使开发人员能够轻松访问和操作 PDF 内容。该库支持从多种来源打开 PDF 文件，如文件路径和内存流，并确保高效的处理和资源管理。它提供检查文档属性、提取文本和图像以及对已加载的 PDF 执行其他操作的功能。文档中包含详细的说明和代码示例，帮助开发人员无缝地将 PDF 打开功能集成到其应用程序中。
SoftwareApplication: rust-cpp
---

## 打开现有 PDF 文档

此代码片段演示了使用 Aspose.PDF for Rust 处理 PDF 的基本操作。这些操作包括打开文件、保存更改以及正确关闭资源。这使其成为处理 PDF 文档的开发者的基础示例。

该示例直观简洁，易于理解和修改。它非常适合初学者或用作更复杂应用的模板。

在许多场景中，打开和保存 PDF 文档的能力是核心需求，例如生成报告、修改文档或创建自动化工作流。

该示例展示了 API 在简单 PDF 操作上的易用性，且可以扩展以包括文本提取、批注或表单填写等高级功能。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document named "sample.pdf"
        let pdf = Document::open("sample.pdf")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_open.pdf")?;

        Ok(())
    }
```

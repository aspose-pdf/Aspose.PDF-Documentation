---
title: 使用 Rust 从 PDF 中提取文本
linktitle: 从 PDF 中提取文本
type: docs
weight: 30
url: /zh/rust-cpp/extract-text-from-pdf/
description: 本文介绍了使用 Aspose.PDF for Rust 从 PDF 文档中提取文本的各种方法。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 提取文本
Abstract: 通过 C++ 的 Aspose.PDF for Rust 提供了一种强大且高效的从 PDF 文档中提取文本的方法。该库支持多种提取技术，使用户能够从整个文档、特定页面或 PDF 中的预定义区域检索文本。
SoftwareApplication: rust-cpp
---

## 从 PDF 文档中提取文本

从 PDF 文档中提取文本是一个非常常见且有用的任务。PDF 通常包含需要访问、分析或处理的关键信息，用于各种目的。提取文本可以更容易地在数据库、报告或其他文档中重复使用。

提取文本使 PDF 内容可搜索，允许用户快速定位特定信息，无需手动审阅整个文档。

如果您想从 PDF 文档中提取文本，可以使用 [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) 函数。
请检查以下代码片段，以使用 Rust 从 PDF 文件中提取文本。

1. 使用给定的文件名打开 PDF 文档。
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) 从 PDF 文档中提取文本内容。
1. 将提取的文本打印到控制台。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```
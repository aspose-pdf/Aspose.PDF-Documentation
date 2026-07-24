---
title: 使用 Rust 通过 C++ 旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 50
url: /zh/rust-cpp/rotate-pages/
description: 本主题描述如何使用 Rust 通过 C++ 以编程方式旋转现有 PDF 文件中的页面方向
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 旋转 PDF 页面
Abstract: Aspose.PDF for Rust via C++ 提供强大的功能来旋转 PDF 文档中的页面，允许开发人员根据需要修改页面方向。该库支持将页面旋转 90、180 或 270 度，从而快速高效地调整文档布局。此功能对于纠正方向错误的页面或改变文档的展示方式非常有用。文档中包含一步一步的说明和代码示例，帮助开发人员无缝地将页面旋转功能集成到其应用程序中。
SoftwareApplication: rust-cpp
---

本节描述如何使用 Rust 在现有 PDF 文件中将页面方向从横向更改为纵向，或反之。

旋转页面可确保在专业环境中打印或显示 PDF 时的正确对齐

1. 打开 PDF 文档。
1. 旋转 PDF 页面。该 [旋转](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) 函数将特定的旋转（在本例中为 180 度）应用于给定页面。
1. 将更改保存为新文件。该 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 函数创建一个新的 PDF 文件，以在保存更新版本的同时保留原始文件。

在此示例中，您旋转 PDF 文档中的特定页面：

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```
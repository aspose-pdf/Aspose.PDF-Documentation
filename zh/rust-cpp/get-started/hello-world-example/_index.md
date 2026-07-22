---
title: 使用 Rust 语言的 Hello World 示例
linktitle: Hello World 示例
type: docs
weight: 40
url: /zh/rust-cpp/hello-world-example/
description: 此示例演示如何使用 Aspose.PDF for Rust 创建包含文本 Hello World 的简单 PDF 文档。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Aspose.PDF for Rust 实现 Hello World
Abstract: Aspose.PDF for Rust via C++ 的入门指南提供了使用该库的介绍，涵盖创建和操作 PDF 文档的基本步骤。它包含一个 'Hello World' 示例，演示如何生成包含文本内容的简易 PDF 文件，帮助开发者快速了解 API 的核心功能。
SoftwareApplication: rust-cpp
---

传统上，\"Hello World\" 示例用于通过一个简单的用例来介绍编程语言或软件的特性。

**Aspose.PDF for Rust** 是一个功能丰富的 PDF API，允许开发人员使用 Rust 嵌入 PDF 文档的创建、操作和转换功能。它支持许多流行的文件格式，包括 PDF、TXT、XLSX、EPUB、TEX、DOC、DOCX、PPTX、图像格式等。在本文中，我们将创建一个包含文本 “Hello World!” 的 PDF 文档。安装 Aspose.PDF for Rust 后，您可以运行代码示例，了解 Aspose.PDF API 的工作方式。
下面的代码片段遵循以下步骤：

1. 创建一个新的 PDF 文档实例。
1. 使用以下方式向 PDF 文档添加新页面 [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) 函数。
1. 使用以下方式设置页面大小 [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. 使用以下方式在第一页添加 "Hello World!" 文本 [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. 使用以下方式保存 PDF 文档 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 方法。

以下代码片段是一个 Hello World 程序，用于展示 Aspose.PDF for Rust API 的工作原理。

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```

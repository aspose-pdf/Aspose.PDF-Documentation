---
title: 使用 Rust 向 PDF 添加文本
linktitle: 向 PDF 添加文本
type: docs
weight: 10
url: /zh/rust-cpp/add-text-to-pdf-file/
description: 了解如何使用 Aspose.PDF 在 Rust 中向 PDF 文档添加文本，以实现内容增强和文档编辑。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: 使用 Aspose.PDF for Rust 向 PDF 添加文本
Abstract: Aspose.PDF for C++ 和 Rust 文档中的 “向 PDF 文件添加文本” 部分提供了以编程方式向 PDF 文档插入文本的逐步说明。它涵盖了添加文本的各种方法，包括定位、字体自定义、颜色调整和文本对齐选项。该指南演示了如何向 PDF 中的特定页面和位置添加文本，确保内容精准放置。通过详细的代码示例和解释，开发者可以轻松将文本插入功能集成到其应用程序中，从而提升 PDF 文档管理。
SoftwareApplication: rust-cpp
---

要向现有 PDF 文件添加文本：

1. 打开 PDF 文件。
1. 使用以下方式将文本添加到 PDF 文档中 [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) function.
1. 将修改保存到同一文件。

## 添加文本

以下代码片段展示了如何在现有 PDF 文件中添加文本。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

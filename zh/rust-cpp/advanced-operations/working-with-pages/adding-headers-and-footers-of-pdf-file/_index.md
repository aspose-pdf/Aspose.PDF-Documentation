---
title: 使用 Rust 为 PDF 添加页眉和页脚
linktitle: 为 PDF 添加页眉和页脚
type: docs
weight: 90
url: /zh/rust-cpp/add-headers-and-footers-of-pdf-file/
description: 本文演示了如何使用 Aspose.PDF for Rust via C++ 为 PDF 文档添加文本页眉和页脚。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Rust 为 PDF 添加页眉和页脚
Abstract: 本文演示了如何使用 asposepdf Rust 库为 PDF 文档添加文本页眉和页脚。它解释了如何打开现有的 PDF，在每页的页眉或页脚插入一致的文本，并将修改后的文档另存为新文件。示例展示了一种简单、可靠的工作流，可用于在 Rust 应用程序中以编程方式添加页码、标题或品牌标识等任务。
SoftwareApplication: rust-cpp
---

## 将页眉和页脚添加为文本片段

### 在 PDF 文档的页脚中添加文本

我们的工具可以让您打开现有的 PDF，向所有页面添加文本页脚，并使用 asposepdf Rust 库将修改后的 PDF 保存为新文件。它使用 Rust 的 Result 类型优雅地处理错误。

1. 打开现有的 PDF 文档。
1. 使用以下方式向页脚添加文本 [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. 保存修改后的 PDF。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### 在 PDF 文档的页眉中添加文本

此代码片段演示了如何打开现有的 PDF 文件，向所有页面添加文本页眉，并使用 asposepdf 库将修改后的文档保存为新文件。它提供了一种简单、自动化的方式，将一致的页眉插入 PDF 中。

1. 打开现有的 PDF。
1. 使用帮助向标题添加文本 [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. 保存修改后的 PDF。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```
---
title: 使用 Rust 通过 C++ 删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 30
url: /zh/rust-cpp/delete-pages/
description: 您可以使用 Aspose.PDF for Rust via C++ 删除 PDF 文件中的页面。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 删除 PDF 页面
Abstract: Aspose.PDF for Rust via C++ 提供高效的功能来删除 PDF 文档中的页面，使开发者能够轻松移除不需要或多余的页面。该库通过指定页码或范围，支持删除单页或多页，从而确保文档修改的精确性。此功能通过消除冗余内容并优化文档结构，帮助简化 PDF 文件。文档提供了分步说明和代码示例，以帮助开发者在其应用程序中有效实现页面删除功能。
SoftwareApplication: rust-cpp
---

您可以使用 **Aspose.PDF for Rust via C++** 删除 PDF 文件中的页面。下面的代码片段演示了如何通过删除特定页面来操作 PDF 文档。此方法对于 PDF 文档的操作任务非常高效，特别是用于删除页面、保存修改后的文档以及确保正确的资源管理。

1. 打开 PDF 文件。
1. 使用删除特定页面 [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) 函数。
1. 使用以下方式保存文档 [保存](https://reference.aspose.com/pdf/rust-cpp/core/save/) 方法。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

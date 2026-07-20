---
title: 向 PDF 文档添加页面
linktitle: 添加页面
type: docs
weight: 10
url: /zh/rust-cpp/add-pages/
description: 探索如何在 Rust 中使用 Aspose.PDF 向现有 PDF 添加页面，以增强和扩展您的文档。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 添加 PDF 页面
Abstract: Aspose.PDF for Rust via C++ 提供了强大的功能，可向 PDF 文档添加页面，允许开发者动态创建新页面并根据特定需求进行自定义。该库支持插入空白页面或从现有文档复制页面，同时提供定义页面尺寸、方向和内容的选项。这些功能实现了无缝的文档扩展和定制。文档中包含详细的说明和代码示例，帮助开发者在应用程序中高效实现页面添加功能。
SoftwareApplication: rust-cpp
---

## 在 PDF 文件中添加页面

提供的 Rust 代码片段演示了如何使用 Aspose.PDF 库在 PDF 文档末尾执行 Add Page 操作。

1. 该 [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) 函数允许程序加载现有的 PDF 文件（sample.pdf）进行操作。这对于任何 PDF 相关的操作都是必不可少的，例如编辑、添加内容或读取数据。
1. 该 [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) 该方法用于在现有 PDF 文档中插入一个新的空白页。这对于扩展文档或为添加额外内容做准备非常有用。
1. 该 [保存](https://reference.aspose.com/pdf/rust-cpp/core/save/) 此方法确保对 PDF 的修改写回文件。此步骤对于持久化更改至关重要，例如添加新页面。

此代码片段是一个简洁高效的示例，演示如何使用 Aspose.PDF Rust 库进行基本的 PDF 操作任务。

Aspose.PDF for Rust 允许您在文件的任何位置向 PDF 文档插入页面，也可以在 PDF 文件的末尾添加页面。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## 在 PDF 文件中插入页面

该 [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) 该方法在指定位置插入新页面。当您需要向现有文档中插入额外页面时，此功能非常有用，例如向报告或演示文稿添加新章节或内容。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
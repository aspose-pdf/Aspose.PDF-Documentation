---
title: 获取和设置页面属性
linktitle: 获取和设置页面属性
type: docs
url: /zh/rust-cpp/get-and-set-page-properties/
description: 了解如何使用 Aspose.PDF for Rust 获取和设置 PDF 文档的页面属性，从而实现自定义文档格式化。
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 获取和设置页面属性
Abstract: Aspose.PDF for Rust via C++ 提供了全面的功能，用于在 PDF 文档中获取和设置页面属性，允许开发人员访问和修改诸如尺寸、旋转、边距和元数据等各种页面属性。这些能力使得能够对文档布局和外观进行精确控制，以满足特定的应用需求。该库确保对 PDF 页面进行无缝的自定义和优化。文档提供了详细的指南和代码示例，帮助开发人员在其应用程序中高效地检索和更新页面属性。
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust 让您能够读取和设置 PDF 文件中页面的属性。本节展示了如何获取 PDF 文件的页数，获取有关 PDF 页面属性（如颜色）的信息以及设置页面属性。

## 获取 PDF 文件的页数

在处理文档时，您通常想知道它们包含多少页。使用 Aspose.PDF，这只需不超过两行代码。

**Aspose.PDF for Rust via C++** 允许您使用 [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) 函数。

下面的代码片段旨在打开 PDF 文档，获取其页数，然后打印结果。

该 [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) 该方法用于获取 PDF 文档的总页数。对于需要了解文档长度的任务非常有用，例如提取特定页或对所有页执行操作。此方法是查询文档结构的直接方式。

获取 PDF 文件的页数：

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## 设置页面大小

在此示例中，方法 pdf.PageSetSize() 更改 PDF 文档首页的大小。PageSizeA1 常量确保首页设置为 A1 纸张尺寸。这在将文档转换为标准化格式或确保特定内容正确适配页面时非常有用。

1. 使用以下方式打开 PDF 文档 [打开](https://reference.aspose.com/pdf/rust-cpp/core/open/) 方法。
1. 使用以下方式设置页面大小 [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) 函数。
1. 使用以下方式保存文档 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 方法。

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```
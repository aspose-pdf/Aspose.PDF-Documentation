---
title: 使用 Aspose.PDF for Rust via C++ 进行 PDF 拼版
linktitle: PDF 拼版
type: docs
weight: 30
url: /zh/rust-cpp/pdf-imposition/
description: 本文解释了如何使用 Aspose.PDF for Rust via C++ 重新排列 PDF 页面，以实现印刷优化的布局。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何制作 PDF 文件的手册或 N-Up 排版
Abstract: Aspose.PDF for Rust via C++ 提供了强大的工具，用于重构 PDF 文档以满足印刷和布局需求。本文演示了如何将标准 PDF 转换为手册，确保折叠时的正确页序，以及如何创建将多页合并到单张纸上的 N-Up PDF。通过简洁的 Rust 代码示例，开发者可以快速实现面向文档、出版和归档工作流的可打印 PDF 转换。
SoftwareApplication: rust-cpp
---

## 制作 PDF 的 N-Up

N-Up PDF 将多个源页面放置在单个输出页面上。在此示例中，使用 2 × 2 布局，因此每个输出文档页面会合并四个原始页面。

1. 打开源 PDF 文档。
1. 使用指定的行数和列数的 N-Up 布局保存文档。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## 制作 PDF 小册子

Aspose.PDF for Rust via C++ 解释了如何将标准 PDF 文档转换为小册子样式的 PDF。
小册子格式会重新排列页面，使得在打印和折叠后，文档形成一个正确顺序的完整小册子。

1. 打开源 PDF 文档。
1. 将文档保存为小册子 PDF。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**请注意，完整功能需要免费试用许可证。**

探索创建4页小册子的结果。

![4页小册子的示例](sample_4.png)

探索创建3页小册子的结果。

![3页小册子的示例](sample_3.png)
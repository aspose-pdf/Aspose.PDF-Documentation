---
title: 使用 Rust 为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 10
url: /zh/rust-cpp/add-page-number/
description: 本文演示了如何使用 Aspose.PDF for Rust via C++ 向现有 PDF 文档添加页码。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 添加页码
Abstract: Aspose.PDF for Rust via C++ 使开发者能够仅通过几行代码为现有 PDF 文档添加自动页码。 本示例演示了如何打开 PDF 文件、在所有页面插入页码，并将更新后的文档另存为新文件。 自动化分页确保文档结构一致，尤其适用于报告、合同、手册以及其他用于分发或打印的多页输出。
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++ 提供了内置功能，可对 PDF 文档进行编程式修改。 在本示例中，应用程序打开一个现有的 PDF 文件，对每页应用自动页码，并将修改后的文档另存为新名称。

此方法在生成用于分发、打印或归档的最终文档时非常有用。该过程仅需几行代码，并且除非明确覆盖，否则不会更改原始文件。

页码是报告、发票、合同、手册以及其他多页文档的常见需求。 这 [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) 此方法会自动在文档的所有页面插入页码，确保整篇文件的分页一致。

添加页码后，更新后的文档将保存为新的 PDF 文件。

1. 打开现有的 PDF 文档。
1. 使用 添加页码 [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) 方法。
1. 保存更新后的文档。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```
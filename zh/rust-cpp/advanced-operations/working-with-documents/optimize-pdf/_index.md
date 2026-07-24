---
title: 使用 Aspose.PDF for Rust via C++ 优化 PDF
linktitle: 优化 PDF 文件
type: docs
weight: 10
url: /zh/rust-cpp/optimize-pdf/
description: 使用 Rust 工具优化和压缩 PDF 文件。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 优化和压缩 PDF 文件
Abstract: Aspose.PDF for Rust via C++ 提供强大的优化功能，以缩小 PDF 文档的体积并提升其性能。该库提供多种优化选项，包括压缩图像、删除未使用的对象、减小字体大小以及优化内容流。这些功能有助于提升文档存储效率，并确保更快的处理和加载时间。文档中提供了分步指南和代码示例，帮助开发者在其应用程序中有效实现 PDF 优化。
SoftwareApplication: rust-cpp
---

## 优化 PDF 文档

使用 Aspose.PDF for Rust via C++ 的工具包允许您优化 PDF 文档。

此代码段对那些对 PDF 文件的大小减小或效率提升至关重要的应用场景非常有用，例如网页上传、归档或在带宽受限的情况下共享。

1. 该 [打开](https://reference.aspose.com/pdf/rust-cpp/core/open/) 方法将指定的 PDF 文件 (sample.pdf) 加载到内存中。
1. 该 [优化](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/) 通过执行诸如删除未使用的对象、压缩图像、扁平化注释、取消嵌入字体以及启用内容复用等优化来减小文件大小。这些步骤有助于降低存储需求并提升 PDF 文档的处理速度。
1. 该 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) 该方法将优化后的 PDF 保存为新文件。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```
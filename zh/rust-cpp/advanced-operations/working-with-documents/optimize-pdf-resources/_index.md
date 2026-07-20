---
title: 使用 Rust 通过 C++ 优化 PDF 资源
linktitle: 优化 PDF 资源
type: docs
weight: 15
url: /zh/rust-cpp/optimize-pdf-resources/
description: 使用 Rust 工具优化 PDF 文件的资源。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Rust 优化 PDF 资源
Abstract: 通过 C++ 的 Aspose.PDF for Rust 提供了先进的功能来优化 PDF 资源，提升文档效率并减小文件大小。该库允许开发者通过删除冗余数据和压缩资源来优化字体、图像和元数据，同时不影响文档质量。这些优化技术可提升文档性能，使 PDF 更加适合共享和存储。文档提供了详细的指导和代码示例，帮助开发者在应用程序中有效实现资源优化。
SoftwareApplication: rust-cpp
---

## 优化 PDF 资源

优化文档中的资源：

  1. 未在文档页面使用的资源将被移除。
  1. 相同的资源将合并为单个对象。
  1. 未使用的对象将被删除。

优化可能包括压缩图像、移除未使用的对象以及优化字体以减小文件大小并提升性能。此操作期间的任何错误都会被记录并终止程序。  
 
1. 该 [打开](https://reference.aspose.com/pdf/rust-cpp/core/open/) method 将指定的 PDF 文件（sample.pdf）加载到内存中。
1. 使用 对 PDF 中的资源进行优化以提升效率 [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) method.
1. 该 [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method 将已优化的 PDF 保存到新文件。

以下代码片段展示了如何优化 PDF 文档。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_open.pdf")?;

      Ok(())
  }
```
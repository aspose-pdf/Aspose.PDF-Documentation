---
title: Aspose PDF 许可证
linktitle: 许可及限制
type: docs
weight: 90
url: /zh/rust-cpp/licensing/
description: Aspose.PDF for Rust 邀请其客户获取 Classic License。也可以使用有限许可证来更好地探索产品。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 C++ 的 Aspose.PDF for Rust 许可
Abstract: 通过 C++ 的 Aspose.PDF for Rust 的许可页面说明了该产品可用的许可选项。客户可以在 Classic License、Metered License 或用于评估目的的有限许可证之间进行选择。该页面还强调了获取正式许可证的好处，例如解锁全部功能并消除评估限制。
SoftwareApplication: rust-cpp
---

## 许可证

- 该 **Rust 源代码** 在 MIT 许可证下授权。
- 该 **共享库** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) 为专有软件，需要商业许可证。要使用全部功能，您必须获取许可证。

## 评估版

您可以免费使用 **Aspose.PDF for Rust via C++** 进行评估。评估版提供了几乎全部产品功能，但有一定限制。当您购买许可证并添加少量代码以应用许可证后，同一评估版即转为正式授权版。

- 如果您想在没有评估版限制的情况下测试 Aspose.PDF for Rust，您也可以申请 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)?

### 评估版的限制

我们希望客户在购买之前彻底测试我们的组件，因此评估版允许您像平常一样使用它。

- **带有评估水印的文档**。Aspose.PDF for Rust 的评估版提供完整的产品功能，但生成文件的所有页面顶部都会加上文字“Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd.”的水印。
- **可处理页面数量的限制**。在评估版中，您只能处理文档的前四页。

### 在生产环境中使用

在生产环境中需要商业许可证密钥。请联系我们购买商业许可证。

### 应用许可证

通过使用许可证文件 (Aspose.PDF.RustViaCPP.lic) 为 Aspose.PDF for Rust 应用许可证，以启用其完整功能。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```
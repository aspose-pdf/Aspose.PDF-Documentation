---
title: 使用 Rust 打开受密码保护的 PDF
linktitle: 打开受密码保护的 PDF
type: docs
weight: 70
url: /zh/rust-cpp/open-password-protected-pdf/
description: 使用 Aspose.PDF for Rust via C++ 打开受密码保护的 PDF 文件。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 打开受密码保护的 PDF 文档

使用 Aspose.PDF for Rust via C++ 打开受密码保护的 PDF 文档。该文档使用所有者密码打开，授予完整访问权限，并允许进一步操作，例如读取元数据、修改内容、更改权限或移除加密。

1. 使用 ... 打开受保护的 PDF 文档 [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) 并提供文件路径以及所有者密码以解锁文档。
1. 对已打开的文档进行操作。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```
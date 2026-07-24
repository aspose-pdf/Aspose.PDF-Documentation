---
title: 使用 Rust 获取权限
linktitle: 获取权限
type: docs
weight: 60
url: /zh/rust-cpp/get-permissions/
description: 使用 Aspose.PDF for Rust via C++ 读取并显示受密码保护的 PDF 文档的访问权限。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 获取受密码保护的 PDF 文档的权限

本节说明如何在 Rust 中读取并显示受密码保护的 PDF 文档的访问权限。
PDF 使用所有者密码打开，这授予对文档安全设置的完全访问权限。随后检索当前分配的权限并打印到控制台。

1. 打开受保护的 PDF 文档。
1. 调用 [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) 获取定义允许哪些操作的权限标志。
1. 将检索到的权限打印到控制台。

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let pdf = Document::open_with_password("sample_with_permissions.pdf", "ownerpass")?;

        // Get current permissions of PDF-document
        let permissions: Permissions = pdf.get_permissions()?;

        // Print permissions
        println!("Permissions: {}", permissions);

        Ok(())
    }
```
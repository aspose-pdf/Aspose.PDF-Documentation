---
title: 使用 Rust 为 PDF 文档设置权限
linktitle: 设置权限
type: docs
weight: 80
url: /zh/rust-cpp/set_permissions/
description: 使用 Aspose.PDF for Rust via C++ 为 PDF 文档设置权限。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 为 PDF 文档设置访问权限

创建一个新的 PDF 文档，并使用用户密码和所有者密码进行保护，同时明确允许特定操作——例如打印、修改内容和填写表单。然后在应用定义的权限限制后保存文档。

1. 创建一个新的 PDF 文档。
1. 调用 [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) 以保护文档。
1. 指定用户密码以限制访问。
1. 指定拥有者密码以控制安全设置。
1. 使用权限位标志定义允许的操作。
1. 使用以下方式保存已应用权限的 PDF [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Set permissions for PDF-document.
        pdf.set_permissions(
            "userpass",  // User password
            "ownerpass", // Owner password
            Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
        )?;

        // Save the PDF-document with the updated permissions
        pdf.save_as("sample_with_permissions.pdf")?;

        Ok(())
    }
```
---
title: الحصول على الأذونات باستخدام Rust
linktitle: الحصول على الأذونات
type: docs
weight: 60
url: /ar/rust-cpp/get-permissions/
description: قراءة وعرض أذونات الوصول لمستند PDF محمي بكلمة مرور باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## الحصول على أذونات مستند PDF محمي بكلمة مرور

يوضح هذا القسم كيفية قراءة وعرض أذونات الوصول لمستند PDF محمي بكلمة مرور باستخدام Rust.
يتم فتح ملف PDF باستخدام كلمة مرور المالك، والتي تمنح وصولًا كاملًا إلى إعدادات أمان المستند. ثم تُسترجع الأذونات المخصصة حاليًا وتُطبع إلى وحدة التحكم.

1. افتح مستند PDF المحمي.
1. استدع [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) للحصول على أعلام الأذونات التي تحدد أي العمليات مسموح بها.
1. اطبع الأذونات المستخرجة إلى وحدة التحكم.

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
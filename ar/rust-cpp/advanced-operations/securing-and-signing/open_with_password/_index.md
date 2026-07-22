---
title: افتح ملف PDF محمي بكلمة مرور باستخدام Rust
linktitle: افتح PDF محمي بكلمة مرور
type: docs
weight: 70
url: /ar/rust-cpp/open-password-protected-pdf/
description: افتح ملف PDF محمي بكلمة مرور باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## افتح مستند PDF محمي بكلمة مرور

افتح مستند PDF محمي بكلمة مرور باستخدام Aspose.PDF for Rust عبر C++. يتم فتح المستند باستخدام كلمة مرور المالك، التي تمنح وصولًا كاملاً وتسمح بإجراء عمليات أخرى مثل قراءة البيانات الوصفية، تعديل المحتوى، تغيير الأذونات، أو إزالة التشفير.

1. افتح المستند PDF المحمي باستخدام [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) وقدم مسار الملف مع كلمة مرور المالك لفتح المستند.
1. اعمل مع المستند المفتوح.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```
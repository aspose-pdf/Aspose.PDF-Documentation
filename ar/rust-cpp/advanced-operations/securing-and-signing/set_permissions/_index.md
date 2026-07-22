---
title: تعيين أذونات لمستند PDF باستخدام Rust
linktitle: تعيين الأذونات
type: docs
weight: 80
url: /ar/rust-cpp/set_permissions/
description: تعيين أذونات لمستند PDF باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تعيين أذونات الوصول لمستند PDF

تم إنشاء مستند PDF جديد وحمايته بكلمات مرور للمستخدم والمالك، بينما تُسمح صراحةً إجراءات محددة—مثل الطباعة وتعديل المحتوى وملء النماذج—. ثم يتم حفظ المستند مع تطبيق قيود الأذونات المحددة.

1. إنشاء مستند PDF جديد.
1. استدعاء [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) لحماية المستند.
1. حدد كلمة مرور المستخدم لتقييد الوصول.
1. حدد كلمة مرور المالك للتحكم في إعدادات الأمان.
1. حدد العمليات المسموح بها باستخدام علم أذونات البت.
1. احفظ ملف PDF مع تطبيق الأذونات باستخدام [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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
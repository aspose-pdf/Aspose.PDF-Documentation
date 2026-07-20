---
title: إضافة نص إلى PDF باستخدام Rust
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: /ar/rust-cpp/add-text-to-pdf-file/
description: تعلم كيفية إضافة نص إلى مستند PDF في Rust باستخدام Aspose.PDF لتحسين المحتوى وتحرير المستندات.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: إضافة نص إلى PDF باستخدام Aspose.PDF لـ Rust
Abstract: يوفر قسم "إضافة نص إلى ملف PDF" في وثائق Aspose.PDF للـ C++ و Rust إرشادات خطوة بخطوة حول إدراج النص في مستندات PDF برمجيًا. يغطي طرقًا مختلفة لإضافة النص، بما في ذلك تحديد الموقع، وتخصيص الخط، وضبط الألوان، وخيارات محاذاة النص. يوضح الدليل كيفية إضافة النص إلى صفحات ومواقع معينة داخل PDF، مما يضمن وضع المحتوى بدقة. مع أمثلة شفرة مفصلة وتفسيرات، يمكن للمطورين دمج ميزات إدراج النص بسهولة في تطبيقاتهم لإدارة مستندات PDF محسّنة.
SoftwareApplication: rust-cpp
---

لإضافة نص إلى ملف PDF موجود:

1. فتح ملف PDF.
1. أضف النص إلى مستند PDF باستخدام [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) دالة.
1. يحفظ التعديلات في نفس الملف.

## إضافة نص

المقتطف البرمجي التالي يوضح لك كيفية إضافة نص في ملف PDF موجود.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

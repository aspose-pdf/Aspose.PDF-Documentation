---
title: إضافة علامة مائية إلى PDF باستخدام Rust
linktitle: إضافة علامة مائية
type: docs
weight: 80
url: /ar/rust-cpp/add-watermarks/
description: يوضح هذا المثال كيفية إضافة علامة مائية نصية قابلة للتخصيص إلى مستند PDF باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة علامة مائية نصية
Abstract: Aspose.PDF for Rust عبر C++ يوفّر طريقة مرنة لإضافة علامات مائية نصية إلى مستندات PDF. يوضح هذا المثال كيفية إدراج علامة مائية قابلة للتخصيص عن طريق تحديد محتوى النص، Font، الحجم، اللون، الموقع، زاوية الدوران، سلوك الطبقة، والشفافية. تُستخدم العلامات المائية غالبًا للعلامة التجارية، تسميات السرية، علامات المسودة، أو حماية المستند.
SoftwareApplication: rust-cpp
---

ال [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) تتيح الطريقة للمطورين تطبيق علامة مائية نصية برمجياً على مستند PDF موجود. يمكن تخصيص العلامة المائية بالكامل، بما في ذلك:

- نص العلامة المائية
- عائلة الخط
- حجم الخط
- لون النص (بتنسيق HEX)
- إحداثيات الموضع X و Y
- زاوية الدوران
- وضعية أمامية أو خلفية
- العتامة (مستوى الشفافية)

في هذا المثال، يفتح التطبيق ملف PDF موجودًا، يطبق علامة مائية مائلة نصف شفافة، ويحفظ المستند المعدل تحت اسم ملف جديد.

هذه الميزة مفيدة بشكل خاص لتعليم المستندات كمسودة أو سرية أو نموذجية، أو لإضافة عناصر العلامة التجارية قبل التوزيع.

1. افتح مستند PDF الموجود.
1. استدعِ طريقة add_watermark وقم بتكوين خصائص العلامة المائية.
1. احفظ المستند المحدث.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```
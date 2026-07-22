---
title: تدوير صفحات PDF باستخدام Rust عبر C++
linktitle: تدوير صفحات PDF
type: docs
weight: 50
url: /ar/rust-cpp/rotate-pages/
description: يتناول هذا الموضوع كيفية تدوير توجيه الصفحة في ملف PDF موجود برمجياً باستخدام Rust عبر C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تدوير صفحات PDF باستخدام Aspose.PDF for Rust
Abstract: توفر Aspose.PDF for Rust عبر C++ وظائف قوية لتدوير الصفحات في مستندات PDF، مما يسمح للمطورين بتعديل توجيه الصفحة حسب الحاجة. تدعم المكتبة تدوير الصفحات بزاوية 90 أو 180 أو 270 درجة، مما يتيح تعديلًا سريعًا وفعالًا لتخطيط المستند. هذه الميزة مفيدة لتصحيح الصفحات غير الموجهة بشكل صحيح أو لتغيير عرض المستند. تشمل الوثائق إرشادات خطوة بخطوة وعينات شفرة لمساعدة المطورين على دمج قدرات تدوير الصفحات بسلاسة في تطبيقاتهم.
SoftwareApplication: rust-cpp
---

يصف هذا القسم كيفية تغيير توجيه الصفحة من وضعية أفقية إلى عمودية والعكس في ملف PDF موجود باستخدام Rust.

تدوير الصفحات يضمن محاذاة صحيحة للطباعة أو عرض ملفات PDF في البيئات المهنية

1. افتح مستند PDF.
1. تدوير صفحات PDF. الـ [تدوير](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) تطبق الدالة دورانًا محددًا (في هذه الحالة، 180 درجة) على صفحة معينة.
1. احفظ التغييرات إلى ملف جديد. الـ [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) تنشئ الدالة ملف PDF جديد للحفاظ على الأصلي مع تخزين النسخة المحدثة.

في هذا المثال، تقوم بتدوير صفحة محددة في مستند PDF:

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```
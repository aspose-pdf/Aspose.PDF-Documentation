---
title: إضافة رقم الصفحة إلى PDF باستخدام Rust
linktitle: إضافة رقم الصفحة
type: docs
weight: 10
url: /ar/rust-cpp/add-page-number/
description: توضح هذه المقالة كيفية إضافة أرقام الصفحات إلى مستند PDF موجود باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أرقام الصفحات
Abstract: Aspose.PDF for Rust عبر C++ يتيح للمطورين تحسين مستندات PDF الموجودة باستخدام ترقيم الصفحات التلقائي في بضع أسطر من الشيفرة فقط. يوضح هذا المثال كيفية فتح ملف PDF، وإدراج أرقام الصفحات عبر جميع الصفحات، وحفظ المستند المحدّث كملف جديد. يضمن أتمتة الترميز الصفحي بنية مستندية متسقة ويكون مفيدًا بشكل خاص للتقارير والعقود والكتيبات وغيرها من المخرجات متعددة الصفحات التي تُعد للتوزيع أو الطباعة.
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust عبر C++ يوفر وظائف مدمجة لتعديل مستندات PDF برمجيًا. في هذا المثال، يفتح التطبيق ملف PDF موجود، ويطبق ترقيم الصفحات التلقائي على كل صفحة، ويحفظ المستند المعدل باسم جديد.

هذا النهج مفيد عند إنشاء مستندات نهائية للتوزيع أو الطباعة أو الأرشفة. العملية تتطلب فقط بضع أسطر من الشيفرة ولا تُغيّر الملف الأصلي إلا إذا تم استبداله صراحةً.

ترقيم الصفحات هو مطلب شائع للتقارير والفواتير والعقود والكتيبات وغيرها من المستندات متعددة الصفحات. الـ [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) الطريقة تُدرج أرقام الصفحات تلقائيًا في جميع صفحات المستند، مما يضمن ترقيمًا ثابتًا عبر الملف.

بعد إضافة أرقام الصفحات، يتم حفظ المستند المحدث كملف PDF جديد.

1. افتح مستند PDF الموجود.
1. إضافة أرقام الصفحات باستخدام [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) طريقة.
1. احفظ المستند المحدث.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```
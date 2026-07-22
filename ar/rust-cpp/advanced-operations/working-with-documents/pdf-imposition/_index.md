---
title: ترتيب صفحات PDF باستخدام Aspose.PDF for Rust عبر C\u002B\u002B
linktitle: ترتيب صفحات PDF
type: docs
weight: 30
url: /ar/rust-cpp/pdf-imposition/
description: تشرح هذه المقالة كيفية إعادة ترتيب صفحات PDF لتصاميم مخصصة للطباعة باستخدام Aspose.PDF for Rust عبر C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إنشاء كتاب مطوي أو N-Up لملفات PDF
Abstract: Aspose.PDF for Rust عبر C\u002B\u002B يقدم أدوات قوية لإعادة هيكلة مستندات PDF لتلبية متطلبات الطباعة وتخطيط الصفحات. تُظهر هذه المقالة كيفية تحويل PDF عادي إلى كتاب مطوي، مع ضمان ترتيب الصفحات الصحيح للطي، وكيفية إنشاء PDF بنظام N-Up يجمع عدة صفحات في ورقة واحدة. باستخدام أمثلة شفرة Rust مختصرة، يمكن للمطورين تنفيذ تحويلات PDF جاهزة للطباعة بسرعة للتوثيق والنشر وسير العمل الأرشيفية.
SoftwareApplication: rust-cpp
---

## إنشاء N-Up من PDF

يضع ملف PDF بنمط N‑Up صفحات متعددة من المصدر على صفحة إخراج واحدة. في هذا المثال، تم استخدام تخطيط 2 × 2، لذا يتم دمج أربع صفحات أصلية في كل صفحة من وثيقة الإخراج.

1. افتح مستند PDF المصدر.
1. احفظ المستند باستخدام تخطيط N‑Up بعدد الصفوف والأعمدة المحدد.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## إنشاء كتيب من PDF

يوضح Aspose.PDF for Rust via C++ كيفية تحويل مستند PDF قياسي إلى PDF بنمط كتيب.
يعيد تنسيق الكتيب ترتيب الصفحات بحيث، عند طباعتها وطيها، يتشكل المستند ككتيب صحيح مع الصفحات بالترتيب المناسب.

1. افتح مستند PDF المصدر.
1. احفظ المستند كملف PDF كتيب.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**يرجى ملاحظة أن ترخيص تجربة مجانية مطلوب للحصول على الوظائف الكاملة.**

استكشف نتيجة إنشاء كتيب من 4 صفحات.

![مثال على كتيب من 4 صفحات](sample_4.png)

استكشف نتيجة إنشاء كتيب من 3 صفحات.

![مثال على كتيب من 3 صفحات](sample_3.png)
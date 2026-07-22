---
title: استخراج البيانات من AcroForm باستخدام Rust
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF يسهل استخراج بيانات حقول النموذج من ملفات PDF. تعلم كيفية استخراج البيانات من AcroForms وحفظها بتنسيق XML أو FDF أو XFDF.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من AcroForm عبر Rust
Abstract: تشرح هذه المقالة كيفية استخراج بيانات AcroForm من ملفات PDF باستخدام Aspose.PDF for Rust عبر C++ وتصديرها إلى صيغ تبادل البيانات واسعة الاستخدام - XML، FDF، وXFDF. توضح كيفية فتح مستند PDF يحتوي على حقول نموذج تفاعلية وتصدير أسماء الحقول وقيمها برمجياً لإعادة استخدامها خارج ملف PDF الأصلي. من خلال توفير أمثلة عملية بلغة Rust لكل صيغة تصدير، تسلط المقالة الضوء على سير عمل شائع، بما في ذلك معالجة البيانات، تقديم النماذج، تكامل الأنظمة، وتخزين البيانات على المدى الطويل، مما يساعد المطورين على إدارة وإعادة استخدام بيانات نماذج PDF بفعالية في تطبيقاتهم.
---

## تصدير البيانات إلى XML من ملف PDF

تظهر هذه القطعة من الشفرة كيفية تصدير بيانات AcroForm من مستند PDF إلى ملف XML باستخدام Aspose.PDF for Rust.
تنطوي العملية على فتح ملف PDF موجود يحتوي على حقول نموذج، ثم تصدير تلك الحقول وقيمها إلى مستند XML لمعالجة إضافية أو تخزين أو تبادل البيانات.

1. افتح مستند PDF.
1. استدعِ الدالة 'export_xml' لاستخراج بيانات حقول النموذج وحفظها كملف XML.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## تصدير البيانات إلى FDF من ملف PDF

Aspose.PDF for Rust via C++ يتيح لك تصدير بيانات AcroForm من مستند PDF إلى ملف FDF. ملف تنسيق بيانات النماذج (FDF) يخزن أسماء الحقول وقيمها بشكل منفصل عن PDF، مما يجعله مفيدًا لتبادل البيانات، وسير عمل تقديم النماذج، وأرشفة بيانات النموذج دون تضمينها في المستند الأصلي.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## تصدير البيانات إلى XFDF من ملف PDF

XFDF (XML Forms Data Format) هو تنسيق قائم على XML يمثل بيانات حقول النماذج بشكل منفصل عن ملف PDF، مما يجعله مثالياً لتبادل البيانات، وإرسال النماذج، والتكامل مع سير العمل القائم على الويب.
Aspose.PDF for Rust عبر C++ يساعد على تصدير بيانات AcroForm من مستند PDF إلى ملف XFDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```

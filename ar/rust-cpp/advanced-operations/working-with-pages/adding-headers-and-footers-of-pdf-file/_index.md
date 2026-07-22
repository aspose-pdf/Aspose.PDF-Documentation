---
title: إضافة رأس وتذييل إلى PDF باستخدام Rust
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 90
url: /ar/rust-cpp/add-headers-and-footers-of-pdf-file/
description: تعلم كيفية إضافة رؤوس وتذييلات إلى ملف PDF باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة رأس وتذييل إلى PDF باستخدام Rust
Abstract: يُظهر هذا المقال كيفية إضافة رؤوس وتذييلات نصية إلى مستندات PDF باستخدام مكتبة asposepdf لRust. يشرح كيفية فتح ملف PDF موجود، وإدراج نص ثابت في الرأس أو التذييل لكل صفحة، وحفظ المستند المعدل كملف جديد. تُظهر الأمثلة سير عمل بسيط وآمن من الأخطاء يمكن استخدامه لمهام مثل إضافة أرقام الصفحات، والعناوين، أو العلامة التجارية برمجياً في تطبيقات Rust.
SoftwareApplication: rust-cpp
---

## إضافة رؤوس وتذييلات كمقاطع نصية

### إضافة نص في تذييل مستند PDF-document

تتيح لك أداتنا فتح ملف PDF موجود، وإضافة تذييل نصي إلى جميع الصفحات، وحفظ ملف PDF المعدل كملف جديد باستخدام مكتبة asposepdf Rust. تتعامل مع الأخطاء بشكل سلس باستخدام نوع Result في Rust.

1. افتح مستند PDF موجود.
1. أضف نصًا إلى التذييل باستخدام [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. احفظ ملف PDF المعدل.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### أضف نصًا في رأس مستند PDF

يُظهر هذا المقتطف من الشفرة كيفية فتح ملف PDF موجود، إضافة رأس نص إلى جميع الصفحات، وحفظ المستند المعدل كملف جديد باستخدام مكتبة asposepdf. وهو يوفر طريقة بسيطة ومؤتمتة لإدراج رؤوس متسقة في ملفات PDF.

1. افتح ملف PDF موجود.
1. إضافة نص إلى الرأس مع المساعدة [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. احفظ ملف PDF المعدل.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```
---
title: حذف صفحات PDF باستخدام Rust عبر C++
linktitle: حذف صفحات PDF
type: docs
weight: 30
url: /ar/rust-cpp/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف صفحات PDF باستخدام Aspose.PDF for Rust
Abstract: تقدم Aspose.PDF for Rust عبر C++ وظائف فعّالة لحذف الصفحات من مستندات PDF، مما يتيح للمطورين إزالة الصفحات غير المرغوبة أو غير الضرورية بسهولة. تسمح المكتبة بحذف صفحة واحدة أو عدة صفحات عن طريق تحديد أرقام الصفحات أو النطاقات، مما يضمن تعديلًا دقيقًا للمستند. تساعد هذه الميزة في تحسين ملفات PDF عن طريق إلغاء المحتوى الزائد وتحسين هيكل المستند. توفر الوثائق إرشادات خطوة بخطوة وعينات شيفرة لمساعدة المطورين على تنفيذ وظيفة حذف الصفحات بفعالية ضمن تطبيقاتهم.
SoftwareApplication: rust-cpp
---

يمكنك حذف الصفحات من ملف PDF باستخدام **Aspose.PDF for Rust عبر C++**. تُظهر مقطع الشيفرة التالي كيفية تعديل مستند PDF بحذف صفحة معينة. هذه الطريقة فعّالة لمهام تعديل مستندات PDF، خاصةً لإزالة الصفحات، وحفظ المستند المعدل، وضمان إدارة الموارد بشكل صحيح.

1. فتح ملف PDF.
1. حذف صفحة محددة باستخدام [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) دالة.
1. حفظ المستند باستخدام [حفظ](https://reference.aspose.com/pdf/rust-cpp/core/save/) طريقة.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

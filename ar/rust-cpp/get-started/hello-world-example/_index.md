---
title: مثال Hello World باستخدام لغة Rust
linktitle: مثال Hello World
type: docs
weight: 40
url: /ar/rust-cpp/hello-world-example/
description: يوضح هذا المثال كيفية إنشاء مستند PDF بسيط يحتوي على نص Hello World باستخدام Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World عبر Aspose.PDF for Rust
Abstract: دليل البدء السريع لـ Aspose.PDF for Rust عبر C++ يوفر مقدمة للعمل مع المكتبة، ويغطي الخطوات الأساسية لإنشاء ومعالجة مستندات PDF. ويتضمن مثال 'Hello World' يوضح كيفية إنشاء ملف PDF بسيط يحتوي على محتوى نصي، مما يساعد المطورين على فهم الوظائف الأساسية للواجهة البرمجية بسرعة.
SoftwareApplication: rust-cpp
---

يُستخدم مثال "Hello World" تقليديًا لتقديم ميزات لغة برمجة أو برنامج من خلال حالة استخدام بسيطة.

**Aspose.PDF for Rust** هو واجهة برمجة تطبيقات PDF غنية بالميزات تسمح للمطورين بدمج إنشاء وثائق PDF، ومعالجتها، وقدرات التحويل باستخدام Rust. يدعم العديد من صيغ الملفات الشائعة، بما في ذلك PDF، TXT، XLSX، EPUB، TEX، DOC، DOCX، PPTX، صيغ الصور وغيرها. في هذه المقالة، نقوم بإنشاء مستند PDF يحتوي على النص "Hello World!" بعد تثبيت Aspose.PDF for Rust في بيئتك، يمكنك تشغيل عينة الشيفرة لرؤية كيفية عمل واجهة Aspose.PDF API.
المقتطف البرمجي أدناه يتبع الخطوات التالية:

1. إنشاء مثيل جديد لوثيقة PDF.
1. إضافة صفحة جديدة إلى وثيقة PDF باستخدام [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) دالة.
1. ضبط حجم الصفحة باستخدام [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. إضافة النص "Hello World!" إلى الصفحة الأولى باستخدام [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. حفظ مستند PDF باستخدام [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) طريقة.

المقتطف التالي من الشيفرة هو برنامج Hello World لعرض عمل Aspose.PDF لـ Rust API.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```

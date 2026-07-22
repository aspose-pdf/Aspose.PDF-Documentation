---
title: استخراج النص من PDF باستخدام Rust
linktitle: استخراج النص من PDF
type: docs
weight: 30
url: /ar/rust-cpp/extract-text-from-pdf/
description: تصفّ هذه المقالة طرقًا متعددة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج النص باستخدام Aspose.PDF for Rust
Abstract: يوفر Aspose.PDF for Rust عبر C++ طريقة قوية وفعّالة لاستخراج النص من مستندات PDF. تدعم المكتبة تقنيات استخراج متعددة، مما يتيح للمستخدمين استرجاع النص من المستندات بالكامل، أو من صفحات محددة، أو من مناطق محددة مسبقًا داخل PDF.
SoftwareApplication: rust-cpp
---

## استخراج النص من مستند PDF

استخراج النص من مستند PDF هو مهمة شائعة ومفيدة جداً. غالبًا ما تحتوي ملفات PDF على معلومات حيوية تحتاج إلى الوصول إليها، أو تحليلها، أو معالجتها لأغراض مختلفة. يتيح استخراج النص إعادة استخدام أسهل في قواعد البيانات، أو التقارير، أو مستندات أخرى.

يعمل استخراج النص على جعل محتوى PDF قابلاً للبحث، مما يسمح للمستخدمين بتحديد المعلومات المحددة بسرعة دون الحاجة إلى مراجعة المستند بأكمله يدويًا.

في حال رغبتك في استخراج النص من مستند PDF، يمكنك استخدام [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) دالة.
يرجى مراجعة مقتطف الشيفرة التالي لاستخراج النص من ملف PDF باستخدام Rust.

1. افتح مستند PDF باستخدام اسم الملف المعطى.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) يستخلص محتوى النص من مستند PDF.
1. اطبع النص المستخرج إلى وحدة التحكم.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```
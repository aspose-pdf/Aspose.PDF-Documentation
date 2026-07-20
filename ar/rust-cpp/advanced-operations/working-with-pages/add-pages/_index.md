---
title: إضافة صفحات إلى مستند PDF
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/rust-cpp/add-pages/
description: استكشف كيفية إضافة صفحات إلى ملف PDF موجود في Rust باستخدام Aspose.PDF لتعزيز وتوسيع مستنداتك.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة صفحات PDF باستخدام Aspose.PDF for Rust
Abstract: يوفر Aspose.PDF for Rust عبر C++ وظائف قوية لإضافة صفحات إلى مستندات PDF، مما يسمح للمطورين بإنشاء صفحات جديدة بصورة ديناميكية وتخصيصها وفقًا لمتطلبات محددة. تدعم المكتبة إدراج صفحات فارغة أو نسخ صفحات من مستندات موجودة مع توفير خيارات لتحديد حجم الصفحة واتجاهها ومحتواها. تمكّن هذه القدرات من توسيع وتخصيص المستندات بسلاسة. تتضمن الوثائق تعليمات مفصلة وعينات شفرة لمساعدة المطورين على تنفيذ ميزات إضافة الصفحات في تطبيقاتهم بكفاءة.
SoftwareApplication: rust-cpp
---

## إضافة صفحة في ملف PDF

يوضح مقطع كود Rust المقدم كيفية تنفيذ عملية إضافة صفحة في نهاية ملف PDF باستخدام مكتبة Aspose.PDF.

1. ال [فتح](https://reference.aspose.com/pdf/rust-cpp/core/open/) تسمح الدالة للبرنامج بتحميل ملف PDF موجود (sample.pdf) للتعامل معه. هذا ضروري لأي عمليات متعلقة بـ PDF، مثل التحرير، إضافة محتوى، أو قراءة البيانات.
1. ال [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) الطريقة تُستخدم لإدراج صفحة فارغة جديدة في مستند PDF الحالي. هذا مفيد لتوسيع المستند أو إعداده لمحتوى إضافي.
1. ال [حفظ](https://reference.aspose.com/pdf/rust-cpp/core/save/) تضمن الطريقة أن التعديلات على ملف PDF تُكتب مرة أخرى إلى الملف. هذه الخطوة ضرورية للحفاظ على التغييرات، مثل إضافة صفحات جديدة.

هذه المقتطفة مثال مختصر وفعال لكيفية استخدام مكتبة Aspose.PDF Rust للقيام بمهام أساسية في معالجة ملفات PDF.

تتيح لك Aspose.PDF for Rust إدراج صفحة في مستند PDF في أي موقع داخل الملف بالإضافة إلى إضافة صفحات إلى نهاية ملف PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## إدراج صفحة في ملف PDF

ال [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) تقوم الطريقة بإدراج صفحة جديدة في الموضع المحدد. هذه الميزة مفيدة عندما تحتاج إلى إدراج صفحات إضافية في مستند موجود، على سبيل المثال، إضافة قسم جديد أو محتوى إلى تقرير أو عرض تقديمي.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
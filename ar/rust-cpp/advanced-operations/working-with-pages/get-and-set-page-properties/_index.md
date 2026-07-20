---
title: الحصول على وتعيين خصائص الصفحة
linktitle: الحصول على وتعيين خصائص الصفحة
type: docs
url: /ar/rust-cpp/get-and-set-page-properties/
description: تعلم كيفية الحصول على وتعيين خصائص الصفحات لمستندات PDF باستخدام Aspose.PDF for Rust، مما يسمح بتنسيق مستند مخصص.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: الحصول على وتعيين خصائص الصفحة باستخدام Aspose.PDF for Rust
Abstract: توفر Aspose.PDF for Rust عبر C++ ميزات شاملة للحصول على وتعيين خصائص الصفحات في مستندات PDF، مما يسمح للمطورين بالوصول إلى وتعديل مختلف سمات الصفحة مثل الحجم، والدوران، والهوامش، والبيانات التعريفية. تمكّن هذه القدرات من التحكم الدقيق في تخطيط ومظهر المستند لتلبية متطلبات التطبيقات المحددة. يضمن المكتبة تخصيصًا سلسًا وتحسينًا لصفحات PDF. تقدم الوثائق إرشادات مفصلة وعينات شفرة لمساعدة المطورين على استرجاع وتحديث خصائص الصفحة بفعالية داخل تطبيقاتهم.
SoftwareApplication: rust-cpp
---


يتيح لك Aspose.PDF for Rust قراءة وتعيين خصائص الصفحات في ملف PDF. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون، وتعيين خصائص الصفحة.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما تريد معرفة عدد الصفحات التي تحتويها. باستخدام Aspose.PDF لا يستغرق ذلك أكثر من سطرين من الشيفرة.

**Aspose.PDF for Rust via C\u002B\u002B** يسمح لك بعدّ الصفحات باستخدام [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) دالة.

المقتطف البرمجي التالي مصمم لفتح مستند PDF، واستخراج عدد صفحاته، ثم طباعة النتيجة.

ال [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) يتم استدعاء الطريقة للحصول على إجمالي عدد الصفحات في مستند PDF. هذا مفيد للمهام التي تحتاج إلى معرفة طول المستند، مثل استخراج صفحات معينة أو تنفيذ عمليات عبر جميع الصفحات. هذه الطريقة تُعد وسيلة مباشرة للاستعلام عن بنية المستند.

للحصول على عدد الصفحات في ملف PDF:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## تعيين حجم الصفحة

في هذا المثال، تُغيّر الطريقة pdf.PageSetSize() حجم الصفحة الأولى من مستند PDF. يضمن الثابت PageSizeA1 أن تُضبط الصفحة الأولى على حجم الورق A1. هذا مفيد عند تحويل المستندات إلى تنسيق موحد أو لضمان أن المحتوى المحدد يتناسب بشكل صحيح مع الصفحات.

1. فتح مستند PDF باستخدام [فتح](https://reference.aspose.com/pdf/rust-cpp/core/open/) طريقة.
1. تعيين حجم الصفحة باستخدام [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) دالة.
1. حفظ المستند باستخدام [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) طريقة.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```
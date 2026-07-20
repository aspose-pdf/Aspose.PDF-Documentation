---
title: قم بتعيين لون الخلفية لملف PDF باستخدام Rust عبر C++
linktitle: تعيين لون الخلفية
type: docs
weight: 80
url: /ar/rust-cpp/set-background-color/
description: قم بتعيين لون الخلفية لملف PDF الخاص بك باستخدام Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتعيين لون الخلفية لملف PDF باستخدام Aspose.PDF for Rust
Abstract: يقدم Aspose.PDF for Rust عبر C++ وظيفة لتعيين لون خلفية صفحات PDF، مما يسمح للمطورين بتخصيص مظهر المستندات. تتيح هذه الميزة تطبيق ألوان صلبة على خلفية الصفحة بأكملها، مما يحسن العرض البصري للمستند. يمكن للمطورين بسهولة تحديد قيم الألوان باستخدام نماذج ألوان قياسية مثل RGB أو CMYK. توفر الوثائق تعليمات مفصلة وعينات شيفرة لمساعدة المطورين على تنفيذ تخصيص لون الخلفية بفعالية داخل تطبيقاتهم المكتوبة بـ C++.
SoftwareApplication: rust-cpp
---

1. يوضح المقتطف البرمجي المقدم كيفية تعيين لون خلفية لملف PDF باستخدام مكتبة Aspose.PDF في Rust.
1. ال [فتح](https://reference.aspose.com/pdf/rust-cpp/core/open/) تقوم الطريقة بتحميل ملف PDF المحدد إلى الذاكرة، مما يتيح المزيد من التعديلات، مثل تعديل مظهره أو محتواه.
1. ال [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) تقوم الطريقة بتطبيق لون خلفية جديد على مستند PDF. تتيح قيم RGB للمستخدمين تخصيص النمط البصري للمستند.
1. ال [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) يقوم الأسلوب بحفظ ملف PDF المحدث تحت اسم جديد.

هذا الكود مثالي للتطبيقات التي تحتاج إلى أتمتة تخصيصات PDF، مثل إنشاء تقارير ذات علامة تجارية، وإضافة علامات مائية، أو تحسين التناسق البصري عبر مستندات متعددة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```
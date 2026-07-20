---
title: تحسين موارد PDF باستخدام Rust عبر C++
linktitle: تحسين موارد PDF
type: docs
weight: 15
url: /ar/rust-cpp/optimize-pdf-resources/
description: تحسين موارد ملفات PDF باستخدام أداة Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحسين موارد PDF باستخدام Aspose.PDF لـ Rust
Abstract: يوفر Aspose.PDF for Rust عبر C++ قدرات متقدمة لتحسين موارد PDF، مما يعزز كفاءة المستند ويقلل حجم الملف. تسمح المكتبة للمطورين بتحسين الخطوط والصور والبيانات الوصفية عن طريق إزالة البيانات الزائدة وضغط الموارد دون الإضرار بجودة المستند. تُحسّن هذه التقنيات من أداء المستند، مما يجعل ملفات PDF أكثر ملاءمةً للمشاركة والتخزين. توفر الوثائق إرشادات مفصلة وأمثلة على الشيفرة لمساعدة المطورين على تنفيذ تحسين الموارد بفعالية في تطبيقاتهم.
SoftwareApplication: rust-cpp
---

## تحسين موارد PDF

تحسين الموارد في المستند:

  1. يتم إزالة الموارد التي لا تُستخدم في صفحات المستند.
  1. يتم دمج الموارد المتساوية في كائن واحد.
  1. يتم حذف الكائنات غير المستخدمة.

قد تشمل التحسينات ضغط الصور، وإزالة الكائنات غير المستخدمة، وتحسين الخطوط لتقليل حجم الملف وتحسين الأداء. يتم تسجيل أي خطأ يحدث خلال هذه العملية وينتهي البرنامج.  
 
1. ال [فتح](https://reference.aspose.com/pdf/rust-cpp/core/open/) تقوم الطريقة بتحميل ملف PDF المحدد (sample.pdf) إلى الذاكرة.
1. يقوم بتحسين الموارد داخل ملف PDF لتحسين الكفاءة باستخدام [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) طريقة.
1. ال [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) تقوم الطريقة بحفظ ملف PDF المحسن إلى ملف جديد.

يعرض مقتطف الشيفرة التالي كيفية تحسين مستند PDF.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_open.pdf")?;

      Ok(())
  }
```
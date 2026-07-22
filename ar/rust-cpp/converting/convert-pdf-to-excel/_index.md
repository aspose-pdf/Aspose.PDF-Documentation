---
title: تحويل PDF إلى Excel في Rust
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/rust-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-20"
description: يتيح لك Aspose.PDF for Rust تحويل PDF إلى تنسيق XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أداة Rust لتحويل مستندات PDF إلى Excel
Abstract: توفر مكتبة Aspose.PDF for Rust عبر C++ حلاً قويًا لتحويل مستندات PDF إلى تنسيق XLSX بدقة عالية وكفاءة ممتازة. تمكّن هذه الميزة المطورين من استخراج البيانات الجدولية من ملفات PDF مع الحفاظ على التخطيط الأصلي لجداول Excel، والبنية، والتنسيق. تقدم الوثائق إرشادات مفصلة حول تنفيذ عملية التحويل، بما في ذلك عينة كود وتعليمات خطوة بخطوة لتسهيل التكامل السلس في تطبيقات Rust.
SoftwareApplication: rust-cpp
---

**Aspose.PDF for Rust** يدعم ميزة تحويل ملفات PDF إلى تنسيق Excel.

## تحويل PDF إلى XLSX

يوفر Excel أدوات متقدمة للفرز والتصفية وتحليل البيانات، مما يجعل من السهل تنفيذ مهام مثل تحليل الاتجاهات أو النمذجة المالية، والتي تكون صعبة مع ملفات PDF الثابتة. النسخ اليدوي للبيانات من PDFs إلى Excel يستغرق وقتًا طويلاً وعرضة للأخطاء. يَقوم التحويل بأتمتة هذه العملية، موفرًا وقتًا كبيرًا لمجموعات البيانات الكبيرة.

يستخدم Aspose.PDF for Rust [save_xlsx](https://reference.aspose.com/pdf/rust-cpp/convert/save_xlsx/) لتحويل ملف PDF الذي تم تنزيله إلى جدول بيانات Excel وحفظه.

1. استيراد الحزم المطلوبة.
1. افتح ملف PDF.
1. حوّل ملف PDF إلى XLSX باستخدام [save_xlsx](https://reference.aspose.com/pdf/rust-cpp/convert/save_xlsx/).

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as XlsX-document
      pdf.save_xlsx("sample.xlsx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**جرّب تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF for Rust يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Excel مع تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}
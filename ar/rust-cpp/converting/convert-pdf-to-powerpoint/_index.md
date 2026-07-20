---
title: تحويل PDF إلى PPTX في Rust
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: يتيح لك Aspose.PDF تحويل PDF إلى تنسيق PPTX باستخدام Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أداة Rust لتحويل PDF إلى PowerPoint
Abstract: يقدم Aspose.PDF لـ Rust عبر C++ حلًا موثوقًا لتحويل مستندات PDF إلى تنسيق PowerPoint (PPTX) مع الحفاظ على التخطيط الأصلي، والتنسيق، وبنية المحتوى. تتيح هذه الوظيفة للمطورين تحويل ملفات PDF الثابتة بسهولة إلى عروض تقديمية ديناميكية قابلة للتحرير. توفر المكتبة خيارات تخصيص للتحكم في عملية التحويل، مما يضمن مخرجات عالية الجودة مناسبة للاستخدام التجاري والمهني. تُوفر الوثائق إرشادات خطوة بخطوة وعينات شفرة لمساعدة المطورين على دمج تحويل PDF إلى PowerPoint بفعالية في تطبيقاتهم.
SoftwareApplication: rust-cpp
---

## تحويل PDF إلى PPTX

يُظهر مقتطف كود Rust المقدم كيفية تحويل مستند PDF إلى PPTX باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. حوِّل ملف PDF إلى PPTX باستخدام [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) دالة.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

تقدم لك Aspose.PDF للـ Rust تطبيقًا مجانيًا عبر الإنترنت [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PPTX باستخدام تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
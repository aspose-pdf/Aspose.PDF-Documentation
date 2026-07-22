---
title: تحويل PDF إلى مستندات Word في Rust
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/rust-cpp/convert-pdf-to-doc/
lastmod: "2026-07-20"
description: تعرف على كيفية كتابة كود Rust لتحويل PDF إلى DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أداة لتحويل PDF إلى Word باستخدام Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ يمكّن التحويل السلس لمستندات PDF إلى تنسيق DOC مع الحفاظ على النص الأصلي، والصور، والجداول، وبنية المستند العامة. تسمح هذه الميزة للمطورين بتحويل ملفات PDF الثابتة إلى ملفات Word قابلة للتحرير لمزيد من التعديل والمعالجة. توفر المكتبة خيارات تخصيص متعددة للتحكم في ناتج التحويل، مما يضمن دقة عالية وموثوقية. يتضمن التوثيق إرشادات مفصلة وعينات كود لمساعدة المطورين على تنفيذ تحويل PDF إلى DOC بكفاءة في تطبيقاتهم.
SoftwareApplication: rust-cpp
---

لتحرير محتوى ملف PDF في Microsoft Word أو معالجات النص الأخرى التي تدعم تنسيقات DOC و DOCX. ملفات PDF قابلة للتحرير، ولكن ملفات DOC و DOCX أكثر مرونة وقابلة للتخصيص.

## تحويل PDF إلى DOC

المقتطف البرمجي بلغة Rust المقدم يوضح كيفية تحويل مستند PDF إلى DOC باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. حوّل ملف PDF إلى DOC باستخدام [save_doc](https://reference.aspose.com/pdf/rust-cpp/convert/save_doc/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Doc-document
      pdf.save_doc("sample.doc")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

Aspose.PDF for Rust يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك واجهة برمجة تطبيقات Aspose.PDF for Rust قراءة وتحويل مستندات PDF إلى DOCX. DOCX هو تنسيق معروف لمستندات Microsoft Word تم تغيير هيكله من ثنائي بسيط إلى مزيج من ملفات XML والملفات الثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات اللاحقة ولكن ليس مع الإصدارات الأقدم من MS Word التي تدعم امتدادات ملفات DOC.

يوضح مقتطف كود Rust المقدم كيفية تحويل مستند PDF إلى DOCX باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل ملف PDF إلى DOCX باستخدام [save_docx](https://reference.aspose.com/pdf/rust-cpp/convert/save_docx/) دالة.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document
      pdf.save_docx("sample.docx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

Aspose.PDF for Rust يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Word تطبيق مجاني](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## تحويل PDF إلى DOCX باستخدام وضع التعرف المحسن

تحويل مستند PDF إلى ملف Microsoft Word (DOCX) باستخدام Aspose.PDF for Rust مع وضع التعرف المحسن.

وضع التعرف المحسّن ينتج ملف DOCX قابل للتحرير بالكامل، مع الحفاظ على:

 - هيكل الفقرة
 - الجداول كجداول Word أصلية
 - تدفق النص المنطقي والتنسيق

1. افتح ملف PDF المصدر.
1. احفظ PDF كملف DOCX مع تمكين التعرف على التخطيط المحسن.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document with Enhanced Recognition Mode (fully editable tables and paragraphs)
      pdf.save_docx_enhanced("sample_enhanced.docx")?;

      Ok(())
  }
```

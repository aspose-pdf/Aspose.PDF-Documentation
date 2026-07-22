---
title: تحويل PDF إلى صيغ الصور في Rust
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: يعرض هذا الموضوع كيفية استخدام Aspose.PDF for Rust لتحويل PDF إلى صيغ صور مختلفة مثل TIFF و BMP و JPEG و PNG و SVG باستخدام بضع أسطر من الشيفرة.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: أداة لتحويل PDF إلى صيغ الصور باستخدام Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ يتيح تحويل سلس لوثائق PDF إلى صيغ صور مختلفة، بما في ذلك JPEG و PNG و BMP و TIFF. يتيح هذا الميزة للمطورين إنشاء صور عالية الجودة مع الحفاظ على محتوى المستند الأصلي وتنسيقه ودقته. توفر المكتبة خيارات مرنة لإعدادات الإخراج مثل الدقة وجودة الصورة وعمق اللون. توفّر الوثائق إرشادات خطوة بخطوة وعينات كود لمساعدة المطورين على دمج تحويل PDF إلى صورة بفعالية في تطبيقاتهم.
SoftwareApplication: rust-cpp
---

## تحويل PDF إلى صورة

في هذه المقالة، سنعرض لك الخيارات لتحويل PDF إلى صيغ الصور.

عادةً ما يتم حفظ المستندات التي تم مسحها ضوئيًا مسبقًا بصيغة ملف PDF. ومع ذلك، هل تحتاج إلى تعديلها في محرر رسومي أو إرسالها لاحقًا بصيغة صورة؟ لدينا أداة شاملة لك لتحويل PDF إلى صور باستخدام **Aspose.PDF for Rust via C++**.
أكثر مهمة شائعة هي عندما تحتاج إلى حفظ مستند PDF كامل أو بعض الصفحات المحددة من مستند كمجموعة من الصور. **Aspose.PDF for Rust via C++** يتيح لك تحويل PDF إلى صيغ JPG و PNG لتبسيط الخطوات المطلوبة للحصول على الصور من ملف PDF محدد.

**Aspose.PDF for Rust via C++** يدعم التحويل إلى صيغ صور متعددة من PDF. يرجى التحقق من القسم [تنسيقات الملفات المدعومة في Aspose.PDF](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### تحويل PDF إلى JPEG

يعرض مقتطف كود Rust المقدم كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة JPEG باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى JPEG باستخدام [صفحة_إلى_JPG](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى JPEG عبر الإنترنت**

يقدم لك Aspose.PDF for Rust تطبيقًا مجانيًا على الإنترنت ["PDF إلى JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى JPEG باستخدام التطبيق المجاني](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### تحويل PDF إلى TIFF

المقتطف البرمجي بلغة Rust المقدم يوضح كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة TIFF باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى TIFF باستخدام [page_to_tiff](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

يقدم لك Aspose.PDF for Rust تطبيقًا مجانيًا على الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF باستخدام تطبيق مجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### تحويل PDF إلى PNG

يظهر مقطع الكود Rust المقدم كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة PNG باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى PNG باستخدام [صفحة_إلى_png](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

يقدم لك Aspose.PDF for Rust تطبيقًا مجانيًا على الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام تطبيق مجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** هي عائلة من المواصفات لملف قائم على XML لتقنيات الرسومات المتجهية ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح يتم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

### تحويل PDF إلى SVG

يوضح مقطع كود Rust المقدم كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة SVG باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى SVG باستخدام [صفحة_إلى_SVG](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

يقدم لك Aspose.PDF for Rust تطبيقًا مجانيًا على الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG باستخدام تطبيق مجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### تحويل PDF إلى أرشيف ZIP بصيغة SVG

المثال التالي يحول مستند PDF إلى أرشيف SVG، حيث يتم حفظ كل صفحة كملف SVG منفصل داخل حاوية ZIP.

1. افتح مستند PDF المصدر.
1. احفظ المستند كملف أرشيف ZIP يحتوي على ملفات SVG.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### تحويل PDF إلى DICOM

المقتطف البرمجي بلغة Rust المقدم يُظهر كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة DICOM باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى DICOM باستخدام [page_to_dicom](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### تحويل PDF إلى BMP

المقتطف البرمجي Rust المقدم يوضح كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة BMP باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى BMP باستخدام [page_to_bmp](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/) دالة.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```
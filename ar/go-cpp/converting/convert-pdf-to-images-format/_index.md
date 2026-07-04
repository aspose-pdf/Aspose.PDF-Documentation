---
title: تحويل PDF إلى صيغ الصورة في Go
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: يعرض هذا الموضوع كيفية استخدام Aspose.PDF for Go لتحويل PDF إلى صيغ صور مختلفة مثل TIFF, BMP, JPEG, PNG, SVG باستخدام بضع أسطر من الكود.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: أداة لتحويل PDF إلى صيغ صور باستخدام Aspose.PDF for Go
Abstract: يتيح Aspose.PDF for Go via C++ تحويلًا سلسًا لمستندات PDF إلى صيغ صور مختلفة، بما في ذلك JPEG و PNG و BMP و TIFF. تسمح هذه الميزة للمطورين بإنشاء صور عالية الجودة مع الحفاظ على محتوى المستند الأصلي وتخطيطه ودقته. توفر المكتبة خيارات مرنة لإعدادات الإخراج مثل الدقة وجودة الصورة وعمق اللون. توفر الوثائق تعليمات خطوة بخطوة وعينات شفرة لمساعدة المطورين على دمج تحويل PDF إلى صورة في تطبيقاتهم بكفاءة.
SoftwareApplication: go-cpp
---

## اذهب حول PDF إلى صورة

في هذه المقالة، سوف نعرض لك الخيارات لتحويل PDF إلى صيغ الصور.

عادةً ما يتم حفظ المستندات الممسوحة ضوئياً بتنسيق ملف PDF. ومع ذلك، هل تحتاج إلى تحريره في محرر رسومي أو إرساله لاحقًا بتنسيق صورة؟ لدينا أداة شاملة لك لتحويل PDF إلى صور باستخدام **Aspose.PDF for Go via C++**.
أكثر مهمة شائعة هي عندما تحتاج إلى حفظ مستند PDF كامل أو بعض الصفحات المحددة من مستند كمجموعة من الصور. **Aspose.PDF for Go via C++** يتيح لك تحويل PDF إلى صيغ JPG و PNG لتبسيط الخطوات المطلوبة للحصول على صورك من ملف PDF معين.

**Aspose.PDF for Go via C++** يدعم تحويل صيغ PDF إلى صور متنوعة. يرجى التحقق من القسم [تنسيقات الملفات المدعومة لـ Aspose.PDF](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## تحويل PDF إلى JPEG

مقتطف الشيفرة Go المقدم يوضح كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة JPEG باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى JPEG باستخدام [صفحة إلى JPG](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) دالة.
1. أغلق مستند PDF وحرّر أي موارد مخصصة.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى JPEG عبر الإنترنت**

تقدم لك Aspose.PDF for Go تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى JPEG باستخدام التطبيق المجاني](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## تحويل PDF إلى TIFF

المقتطف البرمجي المقدم بلغة Go يوضح كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة TIFF باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى TIFF باستخدام [صفحة إلى Tiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) دالة.
1. أغلق مستند PDF وحرّر أي موارد مخصصة.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

تقدم لك Aspose.PDF for Go تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF باستخدام تطبيق مجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## تحويل PDF إلى PNG

يظهر مقتطف الكود المقدم بلغة Go كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة PNG باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى PNG باستخدام [صفحة إلى PNG](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) دالة.
1. أغلق مستند PDF وحرّر أي موارد مخصصة.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى مراجعة الميزة التالية.

تقدم لك Aspose.PDF for Go تطبيقًا مجانيًا عبر الإنترنت [PDF إلى PNG](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام تطبيق مجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** هو عائلة من المواصفات لملف بصيغة XML يُستخدم للرسومات المتجهية ثنائية الأبعاد، سواءً الساكنة أو الديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح يتم تطويره من قبل لجنة الشبكة العالمية (W3C) منذ عام 1999.

## تحويل PDF إلى SVG

يوضح مقتطف الشيفرة Go المقدم كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة SVG باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى SVG باستخدام [صفحة إلى SVG](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) دالة.
1. أغلق مستند PDF وحرّر أي موارد مخصصة.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

تقدم لك Aspose.PDF for Go تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى SVG باستخدام تطبيق مجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## تحويل PDF إلى DICOM

المقتطف البرمجي المقدم بلغة Go يوضح كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة DICOM باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى DICOM باستخدام [صفحة إلى DICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) دالة.
1. أغلق مستند PDF وحرّر أي موارد مخصصة.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## تحويل PDF إلى BMP

توضح المقتطف البرمجي المقدم بلغة Go كيفية تحويل الصفحة الأولى من مستند PDF إلى صورة BMP باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. تحويل صفحة إلى BMP باستخدام [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) دالة.
1. أغلق مستند PDF وحرّر أي موارد مخصصة.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
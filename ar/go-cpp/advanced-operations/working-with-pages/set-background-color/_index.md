---
title: تعيين لون الخلفية لملف PDF باستخدام Go
linktitle: تعيين لون الخلفية
type: docs
weight: 80
url: /ar/go-cpp/set-background-color/
description: تعيين لون الخلفية لملف PDF الخاص بك باستخدام Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعيين لون الخلفية لملف PDF باستخدام Aspose.PDF for Go
Abstract: توفر Aspose.PDF for Go via C++ وظيفة ضبط لون خلفية صفحات PDF، مما يسمح للمطورين بتخصيص مظهر المستندات. تتيح هذه الميزة تطبيق ألوان صلبة على خلفية الصفحة بالكامل، مما يعزز العرض البصري للمستند. يمكن للمطورين تحديد قيم الألوان بسهولة باستخدام نماذج الألوان القياسية مثل RGB أو CMYK. توفر الوثائق تعليمات مفصلة وعينات كود لمساعدة المطورين على تنفيذ تخصيص لون الخلفية بفعالية داخل تطبيقاتهم المكتوبة بلغة C++.
SoftwareApplication: go-cpp
---

1. يوضح الجزء البرمجي المقدم كيفية تعيين لون الخلفية لملف PDF باستخدام مكتبة Aspose.PDF في Go.
1. ال [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) الطريقة تقوم بتحميل ملف PDF المحدد إلى الذاكرة، مما يسمح بمزيد من التلاعب، مثل تعديل مظهره أو محتواه.
1. ال [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) الطريقة تطبق لون خلفية جديد على مستند PDF. قيم RGB تسمح للمستخدمين بتخصيص النمط البصري للمستند.
1. ال [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) تحفظ الطريقة ملف الـ PDF المحدث تحت اسم جديد.

هذا الكود مثالي للتطبيقات التي تحتاج إلى أتمتة تخصيصات PDF، مثل إنشاء تقارير تحمل العلامة التجارية، إضافة علامات مائية، أو تحسين التناسق البصري عبر مستندات متعددة.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
---
title: تحويل PDF إلى PPTX في Go
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF يتيح لك تحويل PDF إلى صيغة PPTX باستخدام Go.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أداة Golang لتحويل PDF إلى PowerPoint
Abstract: Aspose.PDF for Go via C++ يوفر حلاً موثوقًا لتحويل مستندات PDF إلى صيغة PowerPoint (PPTX) مع الحفاظ على التخطيط الأصلي والتنسيق وبنية المحتوى. تمكّن هذه الوظيفة المطورين من تحويل ملفات PDF الثابتة بسلاسة إلى عروض تقديمية ديناميكية قابلة للتعديل. تقدم المكتبة خيارات تخصيص للتحكم في عملية التحويل، مما يضمن مخرجات عالية الجودة مناسبة للاستخدام التجاري والمهني. توفر الوثائق تعليمات خطوة بخطوة وعينات من الشيفرة لمساعدة المطورين على دمج تحويل PDF إلى PowerPoint بفعالية في تطبيقاتهم.
SoftwareApplication: go-cpp
---

## تحويل PDF إلى PPTX

يعرض مقتطف كود Go المقدم كيفية تحويل مستند PDF إلى PPTX باستخدام مكتبة Aspose.PDF:

1. افتح مستند PDF.
1. حوّل ملف PDF إلى PPTX باستخدام [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) دالة.
1. أغلق مستند PDF وأطلق أي موارد مخصصة.

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

تقدم لك Aspose.PDF for Go تطبيقًا مجانيًا عبر الإنترنت [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PPTX مع تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
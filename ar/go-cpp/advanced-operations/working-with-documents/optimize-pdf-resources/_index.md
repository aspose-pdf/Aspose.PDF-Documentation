---
title: تحسين موارد PDF باستخدام Go
linktitle: تحسين موارد PDF
type: docs
weight: 15
url: /ar/go-cpp/optimize-pdf-resources/
description: تحسين موارد ملفات PDF باستخدام أداة Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحسين موارد PDF باستخدام Aspose.PDF for Go
Abstract: توفر Aspose.PDF for Go via C++ إمكانيات متقدمة لتحسين موارد PDF، مما يعزز كفاءة المستند ويقلل من حجم الملف. تسمح المكتبة للمطورين بتحسين الخطوط والصور والبيانات الوصفية عن طريق إزالة البيانات الزائدة وضغط الموارد دون الإضرار بجودة المستند. هذه التقنيات التحسينية تحسن أداء المستند، مما يجعل ملفات PDF أكثر ملاءمة للمشاركة والتخزين. توفر الوثائق إرشادات مفصلة وعينات شفرة لمساعدة المطورين على تنفيذ تحسين الموارد بشكل فعال في تطبيقاتهم.
SoftwareApplication: go-cpp
---

## تحسين موارد PDF

تحسين الموارد في المستند:

1. يتم إزالة الموارد التي لا تُستخدم في صفحات المستند.
1. يتم دمج الموارد المتساوية في كائن واحد.
1. يتم حذف الكائنات غير المستخدمة.

قد تشمل التحسينات ضغط الصور، وإزالة الكائنات غير المستخدمة، وتحسين الخطوط لتقليل حجم الملف وتحسين الأداء. أي خطأ يحدث أثناء هذه العملية يتم تسجيله ويتسبب في إيقاف البرنامج.  

1. تقوم طريقة [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) بتحميل ملف PDF المحدد (sample.pdf) في الذاكرة.
1. يحسن الموارد داخل ملف PDF لزيادة الكفاءة باستخدام [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) طريقة.
1. تقوم طريقة [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) بحفظ ملف PDF المُحسَّن في ملف جديد.

يعرض المقتطف البرمجي التالي كيفية تحسين مستند PDF.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
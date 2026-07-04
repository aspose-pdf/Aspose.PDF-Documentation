---
title: تدوير صفحات PDF باستخدام Go
linktitle: تدوير صفحات PDF
type: docs
weight: 50
url: /ar/go-cpp/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجيًا باستخدام Go عبر C++
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تدوير صفحات PDF باستخدام Aspose.PDF for Go
Abstract: تقدم Aspose.PDF for Go عبر C++ وظائف قوية لتدوير الصفحات في مستندات PDF، مما يسمح للمطورين بتعديل اتجاه الصفحة حسب الحاجة. تدعم المكتبة تدوير الصفحات بمقدار 90 أو 180 أو 270 درجة، مما يتيح تعديلات سريعة وفعَّالة على تخطيط المستند. هذه الميزة مفيدة لتصحيح الصفحات ذات الاتجاه الخاطئ أو لتغيير عرض المستند. تشمل الوثائق تعليمات خطوة بخطوة وعينات كود لمساعدة المطورين على دمج قدرات تدوير الصفحات بسلاسة في تطبيقاتهم.
SoftwareApplication: go-cpp
---

يصف هذا القسم كيفية تغيير اتجاه الصفحة من وضعية أفقية إلى عمودية والعكس في ملف PDF موجود باستخدام Go.

تدوير الصفحات يضمن التوافق الصحيح للطباعة أو عرض ملفات PDF في البيئات المهنية

1. افتح مستند PDF.
1. تدوير صفحات PDF. الـ [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) تطبق الدالة دورانًا محددًا (في هذه الحالة، 180 درجة) على صفحة معينة.
1. احفظ التغييرات إلى ملف جديد. الـ [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) تقوم الدالة بإنشاء ملف PDF جديد للحفاظ على الأصلي مع تخزين النسخة المحدثة.

في هذا المثال، تقوم بتدوير صفحة محددة في مستند PDF:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

لديك أيضًا خيار تدوير جميع صفحات PDF في المستند الخاص بك:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```
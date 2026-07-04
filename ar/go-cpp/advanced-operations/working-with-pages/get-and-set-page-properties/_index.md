---
title: الحصول على وتعيين خصائص الصفحة
linktitle: الحصول على وتعيين خصائص الصفحة
type: docs
url: /ar/go-cpp/get-and-set-page-properties/
description: تعرف على كيفية الحصول على خصائص الصفحة وتعيينها لمستندات PDF باستخدام Aspose.PDF for Go، مما يتيح تنسيقًا مخصصًا للمستند.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: الحصول على وتعيين خصائص الصفحة باستخدام Aspose.PDF for Go
Abstract: توفر Aspose.PDF for Go عبر C\u002B\u002B ميزات شاملة للحصول على خصائص الصفحة وتعيينها في مستندات PDF، مما يتيح للمطورين الوصول إلى وتعديل سمات الصفحة المختلفة مثل الحجم، والدوران، والهوامش، والبيانات الوصفية. تتيح هذه القدرات التحكم الدقيق في تخطيط المستند ومظهره لتلبية متطلبات التطبيق المحددة. تضمن المكتبة تخصيصًا سلسًا وتحسينًا لصفحات PDF. يقدم التوثيق إرشادات مفصلة وعينات من الشيفرة لمساعدة المطورين على استرجاع وتحديث خصائص الصفحة بكفاءة داخل تطبيقاتهم.
SoftwareApplication: go-cpp
---


يتيح لك Aspose.PDF for Go قراءة وتعيين خصائص الصفحات في ملف PDF. يوضح هذا القسم كيفية الحصول على عدد الصفحات في ملف PDF، والحصول على معلومات حول خصائص صفحة PDF مثل اللون وتعيين خصائص الصفحة.

## الحصول على عدد الصفحات في ملف PDF

عند العمل مع المستندات، غالبًا ما تريد معرفة عدد الصفحات التي تحتويها. باستخدام Aspose.PDF لا يتطلب ذلك أكثر من سطرين من الشيفرة.

**Aspose.PDF for Go via C\u002B\u002B** يتيح لك عد الصفحات باستخدام [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) دالة.

المقتطف البرمجي التالي مصمم لفتح مستند PDF، استرجاع عدد صفحاته، ثم طباعة النتيجة.

ال [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) يتم استدعاء الطريقة للحصول على العدد الإجمالي للصفحات في مستند PDF. هذا مفيد للمهام التي تحتاج إلى معرفة طول المستند، مثل استخراج صفحات محددة أو إجراء عمليات عبر جميع الصفحات. هذه الطريقة طريقة مباشرة لاستعلام بنية المستند.

للحصول على عدد الصفحات في ملف PDF:

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)

      }
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## تعيين حجم الصفحة

في هذا المثال، تُغيّر الطريقة pdf.PageSetSize() حجم الصفحة الأولى من مستند PDF. يضمن الثابت PageSizeA1 أن يتم تعيين الصفحة الأولى إلى حجم ورق A1. وهذا مفيد عند تحويل المستندات إلى تنسيق موحد أو لضمان أن المحتوى المحدد يتناسب بشكل صحيح مع الصفحات.

1. فتح مستند PDF باستخدام [فتح](https://reference.aspose.com/pdf/go-cpp/core/open/) طريقة.
1. تعيين حجم الصفحة باستخدام [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) دالة.
1. حفظ المستند باستخدام [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) طريقة.

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
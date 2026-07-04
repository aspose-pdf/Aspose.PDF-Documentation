---
title: مثال Hello World باستخدام لغة Go
linktitle: مثال Hello World
type: docs
weight: 40
url: /ar/go-cpp/hello-world-example/
description: هذه العينة توضح كيفية إنشاء مستند PDF بسيط بنص Hello World باستخدام Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World عبر Aspose.PDF for Go
Abstract: دليل البدء السريع لـ Aspose.PDF for Go عبر C++ يقدم مقدمة للعمل مع المكتبة، ويغطي الخطوات الأساسية لإنشاء ومعالجة مستندات PDF. ويتضمن مثال 'Hello World' يوضح كيفية إنشاء ملف PDF بسيط يحتوي على محتوى نصي، مما يساعد المطورين على فهم الوظيفة الأساسية لواجهة برمجة التطبيقات بسرعة.
SoftwareApplication: go-cpp
---

عادةً ما يُستخدم مثال "Hello World" لتقديم ميزات لغة برمجة أو برنامج بحالة استخدام بسيطة.

**Aspose.PDF for Go** هو واجهة برمجة تطبيقات PDF غنية بالميزات تتيح للمطورين تضمين إنشاء مستندات PDF ومعالجتها وقدرات التحويل باستخدام Go. يدعم العديد من تنسيقات الملفات الشائعة، بما في ذلك PDF، TXT، XPS، EPUB، TEX، DOC، DOCX، PPTX، تنسيقات الصور وغيرها. في هذه المقالة، نقوم بإنشاء مستند PDF يحتوي على النص "Hello World!" بعد تثبيت Aspose.PDF for Go في بيئتك، يمكنك تنفيذ عينة الشيفرة لمعرفة كيفية عمل واجهة برمجة تطبيقات Aspose.PDF.
يتبع المقتطف البرمجي التالي هذه الخطوات:

1. إنشاء مثيل جديد لوثيقة PDF.
1. إضافة صفحة جديدة إلى مستند PDF باستخدام [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) دالة.
1. تعيين حجم الصفحة باستخدام [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. إضافة النص "Hello World!" إلى الصفحة الأولى باستخدام [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. حفظ مستند PDF المُصلح باستخدام [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) طريقة.
1. إغلاق مستند PDF وإطلاق أي موارد مخصصة.

المقتطف البرمجي التالي هو برنامج Hello World لعرض عمل Aspose.PDF for Go API.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```

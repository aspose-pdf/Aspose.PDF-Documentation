---
title: إضافة صفحات إلى مستند PDF
linktitle: إضافة صفحات
type: docs
weight: 10
url: /ar/go-cpp/add-pages/
description: استكشف كيفية إضافة صفحات إلى ملف PDF موجود بلغة Go باستخدام Aspose.PDF لتحسين وتوسيع مستنداتك.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة صفحات PDF باستخدام Aspose.PDF للـ Go
Abstract: يوفر Aspose.PDF للـ Go عبر C++ وظائف قوية لإضافة صفحات إلى مستندات PDF، مما يسمح للمطورين بإنشاء صفحات جديدة ديناميكياً وتخصيصها وفقاً لمتطلبات محددة. تدعم المكتبة إدراج صفحات فارغة أو نسخ صفحات من مستندات موجودة مع تقديم خيارات لتحديد حجم الصفحة، واتجاهها، ومحتواها. تمكّن هذه القدرات من توسيع وتخصيص المستندات بسلاسة. تتضمن الوثائق تعليمات مفصلة وعينات شفرة لمساعدة المطورين على تنفيذ ميزات إضافة الصفحات بفعالية في تطبيقاتهم.
SoftwareApplication: go-cpp
---

## إضافة صفحة في ملف PDF

يوضح مقتطف كود Go المقدم كيفية تنفيذ عملية إضافة صفحة في نهاية ملف PDF باستخدام مكتبة Aspose.PDF. 

1. ال [فتح](https://reference.aspose.com/pdf/go-cpp/core/open/) تتيح الدالة للبرنامج تحميل ملف PDF موجود (sample.pdf) للتلاعب به. وهذا أمر أساسي لأي عمليات متعلقة بـ PDF، مثل التحرير، إضافة محتوى، أو قراءة البيانات.
1. ال [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) يُستخدم الأسلوب لإدراج صفحة فارغة جديدة في مستند PDF الحالي. وهذا مفيد لتوسيع المستند أو إعداده لمحتوى إضافي.
1. ال [حفظ](https://reference.aspose.com/pdf/go-cpp/core/save/) الطريقة تضمن أن التعديلات على الـ PDF تُكتب مرة أخرى إلى الملف. هذه الخطوة ضرورية للحفاظ على التغييرات، مثل إضافة صفحات جديدة.
1. ال [إغلاق](https://reference.aspose.com/pdf/go-cpp/core/close/) يتم استدعاء الطريقة باستخدام defer لإطلاق أي موارد تم تخصيصها أثناء عمليات الـ PDF. هذا مهم لمنع تسرب الذاكرة وضمان استخدام موارد فعال.

هذا المقتطف مثال مختصر وفعال لكيفية استخدام مكتبة Aspose.PDF Go للقيام بمهام أساسية لتلاعب الـ PDF.

تسمح لك Aspose.PDF for Go بإدراج صفحة في مستند PDF في أي موقع داخل الملف وكذلك إضافة صفحات إلى نهاية ملف PDF.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

## إدراج صفحة في ملف PDF

ال [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) تقوم الطريقة بإدراج صفحة جديدة في الموضع المحدد. هذه الميزة مفيدة عندما تحتاج إلى إدراج صفحات إضافية في مستند موجود، على سبيل المثال، إضافة قسم جديد أو محتوى إلى تقرير أو عرض تقديمي.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
---
title: رخصة Aspose PDF
linktitle: الترخيص والقيود
type: docs
weight: 90
url: /ar/go-cpp/licensing/
description: تدعو Aspose. PDF for Go عملاءها للحصول على Classic License. وكذلك استخدام رخصة محدودة لاستكشاف المنتج بشكل أفضل.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: الترخيص لـ Aspose.PDF for Go عبر C++
Abstract: صفحة الترخيص لـ Aspose.PDF for Go عبر C++ تشرح خيارات الترخيص المتاحة للمنتج. يمكن للعملاء الاختيار بين Classic License، Metered License، أو رخصة محدودة لأغراض التقييم. كما تسلط الصفحة الضوء على فوائد الحصول على رخصة صحيحة، مثل إتاحة كامل الوظائف وإزالة قيود التقييم.
SoftwareApplication: go-cpp
---


## قيود نسخة التقييم

نريد عملائنا اختبار مكوّناتنا بدقة قبل الشراء لذا تسمح لك نسخة التقييم باستخدامها كما تفعل عادةً.

- **المستندات التي تم إنشاؤها بعلامة مائية للتقييم.** نسخة التقييم من Aspose.PDF for Go توفر جميع وظائف المنتج، لكن جميع الصفحات في الملفات المُولدة تحمل علامة مائية بالنص "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." في الأعلى.

- **قصر عدد الصفحات التي يمكن معالجتها.**
في نسخة التقييم، يمكنك معالجة الصفحات الأربع الأولى فقط من المستند.

>إذا كنت ترغب في اختبار Aspose.PDF for Go بدون قيود نسخة التقييم، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا. يرجى الرجوع إلى [كيف تحصل على ترخيص مؤقت؟](https://purchase.aspose.com/temporary-license)

## رخصة كلاسيكية

تطبيق ترخيص لتمكين الوظائف الكاملة لمكتبة Aspose.PDF باستخدام ملف ترخيص (Aspose.PDF.GoViaCPP.lic).

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

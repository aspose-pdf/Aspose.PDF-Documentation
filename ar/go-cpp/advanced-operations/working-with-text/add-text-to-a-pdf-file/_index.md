---
title: إضافة نص إلى PDF باستخدام Go
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: /ar/go-cpp/add-text-to-pdf-file/
description: تعرّف على كيفية إضافة نص إلى مستند PDF باستخدام Go و Aspose.PDF لتحسين المحتوى وتحرير المستندات.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: إضافة نص إلى PDF باستخدام Aspose.PDF للـ Go
Abstract: يوفر القسم "Add Text to PDF File" في وثائق Aspose.PDF للغات C++ و Go تعليمات خطوة بخطوة حول إدراج النص في مستندات PDF بصورة برمجية. يغطي طرقًا متعددة لإضافة النص، بما في ذلك تحديد الموقع، تخصيص الخط، تعديل اللون، وخيارات محاذاة النص. يوضح الدليل كيفية إضافة النص إلى صفحات ومواقع محددة داخل PDF، مما يضمن وضع المحتوى بدقة. مع أمثلة كود مفصلة وشروحات، يمكن للمطورين دمج ميزات إدراج النص بسهولة في تطبيقاتهم لتحسين إدارة مستندات PDF.
SoftwareApplication: go-cpp
---

لإضافة نص إلى ملف PDF موجود:

1. افتح ملف PDF.
1. أضف النص إلى مستند PDF باستخدام [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) دالة.
1. يحفظ التعديلات في نفس الملف.

## إضافة نص

القطعة البرمجية التالية توضح لك كيفية إضافة نص إلى ملف PDF موجود.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
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

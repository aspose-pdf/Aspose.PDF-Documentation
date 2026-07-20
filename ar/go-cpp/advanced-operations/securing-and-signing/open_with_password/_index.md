---
title: فتح ملف PDF محمي بكلمة مرور باستخدام Go
linktitle: فتح ملف PDF محمي بكلمة مرور
type: docs
weight: 70
url: /ar/go-cpp/open-password-protected-pdf/
description: فتح ملف PDF محمي بكلمة مرور باستخدام Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## فتح مستند PDF محمي بكلمة مرور

يفسر هذا المقتطف البرمجي كيفية فتح مستند PDF محمي بكلمة مرور باستخدام Aspose.PDF for Go via C++. يتم فتح المستند باستخدام كلمة مرور المالك، والتي توفر الوصول الكامل وتسمح بعمليات إضافية مثل قراءة البيانات الوصفية، فحص الأذونات، فك تشفير الملف، أو تعديل المحتوى.

1. فتح المستند PDF المحمي.
1. استدعِ [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) وقدم اسم الملف مع كلمة مرور المالك لفتح المستند.
1. استخدم 'defer pdf.Close()' لتحرير جميع الموارد المخصصة بمجرد اكتمال المعالجة.
1. بعد فتح المستند، يمكنك المتابعة بالمهام الإضافية مثل فك تشفير PDF، وتغيير الأذونات، أو استخراج المعلومات.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_password.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // working...
    }
```
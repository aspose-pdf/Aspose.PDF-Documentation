---
title:  تشفير PDF باستخدام Go
linktitle: تشفير ملف PDF
type: docs
weight: 10
url: /ar/go-cpp/encrypt-pdf/
description: تشفير ملف PDF باستخدام Aspose.PDF for Go عبر C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تشفير ملف PDF باستخدام كلمة مرور المستخدم أو المالك

لتشفير المستندات بسهولة وأمان، يمكنك استخدام Aspose.PDF for Go عبر C++.

- ‏**userPassword**، إذا تم تعيينه، هو ما تحتاج إلى تقديمه لفتح ملف PDF. سيُظهر Acrobat/Reader للمستخدم طلب إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، فإن المستند لن يفتح.
- إذا تم ضبط **ownerPassword**، فإنه يتحكم في الأذونات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ. سيمنع Acrobat/Reader هذه الأشياء بناءً على إعدادات الأذونات. سيتطلب Acrobat كلمة السر هذه إذا كنت ترغب في ضبط/تغيير الأذونات.

تم حماية ملف PDF بكلمات مرور للمستخدم والمالك، ومُكوَّن بأذونات وصول محددة، ومشفّر باستخدام خوارزمية AES-128 مع أمان متوافق مع PDF 2.0–compatible security. ثم يُحفظ المستند المشفّر إلى القرص.

1. إنشاء مستند PDF جديد.
1. تشفير مستند PDF باستخدام [تشفير](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) طريقة.
1. حدد كلمة مرور مستخدم لتقييد فتح المستند.
1. حدد كلمة مرور مالك للتحكم في الأذونات.
1. حدد الإجراءات المسموح بها باستخدام علم بت للأذونات.
1. اختر AES-128 كخوارزمية التشفير.
1. فعّل تشفير PDF 2.0 للامتثال لأمان حديث.
1. احفظ المستند المؤمّن باستخدام [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), كتابة إلى ملف جديد.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Encrypt(userPassword, ownerPassword, permissions, cryptoAlgorithm, usePdf20) encrypts PDF-document
        err = pdf.Encrypt(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|asposepdf.ModifyContent|asposepdf.FillForm,
            asposepdf.AESx128,
            true,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
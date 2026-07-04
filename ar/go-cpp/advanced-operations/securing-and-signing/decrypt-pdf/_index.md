---
title: فك تشفير PDF باستخدام Go
linktitle: فك تشفير ملف PDF
type: docs
weight: 40
url: /ar/go-cpp/decrypt-pdf/
description: فك تشفير ملف PDF باستخدام Aspose.PDF for Go عبر C++ .
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

يمكنك فتح، فك تشفير، وحفظ مستند PDF محمي بكلمة مرور باستخدام Aspose.PDF for Go عبر C++. يتم فتح ملف PDF باستخدام كلمة مرور المالك، يتم فك تشفيره لإزالة جميع قيود الأمان، ثم يتم حفظه كمستند جديد غير محمي.

1. استدعاء [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) وفر اسم الملف مع كلمة مرور المالك للوصول إلى ملف PDF المشفر.
1. استدعِ [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) الطريقة لإزالة حماية كلمة المرور وجميع القيود الأمنية المرتبطة من المستند.
1. احفظ ملف PDF المفكوك باستخدام [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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
        // Decrypt() decrypts PDF-document
        err = pdf.Decrypt()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_without_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
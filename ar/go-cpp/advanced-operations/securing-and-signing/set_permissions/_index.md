---
title: تعيين أذونات لمستند PDF باستخدام Go
linktitle: تعيين الأذونات
type: docs
weight: 80
url: /ar/go-cpp/set_permissions/
description: تعيين أذونات لمستند PDF باستخدام Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تعيين أذونات الوصول لمستند PDF

تم إنشاء مستند PDF جديد وحمايته بكلمات مرور للمستخدم والمالك، بينما يتم السماح صراحةً بأذونات محددة—مثل الطباعة وتعديل المحتوى وتعبئة النماذج—. ثم يتم حفظ المستند مع تطبيق قيود الأذونات هذه.

1. إنشاء مستند PDF جديد.
1. اتصال [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) لحماية المستند.
1. حدد كلمة مرور المستخدم لتقييد الوصول.
1. حدد كلمة مرور المالك للتحكم في إعدادات الأمان.
1. عرّف العمليات المسموح بها باستخدام علم أذونات البت.
1. حفظ ملف PDF مع تطبيق الأذونات باستخدام [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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

        // SetPermissions(userPassword, ownerPassword, permissions) sets permissions for PDF-document
        err = pdf.SetPermissions(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|
                asposepdf.ModifyContent|
                asposepdf.FillForm,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_permissions.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
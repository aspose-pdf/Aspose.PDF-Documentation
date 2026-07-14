---
title: حذف صفحات PDF باستخدام Go
linktitle: حذف صفحات PDF
type: docs
weight: 30
url: /ar/go-cpp/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حذف صفحات PDF باستخدام Aspose.PDF for Go
Abstract: يوفر Aspose.PDF for Go via C++ وظائف فعّالة لحذف الصفحات من مستندات PDF، مما يمكّن المطورين من إزالة الصفحات غير المرغوب فيها أو غير الضرورية بسهولة. تسمح المكتبة بحذف صفحة واحدة أو عدة صفحات عن طريق تحديد أرقام الصفحات أو النطاقات، مما يضمن تعديلًا دقيقًا للمستند. تساعد هذه الميزة على تبسيط ملفات PDF عن طريق القضاء على المحتوى الزائد وتحسين بنية المستند. توفر الوثائق تعليمات خطوة بخطوة وعينات شفرة لمساعدة المطورين في تنفيذ وظيفة حذف الصفحات بفعالية ضمن تطبيقاتهم.
SoftwareApplication: go-cpp
---

يمكنك حذف الصفحات من ملف PDF باستخدام **Aspose.PDF for Go via C++**. يوضح المقتطف البرمجي التالي كيفية معالجة مستند PDF بحذف صفحة معينة. هذه الطريقة فعّالة لمهام معالجة مستندات PDF، خاصةً لإزالة الصفحات، وحفظ المستند المعدل، وضمان إدارة الموارد بشكل صحيح.

1. فتح ملف PDF.
1. حذف صفحة محددة باستخدام [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) دالة.
1. حفظ المستند باستخدام [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) طريقة.

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
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

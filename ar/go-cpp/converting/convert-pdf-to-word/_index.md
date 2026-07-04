---
title: تحويل PDF إلى مستندات Word في Go
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: تعلم كيفية كتابة كود Go للتحويل من PDF إلى DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أداة لتحويل PDF إلى Word باستخدام Aspose.PDF for Go
Abstract: Aspose.PDF for Go عبر C++ يتيح تحويل مستندات PDF إلى تنسيق DOC بسلاسة مع الحفاظ على النص الأصلي، الصور، الجداول، وبنية المستند العامة. تتيح هذه الميزة للمطورين تحويل ملفات PDF الثابتة إلى ملفات Word قابلة للتعديل لمزيد من التعديل والمعالجة. توفر المكتبة خيارات تخصيص متعددة للتحكم في ناتج التحويل، مما يضمن دقة عالية ووفاء. تشمل الوثائق تعليمات مفصلة وعينات كود لمساعدة المطورين على تنفيذ تحويل PDF إلى DOC بفعالية في تطبيقاتهم.
SoftwareApplication: go-cpp
---

لتحرير محتوى ملف PDF في Microsoft Word أو معالجات نصية أخرى تدعم تنسيقات DOC و DOCX. ملفات PDF قابلة للتحرير، لكن ملفات DOC و DOCX أكثر مرونة وقابلة للتخصيص.

## تحويل PDF إلى DOC

يظهر مقتطف كود Go المقدم كيفية تحويل مستند PDF إلى DOC باستخدام مكتبة Aspose.PDF:

1. فتح مستند PDF.
1. تحويل ملف PDF إلى DOC باستخدام [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) دالة.
1. إغلاق مستند PDF وإطلاق أي موارد مخصصة.

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
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

Aspose.PDF for Go يقدم لك تطبيقًا مجانيًا عبر الإنترنت [“PDF to DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك Aspose.PDF for Go API قراءة وتحويل مستندات PDF إلى DOCX. DOCX هو تنسيق معروف جيدًا لوثائق Microsoft Word التي تم تغيير هيكلها من ثنائي بسيط إلى مزيج من ملفات XML والملفات الثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات اللاحقة ولكن ليس مع الإصدارات الأقدم من MS Word التي تدعم امتدادات ملفات DOC.

يظهر مقطع الشيفرة Go المقدم كيفية تحويل مستند PDF إلى DOCX باستخدام مكتبة Aspose.PDF:

1. فتح مستند PDF.
1. تحويل ملف PDF إلى DOCX باستخدام [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) دالة.
1. إغلاق مستند PDF وإطلاق أي موارد مخصصة.

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
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

Aspose.PDF for Go يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Word تطبيق مجاني](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
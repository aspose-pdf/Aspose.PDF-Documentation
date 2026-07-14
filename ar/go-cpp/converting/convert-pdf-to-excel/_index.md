---
title: تحويل PDF إلى Excel في Go
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/go-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-04"
description: تسمح لك Aspose.PDF for Go بتحويل PDF إلى صيغة XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أداة Golang لتحويل مستندات PDF إلى Excel
Abstract: توفر مكتبة Aspose.PDF for Go via C++ حلاً قوياً لتحويل مستندات PDF إلى صيغة XLSX بدقة وكفاءة عاليتين. تمكن هذه الميزة المطورين من استخراج البيانات الجدولية من ملفات PDF مع الحفاظ على التخطيط الأصلي لجداول Excel والهيكل والتنسيق. تقدم الوثائق إرشادات مفصلة حول تنفيذ عملية التحويل، بما في ذلك رمز عيّنة (sample code) وتعليمات خطوة بخطوة لتسهيل التكامل السلس في تطبيقات Go.
SoftwareApplication: go-cpp
---

**Aspose.PDF for Go** يدعم ميزة تحويل ملفات PDF إلى صيغة Excel.

## تحويل PDF إلى XLSX

يقدم Excel أدوات متقدمة للفرز والتصفية وتحليل البيانات، مما يجعل من السهل أداء مهام مثل تحليل الاتجاهات أو النمذجة المالية، والتي تكون صعبة مع ملفات PDF الثابتة. النسخ اليدوي للبيانات من ملفات PDF إلى Excel يستغرق وقتًا طويلاً وعرضة للأخطاء. التحويل ي automatis هذه العملية، موفرًا وقتًا كبيرًا للبيانات الضخمة.

Aspose.PDF for Go يستخدم [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/) لتحويل ملف PDF الذي تم تنزيله إلى جدول بيانات Excel وحفظه.

1. استيراد الحزم المطلوبة.
1. افتح ملف PDF.
1. حوّل PDF إلى XLSX باستخدام [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/).
1. أغلق مستند PDF.

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
    // SaveXlsX(filename string) saves previously opened PDF-document as XlsX-document with filename
    err = pdf.SaveXlsX("sample.xlsx")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF for Go يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), حيث يمكنك تجربة واستكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى Excel مع تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}
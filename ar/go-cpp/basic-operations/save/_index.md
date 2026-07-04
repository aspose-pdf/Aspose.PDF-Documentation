---
title: حفظ مستند PDF برمجيًا
linktitle: حفظ PDF
type: docs
weight: 30
url: /ar/go-cpp/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF باستخدام Aspose.PDF for Go عبر C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ مستند PDF باستخدام Aspose.PDF for Go عبر C++
Abstract: Aspose.PDF for Go عبر C++ يقدم وظائف شاملة لحفظ مستندات PDF بتنسيقات ومواقع مختلفة بكفاءة ومرونة عالية. تسمح المكتبة للمطورين بحفظ ملفات PDF إلى أنظمة الملفات وتدفقات الذاكرة، أو إخراجها بتنسيقات بديلة مثل DOCX و XLSX والصور. توفر خيارات لتخصيص معلمات الحفظ، تحسين حجم الملف، وضمان سلامة البيانات. تشمل الوثائق تعليمات مفصلة وعينات كود لمساعدة المطورين على تنفيذ قدرات حفظ PDF بفعالية في تطبيقاتهم.
SoftwareApplication: go-cpp
---

## حفظ مستند PDF إلى نظام الملفات

المثال يوضح [New](https://reference.aspose.com/pdf/go-cpp/core/new/) طريقة لإنشاء مستند PDF جديد، وهي ميزة أساسية لإنشاء المستندات ديناميكيًا، مثل التقارير أو الفواتير.

الكود بسيط ويمكن أن يعمل كقالب لميزات أكثر تقدماً مثل إضافة نص، صور، أو تعليقات توضيحية إلى PDF.

هذا المثال يوضح الاستخدام السهل لمكتبة Aspose.PDF Go، مستعرضًا إمكاناتها لإنشاء وتعديل وحفظ المستندات.

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
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

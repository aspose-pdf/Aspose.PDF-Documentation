---
title: استخراج النص من PDF باستخدام Go
linktitle: استخراج النص من PDF
type: docs
weight: 30
url: /ar/go-cpp/extract-text-from-pdf/
description: تصفّح هذه المقالة طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج النص باستخدام Aspose.PDF for Go
Abstract: توفر Aspose.PDF for Go عبر C\u002B\u002B طريقة قوية وفعّالة لاستخراج النص من مستندات PDF. تدعم المكتبة تقنيات استخراج متعددة، مما يتيح للمستخدمين استرجاع النص من المستندات بالكامل، أو صفحات معينة، أو مناطق محددة مسبقًا داخل PDF.
SoftwareApplication: go-cpp
---

## استخراج النص من مستند PDF

استخراج النص من مستند PDF هو مهمة شائعة ومفيدة للغاية. غالبًا ما تحتوي ملفات PDF على معلومات حيوية تحتاج إلى الوصول إليها، أو تحليلها، أو معالجتها لأغراض مختلفة.

استخراج النص يجعل محتوى PDF قابلاً للبحث، مما يسمح للمستخدمين بتحديد المعلومات المحددة بسرعة دون مراجعة المستند بالكامل يدويًا.

في حال أردت استخراج النص من مستند PDF، يمكنك استخدام [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) function.
يرجى مراجعة المقتطف البرمجي التالي لاستخراج النص من ملف PDF باستخدام Go.

1. افتح مستند PDF بالاسم الملف المعطى.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) يستخرج محتوى النص من مستند PDF.
1. اطبع النص المستخرج إلى وحدة التحكم.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
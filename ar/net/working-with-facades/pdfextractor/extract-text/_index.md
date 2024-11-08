```
---
title: استخراج النص من ملف PDF
type: docs
weight: 30
url: /ar/net/extract-text/
description: يشرح هذا القسم كيفية استخراج النص من ملف PDF باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
---

في هذه المقالة، سنلقي نظرة على تفاصيل استخراج النص من ملف PDF. جميع ميزات الاستخراج هذه متوفرة في مكان واحد، في فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). سنرى كيفية استخدام هذه الميزات في كودنا.

توفر فئة [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) ثلاث أنواع من قدرات الاستخراج. هذه الفئات الثلاث هي النصوص والصور والمرفقات. من أجل تنفيذ الاستخراج تحت كل من هذه الفئات الثلاث توفر PdfExtractor طرقًا مختلفة تعمل معًا لتعطيك النتيجة النهائية.

على سبيل المثال، لاستخراج النص يمكنك استخدام ثلاث طرق وهي:
``` 
[ExtractText, GetText, HasNextPageText and GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index).
``` الآن، من أجل البدء في استخراج النص، أولاً وقبل كل شيء، تحتاج إلى استدعاء طريقة [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index)؛ هذا سيقوم باستخراج النص من ملف PDF وسيقوم بتخزينه في الذاكرة. بعد ذلك، ستقوم طريقة [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) بأخذ هذا النص المستخرج وحفظه إلى القرص في الموقع المحدد في ملف. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) تساعدك في التنقل عبر كل صفحة والتحقق مما إذا كانت الصفحة التالية تحتوي على أي نص أم لا. إذا كانت تحتوي على بعض النصوص، فإن [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) ستساعدك في حفظ نص صفحة فردية في الملف.

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // Create an object of the PdfExtractor class
    PdfExtractor pdfExtractor = new PdfExtractor();

    // Bind the input PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // ExtractText
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // Extract the text into separate files
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
To Extract the Text Extraction Mode use the following code:

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // قم بإنشاء كائن من فئة PdfExtractor
    PdfExtractor pdfExtractor = new PdfExtractor();

    // ربط ملف PDF المدخل
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // استخراج النص
    // pdfExtractor.ExtractTextMode = 0; //وضع نقي
    pdfExtractor.ExtractTextMode = 1; //وضع خام
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // استخراج النص في ملفات منفصلة
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
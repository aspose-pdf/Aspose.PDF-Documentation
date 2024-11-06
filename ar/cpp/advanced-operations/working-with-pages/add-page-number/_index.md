---
title: إضافة رقم الصفحة إلى PDF باستخدام C++
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: ar/cpp/add-page-number/
description: تتيح لك Aspose.PDF for C++ إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام فئة PageNumber Stamp.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية إضافة أرقام الصفحات إلى ملف PDF موجود

يجب أن تحتوي جميع الوثائق على أرقام صفحات. تسهل أرقام الصفحات على القارئ تحديد أجزاء مختلفة من الوثيقة.
تتيح لك **Aspose.PDF for C++** إضافة أرقام الصفحات باستخدام PageNumberStamp.

الخطوات التالية والكود المثال يوضح كيفية إضافة تسميات ترقيم الصفحات إلى وثيقة PDF موجودة باستخدام عنصر الصفحة [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) لإضافة أرقام الصفحات تلقائيًا إلى ملف PDF.

خطوات إضافة أرقام الصفحات إلى وثيقة PDF موجودة:

لإضافة ختم رقم الصفحة، تحتاج إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) وكائن [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) باستخدام الخصائص المطلوبة.

بعد ذلك، يمكنك استدعاء [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) طريقة من [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) لإضافة الختم في PDF.

يمكنك أيضًا تعيين خصائص الخط لرقم الصفحة الختم.

يوضح لك مقطع الشفرة التالي كيفية إضافة أرقام الصفحات في ملف PDF.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // إنشاء ختم رقم الصفحة
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// سواء كان الختم في الخلفية
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// تعيين خصائص النص
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // إضافة الختم إلى صفحة معينة
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // حفظ المستند الناتج
    document->Save(_dataDir+ outputFileName);
}
```

## مثال حي

[إضافة أرقام الصفحات إلى PDF](https://products.aspose.app/pdf/page-number) هو تطبيق ويب مجاني على الإنترنت يتيح لك التحقيق في كيفية عمل وظيفة إضافة أرقام الصفحات.

[![كيفية إضافة رقم الصفحة في pdf باستخدام C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## إضافة/إزالة ترقيم بيتس

يُستخدم **ترقيم بيتس** (المعروف أيضًا بختم بيتس) في المجالات القانونية والطبية والتجارية لوضع أرقام تعريف و/أو علامات تاريخ/وقت على الصور والمستندات أثناء مسحها ضوئيًا أو معالجتها، على سبيل المثال، خلال مرحلة الاكتشاف من التحضيرات للمحاكمة أو تحديد إيصالات الأعمال. يوفر هذه العملية التعريف والحماية وترقيم متسلسل تلقائي للصور أو المستندات.

Aspose.PDF لديه دعم محدود لترقيم بيتس في الوقت الحالي. سيتم تحديث هذه الوظيفة وفقًا لطلبات العملاء.

### كيفية إزالة ترقيم بيتس

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // حفظ المستند الناتج
    document->Save(_dataDir + outputFileName);
}
```
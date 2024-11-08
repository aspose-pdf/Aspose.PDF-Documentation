---
title: إضافة طوابع الصفحة في ملف PDF 
linktitle: الطوابع في ملف PDF 
type: docs
weight: 30
url: /ar/cpp/page-stamps-in-the-pdf-file/
description: إضافة طابع صفحة إلى ملف PDF باستخدام فئة PdfPageStamp مع C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة طابع الصفحة باستخدام C++

يمكن استخدام [PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) عندما تحتاج إلى تطبيق طابع مركب يحتوي على رسوميات، نصوص، جداول. يوضح المثال التالي كيفية استخدام الطابع لإنشاء قرطاسية مثل استخدام Adobe InDesign، Illustrator، Microsoft Word. افترض أن لدينا بعض الوثائق المدخلة ونريد تطبيق نوعين من الحدود باللون الأزرق واللون البرقوقي.

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```
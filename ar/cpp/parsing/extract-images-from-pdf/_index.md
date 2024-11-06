---
title: استخراج الصور من PDF
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: ar/cpp/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

أيضًا، مهمة مطلوبة عند العمل مع مستندات PDF هي استخراج الصور من ملف PDF. على سبيل المثال، قد تتلقى بريد إلكتروني بصيغة PDF يحتوي على العديد من الصور الرائعة التي ترغب في استخراجها كملفات منفصلة.

تسمح لك مكتبة Aspose.PDF باستخراج الصور من PDF باستخدام الشيفرة التالية:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extract a particular image
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Save output image
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```
---
title: ما هو الجديد في C++
linktitle: ما هو الجديد
type: docs
weight: 10
url: ar/cpp/whatsnew/
description: في هذه الصفحة يتم تقديم أحدث الميزات الجديدة في Aspose.PDF لـ C++ التي تم تقديمها في الإصدارات الأخيرة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## ما هو الجديد في Aspose.PDF 24.8

إمكانية إضافة صور SVG إلى الصفحة.

## ما هو الجديد في Aspose.PDF 24.4

تم حل مشكلة في تحميل صور SVG.

## ما هو الجديد في Aspose.PDF 24.3

تم إصلاح تسربات الذاكرة أثناء تحويل مستندات PDF إلى صيغ أخرى.

## ما هو الجديد في Aspose.PDF 24.2

منذ الإصدار 24.2 تم تنفيذ:

- تم تحسين أداء JPXDecoder.

- تم إصلاح قراءة المستندات ذات الهيكل المعطوب.

## ما هو الجديد في Aspose.PDF 23.7

- تم تقديم حفظ مستندات PDF إلى صيغة EPUB:

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // String for path name
        String _dataDir("C:\\Samples\\Conversion\\");

        // String for input file name
        String infilename("sample.pdf");
        // String for output file name
        String outfilename("PDFToEPUB_out.epub");

        // Open document
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Save PDF file into EPUB format
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```

- تم تنفيذ تحميل ملفات بتنسيق PCL:

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Error: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Error: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## ما الجديد في Aspose.PDF 23.1

اعتبارًا من الإصدار 23.1 تمت إضافة دعم صور بتنسيق Dicom:

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## ما الجديد في Aspose.PDF 22.11

من الإصدار 22.11 تم الإعلان عن الإصدار العام الأول من **Aspose.PDF ل C++ macOS**.

يسرنا أن نعلن عن الإصدار العام الأول من Aspose.PDF ل C++ macOS. Aspose.PDF ل C++ macOS هو مكتبة C++ خاصة تسمح للمطورين بإنشاء والتعامل مع مستندات PDF دون استخدام Adobe Acrobat.
Aspose.PDF ل C++ macOS يسمح للمطورين بإنشاء النماذج، إضافة/تعديل النصوص، التعامل مع صفحات PDF، إضافة التعليقات التوضيحية، معالجة الخطوط المخصصة، وأكثر من ذلك.

## ما الجديد في Aspose.PDF 22.5

تم تنفيذ دعم النماذج XFA في مستندات PDF.

## ما الجديد في Aspose.PDF 22.4

الإصدار الجديد من Aspose.PDF ل C++ لديه قاعدة شيفرة من Aspose.PDF ل .Net 22.4 و Aspose.Imaging 22.4.

- تم تنفيذ الطريقة System::Drawing::GetThumbnailImage();
- تم تحسين المُنشئ RegionDataNodeRect;
- تم إصلاح تحميل الصور بالأبيض والأسود 1 بت لكل بكسل.

## ما الجديد في Aspose.PDF 22.3

تمت إضافة التحميل الزائد للطريقة إلى العديد من الفئات. هذه المعلمات تدعم ArrayView حيث كان يدعم فقط ArrayPtr سابقًا.

## ما الجديد في Aspose.PDF 22.1

الإصدار الجديد من Aspose.PDF لـ C++ يحتوي على قاعدة الكود الخاصة بـ Aspose.PDF لـ .Net 22.1:

- تم توفير التنفيذ الجديد لـ System::Xml. سابقًا، كنا نمتلك تنفيذًا مخصصًا يستند إلى مكتبات libxml2 وlibxslt. الإصدار الجديد يستند إلى كود CoreFX المحول

- تمت ترقية مكتبة double-conversion إلى الإصدار 3.1.7

- يتم توقيع ملفات Dll بشهادة Aspose

## ما الجديد في Aspose.PDF 21.10

### دعم Aspose.PDF لـ C++ لتحويل SVG إلى تنسيق PDF

يوضح المقتطف التالي من الكود عملية تحويل ملف SVG إلى تنسيق PDF باستخدام Aspose.PDF لـ C++.

```cpp

    void ConvertSVGtoPDF()
    {
        std::clog << "SVG to PDF convert: Start" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("sample.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }
        std::clog << "SVG to PDF convert: Finish" << std::endl;
    }
```
ضع في اعتبارك مثالاً مع الميزات المتقدمة:

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "تحويل من SVG إلى PDF: بدء" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("Aspose.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        options->set_AdjustPageSize(true);
        options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }

        std::clog << "تحويل من SVG إلى PDF: انتهى" << std::endl;
    }
```

## ما الجديد في Aspose.PDF 21.4

### تم تنفيذ حفظ مستندات PDF بصيغة HTML

Aspose.PDF لـ C++ تدعم الميزات لتحويل ملف PDF إلى HTML.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```
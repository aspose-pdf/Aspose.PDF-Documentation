---
title: Aspose.PDF С++ Example
linktitle: Hello World Example
type: docs
weight: 40
url: /ar/cpp/hello-world-example/
description: تعرض هذه الصفحة كيفية استخدام البرمجة البسيطة لإنشاء مستند PDF يحتوي على النص - Hello World.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

يتم استخدام مثال "Hello World" تقليديًا لتقديم ميزات لغة البرمجة أو البرنامج بحالة استخدام بسيطة.

Aspose.PDF لـ C++ هو واجهة برمجة تطبيقات غنية بالميزات تتيح للمطورين تضمين قدرات إنشاء وتعديل وتحويل مستندات PDF في تطبيقات C++ الخاصة بهم. يدعم العمل مع العديد من تنسيقات الملفات الشهيرة بما في ذلك PDF وXFA وTXT وHTML وPCL وXML وXPS وEPUB وTEX وتنسيقات ملفات الصور. في هذه المقالة، نقوم بإنشاء مستند PDF يحتوي على النص "Hello World!". بعد تثبيت Aspose.PDF لـ C++ في بيئتك، يمكنك تنفيذ عينة الكود أدناه لمعرفة كيفية عمل Aspose.PDF API.

يتبع مقطع الكود أدناه هذه الخطوات:

1.
``` أنشئ [فئة سلسلة](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.  
1. أنشئ كائن [وثيقة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). في هذه الخطوة، سننشئ وثيقة PDF فارغة مع بعض البيانات الوصفية ولكن بدون صفحات.  
1. أضف [صفحة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) إلى كائن الوثيقة. الآن، سيكون لدى وثيقتنا صفحة واحدة.  
1. [احفظ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) وثيقة PDF الناتجة  

شفرة البرنامج التالية عبارة عن برنامج Hello World لعرض عمل Aspose.PDF لـ C++ API.

```cpp
void ExampleSimple()
{
    // مخزن للاحتفاظ بالمسار المدمج.
    String outputFileName;

    // سلسلة لاسم المسار.
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // أضف نصًا إلى الصفحة الجديدة
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // احفظ PDF المحدث
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```
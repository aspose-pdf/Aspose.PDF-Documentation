---
title: البحث والحصول على النص من صفحات مستند PDF
linktitle: البحث والحصول على النص
type: docs
weight: 60
url: /ar/cpp/search-and-get-text-from-pdf/
description: يشرح هذا المقال كيفية استخدام أدوات مختلفة للبحث والحصول على نص من مستندات PDF. يمكننا البحث باستخدام تعبير عادي من صفحات معينة أو من المستند بأكمله.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## البحث والحصول على النص من جميع صفحات مستند PDF

تسمح لك فئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) بالعثور على النص، الذي يطابق عبارة معينة، من جميع صفحات مستند PDF. من أجل البحث عن النص من المستند بأكمله، تحتاج إلى استدعاء طريقة Accept من مجموعة [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). تأخذ طريقة 'Accept' كائن TextFragmentAbsorber كمعامل، والذي يعيد مجموعة من كائنات TextFragment.

يوضح لك مقطع الشيفرة التالي كيفية البحث عن النص من جميع الصفحات.
```

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // إنشاء كائن TextAbsorber للعثور على جميع مثيلات عبارة البحث المدخلة
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // قبول المستخلص لجميع الصفحات
    document->get_Pages()->Accept(textFragmentAbsorber);

    // الحصول على أجزاء النص المستخرجة في مجموعة
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // التجول عبر الأجزاء
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"النص :- {0}", textFragment->get_Text());
        Console::WriteLine(u"الموقع :- {0}", textFragment->get_Position());
        Console::WriteLine(u"المسافة الأفقية :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"المسافة الرأسية :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"الخط - الاسم :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"الخط - يمكن الوصول إليه :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"الخط - مدمج :- {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"الخط - جزء من مجموعة :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"حجم الخط :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"لون المقدمة :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## البحث والحصول على النص من جميع الصفحات باستخدام التعبير العادي

يساعدك TextFragmentAbsorber في البحث واسترجاع النص، من جميع الصفحات، بناءً على تعبير عادي. أولاً، تحتاج إلى تمرير تعبير منتظم إلى [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) constructor كعبارة. بعد ذلك، يجب عليك تعيين خاصية [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) لكائن TextFragmentAbsorber. هذه الخاصية تتطلب كائن TextSearchOptions وتحتاج إلى تمرير true كمعامل إلى منشئها أثناء إنشاء الكائنات الجديدة. نظرًا لأنك تريد استرجاع النص المطابق من جميع الصفحات، تحتاج إلى استدعاء طريقة Accept لمجموعة Pages. تقوم [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) بإرجاع TextFragmentCollection تحتوي على جميع الأجزاء المطابقة للمعايير المحددة بواسطة التعبير المنتظم. يوضح لك مقطع الشيفرة التالي كيفية البحث والحصول على النص من جميع الصفحات استنادًا إلى تعبير منتظم.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Text :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Name :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - IsEmbedded - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - IsSubset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Font Size :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Foreground Color :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```
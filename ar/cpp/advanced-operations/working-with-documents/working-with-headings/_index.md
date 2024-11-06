---
title: العمل مع العناوين في PDF
type: docs
weight: 90
url: ar/cpp/working-with-headings/
lastmod: "2021-11-11"
description: إنشاء ترقيم في العنوان لمستند PDF الخاص بك باستخدام C++. يوضح Aspose.PDF for C++ أنواعًا مختلفة من أنماط الترقيم.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تطبيق نمط الترقيم في العنوان

يبدأ أي نص في مستند بعنوان. العناوين جزء لا يتجزأ من المحتوى، بغض النظر عن النمط والموضوع.
تساعد العناوين في جذب الانتباه إلى النص وتساعد المستخدمين في العثور على المعلومات التي يحتاجونها في المستند، مما يحسن من قابلية القراءة والإدراك البصري. باستخدام أنماط العناوين، يمكنك أيضًا إنشاء جدول محتويات بسرعة، وتغيير هيكل المستند.
لذلك، دعونا نتحقق من كيفية العمل مع العناوين باستخدام مكتبة Aspose.PDF for C++.

[Aspose.PDF for C++](/pdf/cpp/) يقدم العديد من أنماط الترقيم المعرفة مسبقًا. هذه الأنماط المحددة مسبقًا للترقيم مخزنة في تعداد، NumberingStyle. القيم المحددة مسبقًا لتعداد NumberingStyle ووصفها موضحة أدناه:

|**أنواع العناوين**|**الوصف**|
| :- | :- |
|NumeralsArabic|النوع العربي، على سبيل المثال، 1,1.1,...|
|NumeralsRomanUppercase|النوع الروماني العلوي، على سبيل المثال، I,I.II, ...|
|NumeralsRomanLowercase|النوع الروماني السفلي، على سبيل المثال، i,i.ii, ...|
|LettersUppercase|النوع الإنجليزي العلوي، على سبيل المثال، A,A.B, ...|
|LettersLowercase|النوع الإنجليزي السفلي، على سبيل المثال، a,a.b, ...|
خاصية **Style** في فئة **Aspose.PDF.Heading** تُستخدم لتعيين أنماط الترقيم للعناوين.

|**الشكل: أنماط الترقيم المحددة مسبقًا**|
| :- |
الشفرة المصدرية للحصول على المخرجات الموضحة في الشكل أعلاه موضحة أدناه في المثال.

```cpp
void WorkingWithHeadingsInPDF() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outputFileName("ApplyNumberStyle_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"List 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"List 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"the value, as of the effective date of the plan, of property to be distributed under the plan onaccount of each allowed");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // Save concatenated output file
    document->Save(_dataDir + outputFileName);
}
```
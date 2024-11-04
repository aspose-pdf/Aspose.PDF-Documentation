---
title: Replace Text in PDF using C++
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /cpp/replace-text-in-pdf/
description: تعرف على المزيد حول الطرق المختلفة لاستبدال النص وإزالته من PDF. تسمح Aspose.PDF باستبدال النص في منطقة معينة أو باستخدام تعبير عادي.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

أحيانًا تظهر مهمة لتصحيح أو استبدال النص في مستند PDF. محاولة القيام بذلك يدويًا ستكون مهمة شاقة، لذا إليك الحل لهذه المشكلة.

بصراحة، تحرير ملف PDF ليس مهمة سهلة. لذلك، ستكون الحالة التي تحتاج فيها إلى العثور على كلمة واستبدالها بأخرى أثناء تحرير ملف PDF صعبة للغاية لأنها ستستغرق وقتًا طويلاً للقيام بها. بالإضافة إلى ذلك، قد تواجه العديد من المشاكل مع مخرجاتك، مثل التنسيق أو الخطوط المكسورة. إذا كنت تريد العثور على النص واستبداله بسهولة في ملفات PDF، نوصي باستخدام برنامج مكتبة Aspose.Pdf لأنه سينجز المهمة في دقائق.

في هذه المقالة، سنوضح لك كيفية العثور على النص واستبداله بنجاح في ملفات PDF الخاصة بك باستخدام Aspose.PDF لـ C++.

## استبدال النص في جميع صفحات مستند PDF

{{% alert color="primary" %}}

يمكنك محاولة العثور على النص واستبداله في المستند باستخدام Aspose.PDF والحصول على النتائج عبر الإنترنت في هذا [الرابط](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

من أجل استبدال النص في جميع صفحات مستند PDF، تحتاج أولاً إلى استخدام TextFragmentAbsorber للعثور على العبارة المحددة التي تريد استبدالها. بعد ذلك، تحتاج إلى المرور عبر جميع TextFragments لاستبدال النص وتغيير أي خصائص أخرى. بمجرد القيام بذلك، تحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة Save لكائن Document. يوضح لك مقطع الشيفرة التالي كيفية استبدال النص في جميع صفحات مستند PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## استبدال النص في منطقة معينة من الصفحة

لكي نستبدل النص في منطقة معينة من الصفحة، أولاً، نحتاج إلى إنشاء كائن TextFragmentAbsorber، وتحديد منطقة الصفحة باستخدام خاصية TextSearchOptions.Rectangle ثم تكرار جميع TextFragments لاستبدال النص. بمجرد الانتهاء من هذه العمليات، نحتاج فقط إلى حفظ ملف PDF الناتج باستخدام طريقة Save لكائن Document. يوضح لك مقطع الشيفرة التالي كيفية استبدال النص في جميع صفحات مستند PDF.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // إنشاء كائن TextFragment Absorber
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // البحث عن النص داخل حدود الصفحة
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // تحديد منطقة الصفحة لخيارات البحث عن النص
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // البحث عن النص من الصفحة الأولى لملف PDF
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // تكرار من خلال كل TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // استبدال النص بـ "---"
        tf->set_Text(u"---");
    }

    // حفظ ملف PDF المحدث
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## استبدال النص بناءً على تعبير عادي

إذا كنت ترغب في استبدال بعض العبارات بناءً على تعبير عادي، يجب أولاً العثور على جميع العبارات التي تطابق ذلك التعبير العادي باستخدام TextFragmentAbsorber. سوف تحتاج إلى تمرير التعبير العادي كمعامل إلى منشئ TextFragmentAbsorber. تحتاج أيضًا إلى إنشاء كائن TextSearchOptions الذي يحدد ما إذا كان يتم استخدام التعبير العادي أم لا. بمجرد الحصول على العبارات المطابقة في TextFragments، تحتاج إلى التكرار عبر جميع هذه العبارات وتحديثها حسب الحاجة. أخيرًا، تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة الحفظ (Save) لكائن الوثيقة (Document). يوضح لك مقطع الكود التالي كيفية استبدال النص بناءً على تعبير عادي.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // إنشاء كائن TextAbsorber للعثور على جميع أمثلة عبارة البحث المدخلة
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // مثل 1999-2000

    // تعيين خيار البحث عن النص لتحديد استخدام التعبير العادي
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // قبول الماصة للصفحة الأولى من الوثيقة
    document->get_Pages()->Accept(textFragmentAbsorber);

    // الحصول على الشظايا النصية المستخرجة في المجموعة
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // التكرار عبر الشظايا
    for (auto textFragment : textFragmentCollection) {
        // تحديث النص وخصائص أخرى
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // حفظ ملف PDF المحدث
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## استبدال الخطوط في ملف PDF موجود

يدعم Aspose.PDF لـ C++ القدرة على استبدال النص في مستند PDF. ومع ذلك، في بعض الأحيان تكون لديك متطلبات لاستبدال الخط المستخدم داخل مستند PDF فقط. لذلك بدلاً من استبدال النص، يتم استبدال الخط المستخدم فقط. يقبل أحد التحميلات الزائدة لمنشئ TextFragmentAbsorber كائن TextEditOptions كحجة ويمكننا استخدام قيمة RemoveUnusedFonts من تعداد TextEditOptions.FontReplace لتحقيق متطلباتنا. يوضح مقطع الشيفرة التالي كيفية استبدال الخط داخل مستند PDF.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // إنشاء كائن Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // البحث عن شظايا النص وتعيين خيار التحرير كإزالة الخطوط غير المستخدمة
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // قبول الماص لجميع صفحات المستند
    document->get_Pages()->Accept(textFragmentAbsorber);

    // التنقل عبر جميع شظايا النص
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // إذا كان اسم الخط ArialMT، استبدل اسم الخط بـ Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // حفظ ملف PDF المحدث
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

في مقطع الشيفرة التالي، سترى كيفية استخدام خط غير إنجليزي عند استبدال النص:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // إنشاء كائن Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // دعنا نقوم بتغيير كل كلمة "PDF" إلى نص ياباني معين بخط محدد
    // MSGothic الذي قد يكون مثبتًا في نظام التشغيل
    // أيضًا، قد يكون خطًا آخر يدعم الرموز الهيروغليفية
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // إنشاء مثيل لخيارات البحث عن النص
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // قبول الماصة لجميع صفحات المستند
    document->get_Pages()->Accept(textFragmentAbsorber);

    // الحصول على الأجزاء النصية المستخرجة في مجموعة
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // حلقة عبر الأجزاء
    for (auto textFragment : textFragmentCollection) {
        // تحديث النص وخصائص أخرى
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // حفظ المستند المحدث
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## يجب أن تقوم استبدال النص بإعادة ترتيب محتويات الصفحة تلقائيًا

يدعم Aspose.PDF لـ C++ العثور على النص واستبداله داخل ملف PDF. ومع ذلك، مؤخرًا، واجه بعض العملاء مشاكل عند استبدال النص، حيث يتم استبدال TextFragment معين بمحتوى أصغر ويظهر بعض الفراغ الإضافي في ملف PDF الناتج، أو إذا تم استبدال TextFragment بسلسلة أطول، فإن الكلمات تتداخل مع محتوى الصفحة الحالي. لذلك، كان من الضروري تقديم آلية تقوم، بعد استبدال النص داخل مستند PDF، بإعادة ترتيب محتوياته.

لتلبية السيناريوهات المذكورة أعلاه، تم تحسين Aspose.PDF لـ C++ بحيث لا تحدث مثل هذه المشاكل عند استبدال النص داخل ملف PDF. يوضح مقطع الكود التالي كيفية استبدال النص داخل ملف PDF ويجب إعادة ترتيب محتويات الصفحة تلقائيًا.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Instantiate Document object
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Create TextFragment Absorber object with regular expression
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // You also can specify the ReplaceAdjustment.WholeWordsHyphenation option to
    // wrap text on the next or current line if the current line becomes too long or
    // short after replacement:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Accept the absorber for all pages of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Replace each TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Set font of text fragment being replaced
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Set font size
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Replace the text with larger string than placeholder
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // Save resultant PDF
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## تصيير الرموز القابلة للاستبدال أثناء إنشاء PDF

الرموز القابلة للاستبدال هي رموز خاصة في سلسلة نصية يمكن استبدالها بالمحتوى المقابل في وقت التشغيل. الرموز القابلة للاستبدال المدعومة حاليًا بواسطة نموذج كائن المستند الجديد في مساحة الأسماء Aspose.PDF هي `$P`, `$p,` `\n`, `\r`. يتم استخدام `$p` و `$P` للتعامل مع ترقيم الصفحات في وقت التشغيل. يتم استبدال `$p` برقم الصفحة التي توجد فيها الفئة الحالية للفقرات. يتم استبدال `$P` بالعدد الإجمالي للصفحات في المستند. عند إضافة `TextFragment` إلى مجموعة الفقرات في مستندات PDF، فإنه لا يدعم تغذية السطر داخل النص. ومع ذلك، لإضافة نص مع تغذية السطر، يرجى استخدام `TextFragment` مع `TextParagraph`:

- استخدم "\r\n" أو Environment.NewLine في TextFragment بدلاً من "\n" واحد؛
- قم بإنشاء كائن TextParagraph. سيضيف نصًا مع تقسيم السطر؛
- أضف TextFragment مع TextParagraph.AppendLine؛
- أضف TextParagraph مع TextBuilder.AppendParagraph.

## الرموز القابلة للاستبدال في منطقة الرأس/التذييل

يمكن أيضًا وضع الرمز القابل للاستبدال داخل قسم الرأس/التذييل في ملف PDF. راجع مقتطف الشيفرة التالي لمعرفة كيفية إضافة رمز قابل للاستبدال إلى قسم التذييل.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Assign the marginInfo instance to Margin property of PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Instantiate a Text paragraph that will store the content to show as header
    auto t1 = MakeObject<TextFragment>("عنوان التقرير");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("اسم التقرير");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Create a HeaderFooter object for the section
    auto hfFoot = MakeObject<HeaderFooter>();

    // Set the HeaderFooter object to odd & even footer
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Add a text paragraph containing current page number of total number of pages
    auto t3 = MakeObject<TextFragment>("تم إنشاؤه في تاريخ الاختبار");
    auto t4 = MakeObject<TextFragment>("اسم التقرير ");
    auto t5 = MakeObject<TextFragment>("الصفحة $p من $P");

    // Instantiate a table object
    auto tab2 = MakeObject<Table>();

    // Add the table in paragraphs collection of the desired section
    hfFoot->get_Paragraphs()->Add(tab2);

    // Set with column widths of the table
    tab2->set_ColumnWidths(u"165 172 165");

    // Create rows in the table and then cells in the rows
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Set the vertical allignment of the text as center alligned
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Add the table in paragraphs collection of the desired section
    page.getParagraphs().add(table);

    // Set default cell border using BorderInfo object
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Set table border using another customized BorderInfo object
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Create rows in the table and then cells in the rows
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"عمود1");
    row1->get_Cells()->Add(u"عمود2");
    row1->get_Cells()->Add(u"عمود3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++ هو تجميع لكل مكون Java تقدمه Aspose. يتم تجميعه على أساس"
                    + CRLF
                    + u"يومي لضمان احتوائه على أحدث الإصدارات من كل مكون Java لدينا. "
                    + CRLF
                    + u"يومي لضمان احتوائه على أحدث الإصدارات من كل مكون Java لدينا. "
                    + CRLF
                    + u"باستخدام Aspose.Total for C++ يمكن للمطورين إنشاء مجموعة واسعة من التطبيقات.");
            else
                c1 = row->get_Cells()->Add(u"عنصر1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## إزالة كل النص من مستند PDF

### إزالة كل النص باستخدام المشغلين

في بعض عمليات النص، تحتاج إلى إزالة كل النص من مستند PDF، وللقيام بذلك، تحتاج عادةً إلى تعيين النص الموجود كقيمة سلسلة فارغة. الحقيقة هي أن تغيير النص لمجموعة من أجزاء النص يسبب عددًا من العمليات للتحقق وضبط موضع النص. وهي مطلوبة في نصوص تحرير النص. تكمن الصعوبة في حقيقة أنك لا تستطيع تحديد عدد أجزاء النص التي سيتم حذفها في النص حيث يتم معالجتها في الحلقة.

لذلك، نوصي باستخدام نهج مختلف لسيناريو إزالة كل النص من صفحات PDF.

يوضح مقتطف التعليمات البرمجية التالي كيفية حل هذه المهمة بسرعة.

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // قم بالمرور على كل صفحات مستند PDF
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // حدد كل النص على الصفحة
        page->get_Contents()->Accept(operatorSelector);
        // حذف كل النص
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // حفظ المستند
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```
---
title: العمل مع الإجراءات في PDF
linktitle: الإجراءات
type: docs
weight: 20
url: /cpp/actions/
description: يشرح هذا القسم كيفية إضافة إجراءات إلى الوثيقة وحقول النموذج برمجيًا باستخدام C++.
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة رابط تشعبي في ملف PDF

تعتبر مستندات PDF وسيلة رائعة لمشاركة المعلومات. فهي سهلة القراءة والتحرير والتوزيع. ومع ذلك، يمكن أن يكون إنشاء الروابط في مستند PDF تحديًا. دعونا نوضح لك كيف.

من الممكن إضافة روابط تشعبية إلى ملفات PDF، إما للسماح للقراء بالتنقل إلى جزء آخر من PDF، أو إلى محتوى خارجي.

على سبيل المثال، قد ترغب في إضافة جدول محتويات قابل للنقر إلى كتبك الإلكترونية، أو الاستشهاد بمصادر خارجية لمقالك، أو التنقل بسرعة بالقارئ إلى صفحة مختلفة على الموقع للحصول على مزيد من المعلومات حول موضوع ما.

لإنشاء روابط تشعبية ببضع نقرات، اتبع هذه الخطوات البسيطة:

1. إنشاء كائن فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. احصل على فئة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) التي تريد إضافة الرابط إليها.
1. أنشئ كائن [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) باستخدام كائنات Page و [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/). يُستخدم كائن المستطيل لتحديد الموقع على الصفحة حيث يجب إضافة الرابط.
1. عيّن خاصية Action إلى كائن [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) الذي يحدد موقع URI البعيد.
1. لعرض نص الارتباط التشعبي، أضف سلسلة نصية في موقع مشابه للمكان الذي وُضِع فيه كائن [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation).
1. لإضافة نص حر:

- قم بإنشاء كائن [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation). 
 كما يقبل كائنات Page وRectangle كمعامل، لذلك من الممكن توفير نفس القيم كما هو محدد ضد منشئ LinkAnnotation.
- باستخدام خاصية Contents الخاصة بكائن [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation)، حدد السلسلة التي يجب عرضها في ملف PDF الناتج.
- بشكل اختياري، قم بتعيين عرض الحدود لكلا الكائنين [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) وFreeTextAnnotation إلى 0 حتى لا يظهروا في مستند PDF.
- بمجرد تعريف كائنات [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) و[FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation)، أضف هذه الروابط إلى مجموعة Annotations الخاصة بكائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

- أخيراً، احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
```
المقتطف البرمجي التالي يوضح لك كيفية إضافة ارتباط تشعبي إلى ملف PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// افتح المستند

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// أنشئ الرابط

auto page = document->get_Pages()->idx_get(1);

// أنشئ كائن LinkAnnotation

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// أنشئ كائن border لـ LinkAnnotation

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// تعيين قيمة عرض الحدود إلى 0

border->set_Width(0);

// تعيين الحدود لـ LinkAnnotation

link->set_Border(border);

// تحديد نوع الرابط كـ remote URI

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// إضافة الرابط التشعبي إلى مجموعة التعليقات التوضيحية للصفحة الأولى من ملف PDF

page->get_Annotations()->Add(link);


// أنشئ التعليق التوضيحي للنص الحر

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// السلسلة النصية التي ستضاف كنص حر

textAnnotation->set_Contents(u"Link to Aspose website");

// تعيين الحدود للتعليق التوضيحي للنص الحر

textAnnotation->set_Border(border);

// إضافة التعليق التوضيحي للنص الحر إلى مجموعة التعليقات التوضيحية للصفحة الأولى من المستند

page->get_Annotations()->Add(textAnnotation);


// حفظ المستند المحدث

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## إنشاء رابط تشعبي للصفحات في نفس ملف PDF

يوفر Aspose.PDF لـ C++ ميزة رائعة لإنشاء ملفات PDF وكذلك التلاعب بها. كما يقدم ميزة إضافة روابط لصفحات PDF ويمكن أن يكون الرابط إما لتوجيه إلى صفحات في ملف PDF آخر، أو عنوان URL على الويب، أو رابط لتشغيل تطبيق أو حتى رابط لصفحات في نفس ملف PDF. لإضافة روابط تشعبية محلية (روابط لصفحات في نفس ملف PDF)، تم إضافة فئة باسم [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) إلى مساحة الأسماء Aspose.PDF وهذه الفئة تحتوي على خاصية باسم TargetPageNumber، والتي تُستخدم لتحديد الصفحة المستهدفة/وجهة الرابط التشعبي.

لإضافة الرابط التشعبي المحلي، نحتاج إلى إنشاء TextFragment بحيث يمكن ربط الرابط بـ TextFragment. The [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) class has a property named Hyperlink which is used to associate LocalHyperlink instance. The following code snippet shows the steps to accomplish this requirement.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Create Document instance

auto document = MakeObject<Document>();


// Add page to pages collection of PDF file

auto page = document->get_Pages()->Add();


// Create Text Fragment instance

auto text = MakeObject<TextFragment>(u"رابط اختبار رقم الصفحة إلى الصفحة 2");


// Create local hyperlink instance

auto link = MakeObject<LocalHyperlink>();


// Set target page for link instance

link->set_TargetPageNumber(2);


// Set TextFragment hyperlink

text->set_Hyperlink(link);


// Add text to paragraphs collection of Page

page->get_Paragraphs()->Add(text);


// Create new TextFragment instance

text = new TextFragment(u"رابط اختبار رقم الصفحة إلى الصفحة 1");


// TextFragment should be added over new page

text->set_IsInNewPage(true);


// Create another local hyperlink instance

link = new LocalHyperlink();


// Set Target page for second hyperlink

link->set_TargetPageNumber(1);


// Set link for second TextFragment

text->set_Hyperlink(link);


// Add text to paragraphs collection of page object

page->get_Paragraphs()->Add(text);


// Save updated document

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## الحصول على وجهة الرابط التشعبي في PDF (URL)

يتم تمثيل الروابط كملاحظات توضيحية في ملف PDF ويمكن إضافتها أو تحديثها أو حذفها. Aspose.PDF for C++ يدعم أيضًا الحصول على الوجهة (URL) للرابط التشعبي في ملف PDF.

للحصول على URL الرابط:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. الحصول على [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) التي تريد استخراج الروابط منها.
1. استخدام فئة [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) لاستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) من الصفحة المحددة.
1. تمرير كائن [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) إلى طريقة Accept لكائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). احصل على جميع تعليقات الرابط المحددة في كائن IList باستخدام خاصية Selected لكائن [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).
1. أخيرًا، استخراج Action الخاص بـ LinkAnnotation كـ GoToURIAction.

يوضح مقتطف الشيفرة التالي كيفية الحصول على وجهات الارتباط التشعبي (URL) من ملف PDF.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// Extract actions

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// Iterate through individual item inside list

if (list->get_Count() == 0)


Console::WriteLine(u"No Hyperlinks found...");

else {


// Loop through all the bookmarks


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// Print the destination URL




Console::WriteLine(u"Destination: " + action->get_URI());



}


}

} // end else
}
```
## الحصول على نص الارتباط التشعبي

يتكون الارتباط التشعبي من جزئين: النص الذي يظهر في المستند، وعنوان URL الوجهة. في بعض الحالات، يكون النص هو ما نحتاجه بدلاً من عنوان URL.

يتم تمثيل النص والتعليقات التوضيحية/الإجراءات في ملف PDF بواسطة كيانات مختلفة. النص الموجود على الصفحة هو مجرد مجموعة من الكلمات والأحرف، بينما تضيف التعليقات التوضيحية بعض التفاعلية مثل تلك الموجودة في الارتباط التشعبي.

للعثور على محتوى URL، تحتاج إلى العمل مع كل من التعليقات التوضيحية والنص. كائن [Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) لا يحتوي على النص بحد ذاته ولكنه يقع تحت النص في الصفحة. لذا للحصول على النص، تقدم التعليقات التوضيحية حدود URL، بينما يعطي كائن النص محتويات URL. يرجى الاطلاع على مقتطف الشيفرة التالي.

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// Extract actions

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// Print the URL of each Link Annotation



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// Print the text associated with hyperlink



Console::WriteLine(extractedText);


}

}
}
```

## إزالة إجراء فتح المستند من ملف PDF

[كيفية تحديد صفحة PDF عند عرض المستند](#how-to-specify-pdf-page-when-viewing-document) يشرح كيفية إرشاد المستند ليفتح على صفحة مختلفة عن الأولى. عند تجميع عدة مستندات، وإذا كان لأحدها أو أكثر إجراء GoTo محدد، فمن المحتمل أنك ترغب في إزالته. على سبيل المثال، عند دمج مستندين وكان للثاني إجراء GoTo يأخذك إلى الصفحة الثانية، فإن المستند الناتج سيفتح على الصفحة الثانية من المستند الثاني بدلاً من الصفحة الأولى من المستند المُدمج. لتجنب هذا السلوك، قم بإزالة أمر فتح الإجراء.

لإزالة إجراء فتح:

1. قم بتعيين خاصية [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) إلى null.
1. احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن Document.

يوضح مقتطف الشيفرة التالي كيفية إزالة إجراء فتح المستند من ملف PDF.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// فتح المستند

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// إزالة إجراء فتح المستند

document->set_OpenAction(nullptr);


// حفظ المستند المحدث

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## كيفية تحديد صفحة PDF عند عرض المستند {#how-to-specify-pdf-page-when-viewing-document}

عند عرض ملفات PDF في عارض PDF مثل Adobe Reader، تفتح الملفات عادةً في الصفحة الأولى. ومع ذلك، من الممكن ضبط الملف ليفتح في صفحة مختلفة.

تسمح لك فئة 'XYZExplicitDestination' بتحديد صفحة في ملف PDF التي ترغب في فتحها. عند تمرير قيمة كائن GoToAction إلى خاصية OpenAction لفئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)، يفتح المستند في الصفحة المحددة مقابل كائن XYZExplicitDestination. يوضح مقتطف الشيفرة التالي كيفية تحديد صفحة كإجراء فتح المستند.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// تحميل ملف PDF

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// الحصول على مثيل الصفحة الثانية من المستند

auto page2 = document->get_Pages()->idx_get(2);

// إنشاء المتغير لضبط عامل التكبير للصفحة المستهدفة

double zoom = 1;

// إنشاء مثيل GoToAction

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// الانتقال إلى الصفحة 2

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// ضبط إجراء فتح المستند

document->set_OpenAction(action);

// حفظ المستند المحدث

document->Save(_dataDir + u"goto2page_out.pdf");
}
```
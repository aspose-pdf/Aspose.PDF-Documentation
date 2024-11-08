---
title: Change PDF Page Size Programmatically 
linktitle: Change PDF Page Size
type: docs
weight: 40
url: /ar/cpp/change-page-size/
description: تغيير حجم الصفحة من ملف PDF الخاص بك باستخدام مكتبة C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF هو تنسيق قابل للطباعة ذو تخطيط ثابت، ولهذا السبب أصبح شائعًا في الحياة التجارية.

ومع ذلك، قد تكون لديك مهام تحتاج فيها إلى تغيير حجم مستند PDF الخاص بك لأن حجم الصفحة أكبر من حجم الورق. ولكن كيف؟

لا تقلق. في هذه الصفحة، ستجد طريقة لحل مهمتك.

لكن أولاً، دعونا نتذكر أن هناك سلسلة أحجام للصفحات.

هناك سلسلتين من أحجام الصفحات معتمدتين على نطاق واسع في العالم.
بالطبع، هناك العديد من التنسيقات، ولكن هناك الأكثر استخدامًا.
الأول هو أحجام الورق وفقًا لمعايير ISO. 
سلسلة A4 تُستخدم للطباعة القياسية واللوازم المكتبية. يُستخدم حجم الورق Letter للإعلانات، واللوحات الجدارية، وما إلى ذلك. تبنت الولايات المتحدة وكندا وجزء من المكسيك سلسلة حجم الصفحة الثانية، وهم اليوم الدول الصناعية الوحيدة التي لا تزال لم تُستخدم فيها أحجام الورق القياسية ISO بشكل واسع.

الآن لنرى كيف تحثك Aspose.PDF على تغيير حجم الصفحة باستخدام مكتبة C++.

## تغيير حجم صفحة PDF

يسمح لك Aspose.PDF لـ C++ بتغيير حجم صفحة PDF بخطوط بسيطة من التعليمات البرمجية في تطبيقات C++ الخاصة بك. يشرح هذا الموضوع كيفية تحديث/تغيير أبعاد الصفحة (الحجم) لملف PDF موجود.

تحتوي فئة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) على طريقة SetPageSize(...) التي تتيح لك تعيين حجم الصفحة. يُحدث مقتطف الشيفرة أدناه أبعاد الصفحة في خطوات بسيطة:

1. تحميل ملف PDF المصدر.
1. الحصول على الصفحات في كائن [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. الحصول على صفحة معينة.
1.
``` اتصل بطريقة SetPageSize(..) لتحديث أبعادها.
1. اتصل بطريقة Save(..) الخاصة بفئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) لإنشاء ملف PDF بأبعاد الصفحة المحدثة.

يظهر مقتطف الشيفرة التالي كيفية تغيير أبعاد صفحة PDF إلى حجم A4.

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // احصل على صفحة معينة
    auto pdfPage = document->get_Pages()->idx_get(1);

    // حدد حجم الصفحة كـ A4 (11.7 x 8.3 بوصة) وفي Aspose.Pdf، 1 بوصة = 72 نقطة
    // لذلك ستكون أبعاد A4 بالنقاط (842.4, 597.6)
    pdfPage->SetPageSize(597.6, 842.4);
    // احفظ المستند المحدث
    document->Save(_dataDir + outputFileName);
}
```

## الحصول على حجم صفحة PDF

يمكنك قراءة حجم صفحة PDF لملف PDF موجود باستخدام Aspose.PDF ل С++. النص التالي يوضح كيفية قراءة أبعاد صفحات PDF باستخدام C++.

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // الحصول على صفحة معينة
    auto page = document->get_Pages()->idx_get(1);

    // الحصول على معلومات ارتفاع وعرض الصفحة
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // تدوير الصفحة بزاوية 90 درجة
    page->set_Rotate(Rotation::on90);
    // الحصول على معلومات ارتفاع وعرض الصفحة
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```
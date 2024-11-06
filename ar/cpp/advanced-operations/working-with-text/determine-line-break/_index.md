---
title: Determine Line Break in TextFragment 
linktitle: Determine Line Break
type: docs
weight: 70
url: ar/cpp/determine-line-break/
description: تعرف على كيفية تحديد فاصل السطر في TextFragment متعدد الأسطر باستخدام C++
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تتبع فواصل السطر في TextFragment متعدد الأسطر

يقدم Aspose.PDF لـ C++ تسجيل (تتبع) معالجة الخلفية (فواصل السطر) لقطع النص متعددة الأسطر في سيناريوهات إضافة النص. يمكنك استخدام طريقة [GetNotifications](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a6bb9655558affa2aa68f357a93395b12)() لـ [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) Class كما يلي، من أجل تتبع فواصل السطر في قطع النص:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void LineBreakDemo() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    for (int i = 0; i < 4; i++)
    {
        auto text = MakeObject<TextFragment>(u"Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.");
        text->get_TextState()->set_FontSize(20);
        page->get_Paragraphs()->Add(text);
    }

    document->Save(_dataDir + u"DetermineLineBreak_out.pdf");

    String notifications = page->GetNotifications();
    Console::WriteLine(notifications);
    System::IO::File::WriteAllText(_dataDir + u"notifications_out.txt",notifications);
}
```
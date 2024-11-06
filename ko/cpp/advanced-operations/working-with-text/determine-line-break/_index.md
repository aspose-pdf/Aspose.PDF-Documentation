---
title: Determine Line Break in TextFragment 
linktitle: Determine Line Break
type: docs
weight: 70
url: ko/cpp/determine-line-break/
description: C++를 사용하여 여러 줄의 TextFragment에서 줄 바꿈을 결정하는 방법에 대해 알아보세요.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 여러 줄 TextFragment의 줄 바꿈 추적

Aspose.PDF for C++는 텍스트 추가 시나리오에서 여러 줄의 텍스트 조각의 줄 바꿈을 백그라운드 처리(추적)하는 로그 기능을 제공합니다. 텍스트 조각의 줄 바꿈을 추적하려면 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스의 [GetNotifications](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a6bb9655558affa2aa68f357a93395b12)() 메서드를 다음과 같이 사용할 수 있습니다:

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
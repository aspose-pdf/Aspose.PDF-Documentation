---
title: テキストフラグメントにおける改行の判定
linktitle: 改行の判定
type: docs
weight: 70
url: /ja/cpp/determine-line-break/
description: C++を使用してマルチラインテキストフラグメントの改行を判定する方法について学ぶ
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## マルチラインテキストフラグメントの改行を追跡

Aspose.PDF for C++は、テキスト追加シナリオにおけるマルチラインテキストフラグメントのバックグラウンド処理（改行）のログ（追跡）を提供します。テキストフラグメントの改行を追跡するために、[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) クラスの [GetNotifications](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a6bb9655558affa2aa68f357a93395b12)() メソッドを次のように使用できます：

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
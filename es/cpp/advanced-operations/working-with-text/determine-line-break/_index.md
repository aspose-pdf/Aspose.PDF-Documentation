---
title: Determinar el Salto de Línea en TextFragment 
linktitle: Determinar el Salto de Línea
type: docs
weight: 70
url: es/cpp/determine-line-break/
description: Aprende más sobre cómo determinar un salto de línea de un TextFragment de varias líneas usando C++
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Seguimiento de la Ruptura de Línea de un TextFragment de Varias Líneas

Aspose.PDF para C++ ofrece el registro (seguimiento) del procesamiento en segundo plano (ruptura de línea) de fragmentos de texto de varias líneas en escenarios de adición de texto. Puedes usar el método [GetNotifications](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a6bb9655558affa2aa68f357a93395b12)() de la Clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) como sigue, para rastrear la ruptura de línea de un fragmento de texto:

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
---
title: Установить Имя Шрифта По Умолчанию с использованием C++
linktitle: Установить Имя Шрифта По Умолчанию
type: docs
weight: 90
url: /ru/cpp/set-default-font-name/
description: Этот раздел описывает, как установить имя шрифта по умолчанию с использованием библиотеки C++.
lastmod: "2021-12-18"
---

**Aspose.PDF для C++** API позволяет установить имя шрифта по умолчанию, когда шрифт недоступен в документе. Вы можете использовать свойство DefaultFontName класса RenderingOptions, чтобы задать имя шрифта по умолчанию. В случае, если DefaultFontName установлен в `nullptr`, будет использован шрифт **Times New Roman**. Следующий фрагмент кода показывает, как установить имя шрифта по умолчанию при сохранении PDF в изображение:

```cpp
void WorkingWithImages::ExampleSetDefaultFontName()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    auto imageStream = System::IO::File::OpenWrite(_dataDir + u"SetDefaultFontName.png");

    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);
    auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    auto ro = MakeObject<RenderingOptions>();
    ro->set_DefaultFontName(u"Arial");
    pngDevice->set_RenderingOptions(ro);
    pngDevice->Process(document->get_Pages()->idx_get(1), imageStream);
}
```
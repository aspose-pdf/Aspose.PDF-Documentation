---
title: Definir Nome de Fonte Padrão usando C++
linktitle: Definir Nome de Fonte Padrão
type: docs
weight: 90
url: pt/cpp/set-default-font-name/
description: Esta seção descreve como definir o nome da fonte padrão usando a biblioteca C++.
lastmod: "2021-12-18"
---

A API **Aspose.PDF for C++** permite definir um nome de fonte padrão quando uma fonte não está disponível no documento. Você pode usar a propriedade DefaultFontName da classe RenderingOptions para definir o nome da fonte padrão. Caso o DefaultFontName seja definido como `nullptr`, a fonte **Times New Roman** será usada. O trecho de código a seguir mostra como definir um nome de fonte padrão ao salvar um PDF em uma imagem:

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
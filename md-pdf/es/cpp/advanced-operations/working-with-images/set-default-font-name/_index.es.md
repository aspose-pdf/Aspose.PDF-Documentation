---
title: Establecer Nombre de Fuente Predeterminada usando C++
linktitle: Establecer Nombre de Fuente Predeterminada
type: docs
weight: 90
url: /cpp/set-default-font-name/
description: Esta sección describe cómo establecer el nombre de fuente predeterminado usando la biblioteca C++.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** API te permite establecer un nombre de fuente predeterminado cuando una fuente no está disponible en el documento. Puedes usar la propiedad DefaultFontName de la clase RenderingOptions para establecer el nombre de fuente predeterminado. En caso de que DefaultFontName esté configurado como `nullptr`, se usará la fuente **Times New Roman**. El siguiente fragmento de código muestra cómo establecer un nombre de fuente predeterminado al guardar un PDF en una imagen:

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
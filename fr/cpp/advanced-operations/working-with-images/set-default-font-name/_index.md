---
title: Définir le Nom de Police par Défaut en utilisant C++
linktitle: Définir le Nom de Police par Défaut
type: docs
weight: 90
url: /fr/cpp/set-default-font-name/
description: Cette section décrit comment définir le nom de police par défaut en utilisant la bibliothèque C++.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** API vous permet de définir un nom de police par défaut lorsqu'une police n'est pas disponible dans le document. Vous pouvez utiliser la propriété DefaultFontName de la classe RenderingOptions pour définir le nom de police par défaut. Dans le cas où DefaultFontName est défini sur `nullptr`, la police **Times New Roman** sera utilisée. L'extrait de code suivant montre comment définir un nom de police par défaut lors de l'enregistrement d'un PDF en image :

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
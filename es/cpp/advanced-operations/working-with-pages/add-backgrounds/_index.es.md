---
title: Añadir fondo al PDF con C++
linktitle: Añadir fondos
type: docs
weight: 110
url: /cpp/add-backgrounds/
descriptions: Agrega una imagen de fondo a tu archivo PDF con C++. Usa el objeto BackgroundArtifact.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Agregar un fondo a los archivos PDF ayuda a mejorar la legibilidad general del documento. El contenido en el PDF es más atractivo y los lectores se darán cuenta si tienes una buena apariencia del documento. El fondo también se puede usar para resaltar los aspectos destacados del PDF.

Las imágenes de fondo se pueden usar para agregar una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF para C++, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) se puede usar para agregar una imagen de fondo a un objeto página.

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a las páginas PDF usando el objeto BackgroundArtifact con C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // Crear un nuevo objeto Document
    auto document = MakeObject<Document>();

    // Añadir una nueva página al objeto documento
    auto page = document->get_Pages()->Add();

    // Crear un objeto Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Especificar la imagen para el objeto backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Añadir backgroundartifact a la colección de artefactos de la página
    page->get_Artifacts()->Add(background);

    // Guardar el documento
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```
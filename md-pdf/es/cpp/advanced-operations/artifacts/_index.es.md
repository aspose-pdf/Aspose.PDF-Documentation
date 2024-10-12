---
title: Trabajando con Artefactos en C++
linktitle: Trabajando con Artefactos
type: docs
weight: 110
url: /cpp/artifacts/
description: Esta página describe cómo trabajar con la clase Artifact usando Aspose.PDF para C++. Los fragmentos de código muestran cómo agregar una imagen de fondo a las páginas PDF y cómo obtener cada marca de agua en la primera página de un archivo PDF.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ¿Cómo obtener una marca de agua en PDF?

**¿Qué es un artefacto en PDF?**

Según la referencia PDF / UA ISO, el contenido que no es importante o no aparece en el fondo no lleva información relevante, debe marcarse como un artefacto para que las tecnologías de asistencia puedan ignorarlo.
Si los artefactos no pueden identificarse en el programa para crear, esto debe hacerse manualmente usando Aspose.PDF para C++.

La clase [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) contiene las siguientes propiedades:

- **Artifact.Type** – obtiene el tipo de artefacto (admite valores de la enumeración Artifact.ArtifactType donde los valores incluyen Fondo, Diseño, Página, Paginación e Indefinido).
- **Artifact.Subtype** – obtiene el subtipo de artefacto (admite los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Fondo, Pie de página, Encabezado, Indefinido, Marca de agua).

{{% alert color="primary" %}}

Tenga en cuenta que las marcas de agua creadas con Adobe Acrobat tienen el tipo Paginación y el subtipo Marca de agua.

{{% /alert %}}

- **Artifact.Contents** – Obtiene una colección de operadores internos de artefactos. Su tipo compatible es System.Collections.ICollection.
- **Artifact.Form** – Obtiene un XForm de un artefacto (si se utiliza XForm). Las marcas de agua, encabezados y pies de página contienen XForm que muestra todos los contenidos del artefacto.
- **Artifact.Image** – Obtiene la imagen de un artefacto (si hay una imagen, de lo contrario es nulo).
- **Artifact.Text** – Obtiene el texto de un artefacto.
- **Artifact.Rectangle** – Obtiene la posición de un artefacto en la página.
- **Artifact.Rotation** – Obtiene la rotación de un artefacto (en grados, un valor positivo indica rotación en sentido antihorario).
- **Artifact.Opacity** – Obtiene la opacidad de un artefacto. Valores posibles están en el rango de 0...1, donde 1 es completamente opaco.

Para un ejemplo de trabajo con artefactos en un archivo PDF, tomemos una marca de agua.

Una marca de agua creada con soporte para Adobe Acrobat se refiere a un artefacto (como se describe en 14.8.2.2 Contenido Presente y Artefactos de Especificación PDF). Para trabajar con artefactos, Aspose.PDF contiene 2 clases:
[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) y [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Para obtener todos los artefactos en una página particular, la clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) tiene la propiedad Artifacts. Este tema muestra cómo trabajar con el artefacto de marca de agua en archivos PDF.

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF con C++:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
Background images can be used to add watermarks or exclusive designs to PDF documents. Aspose.PDF for C++ utiliza la clase [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) para agregar una imagen de fondo al objeto de página.

El siguiente fragmento de código te muestra cómo agregar una imagen de fondo a las páginas PDF con el objeto BackgroundArtifact:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>();

    // Añadir un MakeObject<page al objeto documento
    auto page = pdfDocument->get_Pages()->Add();

    // Crear objeto de artefacto de fondo
    auto background = MakeObject<BackgroundArtifact>();

    // Especificar la imagen para el objeto de artefacto de fondo
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Añadir BackgroundArtifact a la colección de artefactos de la página
    page->get_Artifacts()->Add(background);

    // Guardar PDF modificado
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### Muestras de Programación: Obtener Marcas de Agua

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // Iterar y obtener subtipo, texto y ubicación del artefacto
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### Muestras de Programación: Contar Artefactos de un Tipo Particular

Para calcular el conteo total de artefactos de un tipo particular (por ejemplo, el número total de marcas de agua), use el siguiente código:

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // Si el tipo de artefacto es marca de agua, incrementar el contador
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"Page contains {0} watermarks", count);
}
```
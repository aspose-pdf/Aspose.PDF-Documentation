---
title: Agregar marca de agua a PDF usando C++
linktitle: Agregar marca de agua
type: docs
weight: 90
url: /cpp/add-watermarks/
description: Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs usando programáticamente el C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Una marca de agua es una imagen translúcida que usualmente contiene un logotipo o sello para identificar quién creó el documento o imagen.

**Aspose.PDF para C++** permite agregar marcas de agua a su documento PDF usando la clase Artifact. Por favor, consulte este artículo para resolver su tarea.

Una marca de agua creada con Adobe Acrobat se llama un artefacto (como se describe en 14.8.2.2 Contenido Real y Artefactos de la especificación PDF). Para trabajar con artefactos, Aspose.PDF tiene dos clases: [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) y [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Para obtener todos los artefactos en una página particular, la clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) tiene la propiedad Artifacts. Este tema explica cómo trabajar con artefactos en archivos PDF.

## Trabajando con Artefactos

La clase [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) contiene las siguientes propiedades:

**Artifact.Type** – obtiene el tipo de artefacto (soporta valores de la enumeración Artifact.ArtifactType donde los valores incluyen Fondo, Diseño, Página, Paginación e Indefinido).  
**Artifact.Subtype** – obtiene el subtipo de artefacto (soporta los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Fondo, Pie de página, Encabezado, Indefinido, Marca de agua).

{{% alert color="primary" %}}

Tenga en cuenta que las marcas de agua creadas con Adobe Acrobat tienen el tipo Paginación y subtipo Marca de agua.

{{% /alert %}}

**Artifact.Contents** – Obtiene una colección de operadores internos de artefactos. Su tipo compatible es System.Collections.ICollection.  
**Artifact.Form** – Obtiene el XForm de un artefacto (si se utiliza XForm). Los artefactos de marca de agua, encabezado y pie de página contienen XForm que muestra todos los contenidos del artefacto.

**Artifact.Image** – Obtiene la imagen de un artefacto (si hay una imagen presente, de lo contrario null).**Artifact.Text** – Obtiene el texto de un artefacto.  
**Artifact.Rectangle** – Obtiene la posición de un artefacto en la página.  
**Artifact.Rotation** – Obtiene la rotación de un artefacto (en grados, un valor positivo indica rotación en sentido antihorario).  
**Artifact.Opacity** – Obtiene la opacidad de un artefacto. Los valores posibles están en el rango de 0…1, donde 1 es completamente opaco.

## Ejemplos de Programación: Cómo Añadir Marca de Agua en Archivos PDF

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF con C++.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```
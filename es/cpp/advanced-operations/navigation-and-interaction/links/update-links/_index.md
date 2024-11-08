---
title: Actualizar Enlaces en PDF 
linktitle: Actualizar Enlaces
type: docs
weight: 20
url: /es/cpp/update-links/
description: Actualizar enlaces en PDF programáticamente con Aspose.PDF para C++. Esta guía trata sobre cómo actualizar enlaces en un archivo PDF. 
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Actualizar Enlaces en un Archivo PDF

Como se discutió en Agregar Hipervínculo en un Archivo PDF, la clase [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) permite agregar enlaces en un archivo PDF. También hay una clase similar utilizada para obtener enlaces existentes desde archivos PDF. Úsela si necesita actualizar un enlace existente. Para actualizar un enlace existente:

1. Cargue un archivo PDF.
1. Vaya a una página específica en el archivo PDF.
1. Especifique el destino del enlace usando la propiedad Destination del objeto [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action).
1. La página de destino se especifica usando el constructor [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination).

### Establecer el Destino del Enlace a una Página en el Mismo Documento

El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino en la segunda página del documento.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modificación del enlace: cambiar destino del enlace
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // Especificar el destino para el objeto enlace
    // Representa un destino explícito que muestra la página con las coordenadas (izquierda, arriba) posicionadas en la esquina superior izquierda de
    // la ventana y los contenidos de la página ampliados por el factor de zoom.
    // El 1er parámetro es el número de página de destino.
    // El 2do es la coordenada izquierda
    // El 3ro es la coordenada superior
    // El 4to argumento es el factor de zoom al mostrar la página respectiva. Usar 2 significa que la página se mostrará con un zoom del 200%
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // Guardar el documento con el enlace actualizado
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### Establecer Destino del Enlace a una Dirección Web

Para actualizar el hipervínculo de modo que apunte a una dirección web, instancie el objeto [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) y páselo a la propiedad Action de LinkAnnotation. El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino a una dirección web.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // Cargar el archivo PDF
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modificación del enlace: cambiar la acción del enlace y establecer el destino como dirección web
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // Guardar el documento con el enlace actualizado
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Establecer el Destino del Enlace a Otro Archivo PDF

El siguiente fragmento de código muestra cómo actualizar un enlace en un archivo PDF y establecer su destino en otro archivo PDF.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // Cargar el archivo PDF
    String _dataDir("C:\\Samples\\");
    // Crear instancia de Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modificar enlace: cambiar la acción del enlace y establecer el destino como dirección web
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // La siguiente línea actualiza el destino, no actualiza el archivo
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // La siguiente línea actualiza el archivo
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // Guardar el documento con el enlace actualizado
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Actualizar el color del texto de LinkAnnotation

La anotación de enlace no contiene texto. En su lugar, el texto se coloca en el contenido de la página debajo de la anotación. Por lo tanto, para cambiar el color del texto, reemplace el color del texto de la página en lugar de intentar cambiar el color de la anotación. El siguiente fragmento de código muestra cómo actualizar el color de la anotación de enlace en un archivo PDF.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // Cargar el archivo PDF
    String _dataDir("C:\\Samples\\");

    // Crear instancia de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Añadir página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // Buscar el texto debajo de la anotación
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // Cambiar el color del texto.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // Guardar el documento con el enlace actualizado
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```
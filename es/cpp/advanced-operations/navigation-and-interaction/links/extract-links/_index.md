```
---
title: Extraer Enlaces del Archivo PDF 
linktitle: Extraer Enlaces
type: docs
weight: 30
url: /es/cpp/extract-links/
description: Extraer enlaces de PDF con C#. Este tema te explica cómo extraer enlaces usando la clase AnnotationSelector. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Enlaces del Archivo PDF

Los enlaces se representan como anotaciones en un archivo PDF, por lo que para extraer enlaces, extraiga todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).

1. Cree un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Obtenga la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) de la que desea extraer enlaces.
1.
``` Usa la clase [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) para extraer todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) de la página especificada. 
1. Pasa el objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) al método Accept del objeto Page. 
1. Obtén todas las anotaciones de enlace seleccionadas en un objeto IList usando la propiedad Selected del objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

El siguiente fragmento de código te muestra cómo extraer enlaces de un archivo PDF.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // Cargar el archivo PDF
    String _dataDir("C:\\Samples\\");

    // Crear instancia de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Anotación localizada: {0}", annot->get_Rect());
    }
}
```
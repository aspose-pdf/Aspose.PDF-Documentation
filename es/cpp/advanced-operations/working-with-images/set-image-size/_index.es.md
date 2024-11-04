---
title: Establecer Tamaño de Imagen usando C++
linktitle: Establecer Tamaño de Imagen
type: docs
weight: 80
url: /cpp/set-image-size/
description: Esta sección describe cómo establecer el tamaño de imagen en un archivo PDF usando la biblioteca C++.
lastmod: "2021-12-18"
---

Es posible establecer el tamaño de una imagen que se está añadiendo a un archivo PDF. Para establecer el tamaño, puedes usar las propiedades [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) y [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) de la [Clase Aspose.Pdf.Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

El siguiente fragmento de código demuestra cómo establecer el tamaño de una imagen:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Instanciar objeto Document
    auto document = MakeObject<Document>();
    // añadir página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();
    // Crear una instancia de imagen
    auto img = MakeObject<Image>();
    // Establecer Ancho y Alto de Imagen en Puntos
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // Establecer tipo de imagen como SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // Ruta para el archivo fuente
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // Establecer propiedades de la página
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // guardar archivo PDF resultante
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```
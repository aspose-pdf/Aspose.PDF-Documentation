---
title: Recortar Páginas de PDF programáticamente C++
linktitle: Recortar Páginas
type: docs
weight: 80
url: /es/cpp/crop-pages/
description: Puedes obtener propiedades de página, como el ancho, alto, bleed-, crop- y trimbox usando Aspose.PDF para C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Propiedades de Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, alto, bleed-, crop- y trimbox. Aspose.PDF te permite acceder a estas propiedades.

- **Caja de medios**: La caja de medios es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, Carta US, etc.) seleccionado cuando el documento fue impreso a PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Caja de sangrado**: Si el documento tiene sangrado, el PDF también tendrá una caja de sangrado. Bleed es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y corte al tamaño ("recortado"), la tinta llegará hasta el borde de la página. Incluso si la página se corta mal - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: El trim box indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: El art box es la caja dibujada alrededor del contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: El crop box es el tamaño de "página" en el que se muestra su documento PDF en Adobe Acrobat. En vista normal, solo se muestran los contenidos del crop box en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (comúnmente rectángulo visible) del MediaBox y DropBox. La imagen a continuación ilustra estas propiedades. Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

El fragmento a continuación muestra cómo recortar la página:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Abrir documento fuente
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Crear nuevo Rectángulo Box
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox(newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox(newBox);

    // Guardar documento actualizado
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

Después del cambio, la página se verá como en la Figura 2.  
![Figure 2. Cropped Page](crop_page2.png)
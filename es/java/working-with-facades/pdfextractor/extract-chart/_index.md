---
title: Extraer objetos de gráfico del documento PDF (facades)
type: docs
weight: 20
url: es/java/extract-chart-objects/
description: Esta sección explica cómo extraer objetos de gráfico de un PDF con Aspose.PDF Facades usando la clase PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer objetos de gráfico del documento PDF (facades)

El PDF permite agrupar el contenido de la página en elementos denominados **Contenido Marcado**. Adobe Acrobat los muestra como "contenedores". Los objetos de gráfico se colocan en tales objetos. Hemos introducido un nuevo método extractMarkedContentAsImages() en la clase PdfExtractor para extraer estos objetos. Este método renderiza cada **Contenido Marcado** en una imagen separada. Tenga en cuenta que no todos los gráficos están completamente colocados en un solo contenedor. Debido a esto, algunos gráficos se guardarán en imágenes separadas por partes.

Tenga en cuenta que la correcta agrupación de contenido en contenedores es responsabilidad del diseñador del documento PDF.
 Si deseas obtener gráficos con encabezado u otros objetos, debes editar/crear el documento PDF donde todo el gráfico se coloque en un contenedor.

```java

//Abrir documento

Document document = new Document("sample.pdf");

//instanciar PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Extraer objetos de gráfico como imagen en una carpeta

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```
---
title: Cambiar el Tamaño de Página de un PDF Programáticamente
linktitle: Cambiar el Tamaño de Página de un PDF
type: docs
weight: 40
url: es/cpp/change-page-size/
description: Cambia el tamaño de página de tu archivo PDF usando una biblioteca C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF es un formato imprimible de diseño estático, por eso se ha vuelto tan común en la vida empresarial.

Sin embargo, puede que tengas tareas en las que necesites cambiar el tamaño de tu documento PDF porque el tamaño de la página es más grande que el tamaño del papel. ¿Pero cómo?

No te preocupes. En esta página, encontrarás una manera de resolver tu tarea.

Pero primero, recordemos que existe la Serie de Tamaños de Página.

Hay dos series de tamaños de página ampliamente adoptadas en el mundo.
Por supuesto, hay muchos formatos, pero estos son los más comúnmente utilizados.
El primero es el Tamaño de Papel ISO. Serie A4 se utiliza para impresión y papelería estándar. El tamaño de papel Carta se utiliza para carteles, gráficos murales, etc. Estados Unidos, Canadá y en parte México adoptaron la segunda serie de tamaños de página y hoy son las únicas naciones industrializadas en las que los tamaños de papel estándar ISO aún no se utilizan ampliamente.

Ahora veamos cómo Aspose.PDF te invita a cambiar el tamaño de la página usando la biblioteca C++.

## Cambiar el Tamaño de Página del PDF

Aspose.PDF para С++ te permite cambiar el tamaño de la página PDF con simples líneas de código en tus aplicaciones С++. Este tema explica cómo actualizar/cambiar las dimensiones (tamaño) de la página de un archivo PDF existente.

La clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) contiene el método SetPageSize(...) que te permite establecer el tamaño de la página. El fragmento de código a continuación actualiza las dimensiones de la página en unos pocos pasos sencillos:

1. Cargar el archivo PDF de origen.
1. Obtener las páginas en el objeto [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. Obtener una página dada.
1. Llama al método SetPageSize(..) para actualizar sus dimensiones.
1. Llama al método Save(..) de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) para generar el archivo PDF con las dimensiones de página actualizadas.

El siguiente fragmento de código muestra cómo cambiar las dimensiones de la página PDF al tamaño A4.

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtener una página en particular
    auto pdfPage = document->get_Pages()->idx_get(1);

    // Establecer el tamaño de la página como A4 (11.7 x 8.3 in) y en Aspose.Pdf, 1 pulgada = 72 puntos
    // Entonces las dimensiones de A4 en puntos serán (842.4, 597.6)
    pdfPage->SetPageSize(597.6, 842.4);
    // Guardar el documento actualizado
    document->Save(_dataDir + outputFileName);
}
```

## Obtener el Tamaño de la Página PDF

Puedes leer el tamaño de página PDF de un archivo PDF existente usando Aspose.PDF para С++. El siguiente ejemplo de código muestra cómo leer las dimensiones de la página PDF usando C++.

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtener una página en particular
    auto page = document->get_Pages()->idx_get(1);

    // Obtener información de altura y ancho de la página
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // Rotar página a un ángulo de 90 grados
    page->set_Rotate(Rotation::on90);
    // Obtener información de altura y ancho de la página
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```
---
title: Obtener y establecer propiedades de página
linktitle: Obtener y establecer propiedades de página
type: docs
url: /es/go-cpp/get-and-set-page-properties/
description: Aprenda cómo obtener y establecer propiedades de página para documentos PDF usando Aspose.PDF for Go, lo que permite un formato de documento personalizado.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Obtener y establecer propiedades de página con Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ proporciona funciones completas para obtener y establecer propiedades de página en documentos PDF, lo que permite a los desarrolladores acceder y modificar varios atributos de página como el tamaño, la rotación, los márgenes y los metadatos. Estas capacidades permiten un control preciso sobre el diseño y la apariencia del documento para cumplir con requisitos específicos de la aplicación. La biblioteca garantiza una personalización y optimización sin problemas de las páginas PDF. La documentación ofrece guías detalladas y ejemplos de código para ayudar a los desarrolladores a recuperar y actualizar eficazmente las propiedades de página dentro de sus aplicaciones.
SoftwareApplication: go-cpp
---

Aspose.PDF for Go le permite leer y establecer propiedades de páginas en un archivo PDF. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre propiedades de página PDF como el color y establecer propiedades de página.

## Obtener número de páginas en un archivo PDF

Al trabajar con documentos, a menudo deseas saber cuántas páginas contienen. Con Aspose.PDF esto no requiere más de dos líneas de código.

**Aspose.PDF for Go via C++** permite contar Pages con [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) función.

El siguiente fragmento de código está diseñado para abrir un documento PDF, obtener su recuento de páginas y luego imprimir el resultado.

El método [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) se llama para obtener el número total de páginas en el documento PDF. Esto es útil para tareas que necesitan conocer la longitud del documento, como al extraer páginas específicas o realizar operaciones en todas las páginas. Este método es una forma directa de consultar la estructura del documento.’

Para obtener el número de páginas en un archivo PDF:

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)

      }
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Establecer tamaño de página

En este ejemplo el método pdf.PageSetSize() cambia el tamaño de la primera página del documento PDF. La constante PageSizeA1 asegura que la primera página se establezca al tamaño de papel A1. Esto es útil al convertir documentos a un formato estandarizado o al garantizar que contenido específico encaje correctamente en las páginas.

1. Abriendo el documento PDF con [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) método.
1. Estableciendo el tamaño de página con [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) función.
1. Guardando el documento usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) método.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

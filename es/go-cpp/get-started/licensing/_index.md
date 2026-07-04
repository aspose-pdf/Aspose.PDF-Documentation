---
title: Licencia Aspose PDF
linktitle: Licenciamiento y limitaciones
type: docs
weight: 90
url: /es/go-cpp/licensing/
description: Aspose. PDF for Go invita a sus clientes a obtener una Classic License. Además, usar una licencia limitada para explorar mejor el producto.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamiento de Aspose.PDF para Go vía C\u002B\u002B
Abstract: La página de Licenciamiento de Aspose.PDF para Go a través de C\u002B\u002B explica las opciones de licencia disponibles para el producto. Los clientes pueden elegir entre una Classic License, una Metered License o una licencia limitada para propósitos de evaluación. La página también destaca los beneficios de obtener una licencia adecuada, como desbloquear la funcionalidad completa y eliminar las limitaciones de evaluación.
SoftwareApplication: go-cpp
---


## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben nuestros componentes a fondo antes de comprar, por lo que la versión de evaluación le permite usarla como lo haría normalmente.

- **Documentos creados con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF for Go ofrece la funcionalidad completa del producto, pero todas las páginas en los archivos generados llevan una marca de agua con el texto "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." en la parte superior.

- **Limitar el número de páginas que se pueden procesar.**
En la versión de evaluación, solo puede procesar las primeras cuatro páginas de un documento.

>Si desea probar Aspose.PDF for Go sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días. Por favor, consulte [¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)

## Licencia clásica

Aplicando una licencia para habilitar la funcionalidad completa de la biblioteca Aspose.PDF usando un archivo de licencia (Aspose.PDF.GoViaCPP.lic).

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

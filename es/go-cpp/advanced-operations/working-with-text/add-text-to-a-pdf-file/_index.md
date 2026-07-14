---
title: Agregar texto a PDF usando Go
linktitle: Agregar texto a PDF
type: docs
weight: 10
url: /es/go-cpp/add-text-to-pdf-file/
description: Aprenda cómo agregar texto a un documento PDF en Go usando Aspose.PDF para la mejora de contenido y la edición de documentos.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Agregar texto a PDF usando Aspose.PDF para Go
Abstract: La sección Agregar texto al archivo PDF de la documentación de Aspose.PDF para C++ y Go ofrece instrucciones paso a paso para insertar texto en documentos PDF de forma programática. Cubre varios métodos para agregar texto, incluyendo la posición, personalización de fuentes, ajustes de color y opciones de alineación de texto. La guía muestra cómo agregar texto a páginas y ubicaciones específicas dentro de un PDF, garantizando una colocación precisa del contenido. Con ejemplos de código detallados y explicaciones, los desarrolladores pueden integrar fácilmente funciones de inserción de texto en sus aplicaciones para una mejor gestión de documentos PDF.
SoftwareApplication: go-cpp
---

Para agregar texto a un archivo PDF existente:

1. Abra un archivo PDF.
1. Agregue el texto al documento PDF con [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) función.
1. Guarda las modificaciones en el mismo archivo.

## Agregar texto

El siguiente fragmento de código le muestra cómo agregar texto en un archivo PDF existente.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

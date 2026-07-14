---
title: Agregar páginas al documento PDF
linktitle: Agregar páginas
type: docs
weight: 10
url: /es/go-cpp/add-pages/
description: Explora cómo agregar páginas a un PDF existente en Go con Aspose.PDF para mejorar y ampliar tus documentos.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar páginas PDF con Aspose.PDF para Go
Abstract: Aspose.PDF for Go via C++ ofrece una funcionalidad potente para agregar páginas a documentos PDF, permitiendo a los desarrolladores crear nuevas páginas de forma dinámica y personalizarlas según requisitos específicos. La biblioteca admite la inserción de páginas en blanco o la copia de páginas de documentos existentes, ofreciendo opciones para definir el tamaño de la página, la orientación y el contenido. Estas capacidades permiten una expansión y personalización fluida del documento. La documentación incluye instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a implementar de manera eficiente las funciones de adición de páginas en sus aplicaciones.
SoftwareApplication: go-cpp
---

## Agregar página en un archivo PDF

El fragmento de código Go proporcionado muestra cómo ejecutar la operación Add Page al final del PDF usando la biblioteca Aspose.PDF.

1. El método [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) permite al programa cargar un archivo PDF existente (sample.pdf) para su manipulación. Esto es esencial para cualquier operación relacionada con PDF, como editar, agregar contenido o leer datos.
1. El método [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) se utiliza para insertar una nueva página en blanco en el documento PDF existente. Esto es útil para ampliar un documento o prepararlo para contenido adicional.
1. El método [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) garantiza que las modificaciones al PDF se escriban de nuevo en el archivo. Este paso es crucial para preservar los cambios, como la adición de nuevas páginas.
1. El método [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) se llama usando defer para liberar cualquier recurso asignado durante las operaciones con PDF. Esto es importante para prevenir fugas de memoria y garantizar un uso eficiente de los recursos.

Este fragmento es un ejemplo conciso y eficiente de cómo usar la biblioteca Aspose.PDF Go para tareas básicas de manipulación de PDF.

Aspose.PDF for Go le permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como añadir páginas al final de un archivo PDF.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## Insertar página en un archivo PDF

El método [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) inserta una nueva página en la posición especificada. Esta función es útil cuando necesitas insertar páginas adicionales en un documento existente, por ejemplo, añadiendo una nueva sección o contenido a un informe o presentación.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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
---
title: Ejemplo de Hello World usando el lenguaje Go
linktitle: Ejemplo de Hello World
type: docs
weight: 40
url: /es/go-cpp/hello-world-example/
description: Esta muestra demuestra cómo crear un documento PDF simple con el texto Hello World usando Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World mediante Aspose.PDF for Go
Abstract: La guía de inicio rápido para Aspose.PDF for Go mediante C++ proporciona una introducción a trabajar con la biblioteca, cubriendo los pasos básicos para crear y manipular documentos PDF. Incluye un ejemplo 'Hello World' que demuestra cómo generar un archivo PDF simple con contenido de texto, ayudando a los desarrolladores a comprender rápidamente la funcionalidad central de la API.
SoftwareApplication: go-cpp
---

Un ejemplo "Hello World" se utiliza tradicionalmente para introducir características de un lenguaje de programación o software con un caso de uso simple.

**Aspose.PDF for Go** es una API de PDF rica en funciones que permite a los desarrolladores incrustar la creación, manipulación y conversión de documentos PDF con Go. Soporta muchos formatos de archivo populares, incluyendo PDF, TXT, XPS, EPUB, TEX, DOC, DOCX, PPTX, formatos de imagen, etc. En este artículo, estamos creando un documento PDF que contiene el texto \u0022Hello World!\u0022. Después de instalar Aspose.PDF for Go en su entorno, puede ejecutar el ejemplo de código para ver cómo funciona la API de Aspose.PDF.
El siguiente fragmento de código sigue estos pasos:

1. Cree una nueva instancia de documento PDF.
1. Agregar una nueva página al documento PDF usando [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) función.
1. Establecer el tamaño de página usando [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. Agregar el texto "Hello World!" a la primera página usando [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. Guardar el documento PDF reparado usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) método.
1. Cierre el documento PDF y libere los recursos asignados.

El siguiente fragmento de código es un programa Hello World para demostrar el funcionamiento de la API de Aspose.PDF para Go.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```

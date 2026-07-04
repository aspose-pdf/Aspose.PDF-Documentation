---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/go-cpp/open-pdf-document/
description: Aprenda cómo abrir un archivo PDF con Aspose.PDF for Go vía C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documento PDF con Aspose.PDF for Go vía C++
Abstract: Aspose.PDF for Go vía C++ ofrece una funcionalidad potente para abrir y cargar documentos PDF programáticamente, lo que permite a los desarrolladores acceder y manipular el contenido PDF con facilidad. La biblioteca admite la apertura de archivos PDF desde diversas fuentes, como rutas de archivos y streams de memoria, garantizando un procesamiento eficiente y una gestión adecuada de recursos. Proporciona características para inspeccionar las propiedades del documento, extraer texto e imágenes, y realizar otras operaciones sobre los PDFs cargados. La documentación incluye instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a integrar capacidades de apertura de PDF en sus aplicaciones sin problemas.
SoftwareApplication: go-cpp
---

## Abrir documento PDF existente

El fragmento de código muestra operaciones esenciales para trabajar con PDFs usando Aspose.PDF for Go. Estas son abrir un archivo, guardar cambios y cerrar los recursos correctamente. Esto lo convierte en un ejemplo fundamental para desarrolladores que manejan documentos PDF.

El ejemplo es sencillo, lo que lo hace fácil de entender y modificar. Es ideal para principiantes o como plantilla para aplicaciones más complejas.

La capacidad de abrir y guardar documentos PDF es un requisito básico en muchos escenarios, como generar informes, modificar documentos o crear flujos de trabajo automatizados.

Este ejemplo muestra la facilidad de uso de la API para la manipulación simple de PDF, la cual puede ampliarse para incluir funciones avanzadas como extracción de texto, anotaciones o rellenado de formularios.

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
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

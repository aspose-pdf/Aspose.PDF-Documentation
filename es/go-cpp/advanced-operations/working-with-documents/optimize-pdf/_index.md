---
title: Optimizar PDF usando Aspose.PDF for Go vía C++
linktitle: Optimizar archivo PDF
type: docs
weight: 10
url: /es/go-cpp/optimize-pdf/
description: Optimizar y comprimir archivos PDF usando la herramienta Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimizar y comprimir archivos PDF usando Aspose.PDF for Go
Abstract: Aspose.PDF for Go vía C++ ofrece potentes funcionalidades de optimización para reducir el tamaño y mejorar el rendimiento de los documentos PDF. La biblioteca proporciona diversas opciones de optimización, incluyendo la compresión de imágenes, la eliminación de objetos no utilizados, la reducción de tamaños de Font y la optimización de flujos de contenido. Estas características ayudan a mejorar la eficiencia del almacenamiento de documentos y garantizan tiempos de procesamiento y carga más rápidos. La documentación brinda instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a implementar la optimización de PDF de manera eficaz dentro de sus aplicaciones.
SoftwareApplication: go-cpp
---

## Optimizar documento PDF

Toolkit con Aspose.PDF for Go a través de C++ le permite optimizar un documento PDF.

Este fragmento es útil para aplicaciones donde reducir el tamaño o mejorar la eficiencia de los archivos PDF es crítico, como para cargas web, archivado o compartir mediante un ancho de banda limitado.

1. El [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) método carga el archivo PDF especificado (sample.pdf) en la memoria.
1. El [Método Optimize](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) reduce el tamaño del archivo al realizar optimizaciones como eliminar objetos no utilizados, comprimir imágenes, aplanar anotaciones, desenlazar fuentes y habilitar la reutilización de contenido. Estos pasos ayudan a reducir los requisitos de almacenamiento y a mejorar la velocidad de procesamiento del documento PDF.
1. El [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) el método guarda el PDF optimizado en un nuevo archivo.

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
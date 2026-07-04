---
title: Optimizar recursos PDF usando Go
linktitle: Optimizar recursos PDF
type: docs
weight: 15
url: /es/go-cpp/optimize-pdf-resources/
description: Optimizar recursos de archivos PDF usando la herramienta Go
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimizar recursos PDF usando Aspose.PDF for Go
Abstract: Aspose.PDF for Go a través de C++ proporciona capacidades avanzadas para optimizar recursos PDF, mejorando la eficiencia del documento y reduciendo el tamaño del archivo. La biblioteca permite a los desarrolladores optimizar fuentes, imágenes y metadatos eliminando datos redundantes y comprimiendo recursos sin comprometer la calidad del documento. Estas técnicas de optimización mejoran el rendimiento del documento, haciendo que los PDFs sean más adecuados para compartir y almacenar. La documentación ofrece una guía detallada y ejemplos de código para ayudar a los desarrolladores a implementar eficazmente la optimización de recursos en sus aplicaciones.
SoftwareApplication: go-cpp
---

## Optimizar recursos PDF

Optimizar recursos en el documento:

  1. Los recursos que no se usan en las páginas del documento se eliminan.
  1. Los recursos iguales se combinan en un solo objeto.
  1. Los objetos no utilizados se eliminan.

La optimización puede incluir la compresión de imágenes, la eliminación de objetos no utilizados y la optimización de fuentes para reducir el tamaño del archivo y mejorar el rendimiento. Cualquier error durante esta operación se registra y termina el programa.  
 
1. El [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) method carga el archivo PDF especificado (sample.pdf) en memoria.
1. Optimiza los recursos dentro del PDF para mayor eficiencia usando [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) method.
1. El [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method guarda el PDF optimizado en un archivo nuevo.

El siguiente fragmento de código muestra cómo optimizar un documento PDF.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
---
title: Rotar páginas PDF con Go
linktitle: Rotar páginas PDF
type: docs
weight: 50
url: /es/go-cpp/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente de forma programática con Go a través de C++
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotar páginas PDF con Aspose.PDF para Go
Abstract: Aspose.PDF para Go a través de C++ proporciona una funcionalidad robusta para rotar páginas en documentos PDF, permitiendo a los desarrolladores modificar la orientación de la página según sea necesario. La biblioteca admite rotar páginas en 90, 180 o 270 grados, lo que permite ajustes rápidos y eficientes al diseño del documento. Esta característica es útil para corregir páginas mal orientadas o alterar la presentación del documento. La documentación incluye instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a integrar sin problemas las capacidades de rotación de páginas en sus aplicaciones.
SoftwareApplication: go-cpp
---

Esta sección describe cómo cambiar la orientación de la página de paisaje a retrato y viceversa en un archivo PDF existente usando Go.

Rotar páginas asegura una alineación adecuada para imprimir o visualizar PDFs en entornos profesionales

1. Abra el documento PDF.
1. Rotar páginas PDF. El [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) función aplica una rotación específica (en este caso, 180 grados) a una página dada.
1. Guardar cambios en un nuevo archivo. El [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) La función crea un nuevo archivo PDF para preservar el original mientras almacena la versión actualizada.

En este ejemplo, rotas una página específica en un documento PDF:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

También tiene la opción de rotar todas las páginas PDF en su documento:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```
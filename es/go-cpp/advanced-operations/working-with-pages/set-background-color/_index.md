---
title: Establecer el color de fondo para PDF con Go
linktitle: Establecer color de fondo
type: docs
weight: 80
url: /es/go-cpp/set-background-color/
description: Establezca el color de fondo para su archivo PDF con Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer el color de fondo para PDF con Aspose.PDF for Go
Abstract: Aspose.PDF for Go a través de C++ ofrece funcionalidad para establecer el color de fondo de las páginas PDF, permitiendo a los desarrolladores personalizar la apariencia de los documentos. Esta característica permite la aplicación de colores sólidos en todo el fondo de la página, mejorando la presentación visual del documento. Los desarrolladores pueden especificar fácilmente los valores de color utilizando modelos de color estándar como RGB o CMYK. La documentación proporciona instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a implementar la personalización del color de fondo de manera eficaz dentro de sus aplicaciones C++.
SoftwareApplication: go-cpp
---

1. El fragmento de código proporcionado muestra cómo establecer un color de fondo para un archivo PDF utilizando la biblioteca Aspose.PDF en Go.
1. El método [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) carga el archivo PDF especificado en memoria, permitiendo manipulaciones adicionales, como modificar su apariencia o contenido.
1. El método [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) aplica un nuevo color de fondo al documento PDF. Los valores RGB permiten a los usuarios personalizar el estilo visual del documento.
1. El método [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) guarda el PDF actualizado con un nuevo nombre.

Este código es ideal para aplicaciones que necesitan automatizar personalizaciones de PDF, como crear informes con marca, agregar marcas de agua o mejorar la consistencia visual en varios documentos.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
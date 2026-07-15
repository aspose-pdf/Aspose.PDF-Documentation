---
title: Convertir PDF a PPTX en Go
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /es/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF le permite convertir PDF al formato PPTX usando Go.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Herramienta Golang para Convertir PDF a PowerPoint
Abstract: Aspose.PDF for Go via C++ ofrece una solución fiable para convertir documentos PDF al formato PowerPoint (PPTX) manteniendo el diseño original, el formato y la estructura del contenido. Esta funcionalidad permite a los desarrolladores transformar sin problemas archivos PDF estáticos en presentaciones dinámicas y editables. La biblioteca ofrece opciones de personalización para controlar el proceso de conversión, garantizando una salida de alta calidad adecuada para uso empresarial y profesional. La documentación proporciona instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a integrar eficientemente la conversión de PDF a PowerPoint en sus aplicaciones.
SoftwareApplication: go-cpp
---

## Convertir PDF a PPTX

El fragmento de código Go proporcionado demuestra cómo convertir un documento PDF en un PPTX utilizando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a PPTX usando [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) función.
1. Cerrar el documento PDF y liberar los recursos asignados.

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF for Go te presenta una aplicación gratuita en línea [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes probar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a PPTX con App gratuita](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
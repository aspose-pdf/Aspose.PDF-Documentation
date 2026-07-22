---
title: Convertir PDF a PPTX en Rust
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /es/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF le permite convertir PDF al formato PPTX usando Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Herramienta Rust para convertir PDF a PowerPoint
Abstract: Aspose.PDF for Rust via C++ ofrece una solución fiable para convertir documentos PDF a formato PowerPoint (PPTX) mientras se conserva el diseño original, el formato y la estructura del contenido. Esta funcionalidad permite a los desarrolladores transformar sin problemas los archivos PDF estáticos en presentaciones dinámicas y editables. La biblioteca brinda opciones de personalización para controlar el proceso de conversión, garantizando una salida de alta calidad adecuada para uso empresarial y profesional. La documentación proporciona instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a integrar de manera eficiente la conversión de PDF a PowerPoint en sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Convertir PDF a PPTX

El fragmento de código Rust proporcionado demuestra cómo convertir un documento PDF en un PPTX utilizando la biblioteca Aspose.PDF:

1. Abre un documento PDF.
1. Convertir un archivo PDF a PPTX usando [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) función.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF for Rust le presenta una aplicación gratuita en línea [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a PPTX con App Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
---
title: Establecer el color de fondo para PDF con Rust a través de C++
linktitle: Establecer color de fondo
type: docs
weight: 80
url: /es/rust-cpp/set-background-color/
description: Establecer el color de fondo para su archivo PDF con Rust a través de C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer el color de fondo para PDF con Aspose.PDF para Rust
Abstract: Aspose.PDF para Rust a través de C++ ofrece funcionalidad para establecer el color de fondo de las páginas PDF, lo que permite a los desarrolladores personalizar la apariencia de los documentos. Esta característica permite la aplicación de colores sólidos en todo el fondo de la página, mejorando la presentación visual del documento. Los desarrolladores pueden especificar fácilmente valores de color utilizando modelos de color estándar como RGB o CMYK. La documentación proporciona instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a implementar la personalización del color de fondo de manera eficaz dentro de sus aplicaciones C++.
SoftwareApplication: rust-cpp
---

1. El fragmento de código proporcionado muestra cómo establecer un color de fondo para un archivo PDF utilizando la biblioteca Aspose.PDF en Rust.
1. El [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) El método carga el archivo PDF especificado en memoria, permitiendo manipulaciones adicionales, como modificar su apariencia o contenido.
1. El [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) El método aplica un nuevo color de fondo al documento PDF. Los valores RGB permiten a los usuarios personalizar el estilo visual del documento.
1. El [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) El método guarda el PDF actualizado con un nuevo nombre.

Este código es ideal para aplicaciones que necesitan automatizar la personalización de PDF, como crear informes con marca, añadir marcas de agua o mejorar la consistencia visual en múltiples documentos.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```
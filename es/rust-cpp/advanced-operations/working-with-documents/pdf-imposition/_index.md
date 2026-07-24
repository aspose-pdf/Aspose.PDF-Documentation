---
title: Imposición de PDF usando Aspose.PDF for Rust via C++
linktitle: Imposición de PDF
type: docs
weight: 30
url: /es/rust-cpp/pdf-imposition/
description: Este artículo explica cómo reorganizar páginas PDF para diseños optimizados para impresión usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo crear un folleto o N-Up de archivos PDF
Abstract: Aspose.PDF for Rust via C++ proporciona herramientas potentes para reestructurar documentos PDF para cumplir con los requisitos de impresión y diseño. Este artículo demuestra cómo convertir un PDF estándar en un folleto, asegurando el orden correcto de las páginas para el plegado, y cómo crear un PDF N-Up que combina múltiples páginas en una sola hoja. Usando ejemplos concisos de código Rust, los desarrolladores pueden implementar rápidamente transformaciones de PDF listas para imprimir en flujos de trabajo de documentación, publicación y archivo.
SoftwareApplication: rust-cpp
---

## Crear N-Up de PDF

Un PDF N-Up coloca múltiples páginas de origen en una sola página de salida. En este ejemplo, se utiliza un diseño de 2 × 2, de modo que cuatro páginas originales se combinan en cada página del documento de salida.

1. Abra el documento PDF de origen.
1. Guarde el documento usando un diseño N-Up con el número especificado de filas y columnas.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## Crear folleto de PDF

Aspose.PDF para Rust a través de C++ explica cómo convertir un documento PDF estándar en un PDF con estilo de folleto.
El formato de folleto reorganiza las páginas de modo que, al imprimirse y doblarse, el documento forme un folleto correcto con las páginas en el orden adecuado.

1. Abra el documento PDF de origen.
1. Guarde el documento como un PDF de folleto.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**Tenga en cuenta que se requiere una licencia de prueba gratuita para la funcionalidad completa.**

Explore el resultado de crear un folleto de 4 páginas.

![Ejemplo de un folleto de 4 páginas](sample_4.png)

Explore el resultado de crear un folleto de 3 páginas.

![Ejemplo de un folleto de 3 páginas](sample_3.png)
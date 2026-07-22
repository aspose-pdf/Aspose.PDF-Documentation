---
title: Rotar páginas PDF con Rust a través de C++
linktitle: Rotar páginas PDF
type: docs
weight: 50
url: /es/rust-cpp/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente de forma programática con Rust a través de C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotar páginas PDF con Aspose.PDF para Rust
Abstract: Aspose.PDF para Rust a través de C++ proporciona una funcionalidad robusta para rotar páginas en documentos PDF, permitiendo a los desarrolladores modificar la orientación de la página según sea necesario. La biblioteca soporta rotar páginas en 90, 180 o 270 grados, habilitando ajustes rápidos y eficientes del diseño del documento. Esta característica es útil para corregir páginas mal orientadas o alterar la presentación del documento. La documentación incluye instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a integrar sin problemas las capacidades de rotación de páginas en sus aplicaciones.
SoftwareApplication: rust-cpp
---

Esta sección describe cómo cambiar la orientación de la página de apaisado a retrato y viceversa en un archivo PDF existente usando Rust.

Rotar páginas garantiza una alineación adecuada para imprimir o mostrar PDFs en entornos profesionales

1. Abra el documento PDF.
1. Rotar páginas PDF. El [rotar](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) la función aplica una rotación específica (en este caso, 180 grados) a una página dada.
1. Guardar cambios en un archivo nuevo. El [guardar_como](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) La función crea un nuevo archivo PDF para preservar el original mientras guarda la versión actualizada.

En este ejemplo, gira una página específica en un documento PDF:

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```
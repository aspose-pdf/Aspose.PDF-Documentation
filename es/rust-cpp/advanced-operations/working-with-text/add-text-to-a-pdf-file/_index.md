---
title: Agregar texto a PDF usando Rust
linktitle: Agregar texto a PDF
type: docs
weight: 10
url: /es/rust-cpp/add-text-to-pdf-file/
description: Aprenda cómo agregar texto a un documento PDF en Rust usando Aspose.PDF para la mejora de contenido y la edición de documentos.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Agregar texto a PDF usando Aspose.PDF para Rust
Abstract: La sección Agregar texto al archivo PDF de la documentación de Aspose.PDF para C++ y Rust ofrece instrucciones paso a paso para insertar texto en documentos PDF de forma programática. Cubre varios métodos para agregar texto, incluidas la posición, la personalización de fuentes, los ajustes de color y las opciones de alineación de texto. La guía muestra cómo agregar texto a páginas y ubicaciones específicas dentro de un PDF, garantizando una colocación precisa del contenido. Con ejemplos de código detallados y explicaciones, los desarrolladores pueden integrar fácilmente funciones de inserción de texto en sus aplicaciones para una mejor gestión de documentos PDF.
SoftwareApplication: rust-cpp
---

Para agregar texto a un archivo PDF existente:

1. Abrir un archivo PDF.
1. Añadir el texto al documento PDF con [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) función.
1. Guarda las modificaciones en el mismo archivo.

## Añadiendo Texto

El siguiente fragmento de código le muestra cómo agregar texto en un archivo PDF existente.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

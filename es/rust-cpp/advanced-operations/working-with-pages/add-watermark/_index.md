---
title: Agregar marca de agua al PDF usando Rust
linktitle: Agregar marca de agua
type: docs
weight: 80
url: /es/rust-cpp/add-watermarks/
description: Este ejemplo muestra cómo agregar una marca de agua de texto personalizable a un documento PDF usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar marca de agua de texto
Abstract: Aspose.PDF for Rust via C++ proporciona una forma flexible de agregar marcas de agua de texto a documentos PDF. Este ejemplo muestra cómo insertar una marca de agua personalizable especificando el contenido del texto, Font, size, color, position, rotation angle, layering behavior y transparency. Las marcas de agua se utilizan comúnmente para la marca, etiquetas de confidencialidad, marcas de borrador o protección de documentos.
SoftwareApplication: rust-cpp
---

El [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) El método permite a los desarrolladores aplicar programáticamente una marca de agua de texto a un documento PDF existente. La marca de agua puede personalizarse completamente, incluyendo:

- Texto de la marca de agua
- Familia de fuente
- Tamaño de fuente
- Color del texto (formato HEX)
- Coordenadas de posición X y Y
- Ángulo de rotación
- Colocación en primer plano o fondo
- Opacidad (nivel de transparencia)

En este ejemplo, la aplicación abre un archivo PDF existente, aplica una marca de agua girada semitransparente y guarda el documento modificado bajo un nuevo nombre de archivo.

Esta funcionalidad es particularmente útil para marcar documentos como Borrador, Confidencial, Muestra, o para añadir elementos de marca antes de la distribución.

1. Abra el documento PDF existente.
1. Llame al método add_watermark y configure las propiedades de la marca de agua.
1. Guarde el documento actualizado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```
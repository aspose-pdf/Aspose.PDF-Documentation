---
title: Abrir documento PDF programáticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /es/rust-cpp/open-pdf-document/
description: Aprenda cómo abrir un archivo PDF con Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documento PDF con Aspose.PDF for Rust via C\u002B\u002B
Abstract: Aspose.PDF for Rust via C\u002B\u002B proporciona una funcionalidad poderosa para abrir y cargar documentos PDF de forma programática, permitiendo a los desarrolladores acceder y manipular el contenido PDF con facilidad. La biblioteca admite la apertura de archivos PDF desde diversas fuentes, como rutas de archivo y flujos de memoria, garantizando un procesamiento eficiente y una gestión adecuada de los recursos. Ofrece características para inspeccionar las propiedades del documento, extraer texto e imágenes, y realizar otras operaciones sobre los PDFs cargados. La documentación incluye instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a integrar capacidades de apertura de PDF en sus aplicaciones sin problemas.
SoftwareApplication: rust-cpp
---

## Abrir documento PDF existente

El fragmento de código muestra operaciones esenciales para trabajar con PDFs usando Aspose.PDF for Rust. Estas son abrir un archivo, guardar cambios y cerrar los recursos correctamente. Esto lo convierte en un ejemplo fundamental para desarrolladores que manejan documentos PDF.

El ejemplo es sencillo, lo que facilita su comprensión y modificación. Es ideal para principiantes o como plantilla para aplicaciones más complejas.

La capacidad de abrir y guardar documentos PDF es un requisito esencial en muchos escenarios, como la generación de informes, la modificación de documentos o la creación de flujos de trabajo automatizados.

Este ejemplo muestra la facilidad de uso de la API para la manipulación sencilla de PDFs, que puede ampliarse para incluir funcionalidades avanzadas como extracción de texto, anotación o relleno de formularios.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document named "sample.pdf"
        let pdf = Document::open("sample.pdf")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_open.pdf")?;

        Ok(())
    }
```

---
title: Agregar encabezado y pie de página al PDF usando Rust
linktitle: Agregar encabezado y pie de página al PDF
type: docs
weight: 90
url: /es/rust-cpp/add-headers-and-footers-of-pdf-file/
description:
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar encabezado y pie de página al PDF usando Rust
Abstract: Este artículo muestra cómo agregar encabezados y pies de página de texto a documentos PDF usando la biblioteca asposepdf Rust. Explica cómo abrir un PDF existente, insertar texto consistente en el encabezado o pie de página de cada página y guardar el documento modificado como un nuevo archivo. Los ejemplos presentan un flujo de trabajo simple y a prueba de errores que se puede usar para tareas como agregar números de página, títulos o branding de forma programática en aplicaciones Rust.
SoftwareApplication: rust-cpp
---

## Agregar encabezados y pies de página como fragmentos de texto

### Agregar texto en el pie de página de un PDF-document

Nuestra herramienta le permite abrir un PDF existente, agregar un pie de página de texto a todas las páginas y guardar el PDF modificado como un nuevo archivo usando la biblioteca asposepdf Rust. Maneja los errores de forma elegante con el tipo Result de Rust.

1. Abra un documento PDF existente.
1. Agregar texto al pie de página con [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. Guarde el PDF modificado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### Agregar texto en el encabezado de un documento PDF

Este fragmento de código muestra cómo abrir un archivo PDF existente, agregar un encabezado de texto a todas las páginas y guardar el documento modificado como un nuevo archivo utilizando la biblioteca asposepdf. Proporciona una forma simple y automatizada de insertar encabezados consistentes en PDFs.

1. Abrir un PDF existente.
1. Agregar texto al encabezado con ayuda [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. Guarde el PDF modificado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```
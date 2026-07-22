---
title: Agregar páginas al documento PDF
linktitle: Agregar páginas
type: docs
weight: 10
url: /es/rust-cpp/add-pages/
description: Explore cómo agregar páginas a un PDF existente en Rust con Aspose.PDF para mejorar y ampliar sus documentos.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar páginas PDF con Aspose.PDF para Rust
Abstract: Aspose.PDF for Rust via C++ proporciona una funcionalidad potente para agregar páginas a documentos PDF, permitiendo a los desarrolladores crear nuevas páginas de forma dinámica y personalizarlas según requisitos específicos. La biblioteca admite la inserción de páginas en blanco o la copia de páginas de documentos existentes, ofreciendo opciones para definir el tamaño de la página, la orientación y el contenido. Estas capacidades permiten una expansión y personalización de documentos sin problemas. La documentación incluye instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a implementar de manera eficiente las funciones de agregado de páginas en sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Agregar página en un archivo PDF

El fragmento de código Rust proporcionado demuestra cómo realizar la operación Add Page al final del PDF usando la biblioteca Aspose.PDF.

1. El [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) La función permite al programa cargar un archivo PDF existente (sample.pdf) para su manipulación. Esto es esencial para cualquier operación relacionada con PDF, como editar, agregar contenido o leer datos.
1. El [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) El método se utiliza para insertar una nueva página en blanco en el documento PDF existente. Esto es útil para ampliar un documento o prepararlo para contenido adicional.
1. El [guardar](https://reference.aspose.com/pdf/rust-cpp/core/save/) El método garantiza que las modificaciones al PDF se escriban de nuevo en el archivo. Este paso es crucial para preservar los cambios, como la adición de nuevas páginas.

Este fragmento es un ejemplo conciso y eficiente de cómo usar la biblioteca Aspose.PDF Rust para tareas básicas de manipulación de PDF.

Aspose.PDF for Rust le permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como añadir páginas al final de un archivo PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## Insertar página en un archivo PDF

El [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) El método inserta una nueva página en la posición especificada. Esta funcionalidad es útil cuando necesitas insertar páginas adicionales en un documento existente, por ejemplo, añadiendo una nueva sección o contenido a un informe o presentación.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
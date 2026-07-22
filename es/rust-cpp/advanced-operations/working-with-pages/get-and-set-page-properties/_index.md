---
title: Obtener y establecer propiedades de página
linktitle: Obtener y establecer propiedades de página
type: docs
url: /es/rust-cpp/get-and-set-page-properties/
description: Aprenda cómo obtener y establecer propiedades de página para documentos PDF usando Aspose.PDF para Rust, lo que permite una personalización del formato del documento.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Obtener y establecer propiedades de página con Aspose.PDF para Rust
Abstract: Aspose.PDF para Rust a través de C++ ofrece funciones integrales para obtener y establecer propiedades de página en documentos PDF, permitiendo a los desarrolladores acceder y modificar varios atributos de la página, como el tamaño, la rotación, los márgenes y los metadatos. Estas capacidades permiten un control preciso sobre el diseño y la apariencia del documento para cumplir con requisitos específicos de la aplicación. La biblioteca garantiza una personalización y optimización sin problemas de las páginas PDF. La documentación brinda una guía detallada y ejemplos de código que ayudan a los desarrolladores a recuperar y actualizar eficientemente las propiedades de página dentro de sus aplicaciones.
SoftwareApplication: rust-cpp
---


Aspose.PDF para Rust le permite leer y establecer propiedades de las páginas en un archivo PDF. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre propiedades de página PDF como el color y establecer propiedades de página.

## Obtener el número de páginas en un archivo PDF

Al trabajar con documentos, a menudo deseas saber cuántas páginas contienen. Con Aspose.PDF esto no lleva más de dos líneas de código.

**Aspose.PDF for Rust via C\u002B\u002B** permite contar Pages con [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) función.

El siguiente fragmento de código está diseñado para abrir un documento PDF, obtener su recuento de páginas y luego imprimir el resultado.

El [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) El método se llama para obtener el número total de páginas en el documento PDF. Esto es útil para tareas que necesitan conocer la longitud del documento, como al extraer páginas específicas o realizar operaciones en todas las páginas. Este método es una forma directa de consultar la estructura del documento.

Para obtener el número de páginas en un archivo PDF:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## Establecer tamaño de página

En este ejemplo, el método pdf.page_set_size() cambia el tamaño de la primera página del documento PDF. La constante PageSize::A1 garantiza que la primera página se establezca al tamaño de papel A1. Esto es útil al convertir documentos a un formato estandarizado o al asegurar que el contenido específico encaje correctamente en las páginas.

1. Abriendo el documento PDF con [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) método.
1. Estableciendo el tamaño de página con [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) función.
1. Guardando el documento usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```
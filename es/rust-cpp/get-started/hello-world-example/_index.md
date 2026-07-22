---
title: Ejemplo de Hello World usando el lenguaje Rust
linktitle: Ejemplo de Hello World
type: docs
weight: 40
url: /es/rust-cpp/hello-world-example/
description: Este ejemplo muestra cómo crear un documento PDF simple con el texto Hello World usando Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World vía Aspose.PDF for Rust
Abstract: La guía Get Started para Aspose.PDF for Rust vía C++ proporciona una introducción a trabajar con la biblioteca, cubriendo los pasos básicos para crear y manipular documentos PDF. Incluye un ejemplo 'Hello World' que muestra cómo generar un archivo PDF simple con contenido de texto, ayudando a los desarrolladores a comprender rápidamente la funcionalidad central de la API.
SoftwareApplication: rust-cpp
---

Un ejemplo "Hello World" se usa tradicionalmente para introducir características de un lenguaje de programación o software con un caso de uso sencillo.

**Aspose.PDF for Rust** es una API de PDF con muchas funciones que permite a los desarrolladores incrustar la creación, manipulación y conversión de documentos PDF con Rust. Soporta muchos formatos de archivo populares, incluyendo PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, formatos de imagen, etc. En este artículo, estamos creando un documento PDF que contiene el texto "Hello World!". Después de instalar Aspose.PDF for Rust en su entorno, puede ejecutar el ejemplo de código para ver cómo funciona la API de Aspose.PDF.
El fragmento de código a continuación sigue estos pasos:

1. Cree una nueva instancia de documento PDF.
1. Agregue una nueva página al documento PDF usando [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) función.
1. Establecer el tamaño de la página usando [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. Agregar el texto "Hello World!" a la primera página usando [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. Guardar el documento PDF usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método.

El siguiente fragmento de código es un programa Hello World para exhibir el funcionamiento de Aspose.PDF for Rust API.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```

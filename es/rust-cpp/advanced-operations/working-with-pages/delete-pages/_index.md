---
title: Eliminar páginas PDF con Rust vía C++
linktitle: Eliminar páginas PDF
type: docs
weight: 30
url: /es/rust-cpp/delete-pages/
description: Puede eliminar páginas de su archivo PDF usando Aspose.PDF for Rust vía C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar páginas PDF con Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ ofrece una funcionalidad eficiente para eliminar páginas de documentos PDF, lo que permite a los desarrolladores eliminar páginas no deseadas o innecesarias con facilidad. La biblioteca permite la eliminación de una sola página o de varias páginas al especificar números de página o rangos, garantizando modificaciones precisas del documento. Esta característica ayuda a optimizar los archivos PDF al eliminar contenido redundante y optimizar la estructura del documento. La documentación proporciona instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a implementar la funcionalidad de eliminación de páginas de manera efectiva en sus aplicaciones.
SoftwareApplication: rust-cpp
---

Puede eliminar páginas de un archivo PDF usando **Aspose.PDF for Rust via C++**. El siguiente fragmento de código muestra cómo manipular un documento PDF eliminando una página específica. Este método es eficiente para tareas de manipulación de documentos PDF, específicamente para eliminar páginas, guardar el documento modificado y garantizar una gestión adecuada de los recursos.

1. Abrir un archivo PDF.
1. Eliminando una página específica con [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) función.
1. Guardando el documento usando [save](https://reference.aspose.com/pdf/rust-cpp/core/save/) método.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

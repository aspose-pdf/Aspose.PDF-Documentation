---
title: Extraer texto de PDF usando Rust
linktitle: Extraer texto de PDF
type: docs
weight: 30
url: /es/rust-cpp/extract-text-from-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer texto con Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ proporciona una forma potente y eficiente de extraer texto de documentos PDF. La biblioteca admite múltiples técnicas de extracción, lo que permite a los usuarios recuperar texto de documentos completos, páginas específicas o áreas predefinidas dentro de un PDF.
SoftwareApplication: rust-cpp
---

## Extraer texto de documento PDF

Extraer texto del documento PDF es una tarea muy común y útil. Los PDFs a menudo contienen información crítica que necesita ser accedida, analizada o procesada para diversos propósitos.

Extraer texto hace que el contenido del PDF sea buscable, permitiendo a los usuarios localizar información específica rápidamente sin revisar manualmente todo el documento.

En caso de que quieras extraer texto de un documento PDF, puedes usar [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) función.
Por favor, revisa el siguiente fragmento de código para extraer texto de un archivo PDF usando Rust.

1. Abrir un documento PDF con el nombre de archivo proporcionado.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) extrae el contenido de texto del documento PDF.
1. Imprime el texto extraído en la consola.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```
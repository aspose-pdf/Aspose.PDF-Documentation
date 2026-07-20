---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/rust-cpp/save-pdf-document/
description: Aprenda cómo guardar un archivo PDF con Aspose.PDF para Rust a través de C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardar documento PDF con Aspose.PDF para Rust a través de C\u002B\u002B
Abstract: Aspose.PDF para Rust a través de C\u002B\u002B ofrece una funcionalidad integral para guardar documentos PDF en varios formatos y ubicaciones con alta eficiencia y flexibilidad. La biblioteca permite a los desarrolladores guardar PDFs en sistemas de archivos y flujos de memoria, o exportarlos a formatos alternativos como DOCX, XLSX e imágenes. Proporciona opciones para personalizar los parámetros de guardado, optimizar el tamaño del archivo y garantizar la integridad de los datos. La documentación incluye instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a implementar eficientemente las capacidades de guardado de PDF en sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Guardar documento PDF en el sistema de archivos

El ejemplo demuestra el [nuevo](https://reference.aspose.com/pdf/rust-cpp/core/new/) Método para crear un nuevo documento PDF, que es una característica fundamental para generar documentos de forma dinámica, como informes o facturas.

El código es simple y puede actuar como una plantilla para funciones más avanzadas, como agregar texto, imágenes o anotaciones al PDF.

Este ejemplo demuestra el uso directo de la biblioteca Aspose.PDF Rust, mostrando su potencial para crear, modificar y guardar documentos.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```

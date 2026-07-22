---
title: Agregar número de página a PDF con Rust
linktitle: Agregar número de página
type: docs
weight: 10
url: /es/rust-cpp/add-page-number/
description: Este artículo demuestra cómo agregar números de página a un documento PDF existente usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar números de página
Abstract: Aspose.PDF for Rust via C++ permite a los desarrolladores mejorar los documentos PDF existentes con numeración automática de páginas en solo unas pocas líneas de código. Este ejemplo demuestra cómo abrir un archivo PDF, insertar números de página en todas las páginas y guardar el documento actualizado como un archivo nuevo. Automatizar la paginación garantiza una estructura de documento consistente y es particularmente útil para informes, contratos, manuales y otros documentos de varias páginas preparados para distribución o impresión.
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++ proporciona funcionalidad incorporada para modificar documentos PDF de forma programática. En este ejemplo, la aplicación abre un archivo PDF existente, aplica numeración automática de páginas a cada página y guarda el documento modificado con un nuevo nombre.

Este enfoque es útil al generar documentos finalizados para distribución, impresión o archivo. El proceso requiere solo unas pocas líneas de código y no altera el archivo original a menos que se sobrescriba explícitamente.

La numeración de páginas es un requisito común para informes, facturas, contratos, manuales y otros documentos de varias páginas. El [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) El método inserta automáticamente números de página en todas las páginas del documento, garantizando una paginación consistente en todo el archivo.

Después de agregar los números de página, el documento actualizado se guarda como un nuevo archivo PDF.

1. Abra el documento PDF existente.
1. Agregar números de página con [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) método.
1. Guardar el documento actualizado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```
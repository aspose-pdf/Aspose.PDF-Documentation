---
title: Extraer datos de AcroForm usando Rust
linktitle: Extraer datos de AcroForm
type: docs
weight: 50
url: /es/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprenda cómo extraer datos de AcroForms y guardarlos en formato XML, FDF o XFDF.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de AcroForm vía Rust
Abstract: "Este artículo explica cómo extraer datos AcroForm de archivos PDF usando Aspose.PDF para Rust vía C++ y exportarlos a formatos de intercambio de datos ampliamente utilizados: XML, FDF y XFDF. Demuestra cómo abrir un documento PDF que contiene campos de formulario interactivos y exportar programáticamente los nombres y valores de los campos de formulario para reutilizarlos fuera del PDF original. Al proporcionar ejemplos prácticos en Rust para cada formato de exportación, el artículo destaca flujos de trabajo comunes, incluyendo procesamiento de datos, envío de formularios, integración de sistemas y almacenamiento de datos a largo plazo, ayudando a los desarrolladores a gestionar y reutilizar eficientemente los datos de formularios PDF en sus aplicaciones."
---

## Exportar datos a XML desde un archivo PDF

Este fragmento de código muestra cómo exportar datos AcroForm de un documento PDF a un archivo XML usando Aspose.PDF para Rust.
El proceso implica abrir un archivo PDF existente con campos de formulario, y luego exportar esos campos y sus valores a un documento XML para procesamiento adicional, almacenamiento o intercambio de datos.

1. Abra el documento PDF.
1. Llame al método 'export_xml' para extraer los datos de los campos de formulario y guardarlos como un archivo XML.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## Exportar datos a FDF desde un archivo PDF

Aspose.PDF for Rust via C++ permite exportar datos AcroForm de un documento PDF a un archivo FDF. El archivo Forms Data Format (FDF) almacena los nombres y valores de los campos de formulario por separado del PDF, lo que lo hace útil para el intercambio de datos, flujos de trabajo de envío de formularios y el archivo de datos de formularios sin incrustarlos en el documento original.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## Exportar datos a XFDF desde un archivo PDF

XFDF (Formato de Datos de Formularios XML) es un formato basado en XML que representa los datos de los campos de formulario por separado del archivo PDF, lo que lo hace ideal para el intercambio de datos, envíos de formularios e integración con flujos de trabajo basados en la web.
Aspose.PDF for Rust via C++ ayuda a exportar los datos de AcroForm de un documento PDF a un archivo XFDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```

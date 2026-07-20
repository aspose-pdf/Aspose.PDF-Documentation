---
title: Optimizar PDF usando Aspose.PDF para Rust a través de C++
linktitle: Optimizar archivo PDF
type: docs
weight: 10
url: /es/rust-cpp/optimize-pdf/
description: Optimizar y comprimir archivos PDF usando la herramienta Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimizar y comprimir archivos PDF usando Aspose.PDF para Rust
Abstract: Aspose.PDF para Rust a través de C++ ofrece potentes funciones de optimización para reducir el tamaño y mejorar el rendimiento de los documentos PDF. La biblioteca proporciona varias opciones de optimización, incluyendo la compresión de imágenes, la eliminación de objetos no utilizados, la reducción de tamaños de fuentes y la optimización de flujos de contenido. Estas funciones ayudan a mejorar la eficiencia del almacenamiento de documentos y garantizan tiempos de procesamiento y carga más rápidos. La documentación ofrece instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a implementar la optimización de PDF de manera eficaz dentro de sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Optimizar documento PDF

El kit de herramientas con Aspose.PDF for Rust via C++ le permite optimizar un documento PDF.

Este fragmento es útil para aplicaciones donde reducir el tamaño o mejorar la eficiencia de los archivos PDF es fundamental, como para cargas web, archivado o compartir mediante ancho de banda limitado.

1. El [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) el método carga el archivo PDF especificado (sample.pdf) en memoria.
1. El [optimizar](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/) reduce el tamaño del archivo al realizar optimizaciones como eliminar objetos no utilizados, comprimir imágenes, aplanar anotaciones, desincorporar fuentes y habilitar la reutilización de contenido. Estos pasos ayudan a reducir los requisitos de almacenamiento y mejorar la velocidad de procesamiento del documento PDF.
1. El [guardar_como](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) El método guarda el PDF optimizado en un archivo nuevo.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```
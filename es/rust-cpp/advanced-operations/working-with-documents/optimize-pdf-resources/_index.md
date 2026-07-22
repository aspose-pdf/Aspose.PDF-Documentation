---
title: Optimizar recursos PDF usando Rust via C++
linktitle: Optimizar recursos PDF
type: docs
weight: 15
url: /es/rust-cpp/optimize-pdf-resources/
description: Optimizar recursos de archivos PDF usando la herramienta Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimizar recursos PDF usando Aspose.PDF para Rust
Abstract: Aspose.PDF para Rust via C++ ofrece capacidades avanzadas para optimizar recursos PDF, mejorando la eficiencia del documento y reduciendo el tamaño del archivo. La biblioteca permite a los desarrolladores optimizar fuentes, imágenes y metadatos al eliminar datos redundantes y comprimir recursos sin comprometer la calidad del documento. Estas técnicas de optimización mejoran el rendimiento del documento, haciendo que los PDF sean más adecuados para compartir y almacenar. La documentación brinda una guía detallada y ejemplos de código para ayudar a los desarrolladores a implementar eficazmente la optimización de recursos en sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Optimizar recursos PDF

Optimizar recursos en el documento:

  1. Los recursos que no se utilizan en las páginas del documento se eliminan.
  1. Los recursos iguales se combinan en un único objeto.
  1. Los objetos no utilizados se eliminan.

La optimización puede incluir la compresión de imágenes, la eliminación de objetos no utilizados y la optimización de fuentes para reducir el tamaño del archivo y mejorar el rendimiento. Cualquier error durante esta operación se registra y termina el programa.  
 
1. El [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) método carga el archivo PDF especificado (sample.pdf) en memoria.
1. Optimiza los recursos dentro del PDF para mayor eficiencia usando [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) método.
1. El [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método guarda el PDF optimizado en un nuevo archivo.

El siguiente fragmento de código muestra cómo optimizar un documento PDF.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;

      // Optimize PDF resources
      pdf.optimize_resource()?;

      // Save the optimized PDF-document with new filename
      pdf.save_as("sample_optimize_resources.pdf")?;

      Ok(())
  }
```
---
title: Licencia Aspose PDF
linktitle: Licenciamiento y limitaciones
type: docs
weight: 90
url: /es/rust-cpp/licensing/
description: Aspose. PDF for Rust invita a sus clientes a obtener una Classic License. También pueden usar una licencia limitada para explorar mejor el producto.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamiento de Aspose.PDF para Rust vía C++
Abstract: La página de Licenciamiento para Aspose.PDF for Rust vía C++ explica las opciones de licenciamiento disponibles para el producto. Los clientes pueden elegir entre una Classic License, una Metered License o una licencia limitada con fines de evaluación. La página también destaca los beneficios de obtener una licencia adecuada, como desbloquear la funcionalidad completa y eliminar las limitaciones de evaluación.
SoftwareApplication: rust-cpp
---

## Licencia

- El **código fuente de Rust** está licenciado bajo la Licencia MIT.
- La **biblioteca compartida** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) es propietaria y requiere una licencia comercial. Para usar la funcionalidad completa, debe obtener una licencia.

## Versión de evaluación

Puede usar **Aspose.PDF for Rust via C++** sin costo para la evaluación.La versión de evaluación proporciona casi toda la funcionalidad del producto con ciertas limitaciones. La misma versión de evaluación se convierte en una licencia cuando compra una licencia y agrega un par de líneas de código para aplicar la licencia.

- Si desea probar Aspose.PDF for Rust sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días. Por favor, consulte [¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)?

### Limitación de una versión de evaluación

Queremos que nuestros clientes prueben nuestros componentes a fondo antes de comprar, por lo que la versión de evaluación le permite usarla como lo haría normalmente.

- **Documentos creados con una marca de agua de evaluación**. La versión de evaluación de Aspose.PDF for Rust ofrece toda la funcionalidad del producto, pero todas las páginas de los archivos generados llevan una marca de agua con el texto “Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd.” en la parte superior.
- **Limitar la cantidad de páginas que pueden procesarse**. En la versión de evaluación, solo puede procesar las primeras cuatro páginas de un documento.

### Uso en producción

Se requiere una clave de licencia comercial en un entorno de producción. Por favor, contáctenos para adquirir una licencia comercial.

### Aplicar licencia

Aplicar una licencia para habilitar la funcionalidad completa de Aspose.PDF para Rust usando un archivo de licencia (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```
---
title: Convertir PDF a EPUB, TeX, Texto, XPS en Rust
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /es/rust-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-20"
description: Este tema le muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc., utilizando Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Herramienta Rust para convertir PDF a EPUB, TeX, Texto y XPS
Abstract: Aspose.PDF for Rust via C++ ofrece potentes capacidades para convertir documentos PDF a varios formatos de archivo, incluidos DOCX, PPTX, HTML, EPUB, SVG y más. Esta funcionalidad permite a los desarrolladores extraer y reutilizar el contenido PDF sin problemas, manteniendo el formato, la estructura y la calidad en los diferentes formatos de salida. La biblioteca proporciona opciones flexibles para personalizar el proceso de conversión según requisitos específicos. La documentación incluye guías integrales y ejemplos de código para ayudar a los desarrolladores a implementar de manera eficiente la conversión de PDF a archivo dentro de sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Convertir PDF a EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** es un estándar de libro electrónico libre y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también admite contenido de diseño fijo. El formato está pensado como un formato único que los editores y casas de conversión pueden utilizar internamente, así como para la distribución y venta. Sustituye al estándar Open eBook.

El fragmento de código Rust proporcionado muestra cómo convertir un documento PDF a un EPUB usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir un archivo PDF a EPUB usando [save_epub](https://reference.aspose.com/pdf/rust-cpp/convert/save_epub/) la función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Epub-document
      pdf.save_epub("sample.epub")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF for Rust le presenta una aplicación en línea gratuita ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a EPUB con Aplicación gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convertir PDF a TeX

**Aspose.PDF for Rust** admite la conversión de PDF a TeX.
El formato de archivo LaTeX es un formato de archivo de texto con un marcado especial y se utiliza en el sistema de preparación de documentos basado en TeX para la composición tipográfica de alta calidad.

El fragmento de código Rust proporcionado demuestra cómo convertir un documento PDF en TeX usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir un archivo PDF a TeX usando [save_tex](https://reference.aspose.com/pdf/rust-cpp/convert/save_tex/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as TeX-document
      pdf.save_tex("sample.tex")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF for Rust le presenta una aplicación en línea gratuita ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a LaTeX/TeX con aplicación gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF a TXT

El fragmento de código Rust proporcionado muestra cómo convertir un documento PDF a TXT usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir un archivo PDF a TXT usando [save_txt](https://reference.aspose.com/pdf/rust-cpp/convert/save_txt/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Txt-document
      pdf.save_txt("sample.txt")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir Convert PDF a Texto en línea**

Aspose.PDF for Rust le presenta una aplicación en línea gratuita ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a Texto con la Aplicación Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a XPS

El tipo de archivo XPS está asociado principalmente con la XML Paper Specification de Microsoft Corporation. La XML Paper Specification (XPS), anteriormente con el nombre en código Metro y que engloba el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

**Aspose.PDF for Rust** ofrece la posibilidad de convertir archivos PDF a <abbr title="XML Paper Specification">XPS</abbr> formato. Intentemos usar el fragmento de código presentado para convertir archivos PDF a formato XPS con Rust.

El fragmento de código Rust proporcionado demuestra cómo convertir un documento PDF a XPS utilizando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir un archivo PDF a XPS usando [save_xps](https://reference.aspose.com/pdf/rust-cpp/convert/save_xps/) la función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Xps-document
      pdf.save_xps("sample.xps")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF for Rust le presenta una aplicación en línea gratuita ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a XPS con Aspose.PDF y aplicación gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convertir PDF a PDF en escala de grises

El fragmento de código Rust proporcionado demuestra cómo convertir la primera página de un documento PDF en un PDF en escala de grises utilizando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una página PDF a PDF en escala de grises usando [página_escala_de_grises](https://reference.aspose.com/pdf/rust-cpp/organize/page_grayscale/) función.

Este ejemplo convierte una página específica de su PDF a escala de grises:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Convert page to black and white
      pdf.page_grayscale(1)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_page1_grayscale.pdf")?;

      Ok(())
  }
```

## Convertir PDF a Markdown

El fragmento de código Rust proporcionado demuestra cómo convertir un documento PDF en un archivo Markdown (.md) utilizando Aspose.PDF for Rust.

1. Abra el archivo PDF de origen.
1. Convertir PDF a Markdown.
1. Guarda el documento PDF abierto como un archivo Markdown.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Markdown-document
      pdf.save_markdown("sample.md")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a MD en línea**

Aspose.PDF for Rust le presenta una aplicación en línea gratuita ["PDF a MD"](https://products.aspose.app/pdf/conversion/md), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a MD con aplicación gratuita](pdf_to_md.png)](https://products.aspose.app/pdf/conversion/md)
{{% /alert %}}

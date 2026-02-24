---
title: Convertir PDF a EPUB, LaTeX, Texto, XPS en Python
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /es/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: Este tema le muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc., utilizando Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a otros formatos en Python
Abstract: El artículo ofrece una guía completa sobre cómo convertir archivos PDF a varios formatos usando Aspose.PDF para Python. Cubre la conversión de PDFs a formatos EPUB, LaTeX/TeX, Texto, XPS y XML. Cada sección comienza con una invitación a probar las aplicaciones gratuitas en línea proporcionadas por Aspose para convertir PDFs a los formatos correspondientes, resaltando la facilidad de uso y la calidad de estas herramientas.
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intente convertir PDF a EPUB en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde podrá probar la funcionalidad y la calidad que ofrece.

[![Conversión de Aspose.PDF de PDF a EPUB con aplicación gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> es un estándar de libros electrónicos libre y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también soporta contenido de diseño fijo. El formato está pensado como un formato único que los editores y casas de conversión pueden usar internamente, así como para distribución y venta. Sustituye al estándar Open eBook.

Aspose.PDF para Python también admite la función de convertir documentos PDF al formato EPUB. Aspose.PDF para Python tiene una clase llamada 'EpubSaveOptions' que puede usarse como segundo argumento del método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para generar un archivo EPUB.
Por favor, intente usar el siguiente fragmento de código para cumplir con este requisito con Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF a LaTeX/TeX

**Aspose.PDF for Python via .NET** soporta la conversión de PDF a LaTeX/TeX.
El formato de archivo LaTeX es un formato de texto con marcas especiales y se utiliza en el sistema de preparación de documentos basado en TeX para composición de alta calidad.

{{% alert color="success" %}}
**Intente convertir PDF a LaTeX/TeX en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puede probar la funcionalidad y la calidad que ofrece.

[![Conversión de Aspose.PDF de PDF a LaTeX/TeX con aplicación gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) que proporciona la propiedad OutDirectoryPath para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de convertir archivos PDF al formato TEX con Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Convertir PDF a Texto

**Aspose.PDF para Python** soporta la conversión de todo el documento PDF y de una sola página a un archivo de Texto. Puede convertir un documento PDF a un archivo TXT usando la clase 'TextDevice'. El siguiente fragmento de código explica cómo extraer el texto de todas las páginas.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intente convertir PDF a Texto en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puede probar la funcionalidad y la calidad que ofrece.

[![Conversión de Aspose.PDF de PDF a Texto con aplicación gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a XPS

**Aspose.PDF para Python** brinda la posibilidad de convertir archivos PDF al formato XPS. Intentemos usar el fragmento de código presentado para convertir archivos PDF al formato XPS con Python.

{{% alert color="success" %}}
**Intente convertir PDF a XPS en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puede probar la funcionalidad y la calidad que ofrece.

[![Conversión de Aspose.PDF de PDF a XPS con aplicación gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está asociado principalmente con la especificación XML Paper Specification de Microsoft Corporation. La especificación XML Paper Specification (XPS), anteriormente conocida como Metro y que engloba el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) que se usa como segundo argumento del método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para generar el archivo XPS.

El siguiente fragmento de código muestra el proceso de convertir un archivo PDF al formato XPS.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF a MD

Aspose.PDF tiene la clase 'MarkdownSaveOptions()', que convierte un documento PDF a formato Markdown (MD) mientras preserva imágenes y recursos.

1. Carga el PDF fuente usando 'ap.Document'.
1. Crea una instancia de 'MarkdownSaveOptions'.
1. Establece 'resources_directory_name' a 'images' – las imágenes extraídas se almacenarán en esta carpeta.
1. Guarda el documento Markdown convertido usando las opciones configuradas.
1. Imprime un mensaje de confirmación después de la conversión.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Un archivo Markdown con texto e imágenes enlazadas almacenadas en la carpeta de imágenes especificada.

## Convertir PDF a MobiXML

Este método convierte un documento PDF al formato MOBI (MobiXML), que se usa comúnmente para eBooks en dispositivos Kindle.

1. Carga el documento PDF fuente usando 'ap.Document'.
1. Guarda el documento con el formato 'ap.SaveFormat.MOBI_XML'.
1. Imprime un mensaje de confirmación una vez que la conversión haya finalizado.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```

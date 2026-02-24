---
title: Convertir HTML a PDF en Python
linktitle: Convertir archivo HTML a PDF
type: docs
weight: 40
url: /es/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Aprenda cómo convertir contenido HTML en un documento PDF usando Aspose.PDF para Python a través de .NET
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir HTML a PDF usando Aspose.PDF para Python
Abstract: Aspose.PDF para Python a través de .NET ofrece una solución robusta para crear archivos PDF a partir de páginas web y código HTML sin procesar dentro de aplicaciones. Este artículo proporciona una guía sobre cómo convertir HTML a PDF usando Python, describiendo el uso de Aspose.PDF para Python, una API de manipulación de PDF que permite una conversión sin problemas de documentos HTML al formato PDF. El proceso de conversión puede personalizarse según sea necesario. El artículo incluye un ejemplo de código Python que demuestra el proceso de conversión, que implica crear una instancia de la clase HtmlLoadOptions, inicializar un objeto Document y guardar el documento PDF resultante usando el método Document.Save(). Además, Aspose ofrece una herramienta en línea para convertir HTML a PDF, permitiendo a los usuarios explorar la funcionalidad y la calidad del proceso de conversión.
---

## Conversión de HTML a PDF con Python

**Aspose.PDF para Python** es una API de manipulación de PDF que le permite convertir cualquier documento HTML existente a PDF sin problemas. El proceso de convertir HTML a PDF puede personalizarse de forma flexible.

## Convertir HTML a PDF

El siguiente ejemplo de código Python muestra cómo convertir un documento HTML a PDF.

1. Crear una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Inicializar el objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Guardar el documento PDF de salida llamando al método **document.save()**.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir HTML a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["HTML a PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), donde puede probar e investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF HTML a PDF usando la aplicación gratuita](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Convertir HTML a PDF usando tipo de medio

Este ejemplo muestra cómo convertir un archivo HTML a PDF usando Aspose.PDF para Python a través de .NET con opciones de renderizado específicas.

1. Crear una instancia de la clase [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/). El 'html_media_type' aplica reglas CSS destinadas a la visualización en pantalla. La propiedad 'html_media_type' puede tener múltiples valores. Puede configurarla como HtmlMediaType.SCREEN o HtmlMediaType.PRINT.
1. Cargar el HTML en un ap.Document usando las opciones de carga.
1. Guardar el documento como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir regla CSS @page de prioridad al PDF

Algunos documentos pueden contener configuraciones de diseño que utilizan [la regla Page](https://developer.mozilla.org/en-US/docs/Web/CSS/@page), lo que puede crear ambigüedad al generar el diseño. Puede controlar la prioridad usando la propiedad 'is_priority_css_page_rule'. Si esta propiedad se establece en 'True', la regla CSS se aplica primero.

1. Crear una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Establecer 'is_priority_css_page_rule = False' para desactivar la priorización de reglas CSS @page, permitiendo que otros estilos tengan precedencia.
1. Cargar el HTML en un ap.Document con las opciones configuradas.
1. Guardar el documento como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir HTML a PDF con fuentes incrustadas

Este ejemplo muestra cómo convertir un archivo HTML a PDF mientras se incrustan fuentes. Si necesita un documento PDF con fuentes incrustadas, debe establecer 'is_embed_fonts' en True.

1. Crear 'HtmlLoadOptions()' para configurar la conversión de HTML a PDF.
1. Establecer 'is_embed_fonts = True' para garantizar que todas las fuentes usadas en el HTML se incrusten directamente en el PDF, preservando la fidelidad visual.
1. Cargar el HTML en un ap.Document con estas opciones.
1. Guardar el documento como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Renderizar contenido en una sola página durante la conversión de HTML a PDF

Este ejemplo demuestra cómo convertir un archivo HTML en un PDF de una sola página usando Aspose.PDF para Python.
Puede mostrar todo el contenido en una sola página usando la propiedad 'is_render_to_single_page'.

1. Crear una instancia de 'HtmlLoadOptions()' para configurar el proceso de conversión.
1. Habilitar 'is_render_to_single_page' para renderizar todo el contenido HTML en una única página PDF continua.
1. Cargar el documento con las opciones configuradas en un 'ap.Document'.
1. Guardar el resultado como un archivo PDF.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## Convertir MHTML a PDF

Este ejemplo muestra cómo convertir un archivo MHT (MHTML) en un documento PDF utilizando Aspose.PDF para Python con dimensiones de página específicas.

1. Crea una instancia de ap.MhtLoadOptions() para configurar el procesamiento del archivo MHT.
1. Establece varios parámetros, como el tamaño de página.
1. Inicializa el documento con el archivo de entrada y las opciones de carga configuradas.
1. Guarda el documento resultante como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

---
title: Convertir otros formatos de archivo a PDF en Python
linktitle: Convertir otros formatos de archivo a PDF
type: docs
weight: 80
url: /es/python-net/convert-other-files-to-pdf/
lastmod: "2025-09-01"
description: Este tema le muestra cómo Aspose.PDF permite convertir otros formatos de archivo como EPUB, MD, PCL, XPS, PS, XML y LaTeX a documento PDF.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cómo convertir otros formatos de archivo a PDF en Python
Abstract: Este artículo proporciona una guía completa sobre la conversión de varios formatos de archivo a PDF usando Python, aprovechando las capacidades de Aspose.PDF para Python a través de .NET. El documento describe los procesos de conversión para varios formatos, incluidos EPUB, Markdown, PCL, Texto, XPS, PostScript, XML, XSL-FO y LaTeX/TeX. Cada sección ofrece fragmentos de código específicos e instrucciones para implementar estas conversiones. El artículo enfatiza la utilidad de las características de Aspose.PDF, como las opciones de carga adaptadas a cada tipo de archivo, para garantizar una conversión precisa y eficiente. Además, destaca la disponibilidad de aplicaciones gratuitas de conversión en línea para que los usuarios exploren la funcionalidad de primera mano. La guía sirve como un recurso práctico para desarrolladores que buscan integrar capacidades de conversión a PDF en sus aplicaciones Python.
---

Este artículo explica cómo **convertir varios otros tipos de formatos de archivo a PDF usando Python**. Cubre los siguientes temas.

## Convertir OFD a PDF

OFD significa Open Fixed-layout Document (también llamado formato Open Fixed Document). Es una norma nacional china (GB/T 33190-2016) para documentos electrónicos, introducida como una alternativa al PDF.

Pasos para convertir OFD a PDF en Python:

1. Configurar las opciones de carga OFD usando OfdLoadOptions().
1. Cargar el documento OFD.
1. Guardar como PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir LaTeX/TeX a PDF

El formato de archivo LaTeX es un formato de archivo de texto con marcado en la derivada LaTeX de la familia de lenguajes TeX y LaTeX es un formato derivado del sistema TeX. LaTeX (ˈleɪtɛk/lay-tek o lah-tek) es un sistema de preparación de documentos y un lenguaje de marcado de documentos. Se utiliza ampliamente para la comunicación y publicación de documentos científicos en muchos campos, incluidos matemáticas, física y ciencia de la computación. También desempeña un papel clave en la preparación y publicación de libros y artículos que contienen material multilingüe complejo, como coreano, japonés, caracteres chinos y árabe, incluidas ediciones especiales.

LaTeX usa el programa de composición tipográfica TeX para formatear su salida, y está escrito en el lenguaje de macros TeX.

{{% alert color="success" %}}
**Intente convertir LaTeX/TeX a PDF en línea**

Aspose.PDF para Python a través de .NET le presenta una aplicación gratuita en línea ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), donde puede intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF LaTeX/TeX a PDF con App Gratuita](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Pasos para convertir TEX a PDF en Python:

1. Configurar las opciones de carga LaTeX usando LatexLoadOptions().
1. Cargar el documento LaTeX.
1. Guardar como PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
## Convertir OFD a PDF

OFD significa Open Fixed-layout Document (a veces llamado formato Open Fixed Document). Es una norma nacional china (GB/T 33190-2016) para documentos electrónicos, introducida como una alternativa al PDF.

Pasos para convertir OFD a PDF en Python:

1. Configurar las opciones de carga OFD usando OfdLoadOptions().
1. Cargar el documento OFD.
1. Guardar como PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir LaTeX/TeX a PDF

El formato de archivo LaTeX es un formato de archivo de texto con marcado en la derivada LaTeX de la familia de lenguajes TeX y LaTeX es un formato derivado del sistema TeX. LaTeX (ˈleɪtɛk/lay-tek o lah-tek) es un sistema de preparación de documentos y un lenguaje de marcado de documentos. Se utiliza ampliamente para la comunicación y publicación de documentos científicos en muchos campos, incluidos matemáticas, física y ciencia de la computación. También tiene un papel destacado en la preparación y publicación de libros y artículos que contienen materiales multilingües complejos, como sánscrito y árabe, incluidas ediciones críticas. LaTeX usa el programa de composición tipográfica TeX para formatear su salida, y está escrito en el lenguaje de macros TeX.

{{% alert color="success" %}}
**Intente convertir LaTeX/TeX a PDF en línea**

Aspose.PDF para Python a través de .NET le presenta una aplicación gratuita en línea ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), donde puede intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF LaTeX/TeX a PDF con App Gratuita](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Pasos para convertir TEX a PDF en Python:

1. Configurar las opciones de carga LaTeX usando LatexLoadOptions().
1. Cargar el documento LaTeX.
1. Guardar como PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir EPUB a PDF

**Aspose.PDF for Python vía .NET** le permite simplemente convertir archivos EPUB a formato PDF.

EPUB (abreviatura de electronic publication) es un estándar de libros electrónicos gratuito y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub. EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular.

<abbr title="electronic publication">EPUB</abbr> también soporta contenido de diseño fijo. El formato está pensado como un único formato que los editores y casas de conversión pueden usar internamente, así como para distribución y venta. Reemplaza el estándar Open eBook. La versión EPUB 3 también cuenta con el respaldo del Book Industry Study Group (BISG), una asociación líder en la industria del libro para prácticas estandarizadas, investigación, información y eventos, para el empaquetado de contenidos.

{{% alert color="success" %}}
**Intente convertir EPUB a PDF en línea**

Aspose.PDF for Python vía .NET le presenta la aplicación gratuita en línea ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF EPUB a PDF con App Gratuita](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Pasos para convertir EPUB a PDF en Python:

1. Cargue el documento EPUB con EpubLoadOptions().
1. Convierta EPUB a PDF.
1. Imprima la confirmación.

El siguiente fragmento de código muestra cómo convertir archivos EPUB a formato PDF con Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.EpubLoadOptions()
    document = ap.Document(path_infile, load_options)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir Markdown a PDF

**Esta función es compatible con la versión 19.6 o superior.**

{{% alert color="success" %}}
**Intente convertir Markdown a PDF en línea**

Aspose.PDF for Python vía .NET le presenta la aplicación gratuita en línea ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF Markdown a PDF con App Gratuita](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Este fragmento de código de Aspose.PDF for Python vía .NET ayuda a convertir archivos Markdown en PDFs, permitiendo un mejor intercambio de documentos, preservación del formato y compatibilidad de impresión.

El siguiente fragmento de código muestra cómo usar esta funcionalidad con la biblioteca Aspose.PDF:

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.MdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir PCL a PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) es un lenguaje de impresora de Hewlett-Packard desarrollado para acceder a funciones estándar de la impresora. Los niveles de PCL 1 a 5e/5c son lenguajes basados en comandos que utilizan secuencias de control que se procesan e interpretan en el orden en que se reciben. A nivel de consumidor, los flujos de datos de PCL son generados por un controlador de impresión. La salida de PCL también puede generarse fácilmente mediante aplicaciones personalizadas.

{{% alert color="success" %}}
**Intente convertir PCL a PDF en línea**

Aspose.PDF para .NET le presenta la aplicación gratuita en línea ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF PCL a PDF con App Gratuita](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Para permitir la conversión de PCL a PDF, Aspose.PDF tiene la clase [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) que se usa para inicializar el objeto LoadOptions. Posteriormente, este objeto se pasa como argumento durante la inicialización del objeto Document y ayuda al motor de renderizado PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de convertir un archivo PCL a formato PDF.

Pasos para convertir PCL a PDF en Python:

1. Cargue las opciones para PCL usando PclLoadOptions().
1. Cargue el documento.
1. Guarde como PDF.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir texto preformateado a PDF

**Aspose.PDF for Python vía .NET** soporta la función de convertir texto plano y archivos de texto preformateado a formato PDF.

Convertir texto a PDF significa añadir fragmentos de texto a la página PDF. En cuanto a los archivos de texto, tratamos con 2 tipos de texto: preformateado (por ejemplo, 25 líneas con 80 caracteres por línea) y texto sin formato (texto plano). Dependiendo de nuestras necesidades, podemos controlar esta incorporación nosotros mismos o confiarla a los algoritmos de la biblioteca.

{{% alert color="success" %}}
**Intente convertir TEXTO a PDF en línea**

Aspose.PDF for Python vía .NET le presenta la aplicación gratuita en línea ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF TEXTO a PDF con App Gratuita](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Pasos para convertir TEXTO a PDF en Python:

1. Lea el archivo de texto de entrada línea por línea.
1. Configure una fuente monoespaciada (Courier New) para una alineación de texto constante.
1. Cree un nuevo documento PDF y añada la primera página con márgenes y configuraciones de fuente personalizados.
1. Recorra las líneas del archivo de texto. Para simular una máquina de escribir, utilizamos la fuente 'monospace_font' con tamaño 12.
1. Limite la creación de páginas a 4.
1. Guarde el PDF final en la ruta especificada.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    with open(path_infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir PostScript a PDF

Este ejemplo muestra cómo convertir un archivo PostScript en un documento PDF usando Aspose.PDF para Python a través de .NET.

1. Crear una instancia de 'PsLoadOptions' para interpretar correctamente el archivo PS.
1. Cargar el archivo 'PostScript' en un objeto Document utilizando las opciones de carga.
1. Guardar el documento en formato PDF en la ruta de salida deseada.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PsLoadOptions()

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir XPS a PDF

**Aspose.PDF para Python a través de .NET** admite la conversión de archivos <abbr title="XML Paper Specification">XPS</abbr> al formato PDF. Consulte este artículo para resolver sus tareas.

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con el nombre en código Metro y que engloba el concepto de marketing Ruta de Impresión de Nueva Generación (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en su sistema operativo Windows.

El siguiente fragmento de código muestra el proceso de convertir un archivo XPS al formato PDF con Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XpsLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intente convertir el formato XPS a PDF en línea**

Aspose.PDF para Python a través de .NET le presenta una aplicación en línea gratuita ["XPS a PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF XPS a PDF con Aplicación Gratuita](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convertir XSL-FO a PDF

El siguiente fragmento de código puede usarse para convertir un XSLFO al formato PDF con Aspose.PDF para Python a través de .NET:

```python

    from os import path
    import aspose.pdf as ap

    path_xsltfile = path.join(self.data_dir, xsltfile)
    path_xmlfile = path.join(self.data_dir, xmlfile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XslFoLoadOptions(path_xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
    )
    document = ap.Document(path_xmlfile, load_options)
    document.save(path_outfile)

    print(xmlfile + " converted into " + outfile)
```

## Convertir XML con XSLT a PDF

Este ejemplo muestra cómo convertir un archivo XML en un PDF primero transformándolo a HTML usando una plantilla XSLT y luego cargando el HTML en Aspose.PDF.

1. Crear una instancia de 'HtmlLoadOptions' para configurar la conversión de HTML a PDF.
1. Cargar el archivo HTML transformado en un objeto Document de Aspose.PDF.
1. Guardar el documento como PDF en la ruta de salida especificada.
1. Eliminar el archivo HTML temporal después de una conversión exitosa.

```python

    from os import path
    import aspose.pdf as ap

    def transform_xml_to_html(xml_file, xslt_file, html_file):
        from lxml import etree
        """
        Transform XML to HTML using XSLT and return as a stream
        """
        # Parse XML document
        xml_doc = etree.parse(xml_file)

        # Parse XSLT stylesheet
        xslt_doc = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_doc)

        # Apply transformation
        result = transform(xml_doc)

        # Save result to HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(result))


    def convert_XML_to_PDF(template, infile, outfile):
        path_infile = path.join(data_dir, infile)
        path_outfile = path.join(data_dir, "python", outfile)
        path_template = path.join(data_dir, template)
        path_temp_file = path.join(data_dir, "temp.html")

        load_options = ap.HtmlLoadOptions()
        transform_xml_to_html(path_infile, path_template, path_temp_file)

        document = ap.Document(path_temp_file, load_options)
        document.save(path_outfile)

        if path.exists(path_temp_file):
            os.remove(path_temp_file)

        print(infile + " converted into " + outfile)
```


---
title: Convertir formatos de imagen a PDF en Python
linktitle: Convertir imágenes a PDF
type: docs
weight: 60
url: /es/python-net/convert-images-format-to-pdf/
lastmod: "2026-04-14"
description: Aprenda cómo convertir BMP, CGM, DICOM, PNG, TIFF, EMF, SVG y otros formatos de imagen a PDF en Python con Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Cómo convertir imágenes a PDF en Python
Abstract: Este artículo ofrece una guía completa sobre cómo convertir varios formatos de imagen a PDF utilizando Python, aprovechando específicamente la biblioteca Aspose.PDF para Python via .NET. El artículo cubre una gama de formatos de imagen que incluyen BMP, CGM, DICOM, EMF, GIF, PNG, SVG y TIFF. Cada sección detalla los pasos necesarios para realizar la conversión, proporcionando fragmentos de código para ilustrar el proceso. Por ejemplo, convertir BMP a PDF implica crear un nuevo documento PDF, definir la ubicación de la imagen, insertar la imagen y guardar el documento. De manera similar, para formatos como CGM, DICOM y otros, se describen opciones de carga específicas y pasos de procesamiento. El artículo también destaca las ventajas de usar Aspose.PDF para estas tareas, como su soporte para diferentes métodos de codificación y la capacidad de procesar imágenes de un solo fotograma y de varios fotogramas.
---

## Conversiones relacionadas

- [Convertir PDF a formatos de imagen](/pdf/es/python-net/convert-pdf-to-images-format/) cuando necesites el flujo de trabajo inverso.
- [Convertir HTML a PDF](/pdf/es/python-net/convert-html-to-pdf/) para contenido web y fuentes MHTML.
- [Convertir otros formatos de archivo a PDF](/pdf/es/python-net/convert-other-files-to-pdf/) para EPUB, XPS, texto y otras entradas que no sean imágenes.

## Conversiones de imágenes Python a PDF

**Aspose.PDF for Python via .NET** permite convertir diferentes formatos de imágenes a archivos PDF. Nuestra biblioteca muestra fragmentos de código para convertir los formatos de imagen más populares, como - BMP, CGM, DICOM, EMF, JPG, PNG, SVG y formatos TIFF.

## Convertir BMP a PDF

Convierta archivos BMP a documento PDF utilizando la biblioteca **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> Las imágenes son archivos con extensión. BMP representa archivos de imagen bitmap que se utilizan para almacenar imágenes digitales bitmap. Estas imágenes son independientes del adaptador gráfico y también se denominan formato de archivo bitmap independiente del dispositivo (DIB).

Puede convertir archivos BMP a PDF con la API Aspose.PDF for Python via .NET. Por lo tanto, puede seguir los siguientes pasos para convertir imágenes BMP:

Pasos para convertir BMP a PDF en Python:

1. Crear un documento PDF vacío.
1. Cree la página que necesite, por ejemplo, creamos A4, pero puede especificar su propio formato.
1. Coloca la imagen (de infile) dentro de la página usando el rectángulo definido.
1. Guarde el documento como PDF.

Entonces el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir BMP a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["BMP a PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión BMP a PDF con Aspose.PDF usando una aplicación gratuita](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir CGM a PDF

Convertir un CGM (Computer Graphics Metafile) a PDF (u otro formato compatible) usando Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> es una extensión de archivo para un formato Computer Graphics Metafile, utilizado comúnmente en aplicaciones CAD (computer-aided design) y de gráficos de presentación. CGM es un formato de gráficos vectoriales que admite tres métodos de codificación diferentes: binario (best for program read speed), basado en caracteres (produces the smallest file size and allows for faster data transfers) o codificación en texto claro (allows users to read and modify the file with a text editor).

Revise el siguiente fragmento de código para convertir archivos CGM a formato PDF.

Pasos para convertir CGM a PDF en Python:

1. Definir rutas de archivo
1. Establecer opciones de carga para CGM.
1. Convertir CGM a PDF
1. Mensaje de Conversión de Impresión

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = apdf.CgmLoadOptions()

    # Open PDF document
    document = apdf.Document(path_infile, options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convertir DICOM a PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format es el estándar de la industria médica para la creación, almacenamiento, transmisión y visualización de imágenes médicas digitales y documentos de pacientes examinados.

**Aspose.PDF for Python** permite convertir imágenes DICOM y SVG, pero por razones técnicas para añadir imágenes es necesario especificar el tipo de archivo que se añadirá al PDF.

El siguiente fragmento de código muestra cómo convertir archivos DICOM al formato PDF con Aspose.PDF. Debe cargar la imagen DICOM, colocar la imagen en una página de un archivo PDF y guardar la salida como PDF. Utilizamos la biblioteca adicional pydicom para establecer las dimensiones de esta imagen. Si desea posicionar la imagen en la página, puede omitir este fragmento de código.

1. Inicializa un nuevo 'ap.Document()' y agrega una página
1. Insertar imagen DICOM. Cree un apdf.Image(), establezca su tipo a DICOM y asígnele la ruta del archivo.
1. Ajustar el tamaño de página. Coincidir las dimensiones de la página PDF con el tamaño de la imagen DICOM, eliminar márgenes.
1. Añade la imagen a la página, guarda el documento en el archivo de salida.

1. Cargue el archivo DICOM.
1. Extraer dimensiones de la imagen.
1. Imprimir tamaño de imagen.
1. Cree un nuevo documento PDF.
1. Prepare la imagen DICOM para PDF.
1. Establecer el tamaño de página y los márgenes del PDF.
1. Agregar la imagen a la página.
1. Guardar el PDF.
1. Mensaje de conversión de impresión.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    # Load the DICOM file
    dicom_file = pydicom.dcmread(path_infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = apdf.Document()
    page = document.pages.add()
    image = apdf.Image()
    image.file_type = apdf.ImageFileType.DICOM
    image.file = path_infile

    # Set page dimensions

    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir DICOM a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["DICOM a PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de DICOM a PDF usando la aplicación gratuita](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF a PDF

<abbr title="Enhanced metafile format">EMF</abbr> almacena imágenes gráficas de forma independiente del dispositivo. Los Metafiles EMF están compuestos por registros de longitud variable en orden cronológico que pueden renderizar la imagen almacenada después de analizarla en cualquier dispositivo de salida.

El siguiente fragmento de código muestra cómo convertir un EMF a PDF con Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(path_infile, rectangle)

    # Save the file into PDF format
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir EMF a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["EMF a PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de EMF a PDF con Aspose.PDF usando una aplicación gratuita](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir GIF a PDF

Convertir archivos GIF a documento PDF usando la biblioteca **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> es capaz de almacenar datos comprimidos sin pérdida de calidad en un formato de no más de 256 colores. El formato GIF independiente del hardware se desarrolló en 1987 (GIF87a) por CompuServe para transmitir imágenes bitmap a través de redes.

Entonces el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir GIF a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["GIF a PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de GIF a PDF usando aplicación gratuita](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Convertir PNG a PDF

**Aspose.PDF for Python via .NET** soporta la función de convertir imágenes PNG a formato PDF. Consulte el siguiente fragmento de código para realizar su tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen rasterizada que utiliza compresión sin pérdida, lo que lo hace popular entre sus usuarios.

Puedes convertir una imagen PNG a PDF usando los siguientes pasos:

1. Crear un nuevo documento PDF.
1. Definir la ubicación de la imagen.
1. Guardar el PDF.
1. Mensaje de conversión de impresión.

Además, el fragmento de código a continuación muestra cómo convertir PNG a PDF con Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Intenta convertir PNG a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["PNG a PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PNG a PDF usando la aplicación gratuita](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG a PDF

**Aspose.PDF for Python via .NET** explica cómo convertir imágenes SVG al formato PDF y cómo obtener las dimensiones del archivo SVG de origen.

Scalable Vector Graphics (SVG) es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio de la World Wide Web (W3C) desde 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> las imágenes y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscadas, indexadas, programadas y, si es necesario, comprimidas. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

{{% alert color="success" %}}
**Intenta convertir el formato SVG a PDF en línea**

Aspose.PDF for Python via .NET le presenta una aplicación en línea gratuita ["SVG a PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de SVG a PDF con Aspose.PDF y aplicación gratuita](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

El siguiente fragmento de código muestra el proceso de convertir un archivo SVG a formato PDF con Aspose.PDF for Python.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.SvgLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir TIFF a PDF

**Aspose.PDF** formato de archivo compatible, ya sea una imagen TIFF de un solo fotograma o de varios fotogramas. Significa que puedes convertir la imagen TIFF a PDF.

TIFF o TIF, Tagged Image File Format, representa imágenes ráster que están destinadas a usarse en una variedad de dispositivos que cumplen con este estándar de formato de archivo. La imagen TIFF puede contener varios fotogramas con diferentes imágenes. El formato de archivo Aspose.PDF también es compatible, ya sea una imagen TIFF de un solo fotograma o de varios fotogramas.

Puede convertir TIFF a PDF de la misma manera que los demás formatos de archivo raster gráficos:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir CDR a PDF

El siguiente fragmento de código muestra cómo cargar un archivo CorelDRAW (CDR) y guardarlo como PDF usando 'CdrLoadOptions' en Aspose.PDF for Python via .NET.

1. Crea 'CdrLoadOptions()' para configurar cómo se debe cargar el archivo CDR.
1. Inicializa un objeto Document con el archivo CDR y las opciones de carga.
1. Guarde el documento como un PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.CdrLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Convertir JPEG a PDF

Este ejemplo muestra cómo convertir un archivo JPEG a PDF usando Aspose.PDF for Python via .NET.

1. Cree un nuevo documento PDF.
1. Agregar una nueva página.
1. Defina el rectángulo de colocación (tamaño A4: 595x842 puntos).
1. Inserte la imagen en la página.
1. Guardar el PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

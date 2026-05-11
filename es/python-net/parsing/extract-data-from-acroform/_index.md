---
title: Extraer datos de AcroForm usando Python
linktitle: Extraer datos de AcroForm
type: docs
weight: 50
url: /es/python-net/extract-data-from-acroform/
description: Aspose.PDF facilita la extracción de datos de campos de formulario de archivos PDF. Aprende cómo extraer datos de AcroForms y guardarlos en formato JSON, XML o FDF.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer datos de AcroForm mediante Python
Abstract: El artículo proporciona una guía completa sobre el uso de Aspose.PDF for Python para gestionar campos de formulario dentro de documentos PDF. Detalla varios métodos para extraer, manipular y exportar datos de formularios desde PDFs. El artículo comienza demostrando cómo extraer los valores de los campos de formulario y almacenarlos en un diccionario, para luego generar los datos en formato JSON. Además, ilustra la exportación de datos de formulario directamente a archivos JSON, mejorando las capacidades de serialización de datos. Asimismo, el artículo cubre la exportación de datos de formulario a otros formatos como XML, FDF (Forms Data Format) y XFDF, que son útiles para el intercambio de datos y el almacenamiento estructurado de información. Cada sección incluye fragmentos de código Python para ayudar en la comprensión e implementación. En conjunto, el artículo sirve como un recurso práctico para desarrolladores que desean integrar la manipulación de formularios PDF en sus aplicaciones Python.
---

## Extraer campos de formulario del documento PDF

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) del `aspose.pdf.facades` namespace proporciona una forma sencilla de leer los datos de los campos AcroForm sin abrir el modelo de objeto del documento completo. Iterar sobre `form.field_names` para obtener el nombre de cada campo presente en el formulario, luego llame `form.get_field(name)` para recuperar su valor actual.

1. Construir un `Form` objeto pasando la ruta del archivo de entrada.
1. Iterar sobre `form.field_names` enumerar todos los nombres de campo.
1. Llamar `form.get_field(name)` para cada nombre y almacena el resultado en un diccionario.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Recuperar valor del campo de formulario por título

Cuando sabes el nombre exacto del campo (title) definido en el formulario PDF, puedes obtener su valor directamente con `form.get_field(name)` sin iterar sobre toda la colección de campos. Este es el enfoque más rápido cuando solo se necesitan campos específicos.

1. Construir un [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) objeto con la ruta del archivo de entrada.
1. Llamar `form.get_field("FieldName")` usando el título exacto del campo tal como aparece en el PDF.
1. Utilice el valor de cadena devuelto según sea necesario en su aplicación.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Extraer campos de formulario del documento PDF a JSON

Hay dos maneras de exportar datos de AcroForm a JSON. La primera utiliza la funcionalidad incorporada `export_json` método en [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), que serializa todos los datos de campo directamente a un flujo de archivo en una sola llamada.

1. Construir un `Form` objeto con la ruta del archivo de entrada.
1. Abra el archivo de salida como un flujo binario usando `FileIO`.
1. Llamar `form.export_json(stream, True)` para escribir la salida JSON.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

El segundo enfoque crea un diccionario de Python a partir de `field_names` y `get_field`, luego lo serializa con `json.dumps`. Utilice esto cuando necesite transformar o filtrar los datos antes de escribirlos.

1. Iterar sobre `form.field_names` y rellenar un diccionario con los valores de los campos.
1. Serializa el diccionario con `json.dumps(form_data, indent=4)`.
1. Escribe la cadena JSON resultante en el archivo de salida.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extraer datos a XML desde un archivo PDF

La exportación de XML es útil para integrar los datos de formularios PDF con sistemas que consumen feeds XML estructurados o esquemas. El [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) la clase proporciona `export_xml` para manejar la conversión en un solo paso.

1. Crear un `Form` instancia y enlaza el PDF con `form.bind_pdf(path)`.
1. Abra el archivo de salida como un flujo binario.
1. Llamar `form.export_xml(stream)` para escribir todos los datos de los campos como XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Exportar datos a FDF desde un archivo PDF

FDF (Forms Data Format) es el formato de intercambio estándar para los datos de AcroForm y es ampliamente compatible con los visualizadores de PDF y las herramientas de procesamiento. Usar `export_fdf` en el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) clase para producir un archivo FDF independiente que pueda importarse de nuevo al PDF original o a otro formulario compatible.

1. Crear un `Form` instancia y vincula el PDF de origen con `form.bind_pdf(path)`.
1. Abra el archivo de salida como un flujo binario.
1. Llamar `form.export_fdf(stream)` para escribir los datos FDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Exportar datos a XFDF desde un archivo PDF

XFDF (Formato de Datos de Formularios XML) es el sucesor basado en XML de FDF y está mejor adaptado para su uso en servicios web y canalizaciones de datos modernas. Al igual que FDF, un archivo XFDF puede importarse de nuevo en un formulario PDF compatible. Usar `export_xfdf` en el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) clase para generar la salida.

1. Crear un `Form` instancia y vincula el PDF de origen con `form.bind_pdf(path)`.
1. Abra el archivo de salida como un flujo binario.
1. Llamar `form.export_xfdf(stream)` para escribir los datos XFDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

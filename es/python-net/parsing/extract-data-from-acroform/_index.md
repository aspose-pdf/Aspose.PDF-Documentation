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
Abstract: Este artículo ofrece una guía completa sobre el uso de Aspose.PDF for Python via .NET para gestionar campos de formulario en documentos PDF. Describe varios métodos para extraer, manipular y exportar datos de formulario. Comienza mostrando cómo extraer los valores de los campos y almacenarlos en un diccionario para generar salida JSON. También explica cómo exportar datos de formulario a XML, FDF y XFDF, formatos útiles para el intercambio de datos y el almacenamiento estructurado. Cada sección incluye fragmentos de código Python para facilitar la comprensión y la implementación.
---

## Extraer campos de formulario del documento PDF

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) del espacio de nombres `aspose.pdf.facades` proporciona una forma directa de leer los datos de los campos AcroForm sin abrir el modelo completo del documento. Recorra `form.field_names` para obtener cada nombre de campo presente en el formulario y luego llame a `form.get_field(name)` para recuperar su valor actual.

1. Construya un objeto `Form` pasando la ruta del archivo de entrada.
1. Recorra `form.field_names` para enumerar todos los nombres de campo.
1. Llame a `form.get_field(name)` para cada nombre y almacene el resultado en un diccionario.

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

## Obtener el valor del campo de formulario por título

Cuando conoce el nombre exacto del campo definido en el formulario PDF, puede obtener su valor directamente con `form.get_field(name)` sin recorrer toda la colección de campos. Este es el enfoque más rápido cuando solo necesita campos específicos.

1. Construya un objeto [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) con la ruta del archivo de entrada.
1. Llame a `form.get_field("FieldName")` usando el nombre exacto del campo tal como aparece en el PDF.
1. Utilice el valor de cadena devuelto según sea necesario en su aplicación.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Extraer campos de formulario de un documento PDF a JSON

Hay dos formas de exportar datos de AcroForm a JSON. La primera usa el método incorporado `export_json` de [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), que serializa todos los datos de los campos directamente en un flujo de archivo con una sola llamada.

1. Construya un objeto `Form` con la ruta del archivo de entrada.
1. Abra el archivo de salida como un flujo binario usando `FileIO`.
1. Llame a `form.export_json(stream, True)` para escribir la salida JSON.

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

El segundo enfoque construye un diccionario de Python a partir de `field_names` y `get_field`, y luego lo serializa con `json.dumps`. Use este método cuando necesite transformar o filtrar los datos antes de escribirlos.

1. Recorra `form.field_names` y rellene un diccionario con los valores de los campos.
1. Serialice el diccionario con `json.dumps(form_data, indent=4)`.
1. Escriba la cadena JSON resultante en el archivo de salida.

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

La exportación a XML es útil para integrar datos de formularios PDF con sistemas que consumen fuentes o esquemas XML estructurados. La clase [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) proporciona `export_xml` para realizar la conversión en un solo paso.

1. Cree una instancia de `Form` y vincule el PDF con `form.bind_pdf(path)`.
1. Abra el archivo de salida como un flujo binario.
1. Llame a `form.export_xml(stream)` para escribir todos los datos de los campos como XML.

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

FDF (Forms Data Format) es el formato de intercambio estándar para los datos de AcroForm y es ampliamente compatible con visores de PDF y herramientas de procesamiento. Use `export_fdf` en la clase [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) para generar un archivo FDF independiente que pueda importarse de nuevo en el PDF original o en otro formulario compatible.

1. Cree una instancia de `Form` y vincule el PDF de origen con `form.bind_pdf(path)`.
1. Abra el archivo de salida como un flujo binario.
1. Llame a `form.export_fdf(stream)` para escribir los datos FDF.

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

XFDF (XML Forms Data Format) es el sucesor basado en XML de FDF y está mejor adaptado a servicios web y canalizaciones de datos modernas. Al igual que FDF, un archivo XFDF puede importarse de nuevo en un formulario PDF compatible. Use `export_xfdf` en la clase [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) para generar la salida.

1. Cree una instancia de `Form` y vincule el PDF de origen con `form.bind_pdf(path)`.
1. Abra el archivo de salida como un flujo binario.
1. Llame a `form.export_xfdf(stream)` para escribir los datos XFDF.

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

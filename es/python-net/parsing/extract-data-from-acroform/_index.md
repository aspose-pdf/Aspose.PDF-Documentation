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
Abstract: El artículo ofrece una guía completa sobre el uso de Aspose.PDF para Python para gestionar campos de formulario dentro de documentos PDF. Detalla varios métodos para extraer, manipular y exportar datos de formularios desde PDFs. El artículo comienza demostrando cómo extraer los valores de los campos de formulario y almacenarlos en un diccionario, para luego presentar los datos en formato JSON. Además, muestra cómo exportar los datos del formulario directamente a archivos JSON, mejorando las capacidades de serialización de datos. Asimismo, el artículo cubre la exportación de datos de formularios a otros formatos como XML, FDF (Formato de Datos de Formularios) y XFDF, que son útiles para el intercambio de datos y el almacenamiento estructurado. Cada sección incluye fragmentos de código Python para ayudar en la comprensión e implementación. En conjunto, el artículo sirve como un recurso práctico para desarrolladores que buscan integrar la manipulación de formularios PDF en sus aplicaciones Python.
---

## Extraer campos de formulario del documento PDF

Además de permitirte generar campos de formulario y rellenarlos, Aspose.PDF para Python facilita la extracción de datos de campos de formulario o información sobre los campos de formulario de archivos PDF.

El fragmento de código crea un diccionario para almacenar los valores de todos los campos del formulario PDF. Recorre los nombres de los campos del formulario, recupera sus valores y llena el diccionario con estos datos. Finalmente, imprime los valores del formulario recopilados.

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

## Recuperar el valor del campo de formulario por título

## Extraer campos de formulario del documento PDF a JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

El fragmento de código Python proporcionado extrae los valores de sus campos y serializa estos datos en formato JSON. Importa los módulos necesarios, construye las rutas de archivo de entrada y salida, recupera los nombres y valores de los campos del formulario PDF, y escribe la cadena JSON serializada en un archivo de salida especificado.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Extraer datos a XML desde un archivo PDF

El siguiente fragmento de código Python crea un objeto de formulario, vincula un documento PDF a ese objeto y exporta los datos del formulario a un archivo XML. El código extrae automáticamente los datos de un formulario PDF y los guarda en un formato XML estructurado.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

El siguiente fragmento de código crea un objeto de formulario, vincula un documento PDF a ese formulario y luego exporta los datos del formulario a un archivo FDF (Formato de Datos de Formularios). El archivo FDF es un formato utilizado para almacenar datos de formularios de documentos PDF, lo que permite un intercambio de datos sencillo.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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


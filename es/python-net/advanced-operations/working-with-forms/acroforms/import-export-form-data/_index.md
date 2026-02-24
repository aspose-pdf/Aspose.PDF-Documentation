---
title: Importar y exportar datos de formulario
type: docs
weight: 80
url: /es/python-net/import-export-form-data/
description: Esta sección explica cómo importar y exportar datos de formulario.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Técnicas de importación y exportación utilizando Aspose.PDF para Python a través de .NET.
Abstract: Esta compilación presenta un conjunto completo de técnicas de importación y exportación de datos de formulario utilizando Aspose.PDF para Python a través de .NET. Cubre flujos de trabajo para integrar formularios PDF con formatos de datos externos, incluidos XML, FDF, XFDF y JSON. Los usuarios pueden automatizar el llenado masivo de formularios importando datos estructurados en campos interactivos, o extraer valores de campos para análisis, respaldo o integración con otros sistemas. Los ejemplos demuestran cómo enlazar formularios PDF, transferir datos entre formatos y guardar documentos actualizados, habilitando un procesamiento de documentos escalable y consistente en diversas aplicaciones.
---

## Importar datos de formulario desde un archivo XML

El siguiente ejemplo muestra cómo importar datos de formulario desde un archivo XML a un formulario PDF existente usando Aspose.PDF para Python. Al enlazar un formulario PDF, cargar datos XML y guardar el archivo actualizado, puedes rellenar rápidamente los campos de formulario interactivos sin editar manualmente cada página. Este método es ideal para automatizar el llenado masivo de formularios, procesar grandes conjuntos de datos y garantizar la consistencia de los datos en varios documentos.

Utiliza los siguientes pasos:

1. Crear un objeto Form utilizando Aspose.PDF.
1. Enlazar el formulario PDF.
1. Cargar datos XML.
1. Importar XML al PDF.
1. Guardar el PDF actualizado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## Exportar datos de campos de formulario de un documento PDF a un archivo XML

La biblioteca Python muestra cómo exportar datos de campos de formulario de un documento PDF a un archivo XML usando Aspose.PDF para Python. Al enlazar un formulario PDF y guardar sus valores de campo en formato XML, puedes almacenar, procesar o reutilizar fácilmente los datos del formulario en otras aplicaciones o flujos de trabajo. Este método es ideal para respaldo de datos, análisis e integración con sistemas externos.

Utiliza los siguientes pasos:

1. Crear un objeto Form utilizando Aspose.PDF.
1. Enlazar el formulario PDF
1. Exportar datos del formulario
1. Guardar valores de campo en XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## Importar datos de campos de formulario desde un FDF

El método 'import_data_from_fdf' importa datos de campos de formulario desde un archivo FDF (Formato de Datos de Formularios) a un formulario PDF existente y guarda el documento actualizado. Este método es útil para pre‑rellenar o actualizar formularios PDF programáticamente sin modificar la estructura del documento.

Utiliza los siguientes pasos:

1. Crear un objeto Form utilizando Aspose.PDF.
1. Enlazar el PDF de entrada.
1. Importar los datos del formulario con import_fdf().
1. Guardar el PDF con los datos importados en la ruta de archivo de salida especificada.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## Exportar datos de campos de formulario a FDF

Este ejemplo muestra cómo exportar datos de formulario de un documento PDF a un archivo FDF (Formato de Datos de Formularios) usando Aspose.PDF para Python a través de .NET.

1. Crear un objeto Form utilizando Aspose.PDF.
1. Enlazar el documento PDF.
1. Exportar datos del formulario con export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Importar datos de campos de formulario desde un XFDF

Este ejemplo exporta datos de campos de formulario de un documento PDF a un archivo XFDF (Formato XML de Datos de Formularios) y luego guarda el PDF actualizado usando Aspose.PDF para Python a través de .NET.

1. Crear un objeto Form utilizando Aspose.PDF.
1. Enlazar el documento PDF al formulario.
1. Exportar datos del formulario a un archivo XFDF.
1. Guardar el formulario procesado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## Exportar datos de campos de formulario a XFDF

Este código extrae datos de campos de formulario de un documento PDF y los exporta a un archivo XFDF (Formato XML de Datos de Formularios) usando Aspose.PDF para Python.

1. Crear un objeto Form utilizando Aspose.PDF.
1. Enlazar el documento PDF al formulario.
1. Exportar datos del formulario a un archivo FDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## Importar datos de otro PDF

Este fragmento de código muestra cómo transferir datos de campos de formulario de un PDF origen a un PDF destino. Los datos del formulario se exportan a un flujo XFDF desde el PDF origen y luego se importan al PDF objetivo usando Aspose.PDF para Python a través de .NET.

1. Crear un objeto Form utilizando Aspose.PDF.
1. Vincula el documento PDF al formulario.
1. Exporta los datos del formulario del PDF de origen.
1. Importa los datos del formulario al PDF de destino.
1. Guarda el PDF de destino actualizado.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Extraer campos de formulario a JSON

Este método extrae los campos del formulario de un archivo de entrada y los exporta a un archivo JSON.

1. Crea un objeto Form usando Aspose.PDF.
1. Abre el archivo de salida en modo escritura usando FileIO().
1. Exporta los campos del formulario al archivo JSON usando el método form.export_json().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## Extraer campos de formulario a documento JSON

1. Crea un objeto Form a partir del archivo de entrada.
1. Inicializa un diccionario vacío para almacenar los datos de los campos del formulario.
1. Recorre todos los campos del formulario y extrae sus valores.
1. Serializa el diccionario de datos del formulario a una cadena JSON con una indentación de 4 espacios.
1. Escribe la cadena JSON al archivo de salida con codificación UTF-8.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```


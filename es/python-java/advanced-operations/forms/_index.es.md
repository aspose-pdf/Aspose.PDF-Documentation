---
title: Trabajando con Formularios usando Python
linktitle: Formularios en documento PDF
type: docs
weight: 60
url: /python-java/forms/
lastmod: "2023-05-19"
description: Esta sección contiene artículos relacionados con el trabajo con formularios en documentos PDF usando la API de Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Los formularios son archivos con áreas para que los usuarios seleccionen o completen información con el propósito de recopilar y almacenar información.

Los AcroForms son archivos PDF que contienen campos de formulario. Los usuarios finales o el autor del formulario pueden ingresar datos en estos campos (manualmente o a través de un proceso automatizado). Internamente, los AcroForms son anotaciones o campos aplicados a un documento PDF.

En esta sección se describe un enfoque rápido y simple para completar programáticamente un documento PDF mediante el uso de Aspose.PDF. La sección también discute cómo se podría usar Aspose.PDF para Java para descubrir y mapear los campos disponibles dentro de un PDF existente con AcroForms.

**Nuestra biblioteca Aspose.PDF para Python a través de Java** le permite trabajar con éxito, rápida y fácilmente con formularios en documentos PDF.

- **AcroForms** - crear formulario, llenar campo de formulario, extraer datos del formulario, modificar campos en su PDF con la biblioteca Java.
- **XFA Forms** - llenar campos XFA, convertir XFA, obtener propiedades de campos XFA.

## Las siguientes funciones están disponibles:

- exportar/importar fdf
- exportar/importar xfdf
- exportar/importar xml
- exportar/establecer XfaData
- llenar campos
- aplanar campos
- determinar valores válidos de botones de opción
- obtener nombres de campos, banderas, tipos, valores
- renombrar campos

```python

from asposepdf import Api, Forms


# inicializar licencia
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# ejemplo de llenado de campo

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```
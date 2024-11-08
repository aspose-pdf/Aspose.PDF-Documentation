---
title: Uso de Aspose.PDF para .NET con Python
linktitle: Integración con Python
type: docs
weight: 100
url: /es/net/python-net/
description: En este tutorial, explorarás las diferentes formas de crear y modificar archivos PDF en Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

Este artículo describe breves ejemplos sobre cómo crear PDF utilizando la integración de Aspose.PDF para .NET con Python.

## Prerrequisitos

Para usar Aspose.PDF para .NET en Python, por favor usa el siguiente `requirments.txt`:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

También, deberías colocar `Aspose.PDF.dll` en la carpeta deseada.

## Creando un PDF Simple usando Python

Para trabajar necesitaremos integrar [PythonNet](https://github.com/pythonnet/pythonnet) en nuestra aplicación y hacer algunos ajustes.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### Generar documento simple

Vamos a crear un PDF simple con el texto clásico "Hola, mundo". Para una explicación más detallada, por favor sigue [esta página](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Inicializar el objeto documento
        document = Document()
        # Añadir página
        page = document.Pages.Add()
        # Añadir texto a la nueva página
        textFragment = TextFragment("Hola, mundo!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Crear objeto TextBuilder
        textBuilder = TextBuilder(page)

        # Añadir el fragmento de texto a la página del PDF
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Creando documentos PDF complejos usando Python

Los siguientes ejemplos muestran cómo podemos crear un documento PDF complejo con imágenes y tablas. Este ejemplo se basa en la [siguiente página](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... omitido ...

    # Crear un documento complejo
    def run_complex(self):

        # Inicializar objeto de documento
        document = Document()
        # Agregar página
        page = document.Pages.Add()

        # Agregar imagen
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Agregar encabezado
        header = TextFragment("Nuevas rutas de ferry en otoño de 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Agregar descripción
        descriptionText = "Los visitantes deben comprar boletos en línea y los boletos están limitados a 5,000 por día. \
        El servicio de ferry está operando a media capacidad y con un horario reducido. Espere filas."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # Agregar tabla
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Ciudad de salida")
        headerRow.Cells.Add("Isla de salida")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## Cómo ejecutar la generación de PDFs en Windows

Este fragmento muestra cómo ejecutar los ejemplos anteriores en una PC con Windows. Se asume que `class HelloWorld` está ubicada en el archivo `example_get_started.py`.
Si ejecutas la versión de prueba de Aspose.PDF para .NET, debes pasar una cadena vacía como `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```

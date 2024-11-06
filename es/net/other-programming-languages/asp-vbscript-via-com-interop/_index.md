---
title: ASP - VBScript via COM Interop
type: docs
weight: 30
url: es/net/asp-vbscript-via-com-interop/
---

## Prerrequisitos

{{% alert color="primary" %}}

    Por favor, revise el artículo titulado Utilizar Aspose.pdf para .NET vía COM Interop.

{{% /alert %}}

## Ejemplo ¡Hola Mundo! en VB Script

{{% alert color="primary" %}}

Esta es una aplicación ASP simple que muestra cómo crear un archivo PDF con texto de muestra usando [Aspose.PDF para .NET](/pdf/net/) y VBScript vía COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> usando Aspose.PDF para .NET en un ejemplo clásico de ASP</title>
    </head>
<body>

<h3>creación de un documento PDF de muestra utilizando Aspose.PDF para .NET con ASP clásico y VBScript</h3>

<%

'establecer licencia
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'Instanciar Pdf por medio de su constructor vacío
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Crear una nueva sección en el objeto Pdf
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'Añadir sección al objeto Pdf
pdf.Sections.Add(pdfsection)

' Crear objeto Texto
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'Añadir Segmento de Texto al objeto texto
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'Asignar algún contenido al segmento
seg1.Content = "HelloWorld usando ASP y VBScript"

'Añadir segmento (con color de texto rojo) al párrafo
SampleText.Segments.Add(seg1)

' Añadir párrafo de Texto a la colección de párrafos de una sección
pdfsection.Paragraphs.Add(SampleText)

' Guardar el documento PDF
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## Extracción de texto usando VBScript

{{% alert color="primary" %}}
    Este ejemplo de VBScript extrae texto de un documento PDF existente a través de COM Interop.
    Error rendering macro 'code' : Invalid value specified for parameter lang
{{% /alert %}}

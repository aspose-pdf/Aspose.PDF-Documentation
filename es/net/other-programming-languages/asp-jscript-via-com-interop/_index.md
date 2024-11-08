---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /es/net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

Esta es una aplicación ASP simple que muestra cómo agregar una cadena de texto simple a un archivo PDF usando [Aspose.PDF for .NET](/pdf/es/net/) y JScript a través de COM Interop.

{{% /alert %}}

Ejemplo:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> Uso de Aspose.PDF para .NET en un ejemplo de ASP clásico</title>
    </head>
    <body>
        <h3>creación de un documento PDF de muestra usando Aspose.PDF para .NET con ASP clásico y JScript</h3>
<%
// establecer licencia
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instanciar la instancia de Pdf llamando a su constructor vacío
var pdf = Server.CreateObject("Aspose.PDF.Document");

// Crear una nueva Página en el objeto PDF
var pdfpage = pdf.Pages.Add();

// Crear objeto de Fragmento de Texto
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Asignar algún contenido al Fragmento
sampleText.Text = "Hola Mundo usando ASP y JScript";

// Añadir párrafo de Texto a la colección de párrafos de una sección
pdfpage.Paragraphs.Add(sampleText);

// Guardar el documento PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```
{{% /alert %}}

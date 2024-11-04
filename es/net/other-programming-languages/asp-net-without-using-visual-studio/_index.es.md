---
title: ASP.NET sin usar Visual Studio
type: docs
weight: 60
url: /net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF para .NET](/pdf/net/) se puede utilizar para desarrollar páginas o aplicaciones ASP.NET sin usar Visual Studio. En este ejemplo, escribiremos HTML y el código C# o VB.NET en un único archivo .aspx; esto se conoce comúnmente como ASP.NET Instantáneo.

{{% /alert %}}

## Detalles de implementación

{{% alert color="primary" %}}

Cree una aplicación web de muestra y copie Aspose.PDF.dll en un directorio llamado "Bin" en el directorio de su sitio web (*si la carpeta bin no existe, créela*). Luego cree su página .aspx y copie el siguiente código en ella.
Este ejemplo muestra cómo usar [Aspose.PDF para .NET](/pdf/net/) con código integrado en una página ASP.NET para crear un documento PDF simple con un texto de muestra dentro de él.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> usando Aspose.PDF para .NET con ASP.NET Integrado</title>
    </head>
    <body>
        <h3>creación de un documento PDF simple usando Aspose.PDF para .NET con ASP.NET Integrado</h3>
<%
    // establecer licencia
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Inicializar objeto de documento
    Document document = new Document();
    // Agregar página
    Page page = document.Pages.Add();
    // Agregar texto a la nueva página
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("¡Hola Mundo!"));
    // Guardar PDF actualizado
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```


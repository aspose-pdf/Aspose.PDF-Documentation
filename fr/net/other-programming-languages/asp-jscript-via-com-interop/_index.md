---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /fr/net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

Ceci est une application ASP simple qui vous montre comment ajouter une simple chaîne de texte à un fichier PDF en utilisant [Aspose.PDF for .NET](/pdf/fr/net/) et JScript via COM Interop.

{{% /alert %}}

Exemple :

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title>Utilisation d'Aspose.PDF pour .NET dans un exemple ASP classique</title>
    </head>
    <body>
        <h3>Création d'un document PDF exemple en utilisant Aspose.PDF pour .NET avec ASP classique et JScript</h3>
<%
// définir la licence
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instancier l'objet Pdf en appelant son constructeur vide
var pdf = Server.CreateObject("Aspose.PDF.Document");

// Créer une nouvelle Page dans l'objet PDF
var pdfpage = pdf.Pages.Add();

// Créer un objet Fragment de texte
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Attribuer un contenu au Fragment
sampleText.Text = "HelloWorld en utilisant ASP et JScript";

// Ajouter le paragraphe de texte à la collection de paragraphes d'une section
pdfpage.Paragraphs.Add(sampleText);

// Sauvegarder le document PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```
{{% /alert %}}

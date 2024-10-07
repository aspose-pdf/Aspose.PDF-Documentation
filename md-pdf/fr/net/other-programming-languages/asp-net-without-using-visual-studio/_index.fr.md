---
title: ASP.NET sans utiliser Visual Studio
type: docs
weight: 60
url: /net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF pour .NET](/pdf/net/) peut être utilisé pour développer des pages ou des applications ASP.NET sans utiliser Visual Studio. Dans cet exemple, nous allons écrire du HTML et le code C# ou VB.NET dans un seul fichier .aspx ; cela est communément appelé ASP.NET instantané.

{{% /alert %}}

## Détails de l'implémentation

{{% alert color="primary" %}}

Créez une application web exemple et copiez Aspose.PDF.dll dans un répertoire nommé "Bin" dans votre répertoire de site web ( *si le dossier bin n'existe pas, créez-en un* ). Ensuite, créez votre page .aspx et copiez le code suivant dedans.
Cet exemple montre comment utiliser [Aspose.PDF pour .NET](/pdf/net/) avec du code intégré dans une page ASP.NET afin de créer un document PDF simple avec du texte d'exemple à l'intérieur.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title>Utilisation de Aspose.PDF pour .NET avec ASP.NET Intégré</title>
    </head>
    <body>
        <h3>Création d'un document PDF simple en utilisant Aspose.PDF pour .NET avec ASP.NET Intégré</h3>
<%
    // Définir la licence
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Initialiser l'objet document
    Document document = new Document();
    // Ajouter une page
    Page page = document.Pages.Add();
    // Ajouter du texte à la nouvelle page
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Bonjour le monde !"));
    // Sauvegarder le PDF mis à jour
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```


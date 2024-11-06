---
title: ASP - VBScript via COM Interop
type: docs
weight: 30
url: fr/net/asp-vbscript-via-com-interop/
---

## Prérequis

{{% alert color="primary" %}}

    Veuillez vérifier l'article nommé Utiliser Aspose.pdf pour .NET via COM Interop.

{{% /alert %}}

## Exemple de "Hello World!" en VB Script

{{% alert color="primary" %}}

Il s'agit d'une application ASP simple qui vous montre comment créer un fichier PDF avec du texte d'exemple en utilisant [Aspose.PDF pour .NET](/pdf/net/) et VBScript via COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> Utilisation de Aspose.PDF pour .NET dans un exemple ASP classique</title>
    </head>
<body>

<h3>Création d'un document PDF d'exemple en utilisant Aspose.PDF pour .NET avec ASP classique et VBScript</h3>

<%

'Configurer la licence
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'Instancier l'objet Pdf en appelant son constructeur vide
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Créer une nouvelle section dans l'objet Pdf
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'Ajouter la section à l'objet Pdf
pdf.Sections.Add(pdfsection)

' Créer un objet Texte
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'Ajouter un Segment de Texte à l'objet texte
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'Attribuer un contenu au segment
seg1.Content = "HelloWorld en utilisant ASP et VBScript"

'Ajouter le segment (avec la couleur de texte rouge) au paragraphe
SampleText.Segments.Add(seg1)

' Ajouter le paragraphe Texte à la collection de paragraphes d'une section
pdfsection.Paragraphs.Add(SampleText)

' Sauvegarder le document PDF
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## Extraction de texte à l'aide de VBScript

{{% alert color="primary" %}}
    Cet exemple VBScript extrait le texte d'un document PDF existant via COM Interop.
    Erreur de rendu macro 'code' : Valeur invalide spécifiée pour le paramètre lang
{{% /alert %}}

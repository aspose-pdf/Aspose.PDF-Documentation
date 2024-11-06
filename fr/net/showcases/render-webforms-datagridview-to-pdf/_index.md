---
title: Rendre WebForms DataGridView en PDF
linktitle: Rendre WebForms DataGridView en PDF
type: docs
weight: 20
url: fr/net/render-webforms-datagridview-to-pdf/
description: Cet exemple montre comment utiliser la bibliothèque Aspose.PDF pour transformer un WebForm en PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comment exporter un WebForm en PDF en utilisant Aspose.PDF/Aspose.HTML

### Introduction

En général, pour convertir un WebForm en document PDF, des outils supplémentaires sont utilisés. Cet exemple montre comment utiliser la bibliothèque Aspose.PDF pour transformer un WebForm en PDF. Le contrôle Aspose Export GridView To Pdf est également inclus dans cet exemple pour montrer comment rendre un _contrôle GridView en document PDF._

## Comment transformer un WebForm en PDF

L'idée originale pour transformer un WebForm en PDF est de créer une classe d'assistance, qui hérite de [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), et de surcharger une méthode Render.

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // rendre la page web pour le document PDF
    }
    else
    {
        // rendre la page web dans le navigateur
        base.Render(writer);
    }
}
```
Il y a deux outils Aspose qui peuvent être utilisés pour convertir HTML en PDF :

- Aspose.PDF pour .NET
- Aspose Export GridView control (basé sur Aspose.PDF)

## Fichiers sources

Dans cet exemple, nous avons 2 rapports de démonstration.

- _Default.aspx_ démontre l'exportation en PDF en utilisant Aspose.PDF
- _Report2.aspx_ démontre l'exportation en PDF en utilisant Aspose Export GridView control (basé sur Aspose.PDF)

## Fichiers supplémentaires

`Helpers\PdfPage.cs` - contient une classe d'assistance, qui montre comment utiliser l'API Aspose.PDF.

Le projet Aspose.Pdf.GridViewExport contient un contrôle GridView étendu pour la démonstration dans `Report2.aspx`

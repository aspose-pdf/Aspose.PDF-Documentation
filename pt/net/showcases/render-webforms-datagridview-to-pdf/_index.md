---
title: Renderizar WebForms DataGridView para PDF
linktitle: Renderizar WebForms DataGridView para PDF
type: docs
weight: 20
url: /pt/net/render-webforms-datagridview-to-pdf/
description: Este exemplo mostra como usar a biblioteca Aspose.PDF para renderizar WebForm para PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como exportar WebForm para PDF usando Aspose.PDF/Aspose.HTML

### Introdução

Geralmente, para converter WebForm para documento PDF são utilizadas ferramentas adicionais. Este exemplo mostra como usar a biblioteca Aspose.PDF para renderizar WebForm para PDF. O controle Aspose Export GridView To Pdf também está incluído neste exemplo para mostrar como renderizar _controle GridView para documento PDF._

## Como renderizar WebForm para PDF

A ideia original para renderizar WebForm para PDF é criar uma classe auxiliar, que herda de [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), e sobrescrever o método Render.

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // renderizar página web para documento PDF
    }
    else
    {
        // renderizar página web no navegador
        base.Render(writer);
    }
}
```
Existem duas ferramentas Aspose que podem ser usadas para renderizar HTML para PDF:

- Aspose.PDF para .NET
- Controle Aspose Export GridView (baseado no Aspose.PDF)

## Arquivos Fonte

Neste exemplo, temos 2 relatórios de demonstração.

- _Default.aspx_ demonstra a exportação para PDF usando Aspose.PDF
- _Report2.aspx_ demonstra a exportação para PDF usando o controle Aspose Export GridView (baseado no Aspose.PDF)

## Arquivos Adicionais

`Helpers\PdfPage.cs` - contém uma classe auxiliar, que mostra como usar a API Aspose.PDF.

O projeto Aspose.Pdf.GridViewExport contém um controle GridView extendido para demonstração em `Report2.aspx`

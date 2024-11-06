---
title: Render WebForms DataGridView a PDF
linktitle: Render WebForms DataGridView a PDF
type: docs
weight: 20
url: es/net/render-webforms-datagridview-to-pdf/
description: Este ejemplo muestra cómo usar la biblioteca Aspose.PDF para renderizar WebForm a PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo exportar WebForm a PDF usando Aspose.PDF/Aspose.HTML

### Introducción

Generalmente, para convertir WebForm a documento PDF se utilizan herramientas adicionales. Este ejemplo muestra cómo usar la biblioteca Aspose.PDF para renderizar WebForm a PDF. También se incluye en este ejemplo el Control de Exportación de GridView a PDF de Aspose para mostrar cómo renderizar el control _GridView a documento PDF._

## Cómo renderizar WebForm a PDF

La idea original para renderizar WebForm a PDF es crear una clase de ayuda, que hereda de [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), y sobrescribir el método Render.

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // renderizar página web para documento PDF
    }
    else
    {
        // renderizar página web en navegador
        base.Render(writer);
    }
}
```
Hay dos herramientas de Aspose que se pueden usar para renderizar HTML a PDF:

- Aspose.PDF para .NET
- Aspose Export GridView control (basado en Aspose.PDF)

## Archivos fuente

En este ejemplo tenemos 2 informes de demostración.

- _Default.aspx_ demuestra la exportación a PDF utilizando Aspose.PDF
- _Report2.aspx_ demuestra la exportación a PDF utilizando Aspose Export GridView control (basado en Aspose.PDF)

## Archivos adicionales

`Helpers\PdfPage.cs` - contiene una clase de ayuda, que muestra cómo usar la API de Aspose.PDF.

El proyecto Aspose.Pdf.GridViewExport contiene un control GridView extendido para la demostración en `Report2.aspx`

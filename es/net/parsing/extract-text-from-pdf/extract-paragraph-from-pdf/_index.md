---
title: Extract Paragraph from PDF C#
linktitle: Extract Paragraph from PDF
type: docs
weight: 20
url: /es/net/extract-paragraph-from-pdf/
description: Este artículo describe cómo usar ParagraphAbsorber - una herramienta especial en Aspose.PDF para extraer texto de documentos PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de un documento PDF en forma de párrafos

Podemos obtener texto de un documento PDF buscando un texto en particular (usando "texto plano" o "expresiones regulares") desde una sola página o todo el documento, o podemos obtener el texto completo de una sola página, un rango de páginas o el documento completo.
Podemos obtener texto de un documento PDF buscando un texto en particular (usando "texto plano" o "expresiones regulares") desde una sola página o todo el documento, o podemos obtener el texto completo de una sola página, un rango de páginas o el documento completo.

**1- Dibujando el borde de secciones y párrafos de texto en la página PDF:**

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraph()
{
    // La ruta al directorio de documentos.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    Document doc = new Document(dataDir + "input.pdf");
    Page page = doc.Pages[2];

    ParagraphAbsorber absorber = new ParagraphAbsorber();
    absorber.Visit(page);

    PageMarkup markup = absorber.PageMarkups[0];

    foreach (MarkupSection section in markup.Sections)
    {
        DrawRectangleOnPage(section.Rectangle, page);
        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            DrawPolygonOnPage(paragraph.Points, page);
        }
    }

    doc.Save(dataDir + "output_out.pdf");
}

private static void DrawRectangleOnPage(Rectangle rectangle, Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 1, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(2));
    page.Contents.Add(
        new Aspose.Pdf.Operators.Re(rectangle.LLX,
            rectangle.LLY,
            rectangle.Width,
            rectangle.Height));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}

private static void DrawPolygonOnPage(Point[] polygon, Page page)
{
    page.Contents.Add(new Aspose.Pdf.Operators.GSave());
    page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.Contents.Add(new Aspose.Pdf.Operators.SetRGBColorStroke(0, 0, 1));
    page.Contents.Add(new Aspose.Pdf.Operators.SetLineWidth(1));
    page.Contents.Add(new Aspose.Pdf.Operators.MoveTo(polygon[0].X, polygon[0].Y));
    for (int i = 1; i < polygon.Length; i++)
    {
        page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[i].X, polygon[i].Y));
    }
    page.Contents.Add(new Aspose.Pdf.Operators.LineTo(polygon[0].X, polygon[0].Y));
    page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
    page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
}
```
**2- Al iterar a través de la colección de párrafos y obtener el texto de los mismos:**

El siguiente fragmento de código también funciona con la librería [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir un archivo PDF existente
Document doc = new Document(dataDir + "input.pdf");
// Instanciar ParagraphAbsorber
ParagraphAbsorber absorber = new ParagraphAbsorber();
absorber.Visit(doc);

foreach (PageMarkup markup in absorber.PageMarkups)
{
    int i = 1;
    foreach (MarkupSection section in markup.Sections)
    {
        int j = 1;

        foreach (MarkupParagraph paragraph in section.Paragraphs)
        {
            StringBuilder paragraphText = new StringBuilder();

            foreach (List<TextFragment> line in paragraph.Lines)
            {
                foreach (TextFragment fragment in line)
                {
                    paragraphText.Append(fragment.Text);
                }
                paragraphText.Append("\r\n");
            }
            paragraphText.Append("\r\n");

            Console.WriteLine("Párrafo {0} de la sección {1} en la página {2}:", j, i, markup.Number);
            Console.WriteLine(paragraphText.ToString());

            j++;
        }
        i++;
    }
}
```


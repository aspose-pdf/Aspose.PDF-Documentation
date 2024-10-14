---
title: Extrair Parágrafo de PDF C#
linktitle: Extrair Parágrafo de PDF
type: docs
weight: 20
url: /net/extract-paragraph-from-pdf/
description: Este artigo descreve como usar o ParagraphAbsorber - uma ferramenta especial na Aspose.PDF para extrair texto de documentos PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de documento PDF em Forma de Parágrafos

Podemos obter texto de um documento PDF procurando um texto específico (usando "texto simples" ou "expressões regulares") de uma única página ou do documento inteiro, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo.
Podemos obter texto de um documento PDF pesquisando um texto específico (usando "texto simples" ou "expressões regulares") de uma única página ou de todo o documento, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo.

**1- Desenhando a borda de seções e parágrafos de texto na página do PDF:**

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractParagraph()
{
    // O caminho para o diretório de documentos.
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
**2- Iterando pela coleção de parágrafos e obtendo o texto deles:**

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir um arquivo PDF existente
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

            Console.WriteLine("Parágrafo {0} da seção {1} na página {2}:", j, i, markup.Number);
            Console.WriteLine(paragraphText.ToString());

            j++;
        }
        i++;
    }
}
```


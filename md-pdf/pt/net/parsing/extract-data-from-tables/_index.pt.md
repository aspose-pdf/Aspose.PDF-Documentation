---
title: Extrair Dados de Tabela em PDF com C#
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: /net/extract-data-from-table-in-pdf/
description: Aprenda como extrair dados tabulares de PDF usando Aspose.PDF para .NET em C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Tabelas de PDF Programaticamente

Extrair tabelas de PDFs não é uma tarefa trivial pois a tabela pode ser criada de várias maneiras.

Aspose.PDF para .NET tem uma ferramenta para facilitar a recuperação de tabelas. Para extrair dados de uma tabela você deve realizar os seguintes passos:

1. Abrir documento - instancie um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document);
1. Criar um objeto [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. `TableList` é uma Lista de [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Para obter a data, percorra o `TableList` e manipule [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) e [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)
1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) contém uma coleção de [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Você pode processá-la para seus próprios fins.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

O exemplo a seguir mostra a extração de tabelas de todas as páginas:

```csharp
public static void Extract_Table()
{
    // Carregar o documento PDF de origem
    var filePath="<... insira o caminho para o arquivo pdf aqui ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Extrair tabela em área específica da página do PDF

Cada tabela absorvida possui a propriedade [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) que descreve a posição da tabela na página.

Portanto, se você precisar extrair tabelas localizadas em uma região específica, você terá que trabalhar com coordenadas específicas.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

O seguinte exemplo mostra como extrair uma tabela marcada com Anotação Quadrada:

```csharp
public static void Extract_Marked_Table()
{
    // Carregar o documento PDF fonte
    var filePath="<... insira o caminho para o arquivo pdf aqui ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Extrair dados de tabela de um PDF e armazenar em um arquivo CSV

O exemplo a seguir mostra como extrair uma tabela e armazená-la como um arquivo CSV.
Para ver como converter um PDF em uma planilha do Excel, consulte o artigo [Converter PDF para Excel](/pdf/net/convert-pdf-to-excel/).

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void Extract_Table_Save_CSV()
{
    // Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Carregar documento PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instanciar objeto de opção de salvamento Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // Salvar a saída no formato XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```

---
title: Extrair Dados de Tabela de PDF
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: /pt/java/extract-data-from-table-in-pdf/
description: Aprenda como extrair tabelas de PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraia Tabelas de PDF programaticamente

Extrair tabelas de PDFs não é uma tarefa trivial porque a tabela pode ser criada de várias maneiras.

Aspose.PDF para Java tem uma ferramenta para facilitar a recuperação de tabelas. Para extrair dados de tabela, você deve realizar as seguintes etapas:

1. Abrir documento - instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. Criar um objeto [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. Decida quais páginas serão analisadas e aplique [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) nas páginas desejadas. Os dados tabulares serão escaneados e o resultado será salvo em uma lista de [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Podemos obter essa lista através do método [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Para obter os dados, itere através do `TableList` e manipule a lista de [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) e a lista de células absorvidas. Podemos acessar a primeira lista chamando o método [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) e a segunda chamando o método [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) contém [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Você pode processá-lo para seus próprios propósitos.

O exemplo a seguir mostra a extração de tabela de todas as páginas:

```java
public static void Extract_Table() {
    // Carregar documento PDF de origem        
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // Escanear páginas
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Tabela");
            // Iterar através da lista de linhas
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // Iterar através da lista de células
                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                    for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                        StringBuilder sb = new StringBuilder();
                        for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                            sb.append(seg.getText());
                        System.out.print(sb.toString() + "|");
                    }
                }
                System.out.println();
            }
        }
    }
}
```


## Extrair tabela em área específica da página PDF

Cada tabela absorvida tem a propriedade [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--) que descreve a posição da tabela na página.

Portanto, se você precisar extrair tabelas localizadas em uma região específica, deverá trabalhar com coordenadas específicas.

O exemplo a seguir mostra como extrair a tabela marcada com Anotação Quadrada:

```java
public static void Extract_Marked_Table() {
    // Carregar documento PDF de origem
    String filePath = "<... enter path to pdf file here ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("Tabelas marcadas não encontradas..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```


## Extrair Dados da Tabela de PDF e armazená-los em arquivo CSV

O exemplo a seguir mostra como extrair uma tabela e armazená-la como arquivo CSV. Para ver como converter PDF para Planilha do Excel, consulte o artigo [Converter PDF para Excel](/pdf/pt/java/convert-pdf-to-excel/).

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // Carregar documento PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Instanciar objeto ExcelSave Option
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // Salvar a saída no formato XLS
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```
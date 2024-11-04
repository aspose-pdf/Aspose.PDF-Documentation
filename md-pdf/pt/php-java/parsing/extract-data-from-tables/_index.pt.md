---
title: Extrair Dados de Tabela de PDF
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: /php-java/extract-data-from-table-in-pdf/
description: Aprenda a extrair tabelas de PDF usando Aspose.PDF para PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Tabelas de PDF programaticamente

Extrair tabelas de PDFs não é uma tarefa trivial porque a tabela pode ser criada de várias maneiras.

Aspose.PDF para PHP via Java tem uma ferramenta para facilitar a recuperação de tabelas. Para extrair dados de tabela, você deve realizar as seguintes etapas:

1. Abra o documento PDF - instancie um objeto [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document);
1. Crie um objeto TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) para extrair tabelas do documento.
1. Itere através de cada página do documento.

1. Decida quais páginas serão analisadas e aplique [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) nas páginas desejadas. Os dados tabulares serão escaneados e o resultado será salvo em uma lista de [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). Podemos obter essa lista através do método [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Para obter os dados, itere através de `TableList` e manipule a lista de [absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) e a lista de células absorvidas. Podemos acessar a primeira lista chamando o método [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) e a segunda chamando o método [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Cada [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) contém [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). Você pode processá-lo para seus próprios propósitos.

O exemplo a seguir mostra a extração de tabelas de todas as páginas:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // Iterar através de cada célula na linha.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // Iterar através de cada fragmento de texto na célula.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // Iterar através de cada segmento no fragmento de texto.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// Salvar os dados da tabela no arquivo de saída.
file_put_contents($outputFile, $responseData);

// Fechar o documento PDF.
$document->close();
```


## Extrair Dados da Tabela de PDF e armazená-los em arquivo CSV

O exemplo a seguir mostra como extrair uma tabela e armazená-la como um arquivo CSV. Para ver como converter PDF para Planilha Excel, consulte o artigo [Converter PDF para Excel](/pdf/php-java/convert-pdf-to-excel/).

```php

    // Carregar o documento PDF de entrada usando a classe Document.
    $document = new Document($inputFile);

    // Criar uma instância da classe ExcelSaveOptions para especificar as opções de salvamento.
    $saveOption = new ExcelSaveOptions();

    // Definir o formato de saída para CSV.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // Salvar o documento PDF como um arquivo Excel usando as opções de salvamento especificadas.
    $document->save($outputFile, $saveOption);
```
---
title: Manipular Tabelas em PDF existente
linktitle: Manipular Tabelas
type: docs
weight: 40
url: /pt/cpp/manipulate-tables-in-existing-pdf/
description: Esta seção abrange vários métodos para modificação de tabelas usando Aspose.PDF para C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipular tabelas em PDF existente

Aspose.PDF para C++ permite que você trabalhe rápida e eficientemente com tabelas, ou seja, crie-as do zero ou adicione a documentos PDF existentes.

Você também tem a capacidade de integrar a tabela com o banco de dados (DOM) para criar tabelas dinâmicas com base no conteúdo do banco de dados.

A classe [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) permite que você pesquise e analise tabelas simples que já existem em uma página de documento PDF. O seguinte trecho de código mostra as etapas para atualizar o conteúdo em uma célula específica em uma tabela.

>Cabecalhos:

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Exemplos:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // Carregar arquivo PDF existente
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Criar objeto TableAbsorber para encontrar tabelas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar primeira página com o absorvedor
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obter acesso à primeira tabela na página, sua primeira célula e fragmentos de texto nela
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // Alterar texto do primeiro fragmento de texto na célula
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## Substituir tabela antiga por uma nova em documento PDF

Caso você precise encontrar uma tabela específica e substituí-la pela desejada, você pode usar o método Replace() da Classe [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) para fazer isso.

O exemplo a seguir demonstra a funcionalidade para substituir a tabela dentro do documento PDF:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // Carregar arquivo PDF existente
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Criar objeto TableAbsorber para encontrar tabelas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar a primeira página com o absorvedor
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obter a primeira tabela na página
    auto table = absorber->get_TableList()->idx_get(0);

    // Criar nova tabela
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // Substituir a tabela pela nova
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // Salvar documento
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```
---
title: Remover Tabelas de um PDF Existente
linktitle: Remover Tabelas
type: docs
weight: 50
url: pt/cpp/remove-tables-from-existing-pdf/
description: Esta seção descreve como remover Tabela de documento PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF para C++ permite que você insira e crie uma Tabela dentro de um documento PDF enquanto ele está sendo gerado do zero ou você também pode adicionar o objeto tabela em qualquer documento PDF existente. Mas você pode ter um requisito para [Manipular Tabelas em PDF Existente](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/) onde você pode atualizar o conteúdo nas células da tabela existente. Além disso, você pode se deparar com a necessidade de remover objetos tabela dos documentos PDF existentes.

Para remover as tabelas, precisamos usar a classe [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) para capturar as tabelas no PDF existente e então chamar o método 'Remove'.

## Remover Tabela do Documento PDF

Nós adicionamos uma nova função, ou seja, [Remover](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) para a classe TableAbsorber existente para remover a tabela do documento PDF. Uma vez que o absorvedor encontra com sucesso as tabelas na página, ele se torna capaz de removê-las. Por favor, verifique o seguinte trecho de código mostrando como remover uma tabela de um documento PDF:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // Carregar documento PDF de origem
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // Criar objeto TableAbsorber para encontrar tabelas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar a primeira página com o absorvedor
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obter a primeira tabela na página
    auto table = absorber->get_TableList()->idx_get(0);

    // Remover a tabela
    absorber->Remove(table);

    // Salvar PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## Remover Múltiplas Tabelas de um Documento PDF

Algumas tarefas estarão associadas ao trabalho com várias tabelas em um documento pdf.
E você precisará excluir várias tabelas dele. Para remover várias tabelas de um documento PDF, use o seguinte trecho de código:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // Carregar documento PDF existente
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Criar objeto TableAbsorber para encontrar tabelas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar a primeira página com o absorvedor
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obter uma cópia da coleção de tabelas
    auto tables = absorber->get_TableList();

    // Percorrer a cópia da coleção e remover tabelas
    for(auto table : tables)
    absorber->Remove(table);

    // Salvar documento
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

Por favor, leve em consideração que a remoção ou substituição de uma tabela altera a coleção TableList. Therefore, in case removing/replacing tables in a loop the copying of TableList collection is essential.

{{% /alert %}}
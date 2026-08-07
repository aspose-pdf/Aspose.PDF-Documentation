---
title: Criando e Exportando Modelo
linktitle: Criando e Exportando Modelo
type: docs
weight: 10
url: /pt/sharepoint/creating-and-exporting-template/
lastmod: "2026-08-07"
description: Você pode criar e exportar modelos para PDF no SharePoint usando a API PDF SharePoint.
---

{{% alert color="primary" %}}

Este artigo mostra como criar e exportar modelos usando Aspose.PDF for SharePoint.

A partir do Aspose.PDF for SharePoint 1.9.2, o suporte a modelos PDF também abrange subsites do SharePoint.

{{% /alert %}}

## Criando e Exportando Modelos

{{% alert color="primary" %}}

Para usar o recurso de exportação do Aspose.PDF for SharePoint, primeiro crie uma lista que use “PDF Templates”.

Criando uma lista que usa PDF Templates:

![Criar Lista de Modelos PDF](creating-and-exporting-template_1.png)

Dois modelos de documento, Task Form Templates e Task List Templates são criados:

![Modelos de Documento](creating-and-exporting-template_2.png)

O formulário de modelo permite que você insira as seguintes informações:

- **Name**: o nome do arquivo do modelo.
- **Title**: o título do modelo. (Por padrão, o mesmo que o nome do arquivo.)
- **Description**: uma descrição do modelo. Uma boa descrição facilita o uso do modelo.
- **Assigned List Types**: IDs de lista separados por vírgula (relacionados ao modelo. Este campo também pode conter o valor
- **AllListTypes**. Este campo só se aplica quando o campo **Type** está definido como **List**).
- **Tipos de Conteúdo Atribuídos**: IDs de tipos de conteúdo separados por vírgula relacionados ao modelo. Este campo pode ser definido como **AllListTypes**. Este campo só se aplica quando o campo **Type** está definido como **Item**.
- **Type**: seja modelo de lista ou modelo de item.
- **Status**: as opções são active, inactive (invisível para todos) e debugging (visível apenas para administradores).

O formulário Task List Templates:

![Modelos de Lista de Tarefas](creating-and-exporting-template_3.png)

O formulário Task Form Templates:

![Modelos de Formulário de Tarefa](creating-and-exporting-template_4.png)

Quando são salvos, os novos modelos aparecem na lista de modelos, prontos para ser usados:

Dois modelos de lista de tarefas:*

![Modelos de Lista de Tarefas](creating-and-exporting-template_5.png)

Um modelo de formulário de tarefa:

![Modelos de Formulário de Tarefa](creating-and-exporting-template_6.png)

### Desenvolvendo Modelos

Um modelo é um arquivo XML baseado em Aspose XML PDF. Para criar um modelo para uma lista, coloque marcadores especiais relacionados ao nome interno do campo do tipo de conteúdo de destino do SharePoint no arquivo XML PDF.

### Marcadores

- **SPListItemsCount** – substituído pela contagem de itens da lista.
- **SPListTitle** – substituído pelo título da lista.
- **SPTableIterator** – colocado na primeira célula da tabela e marca a tabela para iteração completa.
- **SPRowIterator** – colocado na primeira célula da tabela e marca a tabela para iteração de linhas.
- **SPField** – substituído pelo valor do campo do item.

Para referência, por favor faça o download [arquivos XML de modelo](attachments/8421394/8618082.zip).

### Exportar para PDF

Quando um modelo está totalmente configurado, você está pronto para exportar listas ou itens para arquivos PDF.

Exportando uma lista para PDF usando um modelo de lista de tarefas:

![Exportar para PDF](creating-and-exporting-template_7.png)

{{% /alert %}}

---
title: Criando e Exportando Template
type: docs
weight: 10
url: /pt/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: Você pode criar e exportar templates para PDF no SharePoint usando a API PDF SharePoint.
---

{{% alert color="primary" %}}

Este artigo mostra como criar e exportar templates usando Aspose.PDF para SharePoint.

A partir do Aspose.PDF para SharePoint 1.9.2, o suporte a templates PDF também cobre sub-sites do SharePoint.

{{% /alert %}}

## **Criando e Exportando Templates**
{{% alert color="primary" %}}

Para usar o recurso de exportação do Aspose.PDF para SharePoint, primeiro crie uma lista que utilize “PDF Templates”.

Criando uma lista que utilize PDF Templates:

![todo:image_alt_text](creating-and-exporting-template_1.png)

Dois templates de documentos, Task Form Templates e Task List Templates são criados:

![todo:image_alt_text](creating-and-exporting-template_2.png)

O formulário de template permite que você insira as seguintes informações:

- **Name**: o nome do arquivo do template.
- **Title**: o título do template.
 (By default, o mesmo que o nome do arquivo.)
- **Descrição**: uma descrição do modelo. Uma boa descrição torna o modelo mais fácil de usar.
- **Tipos de Lista Atribuídos**: IDs de lista separados por vírgula (relacionados ao modelo. Este campo também pode conter o valor **AllListTypes**. Este campo é aplicável apenas quando o campo **Type** está definido como **List**).
- **Tipos de Conteúdo Atribuídos**: IDs de tipos de conteúdo separados por vírgula (relacionados ao modelo. Este campo pode estar definido como **AllListTypes**. Este campo é aplicável apenas quando o campo **Type** está definido como **Item**).
- **Tipo**: modelo de lista ou modelo de item.
- **Status**: as opções são ativo, inativo (invisível para todos) e depuração (visível apenas para administradores).

**O formulário de Modelos de Lista de Tarefas:**

![todo:texto_alt_da_imagem](creating-and-exporting-template_3.png)

**O formulário de Modelos de Formulário de Tarefas:**

![todo:texto_alt_da_imagem](creating-and-exporting-template_4.png)

Quando eles são salvos, os novos modelos aparecem na lista de modelos, prontos para serem usados:

**Dois modelos de lista de tarefas:**
![todo:image_alt_text](creating-and-exporting-template_5.png)

**Um modelo de formulário de tarefa:**

![todo:image_alt_text](creating-and-exporting-template_6.png)

#### **Desenvolvendo Modelos**
Um modelo é um arquivo XML baseado no Aspose XML PDF. Para criar um modelo para uma lista, coloque marcadores especiais relacionados ao nome interno do campo do tipo de conteúdo de destino do SharePoint no arquivo XML PDF.
##### **Marcadores**
- **SPListItemsCount** – substituído pela contagem de itens da lista.
- **SPListTitle** – substituído pelo título da lista.
- **SPTableIterator** – colocado na primeira célula da tabela e marca a tabela para iteração completa.
- **SPRowIterator** – colocado na primeira célula da tabela e marca a tabela para iteração de linha.
- **SPField** – substituído pelo valor do campo do item.

Para referência, por favor, baixe [arquivos XML de modelo](attachments/8421394/8618082.zip).
#### **Exportar para PDF**
Quando um modelo está completamente configurado, você está pronto para exportar listas ou itens para arquivos PDF.

**Exportando uma lista para PDF usando um modelo de lista de tarefas:**
![todo:texto_alt_da_imagem](creating-and-exporting-template_7.png)

{{% /alert %}}
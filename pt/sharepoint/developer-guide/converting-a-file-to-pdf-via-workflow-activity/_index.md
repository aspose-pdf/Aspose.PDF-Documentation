---
title: Convertendo um arquivo em PDF por meio de atividade de fluxo de trabalho
linktitle: Convertendo um arquivo em PDF por meio de atividade de fluxo de trabalho
type: docs
weight: 50
url: /pt/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: A API PDF SharePoint pode ser usada em um fluxo de trabalho do SharePoint que converte um documento em PDF.
---

{{% alert color="primary" %}}

O suporte para fluxos de trabalho é uma funcionalidade fundamental do Microsoft Office SharePoint Server. Os fluxos de trabalho ajudam a automatizar a movimentação de documentos de acordo com a lógica de negócios e a simplificar o custo e o tempo da organização dos documentos. Este artigo demonstra como usar Aspose.PDF para SharePoint em um fluxo de trabalho que converte um documento em PDF.

{{% /alert %}}

## Configurando um fluxo de trabalho

Este exemplo cria um fluxo de trabalho que converte qualquer novo item de uma biblioteca de documentos para o formato PDF e o armazena em outra biblioteca de documentos. O exemplo usa a biblioteca **Documentos Pessoais** como biblioteca de origem e a subpasta **Pdf** na biblioteca **Documentos Compartilhados** como biblioteca de destino.

Aspose.PDF para SharePoint suporta conversão de arquivos HTML, texto e imagem.

### Projete o fluxo de trabalho usando o SharePoint Designer

1. Abra o **SharePoint Designer** e conecte-se ao site onde o fluxo de trabalho será implementado.
1. Selecione **Fluxos de trabalho** em **objetos do site** e abra **Listar fluxo de trabalho**.
1. Selecione a biblioteca **Documentos Pessoais** para criar e anexar um novo fluxo de trabalho de lista à biblioteca de documentos.

   **Selecionando Documentos Pessoais no menu**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_1](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. Crie e anexe o fluxo de trabalho da lista à biblioteca **Documentos pessoais** digitando um nome e uma descrição do fluxo de trabalho.
1. Clique em **OK** para concluir esta etapa.

   **Criando um fluxo de trabalho de lista**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_2](converting-a-file-to-pdf-via-workflow-activity_2.png)

Um editor de etapas do fluxo de trabalho é exibido. Isso é usado para definir condições e ações para fluxos de trabalho. Agora adicione uma ação para converter um novo documento em PDF sem qualquer condição, em **Aspose Actions**.

1. Selecione a ação **Converter arquivo em PDF via Aspose.PDF** no menu **Ação**.

   **Seleção e ação**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_3](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Configure os parâmetros de ação:
   1. Defina o parâmetro **esta pasta** para a pasta de destino.
   1. Deixe os outros parâmetros de ação como valores padrão ou defina-os usando a janela de propriedades da ação. O valor padrão para o parâmetro **Overwrite** é falso.

      **O Editor de Fluxo de Trabalho**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_4](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Definindo a biblioteca de destino**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_5](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Definindo as propriedades**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_6](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. No menu **Fluxo de trabalho**, selecione **Configurações do fluxo de trabalho**.
1. Selecione **iniciar fluxo de trabalho automaticamente quando um novo item for criado** e desmarque outras opções em **Opções iniciais**.

   **Definindo as opções de início**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_7](converting-a-file-to-pdf-via-workflow-activity_7.png)

O design do fluxo de trabalho está concluído.

1. Salve e publique o fluxo de trabalho para implementá-lo no site do SharePoint.

### Teste o fluxo de trabalho

Para testar o fluxo de trabalho:

1. Abra o site do SharePoint e carregue um novo documento na biblioteca de documentos **Documentos Pessoais**.
   Aspose.PDF for SharePoint suporta conversão de arquivos HTML, arquivos de texto e imagens (JPG, PNG, GIF, TIFF e BMP*) para PDF. O fluxo de trabalho é configurado para iniciar automaticamente quando um novo item é criado, para que os arquivos sejam processados ​​automaticamente.
1. Atualize o navegador.
   O status do fluxo de trabalho aparece na coluna do fluxo de trabalho, **Aspose.PDF Workflow** neste caso.

   **Adicionando um documento à biblioteca de origem**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_8](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Abra a biblioteca de documentos de destino para visualizar o documento convertido. **Documentos Compartilhados/Pdf** é o caminho neste exemplo.

   **A biblioteca de destino**

![Convertendo arquivo em PDF por meio da atividade de fluxo de trabalho_9](converting-a-file-to-pdf-via-workflow-activity_9.png)


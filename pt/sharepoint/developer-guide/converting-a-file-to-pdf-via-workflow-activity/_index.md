---
title: Convertendo um arquivo para PDF via atividade de Workflow
linktitle: Convertendo um arquivo para PDF via atividade de Workflows
type: docs
weight: 50
url: /pt/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: A API PDF SharePoint pode ser usada em um fluxo de trabalho do SharePoint que converte um documento para PDF.
---

{{% alert color="primary" %}}

O suporte a fluxos de trabalho é uma funcionalidade chave do Microsoft Office SharePoint Server. Os fluxos de trabalho ajudam a automatizar o movimento de documentos de acordo com a lógica de negócios e a otimizar o custo e o tempo de organização de documentos. Este artigo demonstra como usar Aspose.PDF for SharePoint em um fluxo de trabalho que converte um documento para PDF.

{{% /alert %}}

## **Configurando um fluxo de trabalho**

Este exemplo cria um fluxo de trabalho que converte qualquer novo item em uma biblioteca de documentos para o formato PDF e o armazena em outra biblioteca de documentos. O exemplo usa a biblioteca **Personal Documents** como a biblioteca de origem e a subpasta **Pdf** na biblioteca **Shared Documents** como a biblioteca de destino.

Aspose.PDF for SharePoint suporta a conversão de arquivos HTML, de texto e de imagem.

### **Desenhe o fluxo de trabalho usando o SharePoint Designer**

1. Abra **SharePoint Designer** e conecte-se ao site onde o fluxo de trabalho será implementado.
1. Selecione **Workflows** em **site objects** e então abra **List Workflow**.
1. Selecione a biblioteca **Personal Documents** para criar e anexar um novo fluxo de trabalho de lista à biblioteca de documentos.

   **Selecionando Personal Documents no menu**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. Crie e anexe o fluxo de trabalho de lista à biblioteca **Personal Documents** digitando um nome e uma descrição para o fluxo de trabalho.
1. Clique em **OK** para concluir esta etapa.

   **Criando um fluxo de trabalho de lista**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



Um editor de etapas de fluxo de trabalho aparece. Ele é usado para definir condições e ações para fluxos de trabalho. Agora adicione uma ação para converter um novo documento em PDF sem nenhuma condição, a partir de **Aspose Actions**.

1. Selecione a ação **Convert file to PDF via Aspose.PDF** do menu **Action**.

   **Selecionando uma ação**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. Configure os parâmetros da ação:
   1. Defina o parâmetro **this folder** para a pasta de destino.
   1. Deixe os outros parâmetros de ação com os valores padrão ou defina-os usando a janela de propriedades da ação. O valor padrão do parâmetro **Overwrite** é falso.

      **Editor de Workflow**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Definindo a biblioteca de destino**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Definindo as propriedades**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. No menu **Workflow**, selecione **Workflow Settings**.
1. Selecione **iniciar fluxo de trabalho automaticamente quando um novo item for criado** e limpe as demais opções em **Opções de Início**.

   **Configurando as opções de início**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



O design do fluxo de trabalho está concluído.

1. Salve e publique o fluxo de trabalho para implementá‑lo no site SharePoint.

### **Testar o Fluxo de Trabalho**

Para testar o fluxo de trabalho:

1. Abra o site do SharePoint e faça upload de um novo documento na biblioteca de documentos **Personal Documents**.
   Aspose.PDF for SharePoint suporta conversão de arquivos HTML, arquivos de texto e imagens (JPG, PNG, GIF, TIFF e BMP*) para PDF. O fluxo de trabalho está configurado para iniciar automaticamente quando um novo item é criado, portanto os arquivos são processados automaticamente.
1. Atualize o navegador.
   O status do fluxo de trabalho aparece na coluna de fluxo de trabalho, **Aspose.PDF Workflow** neste caso.

   **Adicionando um documento à biblioteca de origem**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. Abra a biblioteca de documentos de destino para visualizar o documento convertido. **Shared Documents/Pdf** é o caminho neste exemplo.

   **A biblioteca de destino**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)


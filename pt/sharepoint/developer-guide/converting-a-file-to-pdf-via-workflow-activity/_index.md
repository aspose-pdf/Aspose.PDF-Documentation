---
title: Convertendo um Arquivo para PDF via Atividade de Fluxo de Trabalho
type: docs
weight: 50
url: pt/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: A API PDF SharePoint pode ser usada em um fluxo de trabalho do SharePoint que converte um documento para PDF.
---

{{% alert color="primary" %}}

O suporte para fluxos de trabalho é uma funcionalidade chave do Microsoft Office SharePoint Server. Os fluxos de trabalho ajudam a automatizar o movimento de documentos de acordo com a lógica de negócios e a otimizar o custo e o tempo de organização de documentos. Este artigo demonstra como usar o Aspose.PDF para SharePoint em um fluxo de trabalho que converte um documento para PDF.

{{% /alert %}}
## **Configurando um Fluxo de Trabalho**

Este exemplo cria um fluxo de trabalho que converte qualquer novo item em uma biblioteca de documentos para o formato PDF e o armazena em outra biblioteca de documentos. O exemplo usa a biblioteca **Documentos Pessoais** como a biblioteca de origem e a subpasta **Pdf** na biblioteca **Documentos Compartilhados** como a biblioteca de destino.

O Aspose.PDF para SharePoint suporta a conversão de arquivos HTML, texto e imagem.

### **Design the Workflow using SharePoint Designer**

1. Abra o **SharePoint Designer** e conecte-se ao site onde o fluxo de trabalho será implementado.
1. Selecione **Workflows** em **objetos do site** e, em seguida, abra **List Workflow**.
1. Selecione a biblioteca **Documentos Pessoais** para criar e anexar um novo fluxo de trabalho de lista à biblioteca de documentos.

   **Selecionando Documentos Pessoais no menu**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. Crie e anexe o fluxo de trabalho da lista à biblioteca **Documentos Pessoais** digitando um nome e uma descrição para o fluxo de trabalho.
1. Clique em **OK** para completar esta etapa.

   **Criando um fluxo de trabalho de lista**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



Um editor de etapas de fluxo de trabalho aparece. Isso é usado para definir condições e ações para fluxos de trabalho. Agora adicione uma ação para converter um novo documento em PDF sem nenhuma condição, a partir de **Aspose Actions**.
1. Selecione a ação **Converter arquivo para PDF via Aspose.PDF** no menu **Ação**.

   **Selecionando uma ação**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Configure os parâmetros da ação:
   1. Defina o parâmetro **esta pasta** para a pasta de destino.
   1. Deixe os outros parâmetros de ação como valores padrão ou configure usando a janela de propriedades da ação. O valor padrão para o parâmetro **Sobrescrever** é falso.

      **O Editor de Fluxo de Trabalho**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Definindo a biblioteca de destino**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Definindo as propriedades**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. No menu **Fluxo de Trabalho**, selecione **Configurações do Fluxo de Trabalho**.
1. Selecione **iniciar fluxo de trabalho automaticamente quando um novo item for criado** e desmarque outras opções em **Opções de Início**.

   **Definindo as opções de início**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)

O design do fluxo de trabalho está concluído.

1. Salve e publique o fluxo de trabalho para implementá-lo no site do SharePoint.

### **Testar o Fluxo de Trabalho**

Para testar o fluxo de trabalho:

1. Abra o site do SharePoint e faça o upload de um novo documento na biblioteca de documentos **Documentos Pessoais**. O Aspose.PDF para SharePoint suporta a conversão de arquivos HTML, arquivos de texto e imagens (JPG, PNG, GIF, TIFF e BMP*) para PDF. O fluxo de trabalho está configurado para iniciar automaticamente quando um novo item é criado, então os arquivos são processados automaticamente.
1. Atualize o navegador. O status do fluxo de trabalho aparece na coluna de fluxo de trabalho, **Aspose.PDF Workflow** neste caso.

   **Adicionando um documento à biblioteca de origem**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Abra a biblioteca de documentos de destino para visualizar o documento convertido. **Documentos Compartilhados/Pdf** é o caminho neste exemplo.

   **A biblioteca de destino**
![todo:texto_alternativo_da_imagem](converting-a-file-to-pdf-via-workflow-activity_9.png)
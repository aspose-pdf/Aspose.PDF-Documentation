---
title: Como Criar e Converter um Arquivo XML para PDF
type: docs
weight: 30
url: /pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: API PDF SharePoint é capaz de criar e converter arquivos XML para o formato PDF.
---

{{% alert color="primary" %}}

Aspose.PDF para SharePoint é construído com base em nosso premiado componente Aspose.PDF para .NET. Aspose.PDF para .NET oferece recursos notáveis desde a criação de documentos PDF do zero até a manipulação de arquivos PDF existentes. Entre esses recursos, a conversão de XML para PDF é um dos grandes recursos suportados por este produto. Portanto, acreditamos que Aspose.PDF para SharePoint também será capaz de converter arquivos XML para o formato PDF.

{{% /alert %}}

## **Criando um Arquivo XML e Convertendo-o para PDF**

{{% alert color="primary" %}}

Passo a passo, este artigo guia você através do processo de criação de um arquivo XML e sua conversão para PDF:
1. [Criar um arquivo XML](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Criar um modelo PDF](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Carregar o modelo XML](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Especificar o caminho para o caminho de origem](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Especificar propriedades do arquivo](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Exportar o arquivo para PDF](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Salvar o arquivo PDF](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
   
#### **Passo 1: Criar Arquivo XML**
Primeiro crie um arquivo XML baseado no Aspose.PDF para o Modelo de Objeto de Documento .NET.

De acordo com o Aspose.PDF para o DOM .NET, um documento PDF contém uma coleção de objetos Section, e uma Section contém um ou mais elementos Paragraph.
 Text é um objeto de nível de Parágrafo e pode conter um ou mais segmentos. Abaixo, uma string de texto de exemplo é adicionada a um objeto Segment e adicionada a um objeto Text. Finalmente, o elemento Text é adicionado à coleção de parágrafos do objeto Section.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Olá Mundo</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **Etapa 2: Criar Modelo de PDF**
Antes de continuar, certifique-se de que o servidor SharePoint Foundation 2010 esteja devidamente instalado e configurado no sistema onde a conversão ocorrerá.

1. Faça login no site do SharePoint.
1. Selecione **Ação do Site** e **Todos os Itens**.
1. Selecione a opção **Criar** e selecione **Modelo de PDF** na lista.
1. Insira um nome para o modelo.
1. Clique em **Criar**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Etapa 3: Carregar Modelo XML**

Uma vez que o modelo tenha sido criado, carregue [o arquivo XML](/pdf/pt/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. Na página do modelo de PDF, selecione **Adicionar novo item**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Passo 4: Especificar o Caminho do Arquivo de Origem**
Na caixa de diálogo de upload do documento:

1. Clique em **Procurar** e localize o arquivo XML no seu sistema. Você pode habilitar a caixa de seleção para a opção de sobrescrever arquivo existente.
1. Pressione o botão **OK**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Passo 5: Especificar Propriedades do Arquivo**
Quando o arquivo é carregado, adicione informações nos campos obrigatórios (marcados com um asterisco vermelho: *).

Para este exemplo, uma descrição de amostra foi adicionada e os seguintes campos foram preenchidos:

1. Uma breve descrição do documento.
1. Insira **AllListTypes** para o campo **Tipos de Lista Atribuídos**.
1. Selecione **Lista** no menu **Tipo**.
   Certifique-se de que o status permaneça **Ativo**.
1. Clique em **Salvar** para salvar as propriedades.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Passo 6: Exportar para PDF**

Quando o arquivo XML foi adicionado ao modelo de PDF:
Either:

1. Clique com o botão direito no arquivo test.xml.
1. Selecione **Exportar para PDF** no menu.

Or:

1. Selecione **Aspose Tools** em **Ferramentas da Biblioteca**.
1. Clique em **Exportar**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Passo 7: Salvar Documento PDF**
1. No diálogo Exportar para PDF, selecione **Armazenamento de Modelo** (o local onde o arquivo fonte está armazenado).
1. Selecione o arquivo para exportar no menu **Nome do Modelo**.
1. Clique em **Exportar para PDF** para salvar o documento PDF final.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Abrir o PDF**
O documento PDF foi salvo e pode ser aberto. Na imagem abaixo, observe a frase "Hello World" que estava na tag {segment] no XML. Também note que o Produtor de PDF é Aspose.PDF para SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
---
title: Visual Studio Export GridView To PDF Control
type: docs
weight: 10
url: /pt/net/visual-studio-export-gridview-to-pdf-control/
---

## Introdução

Export GridView To Pdf Control é um controle de servidor ASP.NET que permite a exportação do conteúdo de um GridView para um documento Pdf usando [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx). Ele adiciona um botão **Exportar para Pdf** no topo do controle GridView. Ao clicar no botão, o conteúdo do GridView é exportado dinamicamente para um documento Pdf e, em seguida, o arquivo exportado é automaticamente baixado para o local do disco selecionado pelo usuário em apenas alguns segundos.

### Recursos do Módulo

Esta versão inicial do controle oferece os seguintes recursos:

- Obtenha uma cópia offline do seu conteúdo online favorito do GridView para edição, compartilhamento e impressão em um documento Pdf muito popular.
- Herdado do controle GridView ASP.NET padrão e, portanto, possui todas as suas características e propriedades.
- Funciona com todas as versões do .NET a partir do .NET 2.0.
- Capacidade de personalizar/localizar o texto do botão de Exportação.
- Capacidade de personalizar/localizar o texto do botão de Exportação.
- Opção para Exportar em modo Paisagem caso o conteúdo do GridView seja mais largo e não caiba no modo Retrato padrão
- Aplicar a aparência e sensação do seu próprio tema no botão de Exportação usando css.
- Opção para adicionar um cabeçalho personalizado no topo do documento exportado
- Opção para salvar cada documento exportado no servidor em um caminho de disco configurável
- Opção para exportar a página atual ou todas as páginas quando a paginação está ativada

## Requisitos do Sistema e Plataformas Suportadas

### Requisitos do Sistema

O controle Export GridView para PDF para Visual Studio pode ser usado em qualquer sistema que tenha o IIS e o .NET framework 2.0 ou superior instalado.

### Plataformas Suportadas

O controle Export GridView para PDF para Visual Studio é suportado em todas as versões do ASP.NET que funcionam no .NET framework 2.0 ou superior. Você pode usar qualquer uma das seguintes versões do Visual Studio para usar este controle em suas aplicações ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## Downloading
## Baixando

Você pode baixar o Export GridView To Pdf Control de um dos seguintes locais

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## Instalando

É muito simples e fácil instalar o Export GridView To Pdf Control, por favor siga estes passos simples

### **Para Visual Studio 2010, 2012 e 2013**

1. Extraia o arquivo zip baixado, i.e. Aspose.PDF.GridViewExport_1.0.zip
1. Dê duplo clique no arquivo VSIX Aspose.PDF.GridViewExport.vsix
1. Um diálogo aparecerá mostrando as versões do Visual Studio disponíveis e suportadas instaladas em seu computador
1. Selecione as que você deseja adicionar o Export GridView To Pdf Control.
1. Clique em Instalar

Você receberá um diálogo de sucesso uma vez que a instalação estiver concluída.

**Nota:** Por favor, certifique-se de reiniciar o Visual Studio para que as alterações tenham efeito.

### **Para Visual Studio 2005, 2008 e edições Express**

Por favor, siga estes passos para integrar o Export GridView To Pdf Control no Visual Studio para fácil arrastar e soltar, assim como outros controles ASP.NET
Siga estes passos para integrar o controle Export GridView Para Pdf no Visual Studio para fácil arrasto e solta como outros controles ASP.NET

1. Extraia o arquivo zip baixado, i.e. Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Certifique-se de executar o Visual Studio como Administrador

No menu Ferramentas, clique em Escolher Itens da Caixa de Ferramentas.

1. Clique em Procurar.
   A caixa de diálogo Abrir aparece.
1. Navegue até a pasta extraída e selecione Aspose.PDF.GridViewExport.dll
1. Clique em OK.

Quando você abrir um controle aspx ou ascx no Toolbox do lado esquerdo, você verá ExportGridViewToPdf sob a aba Geral

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## Usando

Uma vez instalado, é muito fácil começar a usar este controle em suas aplicações ASP.NET

|**Para .NET framework 4.0 e acima**|**Para .NET framework 2.0 e acima**|** |
| :- | :- | :- |
|Para aplicações rodando em .NET framework 4.0 e acima no Visual Studio 2010 e acima, você deve ver o controle **ExportGridViewToPdf** na aba **Aspose** na Barra de Ferramentas como mostrado abaixo.
|Para aplicações rodando no .NET framework 4.0 e acima no Visual Studio 2010 e superiores, você deve ver o controle **ExportGridViewToPdf** na aba **Aspose** na barra de ferramentas como mostrado abaixo.

### Adicionando manualmente o controle ExportGridViewToPdf

Se você tiver algum problema usando os métodos acima que utilizam a Toolbox do Visual Studio, você pode adicionar manualmente este controle à sua aplicação ASP.NET rodando em qualquer framework .NET superior a 2.0

1. Se você estiver usando o Visual Studio, certifique-se de executá-lo como Administrador
1. Adicione uma referência ao **Aspose.PDF.GridViewExport.dll** disponível no pacote de download extraído no seu projeto ASP.NET ou aplicação web. Certifique-se de que sua aplicação web/Visual Studio tenha acesso total a essa pasta, caso contrário, você pode receber uma exceção de Acesso Negado.
1. Adicione esta linha ao topo da página, controle ou MasterPage

```csharp
<%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```

1.
```csharp
 <aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### FAQs

Perguntas comuns e problemas que você pode enfrentar ao usar este Controle

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. Não consigo ver o controle ExportGridViewToPdf na Caixa de Ferramentas</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 e superior</strong></p>
<ol><li>Certifique-se de que você instalou este controle usando o arquivo de extensão VSIX encontrado no pacote baixado. Para verificar, vá em Ferramentas -&gt; Extensões e Atualizações. Em Instalados, você deve ver 'Aspose Export Export GridView To Pdf Control'. Se não o encontrar, tente reinstalá-lo.</li>
<li>Certifique-se de que sua aplicação web está rodando em .NET framework 4.0 ou superior, para versões inferiores do .NET framework, por favor, verifique o método alternativo acima.
<li>Certifique-se de que sua aplicação web está rodando no framework .NET 4.0 ou superior; para versões inferiores do framework .NET, por favor, verifique o método alternativo acima.
Versões Antigas do Visual Studio</li>
<li>Certifique-se de que você adicionou manualmente esse controle à sua Caixa de Ferramentas conforme as instruções acima.</li></ol>
          </div>
        </div>
    </div>

    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">2. Estou recebendo o erro 'Acesso negado' ao rodar a aplicação</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <ol>
               <li>Se você está enfrentando esse problema em produção, então certifique-se de copiar ambos os arquivos Aspose.PDF.dll e Aspose.PDF.GridViewExport.dll para a sua pasta bin.</li>
               <li>Se você está usando o Visual Studio, certifique-se de executá-lo como Administrador, mesmo que já esteja logado como administrador.</li>

<div>
    <div>
        <div>
            <div>
               <ol>
                    <li>Se você está usando o Visual Studio, certifique-se de executá-lo como Administrador, mesmo que já esteja logado como administrador.</li>
               </ol>
            </div>
        </div>
    </div>
</div>

### **Propriedades do Controle Aspose .NET Export GridView Para Pdf**

As seguintes propriedades estão disponíveis para configurar e utilizar as funcionalidades oferecidas por este controle

|**Nome da Propriedade**|**Tipo**|**Exemplo/Valores Possíveis**|**Descrição**|
| :- | :- | :- | :- |
|ExportButtonText|string|Exportar para Pdf|Você pode usar esta propriedade para substituir o texto padrão existente|
|ExportButtonCssClass|string|btn btn-primary|Classe CSS que é aplicada ao div externo do botão de exportação. Para aplicar css no botão, você pode usar .yourClass input|
|ExportInLandscape|bool|true ou false|Se verdadeiro, altera a orientação do documento de saída para paisagem. O padrão é Retrato|
| | | | |
|ExportFileHeading|string|Exemplo de Relatório de Exportação GridView|Você pode usar tags html para adicionar estilo ao seu cabeçalho|
|ExportOutputPathOnServer|string|c:/temp|Caminho no disco local do servidor onde uma cópia da exportação é automaticamente salva.|
```
|ExportOutputPathOnServer|string|c:/temp|Caminho local no servidor para onde uma cópia da exportação é automaticamente salva.
|ExportDataSource|object|allRowsDataTable|Define o objeto do qual este controle de vinculação de dados recupera sua lista de itens de dados. O objeto deve conter todos os dados que precisam ser exportados. Esta propriedade é usada em adição à propriedade DataSource normal e é útil quando a paginação personalizada está habilitada e a página atual apenas busca as linhas a serem exibidas na tela.|
|LicenseFilePath|string| |Caminho local no servidor para o arquivo de licença. Por exemplo c:/inetpub/Aspose.PDF.lic|

Um exemplo de controle Export GridView para Pdf com todas as propriedades utilizadas é mostrado abaixo

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Exportar para Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Relatório Exemplo</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## Demonstração em Vídeo

Por favor, verifique [o vídeo](https://www.youtube.com/watch?v=WNJ7T8u4JlM) abaixo para ver o módulo em ação.

### Suporte

Desde os primeiros dias da Aspose, sabíamos que apenas fornecer bons produtos não seria suficiente. Também precisávamos oferecer um bom serviço. Somos desenvolvedores também e entendemos como é frustrante quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa fazer. Estamos aqui para resolver problemas, não criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que use nosso produto, seja comprando ou utilizando uma avaliação, merece nossa total atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionadas a este Pdf usando qualquer uma das seguintes plataformas

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Galeria do Visual Studio - Perguntas e Respostas](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Rede de Desenvolvedores Microsoft - Perguntas e Respostas](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Microsoft Developer Network - Perguntas e Respostas](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### Estender e Contribuir

Aspose .NET Export GridView para PDF para Visual Studio é de código aberto e seu código-fonte está disponível nos principais sites de codificação social listados abaixo. Os desenvolvedores são incentivados a baixar o código-fonte e estender a funcionalidade conforme suas próprias necessidades.

#### Código-Fonte

Você pode obter o código-fonte mais recente em um dos seguintes locais

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### Como configurar o código-fonte

Você precisa ter o seguinte instalado para abrir e estender o código-fonte

- Visual Studio 2010

Por favor, siga estes passos simples para começar

1. Baixe/Clone o código-fonte.
1.
1.
1. Navegue até o código-fonte mais recente que você baixou e abra **Aspose.PDF.GridViewExport.sln**

#### Visão geral do código-fonte

Existem três projetos na solução

- Aspose.PDF.GridViewExport - Contém o pacote VSIX e o Server Pdf para .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - GridView Pdf estendido para .NET 2.0
- Aspose.PDF.GridViewExport.Website - Projeto web para testar o GridView Pdf exportável para Word

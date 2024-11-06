---
title: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: pt/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Agora que o SharePoint está instalado e configurado no servidor RS e o RS está configurado através do Gerenciador de Configuração do Reporting Services, podemos avançar para a configuração dentro do Central Admin. O RS 2008 R2 realmente simplificou esse processo. Usávamos ter um processo de 3 etapas que você tinha que realizar para fazer isso funcionar. Agora, temos apenas um passo.

{{% /alert %}}

{{% alert color="primary" %}}

Queremos ir para o site da Web do Administrador Central e, em seguida, para Configurações Gerais da Aplicação. No final, veremos Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Imagem1**:- Diálogo de configuração do SharePoint

Selecione o link "Integração do Reporting Services". A tela a seguir será exibida.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Especificar credenciais de integração dos Serviços de Relatório

{{% /alert %}}

## URL do Serviço Web:

**Forneceremos a URL do Servidor de Relatórios que encontramos no Gerenciador de Configuração dos Serviços de Relatório.**

## Modo de Autenticação:

**Também selecionaremos um Modo de Autenticação. O seguinte link do MSDN detalha quais são esses modos.
Visão Geral de Segurança para Serviços de Relatório no Modo Integrado do SharePoint**

{{% alert color="primary" %}}

**Em resumo, se o seu site estiver usando Autenticação de Claims, você sempre usará Autenticação Confiável, independentemente do que escolher aqui. Se você quiser passar credenciais do Windows, deverá escolher Autenticação do Windows. Para Autenticação Confiável, passaremos o token SPUser e não dependeremos da credencial do Windows. Você também deverá usar Autenticação Confiável se configurou seus sites no Modo Clássico para NTLM e o RS estiver configurado para NTLM. Kerberos seria necessário para usar Autenticação do Windows e passar isso para sua fonte de dados.**

{{% /alert %}}

## Ativar recurso:

{{% alert color="primary" %}}

**Isso lhe dá a opção de ativar os Serviços de Relatório em todas as coleções de sites, ou você pode escolher em quais deseja ativá-lo. Isso realmente significa quais sites poderão usar os Serviços de Relatório. Quando estiver concluído, você deverá ver os seguintes resultados**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Imagem3:**- Integração bem-sucedida dos Serviços de Relatório com o ambiente do SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Voltando ao URL do ReportServer, devemos ver algo semelhante ao seguinte

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Imagem4:**- Os Serviços de Relatório estão conectados com sucesso ao ambiente do SharePoint

**NOTA:** ***Se o seu site do SharePoint estiver configurado para SSL, ele não aparecerá nesta lista. É um problema conhecido e não significa que há um problema. Seus relatórios ainda devem funcionar.***
{{% /alert %}}

Agora que integramos com sucesso ambos os produtos, estamos prontos para usar o Reporting Services no SharePoint 2010. Assim como na versão anterior, temos um recurso (ativado quando configuramos a Integração do Reporting Services) na "Funcionalidade da Coleção de Sites". Além disso, a instalação adicionou 3 tipos de conteúdo para adicionar ao nosso site. Na Imagem 7, podemos ver 2 desses tipos de conteúdo adicionados em uma biblioteca de documentos para criar um relatório personalizado, como podemos ver na Imagem5 abaixo.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Imagem5:**- Construtor de Relatórios
{{% alert color="primary" %}}

O “Construtor de Relatórios” é um controle ActiveX, então precisamos baixá-lo pelo servidor, como podemos ver na Imagem 6 abaixo.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Imagem6:**- Baixar e instalar o Construtor de Relatórios
{{% /alert %}}

{{% alert color="primary" %}}

Uma vez que o processo de download é concluído, carregue o controle “Construtor de Relatórios”. Agora estamos prontos para projetar nosso primeiro relatório, como mostrado na Imagem7 abaixo.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Criador de Relatórios – Novo assistente de geração de relatórios
{{% /alert %}}

{{% alert color="primary" %}}

Após criar nosso relatório, podemos salvá-lo na biblioteca de documentos criada para colocar os relatórios no nosso SharePoint 2010. O outro tipo de conteúdo deve ser usado para criar conexões compartilhadas como fonte de dados e salvá-las em uma biblioteca de documentos no SharePoint. Podemos criar uma biblioteca de documentos, adicionar esse tipo de conteúdo e depois ter nossas conexões disponíveis para alterar a fonte de dados dos relatórios.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integração bem-sucedida do Aspose.PDF para Serviços de Relatório com MS SharePoint
{{% /alert %}}
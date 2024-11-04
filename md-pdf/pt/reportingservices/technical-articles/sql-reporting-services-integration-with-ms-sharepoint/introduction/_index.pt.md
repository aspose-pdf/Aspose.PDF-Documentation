---

title: Introdução  
type: docs  
weight: 10  
url: /reportingservices/introduction/  
lastmod: "2021-06-05"  

---

{{% alert color="primary" %}}

Aspose.PDF para Reporting Services tem sido muito notável para a geração de PDF através do SQL Reporting Services há muitos anos e fornece diversas opções de configuração e parametrização que não são suportadas por padrão no SQL Reporting Services. Recentemente, recebemos algumas solicitações sobre a integração do Aspose.PDF para Reporting Services com o SharePoint. Para este artigo, vamos nos concentrar no MS SharePoint 2010. Antes de prosseguirmos, assumimos que você já configurou um Farm do SharePoint. Neste exemplo, vamos usar o SharePoint Cloud completo. No entanto, os passos são similares para o SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de prosseguirmos, vamos dar uma olhada nos tópicos de referência que consultamos durante a preparação deste artigo.

- [Visão geral da Integração de Serviços de Relatórios e Tecnologia SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuração do Ambiente

Nossa configuração consiste em 4 servidores. Inclui um Controlador de Domínio, um SQL Server, um Servidor SharePoint e um servidor para Serviços de Relatórios. Você pode optar por ter o SharePoint e os Serviços de Relatórios na mesma máquina, o que simplificará um pouco isso, e eu destacarei algumas das diferenças.

## Pré-requisitos de Instalação

{{% alert color="primary" %}}

O suplemento dos Serviços de Relatórios para SharePoint é um dos componentes-chave para fazer a Integração funcionar corretamente. O suplemento precisa ser instalado em qualquer um dos Web Front Ends (WFE) que estão na sua farm do SharePoint juntamente com o servidor Central Admin. Uma das novas mudanças com o SQL 2008 R2 e o SharePoint 2010 é que o suplemento 2008 R2 agora é um pré-requisito para a instalação do SharePoint. Isso significa que o RS Add-In será instalado quando você for instalar o SharePoint. Isso foi mostrado e destacado na figura abaixo. Isso realmente evita muitos problemas que vimos com o SP 2007 e o RS 2008 ao instalar o suplemento.

![todo:image_alt_text](introduction_1.png)

**Imagem1 :- Suplemento de Serviços de Relatórios para SharePoint**
{{% /alert %}}

## Autenticação do SharePoint

**Antes de entrarmos nas peças de Integração do RS, uma coisa que eu quero destacar sobre a Farm do SharePoint é como você configura o Site. Mais especificamente, como você configura a autenticação para o site. Se será Clássico ou Claims. Esta escolha é importante no início. Eu não acredito que você possa mudar esta opção uma vez que esteja feita. Se você puder mudar, não seria um processo simples.

NOTA: ***O Reporting Services 2008 R2 NÃO é compatível com Claims***

Mesmo se você escolher que seu site do SharePoint use Claims, o Reporting Services em si não é compatível com Claims. Dito isso, isso afeta como a autenticação funciona com o Reporting Services. Então, qual é a diferença do ponto de vista do Reporting Services? Depende se você quer encaminhar as Credenciais do Usuário para a fonte de dados. Clássico:- Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados de back-end (precisará usar Kerberos para isso). Claims:- Um token de Claims é usado e não um token do Windows. O RS sempre usará Autenticação Confiável neste cenário e só terá acesso ao token SPUser. Você precisará armazenar suas credenciais dentro de sua fonte de dados.

Clássico :- Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados de back-end (precisará usar Kerberos para isso).
Claims :- Um token de Claims é utilizado e não um token do Windows. RS sempre usará a Autenticação Confiável neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais dentro de sua fonte de dados.

Por enquanto, queremos apenas focar na configuração do RS. Neste ponto, o SharePoint está instalado na minha máquina SharePoint e configurado com um Site de Autenticação Clássica na porta 80. No Servidor RS, acabei de instalar os Serviços de Relatório e é isso.
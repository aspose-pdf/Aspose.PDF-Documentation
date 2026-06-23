---
title: Introdução
linktitle: Introdução
type: docs
weight: 10
url: /pt/reportingservices/introduction/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services tem sido muito notável para a geração de PDF através do SQL Reporting Services há muitos anos e fornece diversas opções de configuração e parametrização que não são suportadas por padrão no SQL Reporting Services. Recentemente recebemos algumas solicitações sobre a Integração do Aspose.PDF for Reporting Services com o SharePoint. Neste artigo, vamos nos concentrar no MS SharePoint 2010. Antes de prosseguirmos, assumimos que você já tem um SharePoint Farm configurado. Neste exemplo, usaremos o SharePoint Cloud completo. Contudo, as etapas são semelhantes para o SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de prosseguirmos, vamos dar uma olhada nos tópicos de referência que consultamos durante a preparação deste artigo.

- [Visão geral da integração das tecnologias Reporting Services e SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologias de Implantação para Reporting Services no Modo Integrado do SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configurando Reporting Services para Integração com SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuração do Ambiente

Nossa configuração consiste em 4 servidores. Inclui um Controlador de Domínio, um SQL Server, um Servidor SharePoint e um servidor para Reporting Services. Você pode optar por ter SharePoint e Reporting Services na mesma máquina, o que simplificará um pouco e eu apontarei algumas das diferenças.

## Pré-requisitos de Instalação

{{% alert color="primary" %}}

O Add-In Reporting Services para SharePoint é um dos componentes principais para que a Integração funcione corretamente. O Add-In precisa ser instalado em qualquer um dos Web Front Ends (WFE) que estejam na sua fazenda SharePoint, juntamente com o servidor Central Admin. Uma das novas mudanças com SQL 2008 R2 & SharePoint 2010 é que o Add-In 2008 R2 agora é um pré-requisito para a Instalação do SharePoint. Isso significa que o Add-In RS será instalado quando você for instalar o SharePoint. Isso foi mostrado e destacado na figura abaixo. Isso realmente evita muitos problemas que vimos com SP 2007 e RS 2008 ao instalar o Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Complemento do Reporting Services para Share Point**
{{% /alert %}}

## Autenticação do SharePoint

**Antes de mergulharmos nas partes de Integração do RS, uma coisa que quero destacar sobre o Farm do SharePoint é como você configura o Site. Mais especificamente, como você configura a autenticação para o site. Se será Classic ou Claims. Essa escolha é importante no início. Não acredito que você possa mudar essa opção depois de concluída. Se você puder mudá-la, não será um processo simples.**

NOTE: ***Reporting Services 2008 R2 NÃO é compatível com Claims***

Mesmo se você escolher seu site SharePoint para usar Claims, o Reporting Services em si não tem consciência de Claims. Dito isso, ele afeta como a autenticação funciona com o Reporting Services. Então, qual é a diferença do ponto de vista do Reporting Services? Tudo se resume a se você deseja encaminhar Credenciais de Usuário para a fonte de dados. Classic:- Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados de back end (será necessário usar Kerberos para isso). Claims:- Um token Claims é usado e não um token do Windows. O RS sempre usará Trusted Authentication neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais dentro da sua fonte de dados.

Classic :- Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados de back end (será necessário usar Kerberos para isso.

Claims :- Um token Claims é usado e não um token do Windows. O RS sempre usará Trusted Authentication neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais dentro da sua fonte de dados.

Por enquanto, queremos apenas nos concentrar na configuração do RS. Neste ponto, o SharePoint está instalado na minha SharePoint Box e configurado com um site Classic Auth na porta 80. No servidor RS, acabei de instalar o Reporting Services e é só.


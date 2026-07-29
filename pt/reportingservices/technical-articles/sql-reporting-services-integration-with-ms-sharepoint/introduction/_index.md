---
title: Introdução
linktitle: Introdução
type: docs
weight: 10
url: /pt/reportingservices/introduction/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services tem sido muito notável para a geração de PDF através do SQL Reporting Services há muitos anos e oferece diversas opções de configuração e parametrização que não são suportadas por padrão no SQL Reporting Services. Recentemente, recebemos algumas solicitações relacionadas à Integração do Aspose.PDF for Reporting Services com o SharePoint. Para este artigo, vamos nos concentrar no MS SharePoint 2010. Antes de prosseguir, assumimos que você já possui uma farm do SharePoint configurada. Neste exemplo, utilizaremos o SharePoint Cloud completo. No entanto, os passos são semelhantes para o SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de prosseguirmos, vamos dar uma olhada nos tópicos de referência que consultamos durante a preparação deste artigo.

- [Visão geral da integração de Reporting Services e SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologias de Implantação para Reporting Services no Modo Integrado do SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configurando Reporting Services para Integração com SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuração do Ambiente

Nossa configuração consiste em 4 servidores. Inclui um Controlador de Domínio, um SQL Server, um Servidor SharePoint e um servidor para Reporting Services. Você pode optar por ter o SharePoint e o Reporting Services no mesmo equipamento, o que simplificará um pouco e eu apontarei algumas das diferenças.

## Pré-requisitos de Instalação

{{% alert color="primary" %}}

O Add-In Reporting Services para SharePoint é um dos componentes essenciais para que a Integração funcione corretamente. O Add-In precisa ser instalado em qualquer um dos Web Front Ends (WFE) que estejam na sua fazenda SharePoint, junto com o servidor Central Admin. Uma das novas mudanças com o SQL 2008 R2 & SharePoint 2010 é que o Add-In 2008 R2 agora é um pré-requisito para a instalação do SharePoint. Isso significa que o Add-In RS será instalado quando você for instalar o SharePoint. Isso foi mostrado e destacado na figura abaixo. Na prática, isso evita muitos dos problemas que vimos com o SP 2007 e RS 2008 ao instalar o Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Complemento do Reporting Services para Share Point**
{{% /alert %}}

## Autenticação do SharePoint

**Antes de mergulharmos nas partes de Integração do RS, uma coisa que quero destacar sobre o Farm do SharePoint é como você configura o Site. Mais especificamente, como você configura a autenticação para o site. Se será Classic ou Claims. Essa escolha é importante no início. Não acredito que você possa mudar essa opção depois que ela for feita. Se você puder mudá-la, não seria um processo simples.**

NOTA: ***Reporting Services 2008 R2 não tem suporte a Claims***

Mesmo que você escolha seu site SharePoint para usar Claims, o Reporting Services em si não tem consciência de Claims. Dito isso, isso afeta como a autenticação funciona com o Reporting Services. Então, qual é a diferença do ponto de vista do Reporting Services? Tudo se resume a se você deseja encaminhar as Credenciais do Usuário para a fonte de dados. Classic:- Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados backend (será necessário usar Kerberos para isso). Claims:- Um token Claims é usado e não um token do Windows. O RS sempre usará Trusted Authentication neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais na sua fonte de dados.

Classic :- Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados back end (será necessário usar Kerberos para isso.

Claims :- Um token Claims é usado e não um token do Windows. O RS sempre usará Trusted Authentication neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais na sua fonte de dados.

Por enquanto, queremos apenas nos concentrar na configuração do RS. Neste ponto, o SharePoint está instalado na minha caixa SharePoint e configurado com um site Classic Auth na porta 80. No servidor RS, acabei de instalar o Reporting Services e é isso.

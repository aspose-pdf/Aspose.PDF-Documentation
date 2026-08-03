---
title: Introdução
linktitle: Introduction
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para Reporting Services tem sido notável na geração de PDF por meio do SQL Reporting Services há muitos anos e fornece diversas opções de configuração e parametrização que não são suportadas por padrão no SQL Reporting Services. Recentemente, recebemos algumas solicitações relacionadas ao Aspose.PDF para integração do Reporting Services com o SharePoint. Neste artigo, vamos nos concentrar no MS SharePoint 2010. Antes de prosseguirmos, presumimos que você já tenha uma configuração do Farm do SharePoint. Neste exemplo, usaremos o SharePoint Cloud completo. No entanto, as etapas são semelhantes para o SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de prosseguirmos, vamos dar uma olhada nos tópicos de referência que consultamos durante a preparação deste artigo.

- [Overview of Reporting Services and SharePoint Technology Integration](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuração do ambiente

A configuração externa consiste em 4 servidores. Inclui um Controlador de Domínio, um SQL Server, um SharePoint Server e um servidor para Reporting Services. Você pode optar por ter o SharePoint e o Reporting Services na mesma caixa, o que simplificará um pouco isso e apontarei algumas das diferenças.

## Pré-requisitos de instalação

{{% alert color="primary" %}}

O suplemento Reporting Services para SharePoint é um dos principais componentes para que a integração funcione corretamente. O suplemento precisa ser instalado em qualquer Web Front Ends (WFE) que esteja em seu farm do SharePoint junto com o servidor Central Admin. Uma das novas mudanças no SQL 2008 R2 e no SharePoint 2010 é que o complemento 2008 R2 agora é um pré-requisito para a instalação do SharePoint. Isso significa que o suplemento RS será instalado quando você instalar o SharePoint. Ele foi mostrado e destacado na figura abaixo. Na verdade, isso evita muitos problemas que vimos com o SP 2007 e o RS 2008 ao instalar o complemento.

![Introduction](introduction_1.png)

**Imagem1: - Suplemento Reporting Services para Share Point**
{{% /alert %}}

## Autenticação do SharePoint

**Antes de entrarmos nas partes da Integração RS, uma coisa que quero destacar sobre o Farm do SharePoint é como você configura o Site. Mais especificamente como você configura a autenticação do site. Seja Clássico ou Claims. Essa escolha é importante no começo. Não acredito que você possa alterar essa opção depois de concluída. Se você pudesse mudar isso, não seria um processo simples.

NOTA: ***O Reporting Services 2008 R2 NÃO tem reconhecimento de reivindicações***

Mesmo que você escolha seu site do SharePoint para usar Declarações, o Reporting Services em si não reconhece as Declarações. Dito isto, isso afeta o modo como a autenticação funciona com o Reporting Services. Então, qual é a diferença da perspectiva do Reporting Services? A questão é se você deseja encaminhar as credenciais do usuário para a fonte de dados. Clássico: - Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados back-end (será necessário usar Kerberos para isso). Reivindicações: - Um token de reivindicações é usado e não um token do Windows. O RS sempre usará autenticação confiável neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais em sua fonte de dados.

Clássico: - Pode usar Kerberos e encaminhar as credenciais do usuário para sua fonte de dados de back-end (será necessário usar Kerberos para isso.

Reivindicações: - Um token de reivindicações é usado e não um token do Windows. O RS sempre usará autenticação confiável neste cenário e terá acesso apenas ao token SPUser. Você precisará armazenar suas credenciais em sua fonte de dados.

Por enquanto, queremos apenas nos concentrar na configuração do RS. Neste ponto, o SharePoint está instalado em meu SharePoint Box e configurado com um Classic Auth Site na porta 80. No servidor RS, acabei de instalar o Reporting Services e pronto.

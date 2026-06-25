---
title: Configurando o Reporting Services
linktitle: Configurando o Reporting Services
type: docs
weight: 20
url: /pt/reportingservices/setting-up-reporting-services/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Nossa primeira parada no Servidor Reporting Services é o Gerenciador de Configuração do Reporting Services.

{{% /alert %}}

## Conta de Serviço:

**Certifique‑se de entender qual conta de serviço você está usando para o Reporting Services. Se encontrarmos problemas, eles podem estar relacionados à conta de serviço que você está usando. O padrão é Network Service. Quando implantamos novas versões, sempre usamos Contas de Domínio, pois é onde provavelmente encontraremos problemas. Para esta instância do servidor, usamos uma Conta de Domínio chamada RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Configurando a conta de serviço**

## URL do Serviço Web:

{{% alert color="primary" %}}

**Precisaremos configurar a URL do Serviço Web. Este é o diretório virtual (vdir) do ReportServer que hospeda os Serviços Web usados pelo Reporting Services, e com o qual o SharePoint se comunicará. A menos que você queira personalizar as propriedades do vdir (ou seja, SSL, portas, cabeçalhos de host, etc… ), você deve simplesmente clicar em Aplicar aqui e estará pronto para usar.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Configurando a URL do Serviço Web Uma vez que a URL do Serviço Web tenha sido configurada, você deve ser capaz de ver os seguintes resultados**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Configuração bem-sucedida da URL do Serviço Web**
{{% /alert %}}

## Banco de dados:

**Precisamos criar o Banco de Dados do Catálogo do Reporting Services. Isso pode ser colocado em qualquer mecanismo de banco de dados SQL 2008 ou SQL 2008 R2. O SQL11 também funcionaria bem, mas ainda está em BETA. Esta ação criará dois bancos de dados, ReportServer e ReportServerTempDB, por padrão.**

{{% alert color="primary" %}}
**A outra etapa importante nisso é garantir que você escolha SharePoint Integrated para o tipo de banco de dados. Uma vez feita essa escolha, ela não pode ser alterada.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- Criando o banco de dados do servidor de relatórios**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- Configurando o servidor de banco de dados e o tipo de autenticação**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- Configurando o nome do banco de dados e o Modo**
{{% /alert %}}

**Para as credenciais, é assim que o Report Server se comunicará com o SQL Server. Qualquer conta que você selecionar receberá certos direitos dentro do banco de dados Catalog, bem como alguns dos bancos de dados do sistema via RSExecRole. MSDB é um desses bancos de dados para uso de assinaturas, pois utilizamos o SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Configurando as credenciais do banco de dados do Report Server**

{{% alert color="primary" %}}

**Depois que as credenciais do banco de dados forem especificadas, deveríamos ser capazes de obter os resultados conforme especificado abaixo.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Progresso da criação do banco de dados do Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Resumo da conclusão do banco de dados do Report Server**
{{% /alert %}}

## URL do Report Manager:

**Podemos ignorar a URL do Report Manager, pois não é usada quando estamos no modo Integrado ao SharePoint. O SharePoint é nossa interface. O Report Manager não funciona.**

## Chaves de Criptografia:

{{% alert color="primary" %}}
**Faça backup das suas Chaves de Criptografia e certifique-se de saber onde as guarda. Se você se deparar com uma situação em que precise migrar o Banco de Dados ou restaurá‑lo, você precisará delas.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- backup da chave de criptografia do Report Server**
{{% /alert %}}

{{% alert color="primary" %}}
**Parabéns! Configuramos com sucesso o Reporting Services usando o Configuration Manager. Se você acessar a URL na aba Web Service URL, ela deve mostrar algo semelhante ao seguinte.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Acesso ao Report Server após a instalação**

**Motivo do erro: O SharePoint está instalado em nosso WFE e concluímos a configuração do Reporting Services. Neste exemplo, Reporting Services e SharePoint estão em máquinas diferentes. Se estivessem na mesma máquina, você não teria visto esse erro. Precisamos tecnicamente instalar o SharePoint na caixa RS. Isso significa que o IIS também será habilitado.**
{{% /alert %}}



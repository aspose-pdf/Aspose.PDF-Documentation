---
title: Configurando o Reporting Services
linktitle: Setting up Reporting Services
type: docs
weight: 20
url: /reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Nossa primeira parada no Reporting Services Server é o Reporting Services Configuration Manager.

{{% /alert %}}

## Conta de serviço:

**Certifique-se de entender qual conta de serviço você está usando para o Reporting Services. Se tivermos problemas, isso pode estar relacionado à conta de serviço que você está usando. O padrão é Serviço de Rede. Quando vamos implantar novas compilações, sempre usamos contas de domínio, porque é aí que provavelmente encontraremos problemas. Para esta instância de servidor, usamos uma conta de domínio chamada RSService.**

![Set Up](setting-up-reporting-services_1.png)

**Imagem1: – Configurando conta de serviço**

## URL do serviço web:

{{% alert color="primary" %}}

**Precisaremos configurar a URL do serviço Web. Este é o diretório virtual ReportServer (vdir) que hospeda os serviços Web Reporting Services usados ​​e com o qual o SharePoint se comunicará. A menos que você queira personalizar as propriedades do vdir (ou seja, SSL, portas, cabeçalhos de host, etc.), basta clicar em Aplicar aqui e pronto.**
![Web Service URL](setting-up-reporting-services_2.png)

**Imagem2: - Configurando o URL do serviço da Web Depois que o URL do serviço da Web for configurado, você poderá ver os seguintes resultados **

![Web Service URL Results](setting-up-reporting-services_3.png)

**Imagem3: - Configuração bem-sucedida do URL do serviço Web**
{{% /alert %}}

## Banco de dados:

**Precisamos criar o banco de dados do catálogo do Reporting Services. Isso pode ser colocado em qualquer Mecanismo de Banco de Dados SQL 2008 ou SQL 2008 R2. SQL11 também funcionaria bem, mas ainda está em BETA. Esta ação criará dois bancos de dados, ReportServer e ReportServerTempDB, por padrão.**

{{% alert color="primary" %}}
**A outra etapa importante é certificar-se de escolher SharePoint Integrado para o tipo de banco de dados. Uma vez feita esta escolha, ela não poderá ser alterada.**

![Creating Report Server Database](setting-up-reporting-services_4.png)

**Imagem4:- Criando banco de dados do servidor de relatório**

![Setting up Database Server and Authentication Type](setting-up-reporting-services_5.png)

**Imagem5:- Configurando servidor de banco de dados e tipo de autenticação**

![Setting up Database Name and Mode](setting-up-reporting-services_6.png)

**Imagem6: - Configurando nome e modo do banco de dados**
{{% /alert %}}

**Para as credenciais, é assim que o Report Server se comunicará com o SQL Server. Qualquer conta que você selecionar receberá determinados direitos no banco de dados do Catálogo, bem como em alguns bancos de dados do sistema por meio do RSExecRole. MSDB é um desses bancos de dados para uso de assinatura, pois usamos o SQL Agent.**

![Setting up Report Server database credentials](setting-up-reporting-services_7.png)

**Imagem7: - Configurando credenciais do banco de dados do Report Server**

{{% alert color="primary" %}}

**Depois que as credenciais do banco de dados forem especificadas, poderemos obter os resultados conforme especificado abaixo.**

![Report Server database creation progress](setting-up-reporting-services_8.png)

**Imagem8: - Progresso da criação do banco de dados do Servidor de Relatórios**

![Report Server database completion summary](setting-up-reporting-services_9.png)

**Imagem9: - Resumo de conclusão do banco de dados do Report Server**
{{% /alert %}}

## URL do gerenciador de relatórios:

**Podemos ignorar o URL do Report Manager, pois ele não é usado quando estamos no modo integrado do SharePoint. SharePoint é nosso front-end. O Gerenciador de relatórios não funciona.**

## Chaves de criptografia:

{{% alert color="primary" %}}
**Faça backup de suas chaves de criptografia e certifique-se de saber onde as guarda. Se você se encontrar em uma situação em que precise migrar o banco de dados ou restaurá-lo, você precisará deles.**

![Report Server Encryption key backup](setting-up-reporting-services_10.png)

**Imagem10: - Backup da chave de criptografia do servidor de relatório**
{{% /alert %}}

{{% alert color="primary" %}}
**Parabéns! Configuramos o Reporting Services com êxito usando o Configuration Manager. Se você navegar até o URL na guia URL do serviço Web, ele deverá mostrar algo semelhante ao seguinte.**

![Report Server access after installation](setting-up-reporting-services_11.png)

**Imagem11:- Reportar acesso ao servidor após instalação**

**Motivo do erro: o SharePoint está instalado em nosso WFE e concluímos a configuração do Reporting Services. Neste exemplo, o Reporting Services e o SharePoint estão em máquinas diferentes. Se eles estivessem na mesma máquina, você não teria visto esse erro. Tecnicamente, precisamos instalar o SharePoint no RS Box. Isso significa que o IIS também estará habilitado.**
{{% /alert %}}


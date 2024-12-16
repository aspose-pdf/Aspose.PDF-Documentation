---
title: Configurando Serviços de Relatórios
type: docs
weight: 20
url: /pt/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Nosso primeiro ponto no Servidor de Serviços de Relatórios é o Gerenciador de Configuração dos Serviços de Relatórios.

{{% /alert %}}

## Conta de Serviço:

**Certifique-se de entender qual conta de serviço você está usando para os Serviços de Relatórios. Se encontrarmos problemas, pode estar relacionado à conta de serviço que você está usando. O padrão é o Serviço de Rede. Quando vamos implantar novas builds, sempre usamos Contas de Domínio, porque é onde provavelmente enfrentaremos problemas. Para esta instância do servidor, usamos uma Conta de Domínio chamada RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Imagem1:- Configurando conta de serviço**

## URL do Serviço Web:

{{% alert color="primary" %}}

**Precisaremos configurar a URL do Serviço Web. **Este é o diretório virtual (vdir) do ReportServer que hospeda os Serviços Web que o Reporting Services usa, e com o qual o SharePoint se comunicará. A menos que você queira personalizar as propriedades do vdir (ou seja, SSL, portas, cabeçalhos de host, etc...), você deve simplesmente clicar em Aplicar aqui e estará pronto para prosseguir.**

![todo:image_alt_text](setting-up-reporting-services_2.png)

**Imagem2:- Configurando o URL do Serviço Web Uma vez que o URL do serviço Web tenha sido configurado, você deve ser capaz de ver os seguintes resultados**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Imagem3:- Configuração bem-sucedida do URL do serviço Web**
{{% /alert %}}

## Banco de Dados:

**Precisamos criar o Banco de Dados do Catálogo do Reporting Services. Isso pode ser colocado em qualquer SQL 2008 ou SQL 2008 R2 Database Engine. O SQL11 também funcionaria bem, mas ainda está em BETA. Esta ação criará dois bancos de dados, ReportServer e ReportServerTempDB, por padrão.**

{{% alert color="primary" %}}
**Outro passo importante com isso é garantir que você escolha SharePoint Integrated para o tipo de banco de dados. Uma vez que esta escolha é feita, ela não pode ser alterada.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Imagem4:- Criando banco de dados do servidor de relatórios**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Imagem5:- Configurando servidor de banco de dados e tipo de autenticação**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Imagem6:- Configurando nome do banco de dados e Modo**
{{% /alert %}}

**Para as credenciais, é assim que o Servidor de Relatórios se comunicará com o SQL Server. Seja qual for a conta que você selecionar, será dada certos direitos dentro do banco de dados Catálogo, bem como alguns dos bancos de dados do sistema através do RSExecRole. MSDB é um desses bancos de dados para uso de Assinatura, pois utilizamos o SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Imagem7:- Configurando credenciais do banco de dados do Servidor de Relatórios**

{{% alert color="primary" %}}

**Uma vez especificadas as credenciais do banco de dados, devemos ser capazes de obter os resultados conforme especificado abaixo.**

![todo:image_alt_text](setting-up-reporting-services_8.png)
**Imagem8:- Progresso da criação do banco de dados do Report Server**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Imagem9:- Resumo da conclusão do banco de dados do Report Server**
{{% /alert %}}

## URL do Gerenciador de Relatórios:

**Podemos pular a URL do Gerenciador de Relatórios, pois não é usada quando estamos no modo Integrado do SharePoint. O SharePoint é nosso frontend. O Gerenciador de Relatórios não funciona.**

## Chaves de Criptografia:

{{% alert color="primary" %}}
**Faça backup das suas Chaves de Criptografia e certifique-se de saber onde guardá-las. Se você se deparar com uma situação em que precisa migrar o Banco de Dados ou restaurá-lo, você precisará delas.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Imagem10:- Backup da chave de criptografia do Report Server**
{{% /alert %}}

{{% alert color="primary" %}}
**Parabéns! Configuramos com sucesso os Serviços de Relatório usando o Gerenciador de Configurações. Se você acessar a URL na aba URL do Serviço Web, deverá mostrar algo semelhante ao seguinte.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Acesso ao Servidor de Relatórios após a instalação**

**Reason of error: SharePoint está instalado no nosso WFE e terminamos a configuração dos Serviços de Relatórios. Neste exemplo, os Serviços de Relatórios e o SharePoint estão em máquinas diferentes. Se estivessem na mesma máquina, você não veria esse erro. Tecnicamente, precisamos instalar o SharePoint na Caixa RS. Isso significa que o IIS também será habilitado.**
{{% /alert %}}
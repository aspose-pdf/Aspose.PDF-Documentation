---
title: Aspose.PDF Java para PHP
linktitle: Aspose.PDF Java para PHP
type: docs
weight: 50
url: /pt/java/aspose-pdf-java-for-php/
description: Aprenda como integrar o Aspose.PDF for Java em projetos PHP. Desbloqueie funcionalidades avançadas de PDF para suas aplicações web.
lastmod: "2026-10-06"
---
## Introdução ao Aspose.PDF Java para PHP

### Ponte PHP / Java

O PHP/Java Bridge é uma implementação de streaming, baseada em XML\u0412 [protocolo de rede](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), que pode ser usado para conectar um mecanismo de script nativo, por exemplo PHP, Scheme ou Python, com uma máquina virtual Java. É até 50 vezes mais rápido que RPC local via SOAP, requer menos recursos no lado do servidor web. É\u0412 [mais rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) e mais confiável que a comunicação direta via Java Native Interface, e não requer componentes adicionais para invocar procedimentos Java a partir de PHP ou procedimentos PHP a partir de Java.

Leia mais em [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF for Java

Aspose.PDF for Java é um componente de criação de documentos PDF que permite que suas aplicações Java leiam, escrevam e manipulem documentos PDF sem usar o Adobe Acrobat.

Aspose.PDF for Java é um componente com preço acessível que oferece uma incrível variedade de recursos, incluindo: opções de compactação de PDF, criação e manipulação de tabelas, suporte a gráficos, funções de imagem, funcionalidade extensiva de hiperlinks, controles de segurança avançados e manuseio de Font personalizado.

Aspose.PDF for Java permite que você crie arquivos PDF diretamente através da API fornecida e de modelos XML. Usar o Aspose.PDF for Java também permitirá que você adicione recursos PDF às suas aplicações em pouco tempo.

### Aspose.PDF Java para PHP

O projeto Aspose.PDF for PHP mostra como diferentes tarefas podem ser realizadas usando as APIs Aspose.PDF Java em PHP. Este projeto tem como objetivo fornecer exemplos úteis para desenvolvedores PHP que desejam utilizar o Aspose.PDF for Java em seus projetos PHP usando [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Requisitos de sistema e plataformas suportadas

### Requisitos de sistema

A seguir estão os requisitos de sistema para usar Aspose.PDF for PHP via Java:

- Tomcat Server 8.0 ou superior instalado.
- PHP/JavaBridge está configurado.
- FastCGI está instalado.
- Componente Aspose.PDF baixado.

### Plataformas suportadas

A seguir estão as plataformas suportadas:

- PHP 5.3 ou superior
- Java 1.8 ou superior

## Downloads e configurar

### Baixar bibliotecas necessárias

Baixe as bibliotecas necessárias mencionadas abaixo. Elas são necessárias para executar os exemplos Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Baixar exemplos de sites de codificação social

As seguintes versões de exemplos em execução estão disponíveis para download nos sites de codificação social mencionados abaixo:

### GitHub

- Exemplos Aspose.PDF Java para PHP
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Configurar o código-fonte na plataforma Linux

Por favor, siga estes passos simples para abrir e expandir o código-fonte ao usar:

### 1. Install Tomcat Server

Para instalar o servidor tomcat, execute o seguinte comando no console linux. Isso instalará o servidor tomcat com sucesso.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Baixar e configurar PHP/JavaBridge

Para baixar os binários do PHP/JavaBridge, execute o comando a seguir no console do Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descompacte os binários PHP/JavaBridge emitindo o seguinte comando no console linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Isso extrairá o arquivo **JavaBridge.war**. Copie-o para a pasta **webapps** do tomcat88 emitindo o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Ao copiar, tomcat8 criará automaticamente uma nova pasta "**JavaBridge**" in **webapps**.

Se aparecer qualquer mensagem de erro, então instale **FastCGI** emitindo o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Se **JAVA_HOME** erro for exibido, então abra o arquivo /etc/default/tomcat8 e descomente a linha que define o JAVA_HOME.

### 3. Configurar exemplos Aspose.PDF Java para PHP

Clone, exemplos PHP emitindo os seguintes comandos dentro da pasta webapps/JavaBridge.В

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Configurar o código-fonte na plataforma Windows

Por favor, siga os passos simples abaixo para configurar o PHP/Java Bridge na plataforma Windows

1. Instale o PHP5 e configure como você costuma fazer.
2. Instale o JRE 6 (Java Runtime Environment) se você ainda não o tem. Você pode verificar isso em C:\Program Files etc. Você pode baixá-lo aqui. Estou usando o JRE 6 pois ele é compatível com o PHP Java Bridge (PJB).

3. Instale o Apache Tomcat 8.0. Você pode baixá-lo aqui.

4. Baixe [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este arquivo para o diretório webapps do Tomcat.
(ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Reinicie o serviço Tomcat Apache.

6. Acesse http://localhost:8080/JavaBridge/test.php para verificar se o PHP funciona. Você pode encontrar outros exemplos lá.

7. Copie seu [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) arquivo jar para C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.

8. Clonar [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) exemplos dentro da pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\

9. Copie a pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java para a pasta de exemplos do Aspose.PDF Java para PHP.

10. Reinicie o serviço Apache Tomcat e comece a usar os exemplos.

## Suporte, extensão e contribuição

### Suporte

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer bons produtos aos nossos clientes não seria suficiente. Também precisávamos fornecer um bom serviço. Nós somos desenvolvedores nós mesmos e entendemos o quão frustrante é quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa fazer. Estamos aqui para resolver problemas, não criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que usa nosso produto, seja porque o comprou ou está usando uma avaliação, merece toda a nossa atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionados ao Aspose.Cells Java for PHP usando qualquer uma das plataformas a seguir:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Estender e contribuir

Aspose.PDF Java for PHP é de código aberto e seu código-fonte está disponível nos principais sites de codificação social listados abaixo. Os desenvolvedores são incentivados a baixar o código-fonte e contribuir sugerindo ou adicionando novos recursos ou aprimorando os existentes, para que outros também possam se beneficiar dele.

### Código-fonte

Você pode obter o código-fonte mais recente em um dos seguintes locais

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

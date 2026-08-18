---
title: Baixe e configure Aspose.PDF em PHP
linktitle: Baixe e configure Aspose.PDF em PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: Aprenda como baixar e configurar Aspose.PDF em PHP para fácil integração e manipulação de PDF em seus projetos PHP.
lastmod: "2026-06-09"
---
## Baixe as bibliotecas necessárias

Baixe as bibliotecas necessárias mencionadas abaixo. Estes são os necessários para executar exemplos Aspose.PDF Java para PHP.

- **Aspose:** [Aspose.PDF para componente Java](https://downloads.aspose.com/pdf/java)
- Ponte PHP/Java

## Baixe exemplos de sites de codificação social

As seguintes versões de exemplos em execução estão disponíveis para download nos sites de codificação social mencionados abaixo:

### GitHub

- **Aspose.PDF Java para exemplos de PHP**
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Como configurar o código fonte na plataforma Linux

Siga estas etapas simples para abrir e estender o código-fonte ao usar:

## 1. Instale o servidor Tomcat

Para instalar o servidor Tomcat, emita o seguinte comando no console Linux. Isso instalará o servidor Tomcat com êxito.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Baixe e configure PHP/JavaBridge

Para fazer download dos binários PHP/JavaBridge, emita o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descompacte os binários PHP/JavaBridge emitindo o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  descompacte -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Isso extrairá o arquivo **JavaBridge.war**. Copie-o para a pasta tomcat88 **webapps**В emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Ao copiar, o Tomcat8 criará automaticamente uma nova pasta "**JavaBridge**" em **webapps**. Depois que a pasta for criada, verifique se o Tomcat8 está em execução e marque http://localhost:8080/JavaBridge no navegador, ele deve abrir uma página padrão do JavaBridge.

Se alguma mensagem de erro aparecer, instale o **FastCGI** emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Após instalar o php5.5 CGI, reinicie o servidor tomcat8 e verifique http://localhost:8080/JavaBridge novamente no navegador.

Se o erro **JAVA_HOME** for exibido, abra o arquivo /etc/default/tomcat8 e remova o comentário da linha que define o arquivo JAVA_HOME. Marque http://localhost:8080/JavaBridge no navegador novamente, ele deve vir com a página de exemplos de PHP/JavaBridge.

## 3. Configure Aspose.PDF Java para exemplos de PHP

Clone exemplos de PHP emitindo os seguintes comandos dentro da pasta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Como configurar o código-fonte no Windows

Siga as etapas simples abaixo para configurar o PHP/Java Bridge na plataforma Windows

1. Instale o PHP5 e configure normalmente
2. Instale o JRE 6 (Java Runtime Environment) se ainda não o tiver. Você pode verificar isso em C:\Program Arquivos etc. Você pode baixá-lo aqui . Estou usando o JRE 6 porque é compatível com PHP Java Bridge (PJB).

3. Instale o Apache Tomcat 8.0. Você pode baixá-lo aqui

4. Baixe JavaBridge.war.
5. Copie este arquivo para o diretório webapps do Tomcat.
(ex: C:\Program Arquivos\Apache Software Foundation\Tomcat 8.0\webapps )

6. Reinicie o serviço Apache do Tomcat.

7. Vá para http://localhost:8080/JavaBridge/test.php para verificar se o php funciona. Você pode encontrar outros exemplos lá

8. Copie seu arquivo jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) para C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Clone [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) exemplos dentro da pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copie a pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java para sua pasta de exemplos Aspose.PDF Java para PHP.

11. Reinicie o serviço Apache Tomcat e comece a usar exemplos.

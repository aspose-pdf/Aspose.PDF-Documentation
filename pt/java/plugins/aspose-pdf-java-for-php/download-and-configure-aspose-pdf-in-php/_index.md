---
title: Download e Configurar Aspose.PDF em PHP
type: docs
weight: 10
url: pt/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## Baixar Bibliotecas Necessárias

Baixe as bibliotecas necessárias mencionadas abaixo. Estas são necessárias para executar os exemplos do Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Baixar Exemplos de Sites de Codificação Social

As seguintes versões de exemplos em execução estão disponíveis para download nos sites de codificação social mencionados abaixo:

### GitHub

- **Exemplos de Aspose.PDF Java para PHP**
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Como configurar o código-fonte na Plataforma Linux

Por favor, siga estes passos simples para abrir e estender o código-fonte enquanto usa:

## 1. Instalar o Servidor Tomcat

Para instalar o servidor Tomcat, emita o seguinte comando no console do Linux. Isso instalará com sucesso o servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Baixar e Configurar PHP/JavaBridge

Para baixar os binários do PHP/JavaBridge, emita o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Descompacte os binários do PHP/JavaBridge emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Isso irá extrair o arquivo **JavaBridge.war**. Copie-o para a pasta **webapps** do tomcat88 emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}


Ao copiar, o tomcat8 criará automaticamente uma nova pasta "**JavaBridge**" em **webapps**.
 Uma vez que a pasta é criada, certifique-se de que seu tomcat8 está em execução e, em seguida, verifique http://localhost:8080/JavaBridge no navegador, deve abrir uma página padrão do JavaBridge.

Se alguma mensagem de erro aparecer, instale **FastCGI** emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Após instalar o php5.5 CGI, reinicie o servidor tomcat8 e verifique http://localhost:8080/JavaBridge novamente no navegador.

Se o erro **JAVA_HOME** for exibido, abra o arquivo /etc/default/tomcat8 e descomente a linha que define o JAVA_HOME. Verifique http://localhost:8080/JavaBridge no navegador novamente, deve aparecer a página de Exemplos do PHP/JavaBridge.

## 3. Configure Aspose.PDF Java para Exemplos PHP

Clone, exemplos PHP emitindo os seguintes comandos dentro da pasta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;


$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Como configurar o código-fonte no Windows

Por favor, siga os passos simples abaixo para configurar a PHP/Java Bridge na plataforma Windows

1. Instale o PHP5 e configure como você normalmente faz.
2. Instale o JRE 6 (Java Runtime Environment) se você ainda não o tiver. Você pode verificar isso em C:\Program Files etc. Você pode baixá-lo aqui. Estou usando o JRE 6 pois é compatível com o PHP Java Bridge (PJB).

3. Instale o Apache Tomcat 8.0. Você pode baixá-lo aqui.

4. Baixe o JavaBridge.war.
5. Copie este arquivo para o diretório webapps do tomcat.
(ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

6. Reinicie o serviço apache tomcat.

7. Vá para http://localhost:8080/JavaBridge/test.php para verificar se o PHP funciona. Você pode encontrar outros exemplos lá.

8. Copie seu arquivo jar do [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) para C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Clone [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) exemplos dentro da pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copie a pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java para a sua pasta de exemplos do Aspose.PDF Java for PHP.

11. Reinicie o serviço Apache Tomcat e comece a usar os exemplos.